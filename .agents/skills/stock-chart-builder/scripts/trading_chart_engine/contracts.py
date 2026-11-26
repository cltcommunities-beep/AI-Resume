"""Protocol-oriented Dependency Injection contracts (MVVMC Rule 4)."""

from __future__ import annotations

from typing import Any, Protocol

from .models import (
    L2OrderBookSnapshot,
    RawPatternCandidate,
    SwingPoint,
    Timeframe,
    TimeframeSeries,
    TradingChartReport,
    TrendLine,
    ValidatedPattern,
)


class MarketDataProviderProtocol(Protocol):
    """Normalizes raw Robinhood MCP payloads into Daily/Weekly/Monthly series and L2 snapshots."""

    def build_series_bundle(
        self, payload: dict[str, Any]
    ) -> tuple[str, str, float, float | None, dict[Timeframe, TimeframeSeries], L2OrderBookSnapshot | None]:
        ...


class SwingPivotExtractorProtocol(Protocol):
    """Extracts ATR-filtered swing highs/lows, linear trendlines, and S/R clusters."""

    def extract_swings(self, series: TimeframeSeries, window: int = 3) -> list[SwingPoint]:
        ...

    def fit_trendline(self, points: list[tuple[int, float]]) -> TrendLine:
        ...

    def cluster_sr_levels(
        self, series: TimeframeSeries, swings: list[SwingPoint]
    ) -> tuple[list[float], list[float]]:
        ...


class ChartPatternDetectorProtocol(Protocol):
    """Detects all 40 classical price-chart patterns on an OHLCV series."""

    @property
    def supported_patterns(self) -> tuple[str, ...]:
        ...

    def detect(
        self, series: TimeframeSeries, swings: list[SwingPoint]
    ) -> list[RawPatternCandidate]:
        ...


class CandlePatternDetectorProtocol(Protocol):
    """Detects all 30 single-, two-, and three-candle formations with prior-trend context."""

    @property
    def supported_patterns(self) -> tuple[str, ...]:
        ...

    def detect(self, series: TimeframeSeries) -> list[RawPatternCandidate]:
        ...


class PatternValidatorProtocol(Protocol):
    """Runs 5-factor institutional validation and classifies strict 4-state lifecycle."""

    def validate(
        self,
        candidate: RawPatternCandidate,
        series: TimeframeSeries,
        all_series: dict[Timeframe, TimeframeSeries],
        sr_levels: tuple[list[float], list[float]],
        l2_book: L2OrderBookSnapshot | None,
    ) -> ValidatedPattern:
        ...


class TradingChartViewModelProtocol(Protocol):
    """Transforms validated signals into ranked actionable outputs and chart overlay JSON."""

    def build_report(
        self,
        symbol: str,
        as_of: str,
        live_price: float,
        market_value: float | None,
        all_series: dict[Timeframe, TimeframeSeries],
        validated: list[ValidatedPattern],
        macro_gate_note: str,
    ) -> TradingChartReport:
        ...


class ChartHtmlRendererProtocol(Protocol):
    """Reusable UI renderer transforming a TradingChartReport into an 8/8 validated HTML5 chart."""

    def render(self, report: TradingChartReport, render_ctx: dict[str, Any]) -> str:
        ...


class TradingChartCoordinatorProtocol(Protocol):
    """MVVMC Router orchestrating data ingestion, 70-pattern scan, validation, and rendering."""

    def run_scan(self, payload: dict[str, Any]) -> TradingChartReport:
        ...
