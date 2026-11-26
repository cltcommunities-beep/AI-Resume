"""Robinhood MCP Data Adapter — normalizes live Daily, Weekly, Monthly OHLCV & L2 snapshots."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .models import (
    L2OrderBookSnapshot,
    L2Wall,
    OHLCVBar,
    Timeframe,
    TimeframeSeries,
)


def _to_float(val: Any, default: float = 0.0) -> float:
    if val is None or val == "":
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def _compute_sma(values: list[float], period: int) -> tuple[float | None, ...]:
    out: list[float | None] = []
    running = 0.0
    for idx, val in enumerate(values):
        running += val
        if idx >= period:
            running -= values[idx - period]
        if idx + 1 >= period:
            out.append(running / period)
        else:
            out.append(None)
    return tuple(out)


def _compute_atr14(bars: list[OHLCVBar], period: int = 14) -> tuple[float, ...]:
    if not bars:
        return ()
    trs: list[float] = []
    for i, bar in enumerate(bars):
        if i == 0:
            tr = bar.high - bar.low
        else:
            prev_c = bars[i - 1].close
            tr = max(bar.high - bar.low, abs(bar.high - prev_c), abs(bar.low - prev_c))
        trs.append(max(tr, 1e-6))
    atrs: list[float] = []
    running = 0.0
    for i, tr in enumerate(trs):
        if i < period:
            running += tr
            atrs.append(running / (i + 1))
        else:
            prev_atr = atrs[-1]
            atrs.append(((prev_atr * (period - 1)) + tr) / period)
    return tuple(atrs)


def _compute_vol_sma(bars: list[OHLCVBar], period: int = 20) -> tuple[float, ...]:
    out: list[float] = []
    running = 0.0
    for i, b in enumerate(bars):
        running += b.volume
        if i >= period:
            running -= bars[i - period].volume
        denom = min(i + 1, period)
        out.append(max(running / denom, 1.0))
    return tuple(out)


def _compute_rsi14(closes: list[float], period: int = 14) -> float | None:
    if len(closes) <= period:
        return None
    gains = 0.0
    losses = 0.0
    for i in range(1, period + 1):
        delta = closes[i] - closes[i - 1]
        if delta >= 0:
            gains += delta
        else:
            losses += abs(delta)
    avg_gain = gains / period
    avg_loss = losses / period
    for i in range(period + 1, len(closes)):
        delta = closes[i] - closes[i - 1]
        gain = delta if delta > 0 else 0.0
        loss = abs(delta) if delta < 0 else 0.0
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period
    if avg_loss <= 1e-9:
        return 100.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def _infer_trend_direction(
    closes: list[float],
    sma20: tuple[float | None, ...],
    sma50: tuple[float | None, ...],
) -> str:
    if len(closes) < 6:
        return "SIDEWAYS"
    last = closes[-1]
    s20 = sma20[-1] if sma20 else None
    s50 = sma50[-1] if sma50 else None
    lookback = min(10, len(closes) - 1)
    pct_change = (last - closes[-1 - lookback]) / max(closes[-1 - lookback], 1e-6)
    if s20 is not None and s50 is not None:
        if last > s20 > s50 and pct_change > 0.015:
            return "UPTREND"
        if last < s20 < s50 and pct_change < -0.015:
            return "DOWNTREND"
    if pct_change >= 0.04:
        return "UPTREND"
    if pct_change <= -0.04:
        return "DOWNTREND"
    return "SIDEWAYS"


def build_timeframe_series(
    symbol: str, timeframe: Timeframe, bars: list[OHLCVBar]
) -> TimeframeSeries:
    clean = [b for b in bars if not b.interpolated and b.high >= b.low and b.close > 0]
    closes = [b.close for b in clean]
    sma20 = _compute_sma(closes, 20)
    sma50 = _compute_sma(closes, 50)
    sma200 = _compute_sma(closes, 200)
    atr14 = _compute_atr14(clean, 14)
    vol_sma20 = _compute_vol_sma(clean, 20)
    rsi14 = _compute_rsi14(closes, 14)
    trend = _infer_trend_direction(closes, sma20, sma50)
    return TimeframeSeries(
        symbol=symbol.upper(),
        timeframe=timeframe,
        bars=tuple(clean),
        sma20=sma20,
        sma50=sma50,
        sma200=sma200,
        atr14=atr14,
        vol_sma20=vol_sma20,
        rsi14=rsi14,
        trend_direction=trend,
    )


class RobinhoodMarketDataAdapter:
    """Implements MarketDataProviderProtocol for Robinhood MCP JSON payloads."""

    @staticmethod
    def _unwrap_data(raw: Any) -> Any:
        if isinstance(raw, dict) and isinstance(raw.get("data"), dict):
            return raw["data"]
        return raw

    @classmethod
    def _extract_raw_bars(cls, raw: Any) -> list[dict[str, Any]]:
        raw = cls._unwrap_data(raw)
        if raw is None:
            return []
        if isinstance(raw, list):
            return raw
        if isinstance(raw, dict):
            for key in ("bars", "historicals", "data_points", "candles"):
                if isinstance(raw.get(key), list):
                    return raw[key]
            results = raw.get("results")
            if isinstance(results, list) and results:
                first = results[0]
                if isinstance(first, dict):
                    for key in ("bars", "historicals", "data_points"):
                        if isinstance(first.get(key), list):
                            return first[key]
            # Map of symbol -> bars list (from Robinhood MCP multi-symbol response)
            for val in raw.values():
                if isinstance(val, list) and val and isinstance(val[0], dict):
                    return val
                if isinstance(val, dict):
                    for key in ("bars", "historicals"):
                        if isinstance(val.get(key), list):
                            return val[key]
        return []

    @staticmethod
    def _parse_bar(item: dict[str, Any]) -> OHLCVBar | None:
        o = _to_float(item.get("open", item.get("open_price", item.get("open_value", item.get("o")))))
        h = _to_float(item.get("high", item.get("high_price", item.get("high_value", item.get("h")))))
        l = _to_float(item.get("low", item.get("low_price", item.get("low_value", item.get("l")))))
        c = _to_float(item.get("close", item.get("close_price", item.get("close_value", item.get("c")))))
        v = _to_float(item.get("volume", item.get("v")), 0.0)
        if c <= 0 or h <= 0 or l <= 0:
            return None
        ts = str(
            item.get(
                "timestamp",
                item.get("begins_at", item.get("t", item.get("date", ""))),
            )
        )
        return OHLCVBar(
            timestamp=ts,
            open=o if o > 0 else c,
            high=max(h, o if o > 0 else c, c),
            low=min(l, o if o > 0 else c, c),
            close=c,
            volume=max(v, 0.0),
            interpolated=bool(item.get("interpolated", False)),
            is_live_incomplete=bool(item.get("is_live_incomplete", False)),
        )

    @classmethod
    def _normalize_quote(cls, raw_quote: Any) -> dict[str, Any] | None:
        raw_quote = cls._unwrap_data(raw_quote)
        if not isinstance(raw_quote, dict):
            return None
        if isinstance(raw_quote.get("results"), list) and raw_quote["results"]:
            first = raw_quote["results"][0]
            if isinstance(first, dict):
                q = first.get("quote", first)
                if isinstance(q, dict):
                    return q
        return raw_quote

    @classmethod
    def _normalize_fundamentals(cls, raw_fund: Any) -> dict[str, Any] | None:
        raw_fund = cls._unwrap_data(raw_fund)
        if not isinstance(raw_fund, dict):
            return None
        if isinstance(raw_fund.get("results"), list) and raw_fund["results"]:
            first = raw_fund["results"][0]
            if isinstance(first, dict):
                return first
        return raw_fund

    @staticmethod
    def _latest_quote_price_and_ts(quote: dict[str, Any]) -> tuple[float, str]:
        reg_p = _to_float(quote.get("last_trade_price", quote.get("price")))
        reg_t = str(quote.get("venue_last_trade_time", quote.get("updated_at", "")))
        ext_p = _to_float(
            quote.get("last_non_reg_trade_price", quote.get("last_extended_hours_trade_price"))
        )
        ext_t = str(quote.get("venue_last_non_reg_trade_time", ""))
        if ext_p > 0 and (not reg_t or ext_t > reg_t):
            return ext_p, ext_t or reg_t or datetime.now(timezone.utc).isoformat()
        if reg_p > 0:
            return reg_p, reg_t or datetime.now(timezone.utc).isoformat()
        return ext_p, ext_t or datetime.now(timezone.utc).isoformat()

    @classmethod
    def _maybe_append_live_bar(
        cls,
        bars: list[OHLCVBar],
        quote: dict[str, Any] | None,
        fundamentals: dict[str, Any] | None,
        timeframe: Timeframe,
    ) -> list[OHLCVBar]:
        """Appends live unclosed bar strictly tagged is_live_incomplete=True."""
        if not quote or not bars:
            return bars
        live_price, q_ts = cls._latest_quote_price_and_ts(quote)
        if live_price <= 0:
            return bars
        src = fundamentals or {}
        q_open = _to_float(quote.get("open", quote.get("open_price", src.get("open"))), live_price)
        q_high = _to_float(quote.get("high", quote.get("high_price", src.get("high"))), max(q_open, live_price))
        q_low = _to_float(quote.get("low", quote.get("low_price", src.get("low"))), min(q_open, live_price))
        q_vol = _to_float(quote.get("volume", src.get("volume")), 0.0)
        q_date = str(src.get("market_date", q_ts[:10]))[:10]
        last_date = bars[-1].timestamp[:10]

        if timeframe == Timeframe.DAILY and q_date > last_date and q_open > 0:
            live_bar = OHLCVBar(
                timestamp=q_ts,
                open=q_open,
                high=max(q_high, q_open, live_price),
                low=min(q_low if q_low > 0 else live_price, q_open, live_price),
                close=live_price,
                volume=q_vol,
                interpolated=False,
                is_live_incomplete=True,
            )
            return [*bars, live_bar]

        if timeframe in (Timeframe.WEEKLY, Timeframe.MONTHLY) and q_date > last_date:
            prev_c = bars[-1].close
            live_bar = OHLCVBar(
                timestamp=q_ts,
                open=q_open if q_open > 0 else prev_c,
                high=max(q_high, q_open if q_open > 0 else prev_c, live_price),
                low=min(q_low if q_low > 0 else live_price, q_open if q_open > 0 else prev_c, live_price),
                close=live_price,
                volume=q_vol,
                interpolated=False,
                is_live_incomplete=True,
            )
            return [*bars, live_bar]
        return bars

    @classmethod
    def _parse_l2_book(cls, raw_l2: dict[str, Any] | None, spot: float) -> L2OrderBookSnapshot | None:
        raw_l2 = cls._unwrap_data(raw_l2)
        if not isinstance(raw_l2, dict) or spot <= 0:
            return None
        if isinstance(raw_l2.get("books"), list) and raw_l2["books"]:
            raw_l2 = raw_l2["books"][0]
        if not isinstance(raw_l2, dict):
            return None

        def _extract_side(entries: Any, side: str) -> tuple[list[L2Wall], float]:
            walls: list[L2Wall] = []
            near_usd = 0.0
            if not isinstance(entries, list):
                return walls, near_usd
            for e in entries:
                if not isinstance(e, dict):
                    continue
                price = _to_float(e.get("price", e.get("limit_price")))
                shares = _to_float(e.get("quantity", e.get("shares", e.get("size"))))
                if price <= 0 or shares <= 0:
                    continue
                notional = _to_float(e.get("notional_usd"), price * shares)
                if abs(price - spot) / spot <= 0.15:
                    near_usd += notional
                walls.append(L2Wall(price=price, shares=shares, notional_usd=notional, side=side))
            walls.sort(key=lambda w: w.notional_usd, reverse=True)
            return walls[:15], near_usd

        bids_raw = raw_l2.get("bids", raw_l2.get("bid_walls", []))
        asks_raw = raw_l2.get("asks", raw_l2.get("ask_walls", []))
        bid_walls, near_bid = _extract_side(bids_raw, "bid")
        ask_walls, near_ask = _extract_side(asks_raw, "ask")
        near_bid = _to_float(raw_l2.get("near_bid_usd"), near_bid)
        near_ask = _to_float(raw_l2.get("near_ask_usd"), near_ask)
        return L2OrderBookSnapshot(
            spot=spot,
            bid_walls=tuple(bid_walls),
            ask_walls=tuple(ask_walls),
            near_bid_usd=near_bid,
            near_ask_usd=near_ask,
        )

    def build_series_bundle(
        self, payload: dict[str, Any]
    ) -> tuple[str, str, float, float | None, dict[Timeframe, TimeframeSeries], L2OrderBookSnapshot | None]:
        symbol = str(payload.get("symbol", "UNKNOWN")).upper()
        as_of = str(payload.get("as_of", datetime.now(timezone.utc).isoformat()))
        quote = self._normalize_quote(payload.get("quote"))
        fundamentals = self._normalize_fundamentals(payload.get("fundamentals"))

        tf_map = {
            Timeframe.DAILY: payload.get("daily", payload.get("day", payload.get("1D"))),
            Timeframe.WEEKLY: payload.get("weekly", payload.get("week", payload.get("1W"))),
            Timeframe.MONTHLY: payload.get("monthly", payload.get("month", payload.get("1M"))),
        }

        series_dict: dict[Timeframe, TimeframeSeries] = {}
        for tf, raw_tf in tf_map.items():
            raw_list = self._extract_raw_bars(raw_tf)
            parsed = [b for item in raw_list if (b := self._parse_bar(item)) is not None]
            parsed = self._maybe_append_live_bar(parsed, quote, fundamentals, tf)
            if parsed:
                series_dict[tf] = build_timeframe_series(symbol, tf, parsed)

        live_price = _to_float(payload.get("live_price"))
        if live_price <= 0 and quote:
            live_price, _ = self._latest_quote_price_and_ts(quote)
        if live_price <= 0:
            for tf in (Timeframe.DAILY, Timeframe.WEEKLY, Timeframe.MONTHLY):
                if tf in series_dict and series_dict[tf].latest_bar:
                    live_price = series_dict[tf].latest_bar.close
                    break

        market_value: float | None = None
        if payload.get("market_value") is not None:
            market_value = _to_float(payload.get("market_value"))
        elif fundamentals:
            mcap = _to_float(fundamentals.get("market_cap"))
            shs = _to_float(
                fundamentals.get("shares_outstanding", fundamentals.get("diluted_shares"))
            )
            if mcap > 0 and shs > 0:
                market_value = mcap / shs

        l2_book = self._parse_l2_book(payload.get("l2_book"), live_price)
        return symbol, as_of, live_price, market_value, series_dict, l2_book
