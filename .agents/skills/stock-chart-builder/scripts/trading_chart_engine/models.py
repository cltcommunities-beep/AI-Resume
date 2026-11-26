"""Domain models for the tradingChart 70-Pattern Detection Engine (MVVM Model Layer)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Timeframe(str, Enum):
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"


class PatternKind(str, Enum):
    PRICE_CHART = "Price Chart"
    CANDLESTICK = "Candlestick"


class PatternBias(str, Enum):
    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"


class PatternLifecycleState(str, Enum):
    FORMING = "Forming"
    CONFIRMED_BREAKOUT = "Confirmed Breakout"
    FAILED_BREAKOUT = "Failed Breakout"
    INVALIDATED = "Invalidated"


@dataclass(frozen=True)
class OHLCVBar:
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    interpolated: bool = False
    is_live_incomplete: bool = False

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def signed_body(self) -> float:
        return self.close - self.open

    @property
    def range_size(self) -> float:
        return max(self.high - self.low, 1e-9)

    @property
    def upper_wick(self) -> float:
        return max(self.high - max(self.open, self.close), 0.0)

    @property
    def lower_wick(self) -> float:
        return max(min(self.open, self.close) - self.low, 0.0)

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    @property
    def body_ratio(self) -> float:
        return self.body / self.range_size

    @property
    def midpoint(self) -> float:
        return (self.open + self.close) / 2.0


@dataclass(frozen=True)
class L2Wall:
    price: float
    shares: float
    notional_usd: float
    side: str  # "bid" or "ask"


@dataclass(frozen=True)
class L2OrderBookSnapshot:
    spot: float
    bid_walls: tuple[L2Wall, ...] = ()
    ask_walls: tuple[L2Wall, ...] = ()
    near_bid_usd: float = 0.0
    near_ask_usd: float = 0.0

    @property
    def bid_ask_ratio(self) -> float:
        if self.near_ask_usd <= 0:
            return 1.0
        return self.near_bid_usd / self.near_ask_usd


@dataclass(frozen=True)
class SwingPoint:
    index: int
    timestamp: str
    price: float
    kind: str  # "HIGH" or "LOW"


@dataclass(frozen=True)
class TrendLine:
    start_idx: int
    start_price: float
    end_idx: int
    end_price: float
    slope: float
    intercept: float
    r_squared: float

    def value_at(self, idx: int) -> float:
        return self.slope * idx + self.intercept


@dataclass(frozen=True)
class TimeframeSeries:
    symbol: str
    timeframe: Timeframe
    bars: tuple[OHLCVBar, ...]
    sma20: tuple[float | None, ...] = ()
    sma50: tuple[float | None, ...] = ()
    sma200: tuple[float | None, ...] = ()
    atr14: tuple[float, ...] = ()
    vol_sma20: tuple[float, ...] = ()
    rsi14: float | None = None
    trend_direction: str = "SIDEWAYS"  # "UPTREND", "DOWNTREND", "SIDEWAYS"

    @property
    def latest_bar(self) -> OHLCVBar | None:
        return self.bars[-1] if self.bars else None

    @property
    def latest_atr(self) -> float:
        if self.atr14:
            return max(self.atr14[-1], 1e-6)
        if self.bars:
            return max(self.bars[-1].range_size, 1e-6)
        return 1.0


@dataclass(frozen=True)
class RawPatternCandidate:
    pattern_id: str
    name: str
    category: str
    kind: PatternKind
    bias: PatternBias
    timeframe: Timeframe
    start_idx: int
    end_idx: int
    breakout_level: float
    invalidation_level: float
    target_price: float
    geometry_score: float  # 0.0 to 20.0
    geometry_points: tuple[tuple[int, float], ...] = ()
    secondary_breakout_level: float | None = None  # For bilateral patterns (lower rail)
    notes: str = ""


@dataclass(frozen=True)
class ValidationBreakdown:
    geometry_score: float
    volume_score: float
    breakout_score: float
    sr_l2_score: float
    mtf_trend_score: float
    total_score: float
    volume_ratio: float
    breakout_buffer_atr: float
    l2_alignment_note: str
    mtf_note: str


@dataclass(frozen=True)
class ValidatedPattern:
    candidate: RawPatternCandidate
    lifecycle_state: PatternLifecycleState
    resolved_bias: PatternBias
    validation: ValidationBreakdown
    is_live_incomplete_capped: bool = False
    action_summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        c = self.candidate
        v = self.validation
        return {
            "pattern_id": c.pattern_id,
            "name": c.name,
            "category": c.category,
            "kind": c.kind.value,
            "bias": self.resolved_bias.value,
            "lifecycle_state": self.lifecycle_state.value,
            "timeframe": c.timeframe.value,
            "start_idx": c.start_idx,
            "end_idx": c.end_idx,
            "breakout_level": round(c.breakout_level, 4),
            "invalidation_level": round(c.invalidation_level, 4),
            "target_price": round(c.target_price, 4),
            "confidence_score": round(v.total_score, 1),
            "scores": {
                "geometry": round(v.geometry_score, 1),
                "volume": round(v.volume_score, 1),
                "breakout": round(v.breakout_score, 1),
                "sr_l2": round(v.sr_l2_score, 1),
                "mtf_trend": round(v.mtf_trend_score, 1),
            },
            "volume_ratio": round(v.volume_ratio, 2),
            "breakout_buffer_atr": round(v.breakout_buffer_atr, 2),
            "l2_note": v.l2_alignment_note,
            "mtf_note": v.mtf_note,
            "is_live_incomplete_capped": self.is_live_incomplete_capped,
            "action_summary": self.action_summary,
            "geometry_points": [[i, round(p, 4)] for i, p in c.geometry_points],
            "notes": c.notes,
        }


@dataclass(frozen=True)
class TradingChartReport:
    symbol: str
    as_of: str
    live_price: float
    market_value: float | None
    timeframe_summaries: dict[str, dict[str, Any]]
    detections: tuple[ValidatedPattern, ...]
    canvas_overlays: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    macro_gate_note: str = "Verify Tier-0 Weather Light & 72h Macro Calendar before execution."

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "as_of": self.as_of,
            "live_price": round(self.live_price, 4),
            "market_value": round(self.market_value, 4) if self.market_value is not None else None,
            "macro_gate_note": self.macro_gate_note,
            "timeframe_summaries": self.timeframe_summaries,
            "detection_count": len(self.detections),
            "detections": [d.to_dict() for d in self.detections],
            "canvas_overlays": self.canvas_overlays,
        }
