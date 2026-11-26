"""30 Candlestick Pattern Detectors (12 Single, 10 Two-Candle, 8 Three-Candle) with Trend Context."""

from __future__ import annotations

from .models import (
    OHLCVBar,
    PatternBias,
    PatternKind,
    RawPatternCandidate,
    TimeframeSeries,
)

CANDLESTICK_PATTERNS: tuple[str, ...] = (
    # A. Single-Candle (12)
    "Doji",
    "Dragonfly Doji",
    "Gravestone Doji",
    "Long-Legged Doji",
    "Hammer",
    "Hanging Man",
    "Inverted Hammer",
    "Shooting Star",
    "Bullish Marubozu",
    "Bearish Marubozu",
    "Spinning Top",
    "High-Wave Candle",
    # B. Two-Candle (10)
    "Bullish Engulfing",
    "Bearish Engulfing",
    "Bullish Harami",
    "Bearish Harami",
    "Piercing Line",
    "Dark Cloud Cover",
    "Tweezer Bottom",
    "Tweezer Top",
    "Bullish Kicker",
    "Bearish Kicker",
    # C. Three-Candle (8)
    "Morning Star",
    "Evening Star",
    "Morning Doji Star",
    "Evening Doji Star",
    "Three White Soldiers",
    "Three Black Crows",
    "Three Inside Up",
    "Three Inside Down",
)


def _local_trend(bars: tuple[OHLCVBar, ...], idx: int, lookback: int = 5) -> str:
    """Evaluates short-term trend strictly BEFORE bar idx so Hammer/Hanging Man are honest."""
    start = max(0, idx - lookback)
    if idx - start < 2:
        return "SIDEWAYS"
    first = bars[start].close
    prev = bars[idx - 1].close
    pct = (prev - first) / max(first, 1e-6)
    if pct >= 0.015:
        return "UPTREND"
    if pct <= -0.015:
        return "DOWNTREND"
    return "SIDEWAYS"


