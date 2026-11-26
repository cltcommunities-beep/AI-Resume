"""40 Classical Price-Chart Pattern Detectors across 5 Institutional Categories."""

from __future__ import annotations

from typing import Sequence

from .contracts import SwingPivotExtractorProtocol
from .models import (
    OHLCVBar,
    PatternBias,
    PatternKind,
    RawPatternCandidate,
    SwingPoint,
    TimeframeSeries,
)
from .pivots import ATRPivotExtractor

PRICE_CHART_PATTERNS: tuple[str, ...] = (
    # A. Bullish Reversal (10)
    "Double Bottom (W)",
    "Triple Bottom",
    "Inverse Head and Shoulders",
    "Rounding Bottom (Saucer)",
    "V-shaped Bottom",
    "Falling Wedge",
    "Bullish Island Reversal",
    "Adam and Eve Bottom",
    "Pipe Bottom",
    "Broadening Bottom",
    # B. Bearish Reversal (10)
    "Double Top (M)",
    "Triple Top",
    "Head and Shoulders",
    "Rounding Top",
    "Inverted V (Spike Top)",
    "Rising Wedge",
    "Bearish Island Reversal",
    "Adam and Eve Top",
    "Pipe Top",
    "Broadening Top",
    # C. Bullish Continuation (5)
    "Cup and Handle",
    "Bull Flag",
    "Bull Pennant",
    "Ascending Triangle",
    "High and Tight Flag",
    # D. Bearish Continuation (5)
    "Bear Flag",
    "Bear Pennant",
    "Descending Triangle",
    "Inverted Cup and Handle",
    "Bearish Measured Move",
    # E. Neutral / Bilateral (10)
    "Symmetrical Triangle",
    "Rectangle / Trading Range",
    "Broadening Formation (Megaphone)",
    "Diamond Formation",
    "Ascending Broadening Wedge",
    "Descending Broadening Wedge",
    "Horizontal Channel",
    "Rising Channel",
    "Falling Channel",
    "Volatility Contraction Pattern (VCP)",
)


def _pct_diff(a: float, b: float) -> float:
    return abs(a - b) / max(min(a, b), 1e-6)


def _trough_width(bars: Sequence[OHLCVBar], center_idx: int, tol_pct: float = 0.025) -> int:
    """Measures how many bars dwell within tol_pct of the local trough (Adam sharp vs Eve wide)."""
    base = bars[center_idx].low
    w = 1
    for i in range(center_idx - 1, max(-1, center_idx - 12), -1):
        if bars[i].low <= base * (1.0 + tol_pct):
            w += 1
        else:
            break
    for i in range(center_idx + 1, min(len(bars), center_idx + 12)):
        if bars[i].low <= base * (1.0 + tol_pct):
            w += 1
        else:
            break
    return w


def _peak_width(bars: Sequence[OHLCVBar], center_idx: int, tol_pct: float = 0.025) -> int:
    """Measures how many bars dwell within tol_pct of the local peak."""
    peak = bars[center_idx].high
    w = 1
    for i in range(center_idx - 1, max(-1, center_idx - 12), -1):
        if bars[i].high >= peak * (1.0 - tol_pct):
            w += 1
        else:
            break
    for i in range(center_idx + 1, min(len(bars), center_idx + 12)):
        if bars[i].high >= peak * (1.0 - tol_pct):
            w += 1
        else:
            break
    return w


def _prior_slope(bars: Sequence[OHLCVBar], idx: int, lookback: int = 10) -> float:
    start = max(0, idx - lookback)
    if start >= idx:
        return 0.0
    return (bars[idx].close - bars[start].close) / max(bars[start].close, 1e-6)


