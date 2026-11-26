"""ATR-Adaptive Swing Pivot Extractor, Linear Regression Trendlines & S/R Clustering."""

from __future__ import annotations

from .models import SwingPoint, TimeframeSeries, TrendLine


class ATRPivotExtractor:
    """Implements SwingPivotExtractorProtocol using fractal + ATR prominence filtering."""

    def extract_swings(self, series: TimeframeSeries, window: int = 2) -> list[SwingPoint]:
        bars = series.bars
        n = len(bars)
        if n < (window * 2 + 1):
            return []

        raw_pivots: list[SwingPoint] = []
        for i in range(window, n - window):
            hi = bars[i].high
            lo = bars[i].low
            is_high = all(hi >= bars[j].high for j in range(i - window, i + window + 1) if j != i)
            is_low = all(lo <= bars[j].low for j in range(i - window, i + window + 1) if j != i)
            if is_high and not is_low:
                raw_pivots.append(SwingPoint(i, bars[i].timestamp, hi, "HIGH"))
            elif is_low and not is_high:
                raw_pivots.append(SwingPoint(i, bars[i].timestamp, lo, "LOW"))
            elif is_high and is_low:
                # Resolve tie by close polarity
                if bars[i].is_bullish:
                    raw_pivots.append(SwingPoint(i, bars[i].timestamp, hi, "HIGH"))
                else:
                    raw_pivots.append(SwingPoint(i, bars[i].timestamp, lo, "LOW"))

        if not raw_pivots:
            return []

        # Enforce alternating HIGH/LOW sequence, preserving the sharper extreme on adjacent duplicates
        alternating: list[SwingPoint] = [raw_pivots[0]]
        for p in raw_pivots[1:]:
            prev = alternating[-1]
            if p.kind == prev.kind:
                if (p.kind == "HIGH" and p.price >= prev.price) or (
                    p.kind == "LOW" and p.price <= prev.price
                ):
                    alternating[-1] = p
            else:
                # Filter micro-noise reversals smaller than 0.65 * local ATR
                local_atr = series.atr14[p.index] if series.atr14 else series.latest_atr
                if abs(p.price - prev.price) >= max(0.65 * local_atr, prev.price * 0.004):
                    alternating.append(p)
        return alternating

    def fit_trendline(self, points: list[tuple[int, float]]) -> TrendLine:
        if not points:
            return TrendLine(0, 0.0, 0, 0.0, 0.0, 0.0, 0.0)
        if len(points) == 1:
            x0, y0 = points[0]
            return TrendLine(x0, y0, x0, y0, 0.0, y0, 1.0)
        n = len(points)
        xs = [float(p[0]) for p in points]
        ys = [float(p[1]) for p in points]
        mean_x = sum(xs) / n
        mean_y = sum(ys) / n
        ss_xx = sum((x - mean_x) ** 2 for x in xs)
        if ss_xx <= 1e-9:
            return TrendLine(
                int(xs[0]), ys[0], int(xs[-1]), ys[-1], 0.0, mean_y, 0.0
            )
        ss_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
        slope = ss_xy / ss_xx
        intercept = mean_y - slope * mean_x
        ss_tot = sum((y - mean_y) ** 2 for y in ys)
        ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
        r2 = 1.0 if ss_tot <= 1e-9 else max(0.0, 1.0 - (ss_res / ss_tot))
        start_x = int(xs[0])
        end_x = int(xs[-1])
        return TrendLine(
            start_idx=start_x,
            start_price=slope * start_x + intercept,
            end_idx=end_x,
            end_price=slope * end_x + intercept,
            slope=slope,
            intercept=intercept,
            r_squared=r2,
        )

    def cluster_sr_levels(
        self, series: TimeframeSeries, swings: list[SwingPoint]
    ) -> tuple[list[float], list[float]]:
        """Returns clustered (support_levels, resistance_levels) from historical swings."""
        if not series.bars:
            return [], []
        spot = series.bars[-1].close
        tol = max(series.latest_atr * 0.75, spot * 0.015)

        def _cluster(prices: list[float]) -> list[float]:
            if not prices:
                return []
            ordered = sorted(prices)
            groups: list[list[float]] = [[ordered[0]]]
            for pr in ordered[1:]:
                if abs(pr - (sum(groups[-1]) / len(groups[-1]))) <= tol:
                    groups[-1].append(pr)
                else:
                    groups.append([pr])
            # Sort by touch count descending, then proximity to spot
            groups.sort(key=lambda g: (-len(g), abs((sum(g) / len(g)) - spot)))
            return [sum(g) / len(g) for g in groups[:8]]

        lows = [s.price for s in swings if s.kind == "LOW" and s.price <= spot * 1.02]
        highs = [s.price for s in swings if s.kind == "HIGH" and s.price >= spot * 0.98]
        return _cluster(lows), _cluster(highs)
