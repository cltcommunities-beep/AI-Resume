#!/usr/bin/env python3
"""MVVMC Coordinator & Fast 1-Command CLI for the tradingChart 70-Pattern Engine."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from trading_chart_engine.candle_patterns import CandlestickPatternDetector
from trading_chart_engine.chart_patterns import PriceChartPatternDetector
from trading_chart_engine.contracts import (
    CandlePatternDetectorProtocol,
    ChartHtmlRendererProtocol,
    ChartPatternDetectorProtocol,
    MarketDataProviderProtocol,
    PatternValidatorProtocol,
    SwingPivotExtractorProtocol,
    TradingChartViewModelProtocol,
)
from trading_chart_engine.html_renderer import ReusableHtmlChartRenderer
from trading_chart_engine.models import (
    PatternLifecycleState,
    Timeframe,
    TradingChartReport,
    ValidatedPattern,
)
from trading_chart_engine.pivots import ATRPivotExtractor
from trading_chart_engine.robinhood_adapter import RobinhoodMarketDataAdapter
from trading_chart_engine.validator import InstitutionalPatternValidator
from trading_chart_engine.viewmodel import TradingChartViewModel

_STATE_ICON = {
    PatternLifecycleState.CONFIRMED_BREAKOUT: "🟢",
    PatternLifecycleState.FORMING: "🟡",
    PatternLifecycleState.FAILED_BREAKOUT: "🟠",
    PatternLifecycleState.INVALIDATED: "🔴",
}

_VALIDATOR_SCRIPT = Path(__file__).resolve().parent.parent / "validate_chart_contract.py"


def _load_json_opt(path: str | None) -> Any:
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def _to_f(val: Any, default: float = 0.0) -> float:
    try:
        return float(val) if val not in (None, "") else default
    except (TypeError, ValueError):
        return default


def _extract_quote_map(raw_quotes: Any) -> dict[str, dict[str, Any]]:
    """Extracts symbol -> normalized quote dict from raw Robinhood get_equity_quotes output."""
    out: dict[str, dict[str, Any]] = {}
    if not isinstance(raw_quotes, dict):
        return out
    data = raw_quotes.get("data", raw_quotes)
    rows = data.get("results", []) if isinstance(data, dict) else []
    for row in rows:
        if not isinstance(row, dict):
            continue
        q = row.get("quote", row)
        if not isinstance(q, dict) or not q.get("symbol"):
            continue
        sym = str(q["symbol"]).upper()
        reg = _to_f(q.get("last_trade_price"))
        ext = _to_f(q.get("last_non_reg_trade_price", q.get("last_extended_hours_trade_price")))
        reg_t = str(q.get("venue_last_trade_time") or "")
        ext_t = str(q.get("venue_last_non_reg_trade_time") or "")
        cur = ext if (ext > 0 and (not reg_t or ext_t > reg_t)) else (reg if reg > 0 else ext)
        prev = _to_f(q.get("adjusted_previous_close", q.get("previous_close")), cur)
        pct = ((cur - prev) / prev * 100.0) if prev > 0 else 0.0
        out[sym] = {
            "symbol": sym,
            "cur": cur,
            "reg": reg if reg > 0 else cur,
            "prev": prev,
            "pct": pct,
            "ts": ext_t if cur == ext else reg_t,
            "raw": q,
        }
    return out


def _extract_symbol_bars(raw_hist: Any, symbol: str) -> list[dict[str, Any]]:
    if not raw_hist:
        return []
    if isinstance(raw_hist, list):
        return raw_hist
    if isinstance(raw_hist, dict):
        data = raw_hist.get("data", raw_hist)
        results = data.get("results", []) if isinstance(data, dict) else []
        if isinstance(results, list) and results:
            for item in results:
                if isinstance(item, dict) and str(item.get("symbol", "")).upper() == symbol.upper():
                    return list(item.get("bars", item.get("historicals", [])))
            first = results[0]
            if isinstance(first, dict):
                return list(first.get("bars", first.get("historicals", [])))
        if isinstance(data, dict):
            for key in ("bars", "historicals"):
                if isinstance(data.get(key), list):
                    return list(data[key])
    return []


def _extract_symbol_fundamentals(raw_fund: Any, symbol: str) -> dict[str, Any] | None:
    if not isinstance(raw_fund, dict):
        return None
    data = raw_fund.get("data", raw_fund)
    results = data.get("results", []) if isinstance(data, dict) else []
    if isinstance(results, list) and results:
        for item in results:
            if isinstance(item, dict) and str(item.get("symbol", "")).upper() == symbol.upper():
                return item
        if isinstance(results[0], dict):
            return results[0]
    return data if isinstance(data, dict) else None


def _extract_symbol_l2(raw_l2: Any, symbol: str) -> dict[str, Any] | None:
    if not isinstance(raw_l2, dict):
        return None
    data = raw_l2.get("data", raw_l2)
    books = data.get("books", []) if isinstance(data, dict) else []
    if isinstance(books, list) and books:
        for b in books:
            if isinstance(b, dict) and str(b.get("symbol", "")).upper() == symbol.upper():
                return b
        if isinstance(books[0], dict):
            return books[0]
    return data if isinstance(data, dict) else None


def _extract_account_info(raw_pos: Any, raw_port: Any, symbol: str) -> dict[str, float]:
    info = {"quantity": 0.0, "average_buy_price": 0.0, "buying_power": 0.0, "total_value": 0.0}
    if isinstance(raw_pos, dict):
        data = raw_pos.get("data", raw_pos)
        rows = data.get("positions", data.get("results", [])) if isinstance(data, dict) else []
        for p in rows:
            if isinstance(p, dict) and str(p.get("symbol", "")).upper() == symbol.upper():
                info["quantity"] = _to_f(p.get("quantity"))
                info["average_buy_price"] = _to_f(p.get("average_buy_price"))
                break
    if isinstance(raw_port, dict):
        data = raw_port.get("data", raw_port)
        if isinstance(data, dict):
            info["total_value"] = _to_f(data.get("total_value"))
            bp = data.get("buying_power")
            if isinstance(bp, dict):
                info["buying_power"] = _to_f(bp.get("buying_power"), _to_f(data.get("cash")))
            else:
                info["buying_power"] = _to_f(bp, _to_f(data.get("cash")))
    return info


def _extract_vix_and_weather(raw_idx: Any, qmap: dict[str, dict[str, Any]]) -> tuple[float | None, str]:
    vix = None
    if isinstance(raw_idx, dict):
        data = raw_idx.get("data", raw_idx)
        for q in data.get("quotes", []) if isinstance(data, dict) else []:
            if isinstance(q, dict) and str(q.get("symbol", "")).upper() == "VIX":
                vix = _to_f(q.get("value"), 0.0) or None
    xlk = qmap.get("XLK", {}).get("pct", 0.0)
    xlp = qmap.get("XLP", {}).get("pct", 0.0)
    tlt = qmap.get("TLT", {}).get("pct", 0.0)
    if vix is not None and vix > 25.0:
        return vix, "🔴 STORM ACTIVE (Flight-to-Safety)"
    if (xlp - xlk) >= 2.5 or (tlt > 0.25 and xlk < -0.5):
        return vix, "🟡 STORM CLOUDS (Early Rotation)"
    return vix, "🟢 SUNNY (Risk-On Tape)"


def _synthesize_period_tail(
    daily_bars: list[dict[str, Any]],
    period_bars: list[dict[str, Any]],
    live_price: float,
    period: str,
) -> list[dict[str, Any]]:
    """Appends accurate live in-progress Weekly or Monthly bar from completed Daily bars + live tick."""
    clean_d = [b for b in daily_bars if not b.get("interpolated")]
    clean_p = [b for b in period_bars if not b.get("interpolated")]
    if not clean_d or not clean_p:
        return clean_p
    last_p_date = str(clean_p[-1].get("begins_at", clean_p[-1].get("timestamp", "")))[:10]
    last_d_date = str(clean_d[-1].get("begins_at", clean_d[-1].get("timestamp", "")))[:10]
    if last_d_date <= last_p_date:
        return clean_p

    if period == "week":
        # Anchor Monday of the latest daily bar's week
        try:
            dt = datetime.fromisoformat(last_d_date)
            monday = dt.fromordinal(dt.toordinal() - dt.weekday()).strftime("%Y-%m-%d")
        except ValueError:
            monday = last_d_date
        if monday <= last_p_date:
            return clean_p
        tail = [b for b in clean_d if str(b.get("begins_at", b.get("timestamp", "")))[:10] >= monday]
        anchor = f"{monday}T00:00:00Z"
    else:
        month_start = f"{last_d_date[:7]}-01"
        if month_start <= last_p_date:
            return clean_p
        tail = [b for b in clean_d if str(b.get("begins_at", b.get("timestamp", "")))[:10] >= month_start]
        anchor = f"{month_start}T00:00:00Z"

    if not tail:
        return clean_p
    o_val = _to_f(tail[0].get("open_price", tail[0].get("open_value", tail[0].get("open"))))
    h_val = max(max(_to_f(x.get("high_price", x.get("high_value", x.get("high")))) for x in tail), live_price or o_val)
    l_val = min(min(_to_f(x.get("low_price", x.get("low_value", x.get("low")))) for x in tail), live_price or o_val)
    c_val = live_price if live_price > 0 else _to_f(tail[-1].get("close_price", tail[-1].get("close_value", tail[-1].get("close"))))
    v_val = sum(_to_f(x.get("volume")) for x in tail)
    return [
        *clean_p,
        {
            "begins_at": anchor,
            "open_price": f"{o_val:.6f}",
            "high_price": f"{h_val:.6f}",
            "low_price": f"{l_val:.6f}",
            "close_price": f"{c_val:.6f}",
            "volume": v_val,
            "is_live_incomplete": True,
        },
    ]


class TradingChartCoordinator:
    """Protocol-driven MVVMC Coordinator with full Dependency Injection."""

    def __init__(
        self,
        data_provider: MarketDataProviderProtocol | None = None,
        pivot_extractor: SwingPivotExtractorProtocol | None = None,
        chart_detector: ChartPatternDetectorProtocol | None = None,
        candle_detector: CandlePatternDetectorProtocol | None = None,
        validator: PatternValidatorProtocol | None = None,
        viewmodel: TradingChartViewModelProtocol | None = None,
        html_renderer: ChartHtmlRendererProtocol | None = None,
    ) -> None:
        self._data = data_provider or RobinhoodMarketDataAdapter()
        self._pivots = pivot_extractor or ATRPivotExtractor()
        self._chart_detector = chart_detector or PriceChartPatternDetector(self._pivots)
        self._candle_detector = candle_detector or CandlestickPatternDetector()
        self._validator = validator or InstitutionalPatternValidator()
        self._viewmodel = viewmodel or TradingChartViewModel()
        self._html_renderer = html_renderer or ReusableHtmlChartRenderer()

    @property
    def catalog_counts(self) -> tuple[int, int, int]:
        c40 = len(self._chart_detector.supported_patterns)
        k30 = len(self._candle_detector.supported_patterns)
        return c40, k30, c40 + k30

    def run_scan_with_context(
        self, payload: dict[str, Any]
    ) -> tuple[TradingChartReport, dict[str, Any]]:
        symbol, as_of, live_price, market_value, all_series, l2_book = self._data.build_series_bundle(payload)
        macro_note = str(
            payload.get(
                "macro_gate_note",
                "Verify Tier-0 Weather Light & 72h Macro Calendar Gate before acting on any breakout.",
            )
        )

        validated_all: list[ValidatedPattern] = []
        for tf in (Timeframe.DAILY, Timeframe.WEEKLY, Timeframe.MONTHLY):
            series = all_series.get(tf)
            if not series or len(series.bars) < 4:
                continue
            swings = self._pivots.extract_swings(series, window=2)
            sr_levels = self._pivots.cluster_sr_levels(series, swings)

            candidates = []
            candidates.extend(self._chart_detector.detect(series, swings))
            candidates.extend(self._candle_detector.detect(series))

            for cand in candidates:
                validated_all.append(
                    self._validator.validate(cand, series, all_series, sr_levels, l2_book)
                )

        report = self._viewmodel.build_report(
            symbol=symbol,
            as_of=as_of,
            live_price=live_price,
            market_value=market_value,
            all_series=all_series,
            validated=validated_all,
            macro_gate_note=macro_note,
        )
        ctx = {
            "all_series": all_series,
            "l2_book": l2_book,
            "is_market": bool(payload.get("is_market", False)),
            "change_pct": payload.get("change_pct", 0.0),
            "reg_close": payload.get("reg_close", live_price),
            "as_of_short": payload.get("as_of_short", as_of[:16]),
            "vix": payload.get("vix"),
            "weather_tag": payload.get("weather_tag", "Check Tier-0 Weather Light"),
            "account": payload.get("account", {}),
            "peers": payload.get("peers", []),
            "corporate_events": payload.get("corporate_events", []),
            "today_bars": payload.get("today_bars"),
            "two_day_bars": payload.get("two_day_bars"),
            "horizons": payload.get("horizons"),
        }
        return report, ctx

    def run_scan(self, payload: dict[str, Any]) -> TradingChartReport:
        report, _ = self.run_scan_with_context(payload)
        return report

    def render_html(self, report: TradingChartReport, render_ctx: dict[str, Any]) -> str:
        return self._html_renderer.render(report, render_ctx)

    @staticmethod
    def format_markdown(report: TradingChartReport, max_rows: int = 18) -> str:
        mv_str = f"`${report.market_value:.2f}`" if report.market_value is not None else "`N/A`"
        lines = [
            f"### 📈 `tradingChart` 70-Pattern Scan — `{report.symbol}` (`{report.as_of}`)",
            f"* **Live Price:** `${report.live_price:.2f}` · **Wall St Market Value:** {mv_str}",
            f"* **Macro Safety Overlay:** {report.macro_gate_note}",
            "",
            "| Timeframe | Bars | Trend | RSI-14 | Confirmed | Forming | Failed | Invalidated |",
            "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
        ]
        for tf_name, info in report.timeframe_summaries.items():
            cnt = info["counts"]
            rsi_s = f"`{info['rsi14']:.1f}`" if info["rsi14"] is not None else "`N/A`"
            lines.append(
                f"| `{tf_name}` | `{info['bar_count']}` | `{info['trend_direction']}` | {rsi_s} | "
                f"`{cnt['confirmed_breakout']}` | `{cnt['forming']}` | `{cnt['failed_breakout']}` | `{cnt['invalidated']}` |"
            )

        lines.extend(
            [
                "",
                "| Timeframe | Pattern Detected | Type & Bias | Lifecycle Status | Confidence | Trigger / Invalidation / Target | 5-Factor Validation Note |",
                "| :---: | :--- | :--- | :---: | :---: | :--- | :--- |",
            ]
        )
        if not report.detections:
            lines.append("| `All` | No qualifying pattern detected | — | — | `—` | — | Clean tape; no forced signals |")
        else:
            for item in report.detections[:max_rows]:
                c = item.candidate
                v = item.validation
                icon = _STATE_ICON[item.lifecycle_state]
                cap_tag = " *(Live)*" if item.is_live_incomplete_capped else ""
                lines.append(
                    f"| `{c.timeframe.value}` | **{c.name}** | `{c.kind.value}` · `{item.resolved_bias.value}` | "
                    f"{icon} `{item.lifecycle_state.value}`{cap_tag} | **`{v.total_score:.1f}/100`** | "
                    f"Trig `${c.breakout_level:.2f}` · Inv `${c.invalidation_level:.2f}` · Tgt `${c.target_price:.2f}` | "
                    f"Vol `{v.volume_ratio:.2f}x` · {v.l2_alignment_note} · {v.mtf_note} |"
                )
        return "\n".join(lines)


def _assemble_payload_from_cli(args: argparse.Namespace) -> dict[str, Any]:
    if args.input:
        return json.loads(Path(args.input).read_text(encoding="utf-8"))

    sym = (args.symbol or "UNKNOWN").upper()
    quotes_raw = _load_json_opt(args.quotes)
    qmap = _extract_quote_map(quotes_raw)
    sym_q = qmap.get(sym, {})
    fund = _extract_symbol_fundamentals(_load_json_opt(args.fundamentals), sym)
    l2 = _extract_symbol_l2(_load_json_opt(args.l2), sym)
    idx_raw = _load_json_opt(args.index_quotes)
    acct = _extract_account_info(_load_json_opt(args.positions), _load_json_opt(args.portfolio), sym)

    daily_bars = _extract_symbol_bars(_load_json_opt(args.daily), sym)
    weekly_bars = _extract_symbol_bars(_load_json_opt(args.weekly), sym)
    monthly_bars = _extract_symbol_bars(_load_json_opt(args.monthly), sym)

    live_price = sym_q.get("cur", 0.0)
    reg_close = sym_q.get("reg", live_price)
    if live_price <= 0 and isinstance(idx_raw, dict):
        idata = idx_raw.get("data", idx_raw)
        for iq in idata.get("quotes", []) if isinstance(idata, dict) else []:
            if isinstance(iq, dict) and str(iq.get("symbol", "")).upper() == sym:
                live_price = _to_f(iq.get("value"))
                reg_close = live_price
                break

    # Append completed RTH session bar from fundamentals if daily_bars hasn't rolled yet
    if daily_bars and fund and fund.get("market_date"):
        m_date = str(fund["market_date"])[:10]
        last_d = str(daily_bars[-1].get("begins_at", daily_bars[-1].get("timestamp", "")))[:10]
        if m_date > last_d and _to_f(fund.get("open")) > 0 and reg_close > 0:
            daily_bars = [
                *daily_bars,
                {
                    "begins_at": f"{m_date}T00:00:00Z",
                    "open_price": str(fund["open"]),
                    "high_price": str(fund.get("high", max(_to_f(fund["open"]), reg_close))),
                    "low_price": str(fund.get("low", min(_to_f(fund["open"]), reg_close))),
                    "close_price": f"{reg_close:.6f}",
                    "volume": _to_f(fund.get("volume")),
                    "interpolated": False,
                    "is_live_incomplete": False,
                },
            ]

    weekly_bars = _synthesize_period_tail(daily_bars, weekly_bars, live_price, "week")
    monthly_bars = _synthesize_period_tail(daily_bars, monthly_bars, live_price, "month")

    vix_val, weather_tag = _extract_vix_and_weather(idx_raw, qmap)
    peer_syms = [p.strip().upper() for p in (args.peers or "").split(",") if p.strip()]
    peers = [
        {"symbol": ps, "price": qmap[ps]["cur"], "pct": qmap[ps]["pct"]}
        for ps in peer_syms
        if ps in qmap
    ]

    market_value = None
    if fund:
        mc = _to_f(fund.get("market_cap"))
        shs = _to_f(fund.get("shares_outstanding"))
        if mc > 0 and shs > 0:
            market_value = mc / shs

    as_of = sym_q.get("ts") or datetime.now(timezone.utc).isoformat()
    macro_note = args.macro_note or (
        f"{weather_tag}" + (f" (VIX {vix_val:.2f})" if vix_val is not None else "") +
        " · Verify 72h Tier-1 Macro/Earnings Calendar before execution."
    )

    return {
        "symbol": sym,
        "as_of": as_of,
        "as_of_short": str(as_of)[:16].replace("T", " "),
        "live_price": live_price,
        "reg_close": reg_close,
        "change_pct": sym_q.get("pct", 0.0),
        "market_value": market_value,
        "daily": daily_bars,
        "weekly": weekly_bars,
        "monthly": monthly_bars,
        "l2_book": l2,
        "vix": vix_val,
        "weather_tag": weather_tag,
        "macro_gate_note": macro_note,
        "account": acct,
        "peers": peers,
        "is_market": bool(getattr(args, "market", False)),
    }


def main(argv: list[str] | None = None) -> int:
    t0 = time.perf_counter()
    parser = argparse.ArgumentParser(description="Fast 1-Command tradingChart 70-Pattern Engine & HTML Renderer.")
    parser.add_argument("--input", help="Pre-assembled JSON bundle path (legacy/direct mode).")
    parser.add_argument("--symbol", help="Target ticker symbol for direct Robinhood MCP file mode.")
    parser.add_argument("--daily", help="Raw Robinhood get_equity_historicals (day) JSON path.")
    parser.add_argument("--weekly", help="Raw Robinhood get_equity_historicals (week) JSON path.")
    parser.add_argument("--monthly", help="Raw Robinhood get_equity_historicals (month) JSON path.")
    parser.add_argument("--quotes", help="Raw Robinhood get_equity_quotes JSON path.")
    parser.add_argument("--l2", help="Raw Robinhood get_equity_price_book JSON path.")
    parser.add_argument("--fundamentals", help="Raw Robinhood get_equity_fundamentals JSON path.")
    parser.add_argument("--positions", help="Raw Robinhood get_equity_positions JSON path.")
    parser.add_argument("--portfolio", help="Raw Robinhood get_portfolio JSON path.")
    parser.add_argument("--index-quotes", help="Raw Robinhood get_index_quotes JSON path.")
    parser.add_argument("--peers", default="", help="Comma-separated peer ticker symbols.")
    parser.add_argument("--macro-note", default="", help="Optional custom Tier-0 macro/calendar banner note.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", help="Optional path to save Markdown/JSON scan report.")
    parser.add_argument("--html-out", help="Optional path to render reusable 8/8 validated HTML5 chart.")
    parser.add_argument("--market", action="store_true", help="Enable Broad Market (Breadth/Credit/VIX/Rotation) mode.")
    parser.add_argument("--validate", action="store_true", help="Automatically run validate_chart_contract.py on --html-out.")
    args = parser.parse_args(argv)

    if not args.input and not args.symbol:
        parser.error("Provide either --input <bundle.json> or --symbol <TICKER> with MCP JSON files.")

    payload = _assemble_payload_from_cli(args)
    coord = TradingChartCoordinator()
    report, ctx = coord.run_scan_with_context(payload)

    if args.html_out:
        html_str = coord.render_html(report, ctx)
        Path(args.html_out).write_text(html_str, encoding="utf-8")

    out = (
        json.dumps(report.to_dict(), indent=2)
        if args.format == "json"
        else coord.format_markdown(report)
    )
    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        print(out)

    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    print(f"\n⚡ Engine + Renderer runtime: {elapsed_ms:.1f} ms", file=sys.stderr)

    if args.html_out and args.validate and _VALIDATOR_SCRIPT.exists():
        cmd = [sys.executable, str(_VALIDATOR_SCRIPT), args.html_out, report.symbol]
        if args.market:
            cmd.append("--market")
        if args.peers:
            cmd.extend(["--peers", args.peers])
        proc = subprocess.run(cmd, check=False)
        return proc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
