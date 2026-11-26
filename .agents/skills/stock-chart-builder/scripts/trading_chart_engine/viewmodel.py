"""MVVM ViewModel — ranks validated patterns, builds timeframe summaries, and exports Canvas overlays."""

from __future__ import annotations

from typing import Any

from .models import (
    PatternLifecycleState,
    Timeframe,
    TimeframeSeries,
    TradingChartReport,
    ValidatedPattern,
)

_STATE_PRIORITY = {
    PatternLifecycleState.CONFIRMED_BREAKOUT: 0,
    PatternLifecycleState.FORMING: 1,
    PatternLifecycleState.FAILED_BREAKOUT: 2,
    PatternLifecycleState.INVALIDATED: 3,
}

_STATE_BADGE_COLORS = {
    PatternLifecycleState.CONFIRMED_BREAKOUT: "#10b981",
    PatternLifecycleState.FORMING: "#f59e0b",
    PatternLifecycleState.FAILED_BREAKOUT: "#f97316",
    PatternLifecycleState.INVALIDATED: "#ef4444",
}


class TradingChartViewModel:
    """Implements TradingChartViewModelProtocol."""

    def build_report(
        self,
        symbol: str,
        as_of: str,
        live_price: float,
        market_value: float | None,
        all_series: dict[Timeframe, TimeframeSeries],
        validated: list[ValidatedPattern],
        macro_gate_note: str = "Verify Tier-0 Weather Light & 72h Macro Calendar before execution.",
    ) -> TradingChartReport:
        ranked = sorted(
            validated,
            key=lambda v: (
                _STATE_PRIORITY.get(v.lifecycle_state, 9),
                -v.validation.total_score,
                v.candidate.timeframe.value,
                v.candidate.name,
            ),
        )

        tf_summaries: dict[str, dict[str, Any]] = {}
        overlays: dict[str, list[dict[str, Any]]] = {}

        for tf in (Timeframe.DAILY, Timeframe.WEEKLY, Timeframe.MONTHLY):
            s = all_series.get(tf)
            if not s or not s.bars:
                continue
            tf_items = [v for v in ranked if v.candidate.timeframe == tf]
            last = s.bars[-1]
            tf_summaries[tf.value] = {
                "bar_count": len(s.bars),
                "latest_timestamp": last.timestamp,
                "latest_close": round(last.close, 4),
                "is_live_incomplete": last.is_live_incomplete,
                "trend_direction": s.trend_direction,
                "rsi14": round(s.rsi14, 2) if s.rsi14 is not None else None,
                "sma20": round(s.sma20[-1], 4) if s.sma20 and s.sma20[-1] is not None else None,
                "sma50": round(s.sma50[-1], 4) if s.sma50 and s.sma50[-1] is not None else None,
                "sma200": round(s.sma200[-1], 4) if s.sma200 and s.sma200[-1] is not None else None,
                "counts": {
                    "confirmed_breakout": sum(1 for v in tf_items if v.lifecycle_state == PatternLifecycleState.CONFIRMED_BREAKOUT),
                    "forming": sum(1 for v in tf_items if v.lifecycle_state == PatternLifecycleState.FORMING),
                    "failed_breakout": sum(1 for v in tf_items if v.lifecycle_state == PatternLifecycleState.FAILED_BREAKOUT),
                    "invalidated": sum(1 for v in tf_items if v.lifecycle_state == PatternLifecycleState.INVALIDATED),
                },
            }
            # Export top 6 highest-signal patterns per timeframe for clean HTML5 Canvas rendering
            overlays[tf.value] = [
                {
                    "pattern_id": v.candidate.pattern_id,
                    "name": v.candidate.name,
                    "kind": v.candidate.kind.value,
                    "bias": v.resolved_bias.value,
                    "lifecycle_state": v.lifecycle_state.value,
                    "badge_color": _STATE_BADGE_COLORS[v.lifecycle_state],
                    "confidence_score": round(v.validation.total_score, 1),
                    "breakout_level": round(v.candidate.breakout_level, 4),
                    "invalidation_level": round(v.candidate.invalidation_level, 4),
                    "target_price": round(v.candidate.target_price, 4),
                    "geometry_points": [[idx, round(pr, 4)] for idx, pr in v.candidate.geometry_points],
                }
                for v in tf_items[:6]
            ]

        return TradingChartReport(
            symbol=symbol,
            as_of=as_of,
            live_price=live_price,
            market_value=market_value,
            timeframe_summaries=tf_summaries,
            detections=tuple(ranked),
            canvas_overlays=overlays,
            macro_gate_note=macro_gate_note,
        )