class PriceChartPatternDetector:
    """Implements ChartPatternDetectorProtocol covering all 40 price-chart formations."""

    def __init__(self, pivot_extractor: SwingPivotExtractorProtocol | None = None) -> None:
        self._pivots = pivot_extractor or ATRPivotExtractor()

    @property
    def supported_patterns(self) -> tuple[str, ...]:
        return PRICE_CHART_PATTERNS

    def detect(
        self, series: TimeframeSeries, swings: list[SwingPoint]
    ) -> list[RawPatternCandidate]:
        bars = series.bars
        n = len(bars)
        if n < 8:
            return []

        found: dict[str, RawPatternCandidate] = {}

        def _add(c: RawPatternCandidate | None) -> None:
            if c is None:
                return
            existing = found.get(c.name)
            if existing is None or c.geometry_score > existing.geometry_score:
                found[c.name] = c

        # Use recent window (last 90 bars) swings for active chart formations
        recent_start = max(0, n - 90)
        recent_swings = [s for s in swings if s.index >= recent_start]
        highs = [s for s in recent_swings if s.kind == "HIGH"]
        lows = [s for s in recent_swings if s.kind == "LOW"]

        # --- A. BULLISH REVERSAL (10) ---
        _add(self._detect_double_bottom(series, lows, highs))
        _add(self._detect_triple_bottom(series, lows, highs))
        _add(self._detect_inverse_h_and_s(series, lows, highs))
        _add(self._detect_rounding_bottom(series))
        _add(self._detect_v_bottom(series))
        _add(self._detect_falling_wedge(series, highs, lows))
        _add(self._detect_bullish_island(series))
        _add(self._detect_adam_eve_bottom(series, lows, highs))
        _add(self._detect_pipe_bottom(series))
        _add(self._detect_broadening_bottom(series, highs, lows))

        # --- B. BEARISH REVERSAL (10) ---
        _add(self._detect_double_top(series, highs, lows))
        _add(self._detect_triple_top(series, highs, lows))
        _add(self._detect_h_and_s(series, highs, lows))
        _add(self._detect_rounding_top(series))
        _add(self._detect_inverted_v_top(series))
        _add(self._detect_rising_wedge(series, highs, lows))
        _add(self._detect_bearish_island(series))
        _add(self._detect_adam_eve_top(series, highs, lows))
        _add(self._detect_pipe_top(series))
        _add(self._detect_broadening_top(series, highs, lows))

        # --- C. BULLISH CONTINUATION (5) ---
        _add(self._detect_cup_and_handle(series))
        _add(self._detect_bull_flag(series))
        _add(self._detect_bull_pennant(series))
        _add(self._detect_ascending_triangle(series, highs, lows))
        _add(self._detect_high_and_tight_flag(series))

        # --- D. BEARISH CONTINUATION (5) ---
        _add(self._detect_bear_flag(series))
        _add(self._detect_bear_pennant(series))
        _add(self._detect_descending_triangle(series, highs, lows))
        _add(self._detect_inverted_cup_and_handle(series))
        _add(self._detect_bearish_measured_move(series, highs, lows))

        # --- E. NEUTRAL / BILATERAL (10) ---
        _add(self._detect_symmetrical_triangle(series, highs, lows))
        _add(self._detect_rectangle(series, highs, lows))
        _add(self._detect_megaphone(series, highs, lows))
        _add(self._detect_diamond(series))
        _add(self._detect_ascending_broadening_wedge(series, highs, lows))
        _add(self._detect_descending_broadening_wedge(series, highs, lows))
        _add(self._detect_horizontal_channel(series, highs, lows))
        _add(self._detect_rising_channel(series, highs, lows))
        _add(self._detect_falling_channel(series, highs, lows))
        _add(self._detect_vcp(series, highs, lows))

        return list(found.values())

    # ==================== A. BULLISH REVERSAL (10) ====================

    def _detect_double_bottom(
        self, series: TimeframeSeries, lows: list[SwingPoint], highs: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(lows) < 2:
            return None
        l1, l2 = lows[-2], lows[-1]
        if l2.index - l1.index < 3 or _pct_diff(l1.price, l2.price) > 0.04:
            return None
        mid_highs = [h for h in highs if l1.index < h.index < l2.index]
        if not mid_highs:
            return None
        neck = max(mid_highs, key=lambda h: h.price)
        floor = min(l1.price, l2.price)
        if (neck.price - floor) / max(floor, 1e-6) < 0.035:
            return None
        height = neck.price - floor
        score = max(11.0, 19.0 - _pct_diff(l1.price, l2.price) * 140.0)
        return RawPatternCandidate(
            pattern_id="chart_01_double_bottom",
            name="Double Bottom (W)",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=l1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck.price,
            invalidation_level=floor * 0.99,
            target_price=neck.price + height,
            geometry_score=min(20.0, score),
            geometry_points=((l1.index, l1.price), (neck.index, neck.price), (l2.index, l2.price)),
            notes=f"Twin lows ${l1.price:.2f}/${l2.price:.2f}, neckline ${neck.price:.2f}",
        )

    def _detect_triple_bottom(
        self, series: TimeframeSeries, lows: list[SwingPoint], highs: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(lows) < 3:
            return None
        l1, l2, l3 = lows[-3], lows[-2], lows[-1]
        prices = [l1.price, l2.price, l3.price]
        spread = (max(prices) - min(prices)) / max(min(prices), 1e-6)
        if spread > 0.045:
            return None
        mid_highs = [h for h in highs if l1.index < h.index < l3.index]
        if len(mid_highs) < 2:
            return None
        neck = max(h.price for h in mid_highs)
        floor = min(prices)
        if (neck - floor) / max(floor, 1e-6) < 0.035:
            return None
        return RawPatternCandidate(
            pattern_id="chart_02_triple_bottom",
            name="Triple Bottom",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=l1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck,
            invalidation_level=floor * 0.99,
            target_price=neck + (neck - floor),
            geometry_score=min(20.0, max(12.0, 19.5 - spread * 120.0)),
            geometry_points=((l1.index, l1.price), (l2.index, l2.price), (l3.index, l3.price)),
            notes=f"3 lows near ${floor:.2f} (spread {spread*100:.1f}%), neckline ${neck:.2f}",
        )

    def _detect_inverse_h_and_s(
        self, series: TimeframeSeries, lows: list[SwingPoint], highs: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(lows) < 3:
            return None
        ls, head, rs = lows[-3], lows[-2], lows[-1]
        if not (head.price < ls.price * 0.965 and head.price < rs.price * 0.965):
            return None
        if _pct_diff(ls.price, rs.price) > 0.065:
            return None
        h_left = [h for h in highs if ls.index < h.index < head.index]
        h_right = [h for h in highs if head.index < h.index < rs.index]
        if not h_left or not h_right:
            return None
        n1 = max(h_left, key=lambda h: h.price)
        n2 = max(h_right, key=lambda h: h.price)
        neck_line = self._pivots.fit_trendline([(n1.index, n1.price), (n2.index, n2.price)])
        breakout = neck_line.value_at(len(series.bars) - 1)
        if breakout <= head.price:
            return None
        height = breakout - head.price
        return RawPatternCandidate(
            pattern_id="chart_03_inverse_h_and_s",
            name="Inverse Head and Shoulders",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=ls.index,
            end_idx=len(series.bars) - 1,
            breakout_level=breakout,
            invalidation_level=min(rs.price, head.price),
            target_price=breakout + height,
            geometry_score=min(20.0, 18.5 - _pct_diff(ls.price, rs.price) * 80.0),
            geometry_points=(
                (ls.index, ls.price),
                (n1.index, n1.price),
                (head.index, head.price),
                (n2.index, n2.price),
                (rs.index, rs.price),
            ),
            notes=f"Head ${head.price:.2f}, shoulders ${ls.price:.2f}/${rs.price:.2f}, neck ${breakout:.2f}",
        )

    def _detect_rounding_bottom(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 18:
            return None
        win = min(45, n)
        seg = bars[n - win :]
        third = win // 3
        left_avg = sum(b.close for b in seg[:third]) / third
        mid_avg = sum(b.close for b in seg[third : 2 * third]) / third
        right_avg = sum(b.close for b in seg[2 * third :]) / max(len(seg) - 2 * third, 1)
        mid_min = min(b.low for b in seg[third : 2 * third])
        rim = max(b.high for b in seg[:third])
        if not (mid_avg < left_avg * 0.94 and mid_avg < right_avg * 0.94 and right_avg >= left_avg * 0.92):
            return None
        # Ensure gradual bowl rather than violent single-bar V spike
        min_idx = min(range(len(seg)), key=lambda i: seg[i].low)
        if _trough_width(seg, min_idx, 0.03) < 4:
            return None
        height = rim - mid_min
        return RawPatternCandidate(
            pattern_id="chart_04_rounding_bottom",
            name="Rounding Bottom (Saucer)",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=n - win,
            end_idx=n - 1,
            breakout_level=rim,
            invalidation_level=mid_min * 0.99,
            target_price=rim + height,
            geometry_score=16.5,
            geometry_points=((n - win, rim), (n - win + min_idx, mid_min), (n - 1, bars[-1].close)),
            notes=f"U-shaped bowl floor ${mid_min:.2f}, rim ${rim:.2f}",
        )

    def _detect_v_bottom(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 12:
            return None
        win = min(24, n)
        seg = bars[n - win :]
        min_i = min(range(len(seg)), key=lambda i: seg[i].low)
        if min_i < 3 or min_i > len(seg) - 4:
            return None
        left_peak = max(b.high for b in seg[:min_i])
        trough = seg[min_i].low
        drop = (left_peak - trough) / max(left_peak, 1e-6)
        rebound = (seg[-1].close - trough) / max(left_peak - trough, 1e-6)
        width = _trough_width(seg, min_i, 0.02)
        if drop >= 0.09 and rebound >= 0.65 and width <= 3:
            return RawPatternCandidate(
                pattern_id="chart_05_v_bottom",
                name="V-shaped Bottom",
                category="Bullish Reversal",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.BULLISH,
                timeframe=series.timeframe,
                start_idx=n - win,
                end_idx=n - 1,
                breakout_level=left_peak,
                invalidation_level=trough * 0.99,
                target_price=left_peak + (left_peak - trough) * 0.618,
                geometry_score=16.0,
                geometry_points=((n - win, left_peak), (n - win + min_i, trough), (n - 1, seg[-1].close)),
                notes=f"Sharp -{drop*100:.1f}% drop into ${trough:.2f} with {rebound*100:.0f}% V-recovery",
            )
        return None

    def _detect_falling_wedge(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if not (upper.slope < 0 and lower.slope < 0):
            return None
        if abs(upper.slope) <= abs(lower.slope) * 1.12:
            return None
        start_i = min(h_pts[0][0], l_pts[0][0])
        end_i = len(series.bars) - 1
        w_start = upper.value_at(start_i) - lower.value_at(start_i)
        w_end = upper.value_at(end_i) - lower.value_at(end_i)
        if w_start <= 0 or w_end >= w_start * 0.85:
            return None
        breakout = upper.value_at(end_i)
        invalidation = lower.value_at(end_i)
        return RawPatternCandidate(
            pattern_id="chart_06_falling_wedge",
            name="Falling Wedge",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=end_i,
            breakout_level=breakout,
            invalidation_level=min(invalidation, lows[-1].price),
            target_price=max(h.price for h in highs[-3:]),
            geometry_score=17.5,
            geometry_points=tuple(h_pts + l_pts),
            notes=f"Converging downward rails; breakout roof ${breakout:.2f}",
        )

    def _detect_bullish_island(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 6:
            return None
        lookback = min(20, n - 2)
        start = n - lookback
        for i in range(start, n - 2):
            if bars[i].high < bars[i - 1].low * 0.995:  # Exhaustion gap down
                for j in range(i + 1, min(i + 9, n)):
                    if bars[j].low > bars[j - 1].high * 1.005:  # Breakaway gap up
                        island_low = min(b.low for b in bars[i:j])
                        gap_roof = bars[i - 1].low
                        return RawPatternCandidate(
                            pattern_id="chart_07_bullish_island",
                            name="Bullish Island Reversal",
                            category="Bullish Reversal",
                            kind=PatternKind.PRICE_CHART,
                            bias=PatternBias.BULLISH,
                            timeframe=series.timeframe,
                            start_idx=i - 1,
                            end_idx=j,
                            breakout_level=bars[j - 1].high,
                            invalidation_level=island_low * 0.99,
                            target_price=gap_roof + (gap_roof - island_low),
                            geometry_score=18.5,
                            geometry_points=((i, island_low), (j, bars[j].close)),
                            notes=f"Isolated {j-i}-bar island low ${island_low:.2f} with upward breakaway gap",
                        )
        return None

    def _detect_adam_eve_bottom(
        self, series: TimeframeSeries, lows: list[SwingPoint], highs: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(lows) < 2:
            return None
        l1, l2 = lows[-2], lows[-1]
        if _pct_diff(l1.price, l2.price) > 0.045 or (l2.index - l1.index) < 5:
            return None
        w1 = _trough_width(series.bars, l1.index, 0.025)
        w2 = _trough_width(series.bars, l2.index, 0.025)
        if not (w1 <= 3 and w2 >= w1 + 2):
            return None
        mid_highs = [h for h in highs if l1.index < h.index < l2.index]
        if not mid_highs:
            return None
        neck = max(h.price for h in mid_highs)
        floor = min(l1.price, l2.price)
        if (neck - floor) / max(floor, 1e-6) < 0.035:
            return None
        return RawPatternCandidate(
            pattern_id="chart_08_adam_eve_bottom",
            name="Adam and Eve Bottom",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=l1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck,
            invalidation_level=floor * 0.99,
            target_price=neck + (neck - floor),
            geometry_score=17.5,
            geometry_points=((l1.index, l1.price), (l2.index, l2.price)),
            notes=f"Sharp Adam trough (w={w1}) + rounded Eve trough (w={w2}), neck ${neck:.2f}",
        )

    def _detect_pipe_bottom(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 8:
            return None
        for i in range(max(4, n - 6), n - 1):
            b1, b2 = bars[i], bars[i + 1]
            atr = series.atr14[i] if series.atr14 else series.latest_atr
            prior_min = min(b.low for b in bars[max(0, i - 6) : i])
            if (
                b1.range_size >= 1.45 * atr
                and b2.range_size >= 1.45 * atr
                and _pct_diff(b1.low, b2.low) <= 0.015
                and min(b1.low, b2.low) <= prior_min * 1.01
                and b2.is_bullish
                and b2.close > b1.midpoint
            ):
                roof = max(b1.high, b2.high)
                floor = min(b1.low, b2.low)
                return RawPatternCandidate(
                    pattern_id="chart_09_pipe_bottom",
                    name="Pipe Bottom",
                    category="Bullish Reversal",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.BULLISH,
                    timeframe=series.timeframe,
                    start_idx=i,
                    end_idx=i + 1,
                    breakout_level=roof,
                    invalidation_level=floor * 0.995,
                    target_price=roof + (roof - floor),
                    geometry_score=17.0,
                    geometry_points=((i, b1.low), (i + 1, b2.low)),
                    notes=f"Twin tall reversal spikes at ${floor:.2f}, trigger ${roof:.2f}",
                )
        return None

    def _detect_broadening_bottom(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h1, h2 = highs[-2], highs[-1]
        l1, l2 = lows[-2], lows[-1]
        start_i = min(h1.index, l1.index)
        if _prior_slope(series.bars, start_i, 8) >= -0.03:
            return None
        if not (h2.price > h1.price * 1.015 and l2.price < l1.price * 0.985):
            return None
        return RawPatternCandidate(
            pattern_id="chart_10_broadening_bottom",
            name="Broadening Bottom",
            category="Bullish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=len(series.bars) - 1,
            breakout_level=h2.price,
            invalidation_level=l2.price * 0.99,
            target_price=h2.price + (h2.price - l2.price) * 0.618,
            geometry_score=15.5,
            geometry_points=((h1.index, h1.price), (l1.index, l1.price), (h2.index, h2.price), (l2.index, l2.price)),
            notes=f"Post-downtrend megaphone expansion (${l2.price:.2f}–${h2.price:.2f})",
        )

    # ==================== B. BEARISH REVERSAL (10) ====================

    def _detect_double_top(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2:
            return None
        h1, h2 = highs[-2], highs[-1]
        if h2.index - h1.index < 3 or _pct_diff(h1.price, h2.price) > 0.04:
            return None
        mid_lows = [l for l in lows if h1.index < l.index < h2.index]
        if not mid_lows:
            return None
        neck = min(mid_lows, key=lambda l: l.price)
        roof = max(h1.price, h2.price)
        if (roof - neck.price) / max(roof, 1e-6) < 0.035:
            return None
        height = roof - neck.price
        return RawPatternCandidate(
            pattern_id="chart_11_double_top",
            name="Double Top (M)",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=h1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck.price,
            invalidation_level=roof * 1.01,
            target_price=max(0.01, neck.price - height),
            geometry_score=min(20.0, max(11.0, 19.0 - _pct_diff(h1.price, h2.price) * 140.0)),
            geometry_points=((h1.index, h1.price), (neck.index, neck.price), (h2.index, h2.price)),
            notes=f"Twin peaks ${h1.price:.2f}/${h2.price:.2f}, neckline ${neck.price:.2f}",
        )

    def _detect_triple_top(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 3:
            return None
        h1, h2, h3 = highs[-3], highs[-2], highs[-1]
        prices = [h1.price, h2.price, h3.price]
        spread = (max(prices) - min(prices)) / max(min(prices), 1e-6)
        if spread > 0.045:
            return None
        mid_lows = [l for l in lows if h1.index < l.index < h3.index]
        if len(mid_lows) < 2:
            return None
        neck = min(l.price for l in mid_lows)
        roof = max(prices)
        if (roof - neck) / max(roof, 1e-6) < 0.035:
            return None
        return RawPatternCandidate(
            pattern_id="chart_12_triple_top",
            name="Triple Top",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=h1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck,
            invalidation_level=roof * 1.01,
            target_price=max(0.01, neck - (roof - neck)),
            geometry_score=min(20.0, max(12.0, 19.5 - spread * 120.0)),
            geometry_points=((h1.index, h1.price), (h2.index, h2.price), (h3.index, h3.price)),
            notes=f"3 peaks near ${roof:.2f}, support neckline ${neck:.2f}",
        )

    def _detect_h_and_s(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 3:
            return None
        ls, head, rs = highs[-3], highs[-2], highs[-1]
        if not (head.price > ls.price * 1.035 and head.price > rs.price * 1.035):
            return None
        if _pct_diff(ls.price, rs.price) > 0.065:
            return None
        l_left = [l for l in lows if ls.index < l.index < head.index]
        l_right = [l for l in lows if head.index < l.index < rs.index]
        if not l_left or not l_right:
            return None
        n1 = min(l_left, key=lambda l: l.price)
        n2 = min(l_right, key=lambda l: l.price)
        neck_line = self._pivots.fit_trendline([(n1.index, n1.price), (n2.index, n2.price)])
        breakout = neck_line.value_at(len(series.bars) - 1)
        if breakout >= head.price:
            return None
        return RawPatternCandidate(
            pattern_id="chart_13_h_and_s",
            name="Head and Shoulders",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=ls.index,
            end_idx=len(series.bars) - 1,
            breakout_level=breakout,
            invalidation_level=max(rs.price, head.price),
            target_price=max(0.01, breakout - (head.price - breakout)),
            geometry_score=min(20.0, 18.5 - _pct_diff(ls.price, rs.price) * 80.0),
            geometry_points=(
                (ls.index, ls.price),
                (n1.index, n1.price),
                (head.index, head.price),
                (n2.index, n2.price),
                (rs.index, rs.price),
            ),
            notes=f"Head ${head.price:.2f}, shoulders ${ls.price:.2f}/${rs.price:.2f}, neck ${breakout:.2f}",
        )

    def _detect_rounding_top(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 18:
            return None
        win = min(45, n)
        seg = bars[n - win :]
        third = win // 3
        left_avg = sum(b.close for b in seg[:third]) / third
        mid_avg = sum(b.close for b in seg[third : 2 * third]) / third
        right_avg = sum(b.close for b in seg[2 * third :]) / max(len(seg) - 2 * third, 1)
        mid_max = max(b.high for b in seg[third : 2 * third])
        rim = min(b.low for b in seg[:third])
        if not (mid_avg > left_avg * 1.06 and mid_avg > right_avg * 1.06 and right_avg <= left_avg * 1.08):
            return None
        max_idx = max(range(len(seg)), key=lambda i: seg[i].high)
        if _peak_width(seg, max_idx, 0.03) < 4:
            return None
        return RawPatternCandidate(
            pattern_id="chart_14_rounding_top",
            name="Rounding Top",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=n - win,
            end_idx=n - 1,
            breakout_level=rim,
            invalidation_level=mid_max * 1.01,
            target_price=max(0.01, rim - (mid_max - rim)),
            geometry_score=16.5,
            geometry_points=((n - win, rim), (n - win + max_idx, mid_max), (n - 1, bars[-1].close)),
            notes=f"Inverted dome top ${mid_max:.2f}, rim support ${rim:.2f}",
        )

    def _detect_inverted_v_top(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 12:
            return None
        win = min(24, n)
        seg = bars[n - win :]
        max_i = max(range(len(seg)), key=lambda i: seg[i].high)
        if max_i < 3 or max_i > len(seg) - 4:
            return None
        left_floor = min(b.low for b in seg[:max_i])
        peak = seg[max_i].high
        surge = (peak - left_floor) / max(left_floor, 1e-6)
        drop_ratio = (peak - seg[-1].close) / max(peak - left_floor, 1e-6)
        width = _peak_width(seg, max_i, 0.02)
        if surge >= 0.09 and drop_ratio >= 0.65 and width <= 3:
            return RawPatternCandidate(
                pattern_id="chart_15_inverted_v_top",
                name="Inverted V (Spike Top)",
                category="Bearish Reversal",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.BEARISH,
                timeframe=series.timeframe,
                start_idx=n - win,
                end_idx=n - 1,
                breakout_level=left_floor,
                invalidation_level=peak * 1.01,
                target_price=max(0.01, left_floor - (peak - left_floor) * 0.618),
                geometry_score=16.0,
                geometry_points=((n - win, left_floor), (n - win + max_i, peak), (n - 1, seg[-1].close)),
                notes=f"Spike top ${peak:.2f} (+{surge*100:.1f}%) reversing {drop_ratio*100:.0f}%",
            )
        return None

    def _detect_rising_wedge(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if not (upper.slope > 0 and lower.slope > 0):
            return None
        if lower.slope <= upper.slope * 1.12:
            return None
        start_i = min(h_pts[0][0], l_pts[0][0])
        end_i = len(series.bars) - 1
        w_start = upper.value_at(start_i) - lower.value_at(start_i)
        w_end = upper.value_at(end_i) - lower.value_at(end_i)
        if w_start <= 0 or w_end >= w_start * 0.85:
            return None
        breakout = lower.value_at(end_i)
        return RawPatternCandidate(
            pattern_id="chart_16_rising_wedge",
            name="Rising Wedge",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=end_i,
            breakout_level=breakout,
            invalidation_level=max(upper.value_at(end_i), highs[-1].price),
            target_price=min(l.price for l in lows[-3:]),
            geometry_score=17.5,
            geometry_points=tuple(h_pts + l_pts),
            notes=f"Converging upward rails; breakdown floor ${breakout:.2f}",
        )

    def _detect_bearish_island(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 6:
            return None
        lookback = min(20, n - 2)
        start = n - lookback
        for i in range(start, n - 2):
            if bars[i].low > bars[i - 1].high * 1.005:  # Exhaustion gap up
                for j in range(i + 1, min(i + 9, n)):
                    if bars[j].high < bars[j - 1].low * 0.995:  # Breakaway gap down
                        island_high = max(b.high for b in bars[i:j])
                        gap_floor = bars[i - 1].high
                        return RawPatternCandidate(
                            pattern_id="chart_17_bearish_island",
                            name="Bearish Island Reversal",
                            category="Bearish Reversal",
                            kind=PatternKind.PRICE_CHART,
                            bias=PatternBias.BEARISH,
                            timeframe=series.timeframe,
                            start_idx=i - 1,
                            end_idx=j,
                            breakout_level=bars[j - 1].low,
                            invalidation_level=island_high * 1.01,
                            target_price=max(0.01, gap_floor - (island_high - gap_floor)),
                            geometry_score=18.5,
                            geometry_points=((i, island_high), (j, bars[j].close)),
                            notes=f"Isolated {j-i}-bar top island ${island_high:.2f} with downward breakaway gap",
                        )
        return None

    def _detect_adam_eve_top(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2:
            return None
        h1, h2 = highs[-2], highs[-1]
        if _pct_diff(h1.price, h2.price) > 0.045 or (h2.index - h1.index) < 5:
            return None
        w1 = _peak_width(series.bars, h1.index, 0.025)
        w2 = _peak_width(series.bars, h2.index, 0.025)
        if not (w1 <= 3 and w2 >= w1 + 2):
            return None
        mid_lows = [l for l in lows if h1.index < l.index < h2.index]
        if not mid_lows:
            return None
        neck = min(l.price for l in mid_lows)
        roof = max(h1.price, h2.price)
        if (roof - neck) / max(roof, 1e-6) < 0.035:
            return None
        return RawPatternCandidate(
            pattern_id="chart_18_adam_eve_top",
            name="Adam and Eve Top",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=h1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=neck,
            invalidation_level=roof * 1.01,
            target_price=max(0.01, neck - (roof - neck)),
            geometry_score=17.5,
            geometry_points=((h1.index, h1.price), (h2.index, h2.price)),
            notes=f"Sharp Adam spike (w={w1}) + rounded Eve dome (w={w2}), neck ${neck:.2f}",
        )

    def _detect_pipe_top(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 8:
            return None
        for i in range(max(4, n - 6), n - 1):
            b1, b2 = bars[i], bars[i + 1]
            atr = series.atr14[i] if series.atr14 else series.latest_atr
            prior_max = max(b.high for b in bars[max(0, i - 6) : i])
            if (
                b1.range_size >= 1.45 * atr
                and b2.range_size >= 1.45 * atr
                and _pct_diff(b1.high, b2.high) <= 0.015
                and max(b1.high, b2.high) >= prior_max * 0.99
                and b2.is_bearish
                and b2.close < b1.midpoint
            ):
                roof = max(b1.high, b2.high)
                floor = min(b1.low, b2.low)
                return RawPatternCandidate(
                    pattern_id="chart_19_pipe_top",
                    name="Pipe Top",
                    category="Bearish Reversal",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.BEARISH,
                    timeframe=series.timeframe,
                    start_idx=i,
                    end_idx=i + 1,
                    breakout_level=floor,
                    invalidation_level=roof * 1.005,
                    target_price=max(0.01, floor - (roof - floor)),
                    geometry_score=17.0,
                    geometry_points=((i, b1.high), (i + 1, b2.high)),
                    notes=f"Twin tall spike rejections at ${roof:.2f}, breakdown ${floor:.2f}",
                )
        return None

    def _detect_broadening_top(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h1, h2 = highs[-2], highs[-1]
        l1, l2 = lows[-2], lows[-1]
        start_i = min(h1.index, l1.index)
        if _prior_slope(series.bars, start_i, 8) <= 0.03:
            return None
        if not (h2.price > h1.price * 1.015 and l2.price < l1.price * 0.985):
            return None
        return RawPatternCandidate(
            pattern_id="chart_20_broadening_top",
            name="Broadening Top",
            category="Bearish Reversal",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=len(series.bars) - 1,
            breakout_level=l2.price,
            invalidation_level=h2.price * 1.01,
            target_price=max(0.01, l2.price - (h2.price - l2.price) * 0.618),
            geometry_score=15.5,
            geometry_points=((h1.index, h1.price), (l1.index, l1.price), (h2.index, h2.price), (l2.index, l2.price)),
            notes=f"Post-uptrend megaphone top (${l2.price:.2f}–${h2.price:.2f})",
        )

    # ==================== C. BULLISH CONTINUATION (5) ====================

    def _detect_cup_and_handle(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 24:
            return None
        win = min(60, n)
        seg = bars[n - win :]
        handle_len = max(4, min(12, win // 5))
        cup = seg[: win - handle_len]
        handle = seg[win - handle_len :]
        if len(cup) < 15:
            return None
        left_rim = max(b.high for b in cup[: len(cup) // 3])
        cup_low = min(b.low for b in cup[len(cup) // 4 : 3 * len(cup) // 4])
        right_rim = max(b.high for b in cup[2 * len(cup) // 3 :])
        depth = (left_rim - cup_low) / max(left_rim, 1e-6)
        if not (0.10 <= depth <= 0.50):
            return None
        if right_rim < left_rim * 0.88 or right_rim > left_rim * 1.08:
            return None
        handle_low = min(b.low for b in handle)
        handle_high = max(b.high for b in handle)
        handle_depth = (right_rim - handle_low) / max(right_rim - cup_low, 1e-6)
        if not (0.04 <= handle_depth <= 0.50):
            return None
        rim = max(left_rim, right_rim)
        return RawPatternCandidate(
            pattern_id="chart_21_cup_and_handle",
            name="Cup and Handle",
            category="Bullish Continuation",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=n - win,
            end_idx=n - 1,
            breakout_level=max(handle_high, rim * 0.99),
            invalidation_level=handle_low * 0.99,
            target_price=rim + (rim - cup_low),
            geometry_score=18.5,
            geometry_points=((n - win, left_rim), (n - win + len(cup) // 2, cup_low), (n - handle_len, right_rim), (n - 1, handle_low)),
            notes=f"Cup depth {depth*100:.1f}%, handle pullback {handle_depth*100:.0f}% of cup",
        )

    def _detect_bull_flag(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 14:
            return None
        for flag_len in (5, 7, 10):
            if n < flag_len + 8:
                continue
            pole = bars[n - flag_len - 8 : n - flag_len]
            flag = bars[n - flag_len :]
            pole_low = min(b.low for b in pole[:3])
            pole_high = max(b.high for b in pole[-3:])
            pole_gain = (pole_high - pole_low) / max(pole_low, 1e-6)
            if pole_gain < 0.08:
                continue
            hi_line = self._pivots.fit_trendline([(i, b.high) for i, b in enumerate(flag)])
            lo_line = self._pivots.fit_trendline([(i, b.low) for i, b in enumerate(flag)])
            retrace = (pole_high - min(b.low for b in flag)) / max(pole_high - pole_low, 1e-6)
            if hi_line.slope < 0 and lo_line.slope <= 0 and 0.08 <= retrace <= 0.50:
                slope_ratio = abs(lo_line.slope) / max(abs(hi_line.slope), 1e-6)
                if 0.50 <= slope_ratio <= 1.60:
                    breakout = max(hi_line.value_at(len(flag) - 1), flag[-2].high)
                    return RawPatternCandidate(
                        pattern_id="chart_22_bull_flag",
                        name="Bull Flag",
                        category="Bullish Continuation",
                        kind=PatternKind.PRICE_CHART,
                        bias=PatternBias.BULLISH,
                        timeframe=series.timeframe,
                        start_idx=n - flag_len - 8,
                        end_idx=n - 1,
                        breakout_level=breakout,
                        invalidation_level=min(b.low for b in flag) * 0.99,
                        target_price=breakout + (pole_high - pole_low),
                        geometry_score=18.0,
                        geometry_points=((n - flag_len - 8, pole_low), (n - flag_len, pole_high), (n - 1, flag[-1].close)),
                        notes=f"+{pole_gain*100:.1f}% flagpole + orderly {retrace*100:.0f}% flag drift",
                    )
        return None

    def _detect_bull_pennant(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 14:
            return None
        for plen in (6, 9):
            if n < plen + 8:
                continue
            pole = bars[n - plen - 8 : n - plen]
            pen = bars[n - plen :]
            pole_low = min(b.low for b in pole[:3])
            pole_high = max(b.high for b in pole[-3:])
            pole_gain = (pole_high - pole_low) / max(pole_low, 1e-6)
            if pole_gain < 0.08:
                continue
            hi_line = self._pivots.fit_trendline([(i, b.high) for i, b in enumerate(pen)])
            lo_line = self._pivots.fit_trendline([(i, b.low) for i, b in enumerate(pen)])
            w0 = pen[0].high - pen[0].low
            w1 = pen[-1].high - pen[-1].low
            if hi_line.slope < 0 and lo_line.slope > 0 and w1 <= max(w0 * 0.85, (pole_high - pole_low) * 0.4):
                breakout = hi_line.value_at(len(pen) - 1)
                return RawPatternCandidate(
                    pattern_id="chart_23_bull_pennant",
                    name="Bull Pennant",
                    category="Bullish Continuation",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.BULLISH,
                    timeframe=series.timeframe,
                    start_idx=n - plen - 8,
                    end_idx=n - 1,
                    breakout_level=breakout,
                    invalidation_level=min(b.low for b in pen) * 0.99,
                    target_price=breakout + (pole_high - pole_low),
                    geometry_score=17.5,
                    geometry_points=((n - plen - 8, pole_low), (n - plen, pole_high), (n - 1, breakout)),
                    notes=f"+{pole_gain*100:.1f}% flagpole squeezing into tight pennant",
                )
        return None

    def _detect_ascending_triangle(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        recent_h = highs[-3:]
        recent_l = lows[-3:]
        h_prices = [h.price for h in recent_h]
        h_spread = (max(h_prices) - min(h_prices)) / max(min(h_prices), 1e-6)
        lo_line = self._pivots.fit_trendline([(l.index, l.price) for l in recent_l])
        if h_spread > 0.025 or lo_line.slope <= 0:
            return None
        roof = max(h_prices)
        base = min(l.price for l in recent_l)
        return RawPatternCandidate(
            pattern_id="chart_24_ascending_triangle",
            name="Ascending Triangle",
            category="Bullish Continuation",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BULLISH,
            timeframe=series.timeframe,
            start_idx=min(recent_h[0].index, recent_l[0].index),
            end_idx=len(series.bars) - 1,
            breakout_level=roof,
            invalidation_level=recent_l[-1].price * 0.99,
            target_price=roof + (roof - base),
            geometry_score=18.5,
            geometry_points=tuple([(h.index, h.price) for h in recent_h] + [(l.index, l.price) for l in recent_l]),
            notes=f"Flat roof ${roof:.2f} + rising higher lows",
        )

    def _detect_high_and_tight_flag(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 18:
            return None
        flag_len = min(10, n // 3)
        pole_start = max(0, n - flag_len - 30)
        pole = bars[pole_start : n - flag_len]
        flag = bars[n - flag_len :]
        if len(pole) < 6:
            return None
        pole_low = min(b.low for b in pole[: max(3, len(pole) // 3)])
        pole_high = max(b.high for b in pole)
        surge = (pole_high - pole_low) / max(pole_low, 1e-6)
        pullback = (pole_high - min(b.low for b in flag)) / max(pole_high, 1e-6)
        if surge >= 0.45 and pullback <= 0.25:
            return RawPatternCandidate(
                pattern_id="chart_25_high_and_tight_flag",
                name="High and Tight Flag",
                category="Bullish Continuation",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.BULLISH,
                timeframe=series.timeframe,
                start_idx=pole_start,
                end_idx=n - 1,
                breakout_level=max(b.high for b in flag),
                invalidation_level=min(b.low for b in flag) * 0.99,
                target_price=pole_high + (pole_high - pole_low) * 0.5,
                geometry_score=19.0,
                geometry_points=((pole_start, pole_low), (n - flag_len, pole_high), (n - 1, flag[-1].close)),
                notes=f"Power surge +{surge*100:.0f}% holding tight -{pullback*100:.1f}% shelf",
            )
        return None

    # ==================== D. BEARISH CONTINUATION (5) ====================

    def _detect_bear_flag(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 14:
            return None
        for flag_len in (5, 7, 10):
            if n < flag_len + 8:
                continue
            pole = bars[n - flag_len - 8 : n - flag_len]
            flag = bars[n - flag_len :]
            pole_high = max(b.high for b in pole[:3])
            pole_low = min(b.low for b in pole[-3:])
            drop = (pole_high - pole_low) / max(pole_high, 1e-6)
            if drop < 0.08:
                continue
            hi_line = self._pivots.fit_trendline([(i, b.high) for i, b in enumerate(flag)])
            lo_line = self._pivots.fit_trendline([(i, b.low) for i, b in enumerate(flag)])
            retrace = (max(b.high for b in flag) - pole_low) / max(pole_high - pole_low, 1e-6)
            if lo_line.slope > 0 and hi_line.slope >= 0 and 0.08 <= retrace <= 0.50:
                slope_ratio = abs(hi_line.slope) / max(abs(lo_line.slope), 1e-6)
                if 0.50 <= slope_ratio <= 1.60:
                    breakout = min(lo_line.value_at(len(flag) - 1), flag[-2].low)
                    return RawPatternCandidate(
                        pattern_id="chart_26_bear_flag",
                        name="Bear Flag",
                        category="Bearish Continuation",
                        kind=PatternKind.PRICE_CHART,
                        bias=PatternBias.BEARISH,
                        timeframe=series.timeframe,
                        start_idx=n - flag_len - 8,
                        end_idx=n - 1,
                        breakout_level=breakout,
                        invalidation_level=max(b.high for b in flag) * 1.01,
                        target_price=max(0.01, breakout - (pole_high - pole_low)),
                        geometry_score=18.0,
                        geometry_points=((n - flag_len - 8, pole_high), (n - flag_len, pole_low), (n - 1, flag[-1].close)),
                        notes=f"-{drop*100:.1f}% drop pole + weak upward bear-flag channel",
                    )
        return None

    def _detect_bear_pennant(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 14:
            return None
        for plen in (6, 9):
            if n < plen + 8:
                continue
            pole = bars[n - plen - 8 : n - plen]
            pen = bars[n - plen :]
            pole_high = max(b.high for b in pole[:3])
            pole_low = min(b.low for b in pole[-3:])
            drop = (pole_high - pole_low) / max(pole_high, 1e-6)
            if drop < 0.08:
                continue
            hi_line = self._pivots.fit_trendline([(i, b.high) for i, b in enumerate(pen)])
            lo_line = self._pivots.fit_trendline([(i, b.low) for i, b in enumerate(pen)])
            w0 = pen[0].high - pen[0].low
            w1 = pen[-1].high - pen[-1].low
            if hi_line.slope < 0 and lo_line.slope > 0 and w1 <= max(w0 * 0.85, (pole_high - pole_low) * 0.4):
                breakout = lo_line.value_at(len(pen) - 1)
                return RawPatternCandidate(
                    pattern_id="chart_27_bear_pennant",
                    name="Bear Pennant",
                    category="Bearish Continuation",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.BEARISH,
                    timeframe=series.timeframe,
                    start_idx=n - plen - 8,
                    end_idx=n - 1,
                    breakout_level=breakout,
                    invalidation_level=max(b.high for b in pen) * 1.01,
                    target_price=max(0.01, breakout - (pole_high - pole_low)),
                    geometry_score=17.5,
                    geometry_points=((n - plen - 8, pole_high), (n - plen, pole_low), (n - 1, breakout)),
                    notes=f"-{drop*100:.1f}% drop pole compressing into bear pennant",
                )
        return None

    def _detect_descending_triangle(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        recent_h = highs[-3:]
        recent_l = lows[-3:]
        l_prices = [l.price for l in recent_l]
        l_spread = (max(l_prices) - min(l_prices)) / max(min(l_prices), 1e-6)
        hi_line = self._pivots.fit_trendline([(h.index, h.price) for h in recent_h])
        if l_spread > 0.025 or hi_line.slope >= 0:
            return None
        floor = min(l_prices)
        roof = max(h.price for h in recent_h)
        return RawPatternCandidate(
            pattern_id="chart_28_descending_triangle",
            name="Descending Triangle",
            category="Bearish Continuation",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=min(recent_h[0].index, recent_l[0].index),
            end_idx=len(series.bars) - 1,
            breakout_level=floor,
            invalidation_level=recent_h[-1].price * 1.01,
            target_price=max(0.01, floor - (roof - floor)),
            geometry_score=18.5,
            geometry_points=tuple([(h.index, h.price) for h in recent_h] + [(l.index, l.price) for l in recent_l]),
            notes=f"Flat floor ${floor:.2f} under lower swing highs",
        )

    def _detect_inverted_cup_and_handle(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 24:
            return None
        win = min(60, n)
        seg = bars[n - win :]
        handle_len = max(4, min(12, win // 5))
        cup = seg[: win - handle_len]
        handle = seg[win - handle_len :]
        if len(cup) < 15:
            return None
        left_rim = min(b.low for b in cup[: len(cup) // 3])
        cup_high = max(b.high for b in cup[len(cup) // 4 : 3 * len(cup) // 4])
        right_rim = min(b.low for b in cup[2 * len(cup) // 3 :])
        height = (cup_high - left_rim) / max(left_rim, 1e-6)
        if not (0.10 <= height <= 0.55):
            return None
        if right_rim > left_rim * 1.12 or right_rim < left_rim * 0.92:
            return None
        handle_high = max(b.high for b in handle)
        handle_low = min(b.low for b in handle)
        handle_bounce = (handle_high - right_rim) / max(cup_high - right_rim, 1e-6)
        if not (0.04 <= handle_bounce <= 0.50):
            return None
        rim = min(left_rim, right_rim)
        return RawPatternCandidate(
            pattern_id="chart_29_inverted_cup_handle",
            name="Inverted Cup and Handle",
            category="Bearish Continuation",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=n - win,
            end_idx=n - 1,
            breakout_level=min(handle_low, rim * 1.01),
            invalidation_level=handle_high * 1.01,
            target_price=max(0.01, rim - (cup_high - rim)),
            geometry_score=18.0,
            geometry_points=((n - win, left_rim), (n - win + len(cup) // 2, cup_high), (n - handle_len, right_rim), (n - 1, handle_high)),
            notes=f"Inverted dome peak ${cup_high:.2f} + weak {handle_bounce*100:.0f}% handle bounce",
        )

    def _detect_bearish_measured_move(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 1:
            return None
        h1, h2 = highs[-2], highs[-1]
        mid_lows = [l for l in lows if h1.index < l.index < h2.index]
        if not mid_lows:
            return None
        l1 = min(mid_lows, key=lambda l: l.price)
        leg1 = h1.price - l1.price
        if leg1 / max(h1.price, 1e-6) < 0.08:
            return None
        retrace = (h2.price - l1.price) / max(leg1, 1e-6)
        if not (0.25 <= retrace <= 0.68):
            return None
        return RawPatternCandidate(
            pattern_id="chart_30_bearish_measured_move",
            name="Bearish Measured Move",
            category="Bearish Continuation",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.BEARISH,
            timeframe=series.timeframe,
            start_idx=h1.index,
            end_idx=len(series.bars) - 1,
            breakout_level=l1.price,
            invalidation_level=h2.price * 1.01,
            target_price=max(0.01, h2.price - leg1),
            geometry_score=17.0,
            geometry_points=((h1.index, h1.price), (l1.index, l1.price), (h2.index, h2.price)),
            notes=f"AB={leg1:.2f} drop + {retrace*100:.0f}% BC retrace; CD target ${max(0.01, h2.price - leg1):.2f}",
        )

    # ==================== E. NEUTRAL / BILATERAL (10) ====================

    def _detect_symmetrical_triangle(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if not (upper.slope < 0 and lower.slope > 0):
            return None
        start_i = min(h_pts[0][0], l_pts[0][0])
        end_i = len(series.bars) - 1
        w0 = upper.value_at(start_i) - lower.value_at(start_i)
        w1 = upper.value_at(end_i) - lower.value_at(end_i)
        if w0 <= 0 or w1 >= w0 * 0.72:
            return None
        up_b = upper.value_at(end_i)
        dn_b = lower.value_at(end_i)
        return RawPatternCandidate(
            pattern_id="chart_31_symmetrical_triangle",
            name="Symmetrical Triangle",
            category="Neutral / Bilateral",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.NEUTRAL,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=end_i,
            breakout_level=up_b,
            secondary_breakout_level=dn_b,
            invalidation_level=dn_b,
            target_price=up_b + w0,
            geometry_score=17.5,
            geometry_points=tuple(h_pts + l_pts),
            notes=f"Coiling apex (upper ${up_b:.2f} / lower ${dn_b:.2f})",
        )

    def _detect_rectangle(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_p = [h.price for h in highs[-3:]]
        l_p = [l.price for l in lows[-3:]]
        h_sp = (max(h_p) - min(h_p)) / max(min(h_p), 1e-6)
        l_sp = (max(l_p) - min(l_p)) / max(min(l_p), 1e-6)
        roof, floor = max(h_p), min(l_p)
        height_pct = (roof - floor) / max(floor, 1e-6)
        if h_sp <= 0.025 and l_sp <= 0.025 and 0.035 <= height_pct <= 0.25:
            return RawPatternCandidate(
                pattern_id="chart_32_rectangle",
                name="Rectangle / Trading Range",
                category="Neutral / Bilateral",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.NEUTRAL,
                timeframe=series.timeframe,
                start_idx=min(highs[-2].index, lows[-2].index),
                end_idx=len(series.bars) - 1,
                breakout_level=roof,
                secondary_breakout_level=floor,
                invalidation_level=floor,
                target_price=roof + (roof - floor),
                geometry_score=17.0,
                geometry_points=((highs[-2].index, roof), (lows[-2].index, floor)),
                notes=f"Horizontal box ${floor:.2f}–${roof:.2f} ({height_pct*100:.1f}% width)",
            )
        return None

    def _detect_megaphone(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if not (upper.slope > 0 and lower.slope < 0):
            return None
        start_i = min(h_pts[0][0], l_pts[0][0])
        end_i = len(series.bars) - 1
        w0 = max(upper.value_at(start_i) - lower.value_at(start_i), 1e-6)
        w1 = upper.value_at(end_i) - lower.value_at(end_i)
        if w1 < w0 * 1.25:
            return None
        return RawPatternCandidate(
            pattern_id="chart_33_megaphone",
            name="Broadening Formation (Megaphone)",
            category="Neutral / Bilateral",
            kind=PatternKind.PRICE_CHART,
            bias=PatternBias.NEUTRAL,
            timeframe=series.timeframe,
            start_idx=start_i,
            end_idx=end_i,
            breakout_level=upper.value_at(end_i),
            secondary_breakout_level=lower.value_at(end_i),
            invalidation_level=lower.value_at(end_i),
            target_price=upper.value_at(end_i) + w1 * 0.5,
            geometry_score=16.5,
            geometry_points=tuple(h_pts + l_pts),
            notes=f"Expanding volatility megaphone ({w1/w0:.2f}x width growth)",
        )

    def _detect_diamond(self, series: TimeframeSeries) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 16:
            return None
        win = min(32, n)
        seg = bars[n - win :]
        q = win // 4
        r1 = max(b.high for b in seg[:q]) - min(b.low for b in seg[:q])
        r2 = max(b.high for b in seg[q : 2 * q]) - min(b.low for b in seg[q : 2 * q])
        r3 = max(b.high for b in seg[2 * q : 3 * q]) - min(b.low for b in seg[2 * q : 3 * q])
        r4 = max(b.high for b in seg[3 * q :]) - min(b.low for b in seg[3 * q :])
        mid_max = max(r2, r3)
        if mid_max > r1 * 1.35 and mid_max > r4 * 1.35:
            roof = max(b.high for b in seg[3 * q :])
            floor = min(b.low for b in seg[3 * q :])
            return RawPatternCandidate(
                pattern_id="chart_34_diamond",
                name="Diamond Formation",
                category="Neutral / Bilateral",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.NEUTRAL,
                timeframe=series.timeframe,
                start_idx=n - win,
                end_idx=n - 1,
                breakout_level=roof,
                secondary_breakout_level=floor,
                invalidation_level=floor,
                target_price=roof + mid_max,
                geometry_score=16.5,
                geometry_points=((n - win, seg[0].close), (n - win // 2, seg[win // 2].high), (n - 1, seg[-1].close)),
                notes=f"Broaden-then-contract diamond (center width ${mid_max:.2f})",
            )
        return None

    def _detect_ascending_broadening_wedge(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if upper.slope > 0 and lower.slope > 0 and upper.slope > lower.slope * 1.25:
            end_i = len(series.bars) - 1
            return RawPatternCandidate(
                pattern_id="chart_35_asc_broadening_wedge",
                name="Ascending Broadening Wedge",
                category="Neutral / Bilateral",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.NEUTRAL,
                timeframe=series.timeframe,
                start_idx=min(h_pts[0][0], l_pts[0][0]),
                end_idx=end_i,
                breakout_level=upper.value_at(end_i),
                secondary_breakout_level=lower.value_at(end_i),
                invalidation_level=lower.value_at(end_i),
                target_price=upper.value_at(end_i) + (upper.value_at(end_i) - lower.value_at(end_i)) * 0.5,
                geometry_score=16.0,
                geometry_points=tuple(h_pts + l_pts),
                notes="Diverging upward wedge (steeper upper rail)",
            )
        return None

    def _detect_descending_broadening_wedge(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if upper.slope < 0 and lower.slope < 0 and abs(lower.slope) > abs(upper.slope) * 1.25:
            end_i = len(series.bars) - 1
            return RawPatternCandidate(
                pattern_id="chart_36_desc_broadening_wedge",
                name="Descending Broadening Wedge",
                category="Neutral / Bilateral",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.NEUTRAL,
                timeframe=series.timeframe,
                start_idx=min(h_pts[0][0], l_pts[0][0]),
                end_idx=end_i,
                breakout_level=upper.value_at(end_i),
                secondary_breakout_level=lower.value_at(end_i),
                invalidation_level=lower.value_at(end_i),
                target_price=max(h.price for h in highs[-3:]),
                geometry_score=16.0,
                geometry_points=tuple(h_pts + l_pts),
                notes="Diverging downward wedge (steeper lower rail)",
            )
        return None

    def _detect_horizontal_channel(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-4:]]
        l_pts = [(l.index, l.price) for l in lows[-4:]]
        span = max(h_pts[-1][0], l_pts[-1][0]) - min(h_pts[0][0], l_pts[0][0])
        if span < 12:
            return None
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        mid = max(series.bars[-1].close, 1e-6)
        if abs(upper.slope) / mid <= 0.0015 and abs(lower.slope) / mid <= 0.0015:
            end_i = len(series.bars) - 1
            roof = upper.value_at(end_i)
            floor = lower.value_at(end_i)
            if roof > floor * 1.02:
                return RawPatternCandidate(
                    pattern_id="chart_37_horizontal_channel",
                    name="Horizontal Channel",
                    category="Neutral / Bilateral",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.NEUTRAL,
                    timeframe=series.timeframe,
                    start_idx=min(h_pts[0][0], l_pts[0][0]),
                    end_idx=end_i,
                    breakout_level=roof,
                    secondary_breakout_level=floor,
                    invalidation_level=floor,
                    target_price=roof + (roof - floor),
                    geometry_score=16.5,
                    geometry_points=tuple(h_pts + l_pts),
                    notes=f"Extended horizontal corridor ${floor:.2f}–${roof:.2f} ({span} bars)",
                )
        return None

    def _detect_rising_channel(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if upper.slope > 0 and lower.slope > 0:
            ratio = upper.slope / max(lower.slope, 1e-9)
            if 0.72 <= ratio <= 1.24:
                end_i = len(series.bars) - 1
                return RawPatternCandidate(
                    pattern_id="chart_38_rising_channel",
                    name="Rising Channel",
                    category="Neutral / Bilateral",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.NEUTRAL,
                    timeframe=series.timeframe,
                    start_idx=min(h_pts[0][0], l_pts[0][0]),
                    end_idx=end_i,
                    breakout_level=upper.value_at(end_i),
                    secondary_breakout_level=lower.value_at(end_i),
                    invalidation_level=lower.value_at(end_i),
                    target_price=upper.value_at(end_i) + (upper.value_at(end_i) - lower.value_at(end_i)),
                    geometry_score=17.0,
                    geometry_points=tuple(h_pts + l_pts),
                    notes="Parallel ascending channel rails",
                )
        return None

    def _detect_falling_channel(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        if len(highs) < 2 or len(lows) < 2:
            return None
        h_pts = [(h.index, h.price) for h in highs[-3:]]
        l_pts = [(l.index, l.price) for l in lows[-3:]]
        upper = self._pivots.fit_trendline(h_pts)
        lower = self._pivots.fit_trendline(l_pts)
        if upper.slope < 0 and lower.slope < 0:
            ratio = abs(upper.slope) / max(abs(lower.slope), 1e-9)
            if 0.72 <= ratio <= 1.24:
                end_i = len(series.bars) - 1
                return RawPatternCandidate(
                    pattern_id="chart_39_falling_channel",
                    name="Falling Channel",
                    category="Neutral / Bilateral",
                    kind=PatternKind.PRICE_CHART,
                    bias=PatternBias.NEUTRAL,
                    timeframe=series.timeframe,
                    start_idx=min(h_pts[0][0], l_pts[0][0]),
                    end_idx=end_i,
                    breakout_level=upper.value_at(end_i),
                    secondary_breakout_level=lower.value_at(end_i),
                    invalidation_level=lower.value_at(end_i),
                    target_price=upper.value_at(end_i) + (upper.value_at(end_i) - lower.value_at(end_i)),
                    geometry_score=17.0,
                    geometry_points=tuple(h_pts + l_pts),
                    notes="Parallel descending channel rails",
                )
        return None

    def _detect_vcp(
        self, series: TimeframeSeries, highs: list[SwingPoint], lows: list[SwingPoint]
    ) -> RawPatternCandidate | None:
        bars = series.bars
        n = len(bars)
        if n < 24:
            return None
        win = min(48, n)
        seg = bars[n - win :]
        t_len = win // 3
        c1_hi = max(b.high for b in seg[:t_len])
        c1_lo = min(b.low for b in seg[:t_len])
        c2_hi = max(b.high for b in seg[t_len : 2 * t_len])
        c2_lo = min(b.low for b in seg[t_len : 2 * t_len])
        c3_hi = max(b.high for b in seg[2 * t_len :])
        c3_lo = min(b.low for b in seg[2 * t_len :])
        d1 = (c1_hi - c1_lo) / max(c1_hi, 1e-6)
        d2 = (c2_hi - c2_lo) / max(c2_hi, 1e-6)
        d3 = (c3_hi - c3_lo) / max(c3_hi, 1e-6)
        # Progressive volatility contraction (T1 > T2 > T3) with tight final contraction near pivot
        if d1 >= 0.08 and d2 <= d1 * 0.80 and d3 <= d2 * 0.80 and d3 <= 0.11 and c3_lo > c1_lo:
            pivot = max(c2_hi, c3_hi)
            return RawPatternCandidate(
                pattern_id="chart_40_vcp",
                name="Volatility Contraction Pattern (VCP)",
                category="Neutral / Bilateral",
                kind=PatternKind.PRICE_CHART,
                bias=PatternBias.NEUTRAL,
                timeframe=series.timeframe,
                start_idx=n - win,
                end_idx=n - 1,
                breakout_level=pivot,
                secondary_breakout_level=c3_lo,
                invalidation_level=c3_lo * 0.99,
                target_price=pivot * (1.0 + max(d1, 0.12)),
                geometry_score=18.5,
                geometry_points=((n - win, c1_hi), (n - 2 * t_len, c2_lo), (n - 1, c3_hi)),
                notes=f"VCP contractions {d1*100:.1f}% -> {d2*100:.1f}% -> {d3*100:.1f}%, pivot ${pivot:.2f}",
            )
        return None