class CandlestickPatternDetector:
    """Implements CandlePatternDetectorProtocol covering all 30 candlestick formations."""

    @property
    def supported_patterns(self) -> tuple[str, ...]:
        return CANDLESTICK_PATTERNS

    def detect(self, series: TimeframeSeries) -> list[RawPatternCandidate]:
        bars = series.bars
        n = len(bars)
        if n < 4:
            return []

        found: dict[str, RawPatternCandidate] = {}

        def _add(c: RawPatternCandidate | None) -> None:
            if c is None:
                return
            existing = found.get(c.name)
            # Prefer most recent occurrence, breaking ties by geometry score
            if existing is None or c.end_idx > existing.end_idx or (
                c.end_idx == existing.end_idx and c.geometry_score > existing.geometry_score
            ):
                found[c.name] = c

        # Scan the latest 4 bars so both live forming candles AND recent completed candles
        # (whose breakout confirmation occurs on the following bar) are captured cleanly.
        scan_start = max(2, n - 4)
        for idx in range(scan_start, n):
            atr = series.atr14[idx] if series.atr14 else series.latest_atr
            self._scan_single(series, idx, atr, _add)
            if idx >= 1:
                self._scan_two_candle(series, idx, atr, _add)
            if idx >= 2:
                self._scan_three_candle(series, idx, atr, _add)

        return list(found.values())

    def _mk(
        self,
        series: TimeframeSeries,
        pid: str,
        name: str,
        category: str,
        bias: PatternBias,
        start_idx: int,
        end_idx: int,
        breakout: float,
        invalidation: float,
        target: float,
        score: float,
        notes: str,
        secondary_breakout: float | None = None,
    ) -> RawPatternCandidate:
        bars = series.bars
        return RawPatternCandidate(
            pattern_id=pid,
            name=name,
            category=category,
            kind=PatternKind.CANDLESTICK,
            bias=bias,
            timeframe=series.timeframe,
            start_idx=start_idx,
            end_idx=end_idx,
            breakout_level=breakout,
            secondary_breakout_level=secondary_breakout,
            invalidation_level=invalidation,
            target_price=max(0.01, target),
            geometry_score=min(20.0, max(10.0, score)),
            geometry_points=tuple((i, bars[i].close) for i in range(start_idx, end_idx + 1)),
            notes=notes,
        )

    # ==================== A. SINGLE-CANDLE (12) ====================

    def _scan_single(
        self, series: TimeframeSeries, i: int, atr: float, add
    ) -> None:
        bars = series.bars
        b = bars[i]
        rng = b.range_size
        br = b.body_ratio
        uw = b.upper_wick / rng
        lw = b.lower_wick / rng
        trend = _local_trend(bars, i)

        # 1-4. Doji family
        if br <= 0.11:
            if lw >= 0.65 and uw <= 0.14:
                add(self._mk(series, "candle_02_dragonfly_doji", "Dragonfly Doji", "Single-Candle", PatternBias.BULLISH, i, i, b.high, b.low, b.high + rng, 17.5, "Long lower tail rejection with flat open/close near high"))
            elif uw >= 0.65 and lw <= 0.14:
                add(self._mk(series, "candle_03_gravestone_doji", "Gravestone Doji", "Single-Candle", PatternBias.BEARISH, i, i, b.low, b.high, b.low - rng, 17.5, "Long upper rejection wick with open/close near low"))
            elif uw >= 0.30 and lw >= 0.30 and rng >= 1.60 * atr:
                add(self._mk(series, "candle_04_long_legged_doji", "Long-Legged Doji", "Single-Candle", PatternBias.NEUTRAL, i, i, b.high, b.low, b.high + rng, 16.5, "High-volatility indecision with long upper & lower wicks", secondary_breakout=b.low))
            else:
                add(self._mk(series, "candle_01_doji", "Doji", "Single-Candle", PatternBias.NEUTRAL, i, i, b.high, b.low, b.high + rng, 15.0, "Open/close parity signaling tug-of-war indecision", secondary_breakout=b.low))

        # 5-6. Hammer (downtrend) vs Hanging Man (uptrend)
        if 0.08 <= br <= 0.38 and b.lower_wick >= 2.0 * max(b.body, 1e-6) and b.upper_wick <= 0.45 * max(b.body, rng * 0.12):
            if trend == "DOWNTREND":
                add(self._mk(series, "candle_05_hammer", "Hammer", "Single-Candle", PatternBias.BULLISH, i, i, b.high, b.low, b.high + 1.5 * rng, 18.0, "Downtrend hammer tail absorbing sell pressure"))
            elif trend == "UPTREND":
                add(self._mk(series, "candle_06_hanging_man", "Hanging Man", "Single-Candle", PatternBias.BEARISH, i, i, b.low, b.high, b.low - 1.5 * rng, 17.0, "Uptrend hanging man warning of supply beneath surface"))

        # 7-8. Inverted Hammer (downtrend) vs Shooting Star (uptrend)
        if 0.08 <= br <= 0.38 and b.upper_wick >= 2.0 * max(b.body, 1e-6) and b.lower_wick <= 0.45 * max(b.body, rng * 0.12):
            if trend == "DOWNTREND":
                add(self._mk(series, "candle_07_inverted_hammer", "Inverted Hammer", "Single-Candle", PatternBias.BULLISH, i, i, b.high, b.low, b.high + 1.5 * rng, 16.5, "Downtrend inverted hammer probing higher liquidity"))
            elif trend == "UPTREND":
                add(self._mk(series, "candle_08_shooting_star", "Shooting Star", "Single-Candle", PatternBias.BEARISH, i, i, b.low, b.high, b.low - 1.5 * rng, 18.0, "Uptrend shooting star sharp rejection at highs"))

        # 9-10. Marubozu
        if br >= 0.85 and b.body >= 1.05 * atr:
            if b.is_bullish:
                add(self._mk(series, "candle_09_bullish_marubozu", "Bullish Marubozu", "Single-Candle", PatternBias.BULLISH, i, i, b.high, b.low, b.close + b.body, 18.5, "Full-body bullish drive with negligible wicks"))
            elif b.is_bearish:
                add(self._mk(series, "candle_10_bearish_marubozu", "Bearish Marubozu", "Single-Candle", PatternBias.BEARISH, i, i, b.low, b.high, b.close - b.body, 18.5, "Full-body bearish liquidation with negligible wicks"))

        # 11-12. Spinning Top & High-Wave Candle
        if 0.11 < br <= 0.34 and uw >= 0.22 and lw >= 0.22:
            if rng >= 1.55 * atr and uw >= 0.30 and lw >= 0.30:
                add(self._mk(series, "candle_12_high_wave", "High-Wave Candle", "Single-Candle", PatternBias.NEUTRAL, i, i, b.high, b.low, b.high + rng, 16.0, "Wide-range violent two-way volatility candle", secondary_breakout=b.low))
            else:
                add(self._mk(series, "candle_11_spinning_top", "Spinning Top", "Single-Candle", PatternBias.NEUTRAL, i, i, b.high, b.low, b.high + rng, 14.5, "Small real body with balanced upper/lower shadows", secondary_breakout=b.low))

    # ==================== B. TWO-CANDLE (10) ====================

    def _scan_two_candle(
        self, series: TimeframeSeries, i: int, atr: float, add
    ) -> None:
        bars = series.bars
        c1, c2 = bars[i - 1], bars[i]
        trend = _local_trend(bars, i - 1)
        span_hi = max(c1.high, c2.high)
        span_lo = min(c1.low, c2.low)
        span = max(span_hi - span_lo, atr)

        # 13-14. Bullish & Bearish Engulfing
        if c1.is_bearish and c2.is_bullish and c2.open <= c1.close * 1.002 and c2.close >= c1.open * 0.998 and c2.body > c1.body * 1.05:
            if trend != "UPTREND":
                add(self._mk(series, "candle_13_bullish_engulfing", "Bullish Engulfing", "Two-Candle", PatternBias.BULLISH, i - 1, i, span_hi, span_lo, span_hi + span, 18.5, "Green candle body fully engulfs prior red candle"))

        if c1.is_bullish and c2.is_bearish and c2.open >= c1.close * 0.998 and c2.close <= c1.open * 1.002 and c2.body > c1.body * 1.05:
            if trend != "DOWNTREND":
                add(self._mk(series, "candle_14_bearish_engulfing", "Bearish Engulfing", "Two-Candle", PatternBias.BEARISH, i - 1, i, span_lo, span_hi, span_lo - span, 18.5, "Red candle body fully engulfs prior green candle"))

        # 15-16. Bullish & Bearish Harami
        if c1.is_bearish and c1.body >= 0.75 * atr and c2.is_bullish and c2.open > c1.close and c2.close < c1.open and c2.body <= c1.body * 0.65:
            if trend != "UPTREND":
                add(self._mk(series, "candle_15_bullish_harami", "Bullish Harami", "Two-Candle", PatternBias.BULLISH, i - 1, i, c1.open, span_lo, c1.open + span, 16.5, "Small bullish inside body pausing bearish momentum"))

        if c1.is_bullish and c1.body >= 0.75 * atr and c2.is_bearish and c2.open < c1.close and c2.close > c1.open and c2.body <= c1.body * 0.65:
            if trend != "DOWNTREND":
                add(self._mk(series, "candle_16_bearish_harami", "Bearish Harami", "Two-Candle", PatternBias.BEARISH, i - 1, i, c1.open, span_hi, c1.open - span, 16.5, "Small bearish inside body stalling rally"))

        # 17-18. Piercing Line & Dark Cloud Cover
        if c1.is_bearish and c1.body >= 0.7 * atr and c2.is_bullish and c2.open < c1.close and c1.midpoint < c2.close < c1.open:
            if trend != "UPTREND":
                add(self._mk(series, "candle_17_piercing_line", "Piercing Line", "Two-Candle", PatternBias.BULLISH, i - 1, i, c1.open, span_lo, c1.open + span, 17.5, "Bullish bar gaps below prior close and pierces >50% of red body"))

        if c1.is_bullish and c1.body >= 0.7 * atr and c2.is_bearish and c2.open > c1.close and c1.open < c2.close < c1.midpoint:
            if trend != "DOWNTREND":
                add(self._mk(series, "candle_18_dark_cloud_cover", "Dark Cloud Cover", "Two-Candle", PatternBias.BEARISH, i - 1, i, c1.open, span_hi, c1.open - span, 17.5, "Bearish bar opens above prior close and drives >50% into green body"))

        # 19-20. Tweezer Bottom & Tweezer Top
        tol = max(0.18 * atr, c1.close * 0.003)
        if c1.is_bearish and c2.is_bullish and abs(c1.low - c2.low) <= tol and trend != "UPTREND":
            add(self._mk(series, "candle_19_tweezer_bottom", "Tweezer Bottom", "Two-Candle", PatternBias.BULLISH, i - 1, i, span_hi, span_lo, span_hi + span, 17.0, f"Matched double-tap floor near ${span_lo:.2f}"))

        if c1.is_bullish and c2.is_bearish and abs(c1.high - c2.high) <= tol and trend != "DOWNTREND":
            add(self._mk(series, "candle_20_tweezer_top", "Tweezer Top", "Two-Candle", PatternBias.BEARISH, i - 1, i, span_lo, span_hi, span_lo - span, 17.0, f"Matched double-tap rejection near ${span_hi:.2f}"))

        # 21-22. Bullish & Bearish Kicker
        if c1.is_bearish and c1.body_ratio >= 0.55 and c2.is_bullish and c2.body_ratio >= 0.55 and c2.open >= c1.open * 1.001 and c2.low >= c1.open * 0.995:
            add(self._mk(series, "candle_21_bullish_kicker", "Bullish Kicker", "Two-Candle", PatternBias.BULLISH, i - 1, i, c2.high, c1.low, c2.high + span, 19.0, "Violent gap-up sentiment reversal above prior open"))

        if c1.is_bullish and c1.body_ratio >= 0.55 and c2.is_bearish and c2.body_ratio >= 0.55 and c2.open <= c1.open * 0.999 and c2.high <= c1.open * 1.005:
            add(self._mk(series, "candle_22_bearish_kicker", "Bearish Kicker", "Two-Candle", PatternBias.BEARISH, i - 1, i, c2.low, c1.high, c2.low - span, 19.0, "Violent gap-down sentiment reversal below prior open"))

    # ==================== C. THREE-CANDLE (8) ====================

    def _scan_three_candle(
        self, series: TimeframeSeries, i: int, atr: float, add
    ) -> None:
        bars = series.bars
        c1, c2, c3 = bars[i - 2], bars[i - 1], bars[i]
        trend = _local_trend(bars, i - 2)
        span_hi = max(c1.high, c2.high, c3.high)
        span_lo = min(c1.low, c2.low, c3.low)
        span = max(span_hi - span_lo, atr)

        # 23 & 25. Morning Star / Morning Doji Star
        if (
            c1.is_bearish
            and c1.body >= 0.65 * atr
            and c2.body <= c1.body * 0.40
            and max(c2.open, c2.close) <= c1.close * 1.01
            and c3.is_bullish
            and c3.close >= c1.midpoint
            and trend != "UPTREND"
        ):
            if c2.body_ratio <= 0.12:
                add(self._mk(series, "candle_25_morning_doji_star", "Morning Doji Star", "Three-Candle", PatternBias.BULLISH, i - 2, i, span_hi, span_lo, span_hi + span, 19.0, "3-bar reversal anchored by low-range Doji star"))
            else:
                add(self._mk(series, "candle_23_morning_star", "Morning Star", "Three-Candle", PatternBias.BULLISH, i - 2, i, span_hi, span_lo, span_hi + span, 18.5, "3-bar bullish reversal reclaiming >50% of first red bar"))

        # 24 & 26. Evening Star / Evening Doji Star
        if (
            c1.is_bullish
            and c1.body >= 0.65 * atr
            and c2.body <= c1.body * 0.40
            and min(c2.open, c2.close) >= c1.close * 0.99
            and c3.is_bearish
            and c3.close <= c1.midpoint
            and trend != "DOWNTREND"
        ):
            if c2.body_ratio <= 0.12:
                add(self._mk(series, "candle_26_evening_doji_star", "Evening Doji Star", "Three-Candle", PatternBias.BEARISH, i - 2, i, span_lo, span_hi, span_lo - span, 19.0, "3-bar bearish reversal anchored by top Doji star"))
            else:
                add(self._mk(series, "candle_24_evening_star", "Evening Star", "Three-Candle", PatternBias.BEARISH, i - 2, i, span_lo, span_hi, span_lo - span, 18.5, "3-bar bearish reversal breaking below >50% of green bar"))

        # 27. Three White Soldiers
        if (
            c1.is_bullish and c2.is_bullish and c3.is_bullish
            and c1.body_ratio >= 0.55 and c2.body_ratio >= 0.55 and c3.body_ratio >= 0.55
            and c1.close < c2.close < c3.close
            and c1.open <= c2.open <= c1.close * 1.01
            and c2.open <= c3.open <= c2.close * 1.01
        ):
            add(self._mk(series, "candle_27_three_white_soldiers", "Three White Soldiers", "Three-Candle", PatternBias.BULLISH, i - 2, i, c3.high, c1.low, c3.high + span, 18.5, "3 consecutive strong bullish advances with higher closes"))

        # 28. Three Black Crows
        if (
            c1.is_bearish and c2.is_bearish and c3.is_bearish
            and c1.body_ratio >= 0.55 and c2.body_ratio >= 0.55 and c3.body_ratio >= 0.55
            and c1.close > c2.close > c3.close
            and c1.close * 0.99 <= c2.open <= c1.open
            and c2.close * 0.99 <= c3.open <= c2.open
        ):
            add(self._mk(series, "candle_28_three_black_crows", "Three Black Crows", "Three-Candle", PatternBias.BEARISH, i - 2, i, c3.low, c1.high, c3.low - span, 18.5, "3 consecutive strong bearish breakdowns with lower closes"))

        # 29. Three Inside Up
        if (
            c1.is_bearish and c1.body >= 0.6 * atr
            and c2.is_bullish and c2.open > c1.close and c2.close < c1.open
            and c3.is_bullish and c3.close > c1.open
        ):
            add(self._mk(series, "candle_29_three_inside_up", "Three Inside Up", "Three-Candle", PatternBias.BULLISH, i - 2, i, c3.high, span_lo, c3.high + span, 18.5, "Bullish Harami confirmed by bar-3 close above bar-1 open"))

        # 30. Three Inside Down
        if (
            c1.is_bullish and c1.body >= 0.6 * atr
            and c2.is_bearish and c2.open < c1.close and c2.close > c1.open
            and c3.is_bearish and c3.close < c1.open
        ):
            add(self._mk(series, "candle_30_three_inside_down", "Three Inside Down", "Three-Candle", PatternBias.BEARISH, i - 2, i, c3.low, span_hi, c3.low - span, 18.5, "Bearish Harami confirmed by bar-3 close below bar-1 open"))
