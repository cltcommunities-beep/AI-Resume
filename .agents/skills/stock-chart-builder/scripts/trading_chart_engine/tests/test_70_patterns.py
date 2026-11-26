#!/usr/bin/env python3
"""
Comprehensive Test Suite for tradingChart 70-Pattern Engine:
  1. Verifies exact catalog parity: 40 Price-Chart + 30 Candlestick = 70 unique patterns.
  2. Verifies positive detection of EVERY SINGLE ONE of the 40 Price-Chart Patterns.
  3. Verifies positive detection of EVERY SINGLE ONE of the 30 Candlestick Patterns.
  4. Verifies all 4 Lifecycle States (Forming, Confirmed Breakout, Failed Breakout, Invalidated).
  5. Verifies Live Incomplete Bar Cap (never Confirmed Breakout before candle close).
  6. Verifies 5-Factor Scoring (Volume, L2 Ask/Bid Walls, Multi-Timeframe D/W/M Confluence).
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ENGINE_PARENT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ENGINE_PARENT))

from trading_chart_engine.candle_patterns import CANDLESTICK_PATTERNS, CandlestickPatternDetector
from trading_chart_engine.chart_patterns import PRICE_CHART_PATTERNS, PriceChartPatternDetector
from trading_chart_engine.coordinator import TradingChartCoordinator
from trading_chart_engine.models import (
    L2OrderBookSnapshot,
    L2Wall,
    OHLCVBar,
    PatternLifecycleState,
    Timeframe,
)
from trading_chart_engine.pivots import ATRPivotExtractor
from trading_chart_engine.robinhood_adapter import build_timeframe_series


def _bar(
    idx: int,
    o: float,
    h: float,
    l: float,
    c: float,
    v: float = 1_000_000.0,
    is_live: bool = False,
) -> OHLCVBar:
    return OHLCVBar(
        timestamp=f"2026-01-{idx + 1:02d}T00:00:00Z",
        open=o,
        high=max(h, o, c),
        low=min(l, o, c),
        close=c,
        volume=v,
        interpolated=False,
        is_live_incomplete=is_live,
    )


def _bars_from_closes(
    closes: list[float],
    spread: float = 0.012,
    volumes: list[float] | None = None,
) -> list[OHLCVBar]:
    bars: list[OHLCVBar] = []
    for i, c in enumerate(closes):
        o = closes[i - 1] if i > 0 else c * 0.998
        hi = max(o, c) * (1.0 + spread)
        lo = min(o, c) * (1.0 - spread)
        vol = volumes[i] if volumes else 1_000_000.0
        bars.append(_bar(i, o, hi, lo, c, vol))
    return bars


def _interp_path(anchors: list[tuple[int, float]]) -> list[float]:
    """Linearly interpolates prices across (bar_index, price) control points."""
    out: list[float] = []
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        steps = x1 - x0
        for s in range(steps):
            frac = s / max(steps, 1)
            out.append(y0 + (y1 - y0) * frac)
    out.append(anchors[-1][1])
    return out


class Test70PatternCatalog(unittest.TestCase):
    def test_exact_70_pattern_count(self) -> None:
        coord = TradingChartCoordinator()
        c40, k30, total = coord.catalog_counts
        self.assertEqual(c40, 40)
        self.assertEqual(k30, 30)
        self.assertEqual(total, 70)
        self.assertEqual(len(set(PRICE_CHART_PATTERNS)), 40)
        self.assertEqual(len(set(CANDLESTICK_PATTERNS)), 30)


class TestAll40PriceChartPatterns(unittest.TestCase):
    def setUp(self) -> None:
        self.pivots = ATRPivotExtractor()
        self.detector = PriceChartPatternDetector(self.pivots)

    def _assert_chart_detected(self, expected_name: str, bars: list[OHLCVBar]) -> None:
        series = build_timeframe_series("TEST", Timeframe.DAILY, bars)
        swings = self.pivots.extract_swings(series, window=2)
        names = {c.name for c in self.detector.detect(series, swings)}
        self.assertIn(
            expected_name,
            names,
            f"Expected '{expected_name}' not detected. Found: {sorted(names)} (swings={[(s.index, s.kind, round(s.price, 2)) for s in swings]})",
        )

    def test_a_bullish_reversal_10(self) -> None:
        # 1. Double Bottom (W)
        self._assert_chart_detected(
            "Double Bottom (W)",
            _bars_from_closes(_interp_path([(0, 120), (5, 100), (10, 115), (15, 101), (19, 112)])),
        )
        # 2. Triple Bottom
        self._assert_chart_detected(
            "Triple Bottom",
            _bars_from_closes(_interp_path([(0, 120), (4, 100), (8, 114), (12, 101), (16, 115), (20, 100.5), (24, 112)])),
        )
        # 3. Inverse Head and Shoulders
        self._assert_chart_detected(
            "Inverse Head and Shoulders",
            _bars_from_closes(_interp_path([(0, 120), (4, 105), (8, 116), (12, 92), (16, 116), (20, 106), (24, 114)])),
        )
        # 4. Rounding Bottom (Saucer)
        saucer = [110.0 + 18.0 * ((i - 18) / 18.0) ** 2 for i in range(37)]
        self._assert_chart_detected("Rounding Bottom (Saucer)", _bars_from_closes(saucer, spread=0.004))
        # 5. V-shaped Bottom
        self._assert_chart_detected(
            "V-shaped Bottom",
            _bars_from_closes(_interp_path([(0, 120), (6, 120), (11, 95), (17, 116)])),
        )
        # 6. Falling Wedge
        self._assert_chart_detected(
            "Falling Wedge",
            _bars_from_closes(_interp_path([(0, 130), (4, 110), (8, 122), (12, 107), (16, 114), (20, 105), (23, 110)])),
        )
        # 7. Bullish Island Reversal
        isl = [
            _bar(0, 112, 113, 110, 111), _bar(1, 111, 112, 109, 110),
            _bar(2, 110, 111, 108, 109), _bar(3, 109, 110, 107, 108),
            # Exhaustion gap down (< 107)
            _bar(4, 102, 103, 100, 101), _bar(5, 101, 103, 100, 102), _bar(6, 102, 104, 101, 103),
            # Breakaway gap up (> 104)
            _bar(7, 108, 112, 107.5, 111), _bar(8, 111, 114, 110, 113),
        ]
        self._assert_chart_detected("Bullish Island Reversal", isl)
        # 8. Adam and Eve Bottom (sharp narrow L1 + wide rounded L2)
        ae_closes = _interp_path([(0, 120), (3, 115), (5, 98), (7, 115), (10, 116), (13, 101)]) + [100.0, 99.5, 99.2, 99.4, 99.8, 100.5, 106.0, 112.0]
        self._assert_chart_detected("Adam and Eve Bottom", _bars_from_closes(ae_closes, spread=0.005))
        # 9. Pipe Bottom
        pipe_b = [_bar(i, 115 - i, 116 - i, 114 - i, 114.5 - i) for i in range(8)]
        pipe_b.append(_bar(8, 107, 107.5, 98.0, 99.5))
        pipe_b.append(_bar(9, 99.5, 109.0, 98.2, 108.5))
        self._assert_chart_detected("Pipe Bottom", pipe_b)
        # 10. Broadening Bottom (downtrend into expanding megaphone)
        self._assert_chart_detected(
            "Broadening Bottom",
            _bars_from_closes(_interp_path([(0, 145), (8, 115), (11, 122), (14, 108), (18, 128), (22, 100), (26, 118)])),
        )

    def test_b_bearish_reversal_10(self) -> None:
        # 11. Double Top (M)
        self._assert_chart_detected(
            "Double Top (M)",
            _bars_from_closes(_interp_path([(0, 100), (5, 120), (10, 105), (15, 119), (19, 108)])),
        )
        # 12. Triple Top
        self._assert_chart_detected(
            "Triple Top",
            _bars_from_closes(_interp_path([(0, 100), (4, 120), (8, 106), (12, 119), (16, 105), (20, 119.5), (24, 108)])),
        )
        # 13. Head and Shoulders
        self._assert_chart_detected(
            "Head and Shoulders",
            _bars_from_closes(_interp_path([(0, 100), (4, 115), (8, 104), (12, 128), (16, 104), (20, 114), (24, 106)])),
        )
        # 14. Rounding Top
        dome = [130.0 - 20.0 * ((i - 18) / 18.0) ** 2 for i in range(37)]
        self._assert_chart_detected("Rounding Top", _bars_from_closes(dome, spread=0.004))
        # 15. Inverted V (Spike Top)
        self._assert_chart_detected(
            "Inverted V (Spike Top)",
            _bars_from_closes(_interp_path([(0, 100), (6, 100), (11, 125), (17, 104)])),
        )
        # 16. Rising Wedge
        self._assert_chart_detected(
            "Rising Wedge",
            _bars_from_closes(_interp_path([(0, 90), (4, 112), (8, 98), (12, 116), (16, 107), (20, 119), (23, 114)])),
        )
        # 17. Bearish Island Reversal
        b_isl = [
            _bar(0, 100, 102, 99, 101), _bar(1, 101, 103, 100, 102),
            _bar(2, 102, 104, 101, 103), _bar(3, 103, 105, 102, 104),
            _bar(4, 110, 112, 109, 111), _bar(5, 111, 113, 110, 111), _bar(6, 111, 112, 109, 110),
            _bar(7, 104, 105, 100, 101), _bar(8, 101, 102, 98, 99),
        ]
        self._assert_chart_detected("Bearish Island Reversal", b_isl)
        # 18. Adam and Eve Top
        ae_top = _interp_path([(0, 100), (3, 105), (5, 122), (7, 105), (10, 104), (13, 119)]) + [120.5, 121.0, 121.2, 120.8, 120.3, 119.5, 113.0, 108.0]
        self._assert_chart_detected("Adam and Eve Top", _bars_from_closes(ae_top, spread=0.005))
        # 19. Pipe Top
        pipe_t = [_bar(i, 100 + i, 101 + i, 99 + i, 100.5 + i) for i in range(8)]
        pipe_t.append(_bar(8, 108, 118.0, 107.5, 117.0))
        pipe_t.append(_bar(9, 117.0, 117.8, 106.5, 107.0))
        self._assert_chart_detected("Pipe Top", pipe_t)
        # 20. Broadening Top (uptrend into expanding megaphone)
        self._assert_chart_detected(
            "Broadening Top",
            _bars_from_closes(_interp_path([(0, 85), (8, 115), (11, 108), (14, 122), (18, 102), (22, 130), (26, 112)])),
        )

    def test_c_bullish_continuation_5(self) -> None:
        # 21. Cup and Handle
        cup = [100.0 + 25.0 * ((i - 14) / 14.0) ** 2 for i in range(29)]
        handle = [124.0, 122.5, 121.0, 120.0, 119.5, 121.0, 123.5]
        self._assert_chart_detected("Cup and Handle", _bars_from_closes(cup + handle, spread=0.005))
        # 22. Bull Flag
        b_flag = _interp_path([(0, 95), (3, 97), (9, 125), (16, 117)])
        self._assert_chart_detected("Bull Flag", _bars_from_closes(b_flag, spread=0.006))
        # 23. Bull Pennant
        pole = _interp_path([(0, 95), (7, 126)])
        pen = [
            _bar(8, 125, 126.5, 119.5, 121),
            _bar(9, 121, 125.5, 120.5, 124),
            _bar(10, 124, 124.8, 121.5, 122),
            _bar(11, 122, 124.2, 122.0, 123.5),
            _bar(12, 123.5, 123.9, 122.4, 123.0),
            _bar(13, 123.0, 123.5, 122.6, 123.2),
        ]
        self._assert_chart_detected("Bull Pennant", _bars_from_closes(pole, spread=0.005) + pen)
        # 24. Ascending Triangle
        self._assert_chart_detected(
            "Ascending Triangle",
            _bars_from_closes(_interp_path([(0, 100), (4, 120), (8, 105), (12, 120), (16, 111), (20, 120), (23, 116)])),
        )
        # 25. High and Tight Flag
        htf = _interp_path([(0, 50), (15, 92), (24, 83)])
        self._assert_chart_detected("High and Tight Flag", _bars_from_closes(htf, spread=0.006))

    def test_d_bearish_continuation_5(self) -> None:
        # 26. Bear Flag
        bear_f = _interp_path([(0, 130), (3, 128), (9, 100), (16, 108)])
        self._assert_chart_detected("Bear Flag", _bars_from_closes(bear_f, spread=0.006))
        # 27. Bear Pennant
        bpole = _interp_path([(0, 130), (7, 98)])
        bpen = [
            _bar(8, 99, 104.5, 98.0, 102),
            _bar(9, 102, 103.8, 99.0, 100),
            _bar(10, 100, 103.0, 99.6, 102),
            _bar(11, 102, 102.4, 100.2, 101),
            _bar(12, 101, 101.9, 100.6, 101.2),
            _bar(13, 101.2, 101.5, 100.8, 101.0),
        ]
        self._assert_chart_detected("Bear Pennant", _bars_from_closes(bpole, spread=0.005) + bpen)
        # 28. Descending Triangle
        self._assert_chart_detected(
            "Descending Triangle",
            _bars_from_closes(_interp_path([(0, 125), (4, 100), (8, 118), (12, 100), (16, 112), (20, 100), (23, 106)])),
        )
        # 29. Inverted Cup and Handle
        icup = [125.0 - 25.0 * ((i - 14) / 14.0) ** 2 for i in range(29)]
        ihandle = [101.0, 103.0, 104.5, 105.5, 106.0, 104.0, 101.5]
        self._assert_chart_detected("Inverted Cup and Handle", _bars_from_closes(icup + ihandle, spread=0.005))
        # 30. Bearish Measured Move
        self._assert_chart_detected(
            "Bearish Measured Move",
            _bars_from_closes(_interp_path([(0, 120), (4, 135), (10, 105), (16, 120), (20, 110)])),
        )

    def test_e_neutral_bilateral_10(self) -> None:
        # 31. Symmetrical Triangle
        self._assert_chart_detected(
            "Symmetrical Triangle",
            _bars_from_closes(_interp_path([(0, 110), (4, 128), (8, 96), (12, 121), (16, 103), (20, 116), (24, 108), (27, 112)])),
        )
        # 32. Rectangle / Trading Range
        self._assert_chart_detected(
            "Rectangle / Trading Range",
            _bars_from_closes(_interp_path([(0, 110), (4, 120), (8, 105), (12, 120), (16, 105), (20, 120), (23, 112)])),
        )
        # 33. Broadening Formation (Megaphone)
        self._assert_chart_detected(
            "Broadening Formation (Megaphone)",
            _bars_from_closes(_interp_path([(0, 110), (4, 116), (8, 106), (12, 122), (16, 100), (20, 128), (24, 94), (27, 110)])),
        )
        # 34. Diamond Formation
        dia_bars = []
        amps = [2, 2, 3, 4, 6, 8, 10, 12, 14, 15, 14, 12, 9, 7, 5, 3, 2, 2, 2, 2]
        for i, a in enumerate(amps):
            sign = 1 if i % 2 == 0 else -1
            c = 100.0 + sign * a * 0.5
            dia_bars.append(_bar(i, 100.0, 100.0 + a, 100.0 - a, c))
        self._assert_chart_detected("Diamond Formation", dia_bars)
        # 35. Ascending Broadening Wedge
        self._assert_chart_detected(
            "Ascending Broadening Wedge",
            _bars_from_closes(_interp_path([(0, 100), (4, 108), (8, 103), (12, 118), (16, 106), (20, 130), (24, 109), (27, 120)])),
        )
        # 36. Descending Broadening Wedge
        self._assert_chart_detected(
            "Descending Broadening Wedge",
            _bars_from_closes(_interp_path([(0, 130), (4, 120), (8, 127), (12, 108), (16, 124), (20, 94), (24, 121), (27, 108)])),
        )
        # 37. Horizontal Channel
        self._assert_chart_detected(
            "Horizontal Channel",
            _bars_from_closes(_interp_path([(0, 108), (5, 118), (10, 104), (15, 118), (20, 104), (25, 118), (30, 104), (34, 112)])),
        )
        # 38. Rising Channel
        self._assert_chart_detected(
            "Rising Channel",
            _bars_from_closes(_interp_path([(0, 100), (4, 112), (8, 105), (12, 117), (16, 110), (20, 122), (24, 115), (27, 120)])),
        )
        # 39. Falling Channel
        self._assert_chart_detected(
            "Falling Channel",
            _bars_from_closes(_interp_path([(0, 130), (4, 118), (8, 125), (12, 113), (16, 120), (20, 108), (24, 115), (27, 110)])),
        )
        # 40. Volatility Contraction Pattern (VCP)
        vcp_closes = (
            _interp_path([(0, 120), (5, 96), (11, 119)])  # -20% T1
            + _interp_path([(0, 119), (5, 105), (11, 119)])[1:]  # -11.8% T2
            + _interp_path([(0, 119), (4, 113), (8, 119), (11, 116)])[1:]  # -5% T3
        )
        self._assert_chart_detected("Volatility Contraction Pattern (VCP)", _bars_from_closes(vcp_closes, spread=0.004))


class TestAll30CandlestickPatterns(unittest.TestCase):
    def setUp(self) -> None:
        self.detector = CandlestickPatternDetector()

    @staticmethod
    def _prefix(direction: str, count: int = 8) -> list[OHLCVBar]:
        bars: list[OHLCVBar] = []
        base = 100.0
        step = 1.5 if direction == "UP" else (-1.5 if direction == "DOWN" else 0.0)
        for i in range(count):
            o = base + i * step
            c = o + (1.0 if direction == "UP" else (-1.0 if direction == "DOWN" else 0.2))
            bars.append(_bar(i, o, max(o, c) + 0.5, min(o, c) - 0.5, c))
        return bars

    def _assert_candle_detected(self, expected_name: str, bars: list[OHLCVBar]) -> None:
        series = build_timeframe_series("TEST", Timeframe.DAILY, bars)
        names = {c.name for c in self.detector.detect(series)}
        self.assertIn(expected_name, names, f"Expected '{expected_name}' not detected. Found: {sorted(names)}")

    def test_a_single_candle_12(self) -> None:
        # 1. Doji
        self._assert_candle_detected("Doji", self._prefix("FLAT") + [_bar(8, 100.0, 101.0, 99.0, 100.05)])
        # 2. Dragonfly Doji
        self._assert_candle_detected("Dragonfly Doji", self._prefix("DOWN") + [_bar(8, 88.0, 88.1, 83.0, 88.0)])
        # 3. Gravestone Doji
        self._assert_candle_detected("Gravestone Doji", self._prefix("UP") + [_bar(8, 112.0, 117.0, 111.9, 112.0)])
        # 4. Long-Legged Doji
        self._assert_candle_detected("Long-Legged Doji", self._prefix("FLAT") + [_bar(8, 100.0, 104.0, 96.0, 100.1)])
        # 5. Hammer (downtrend)
        self._assert_candle_detected("Hammer", self._prefix("DOWN") + [_bar(8, 87.2, 88.1, 82.0, 88.0)])
        # 6. Hanging Man (uptrend)
        self._assert_candle_detected("Hanging Man", self._prefix("UP") + [_bar(8, 112.2, 113.1, 107.0, 113.0)])
        # 7. Inverted Hammer (downtrend)
        self._assert_candle_detected("Inverted Hammer", self._prefix("DOWN") + [_bar(8, 87.0, 93.0, 86.9, 87.8)])
        # 8. Shooting Star (uptrend)
        self._assert_candle_detected("Shooting Star", self._prefix("UP") + [_bar(8, 113.0, 119.0, 112.9, 113.8)])
        # 9. Bullish Marubozu
        self._assert_candle_detected("Bullish Marubozu", self._prefix("FLAT") + [_bar(8, 100.0, 105.1, 99.9, 105.0)])
        # 10. Bearish Marubozu
        self._assert_candle_detected("Bearish Marubozu", self._prefix("FLAT") + [_bar(8, 105.0, 105.1, 99.9, 100.0)])
        # 11. Spinning Top
        self._assert_candle_detected("Spinning Top", self._prefix("FLAT") + [_bar(8, 100.0, 101.2, 99.2, 100.4)])
        # 12. High-Wave Candle
        self._assert_candle_detected("High-Wave Candle", self._prefix("FLAT") + [_bar(8, 100.0, 104.5, 96.0, 101.2)])

    def test_b_two_candle_10(self) -> None:
        # 13. Bullish Engulfing
        self._assert_candle_detected("Bullish Engulfing", self._prefix("DOWN") + [_bar(8, 88.0, 88.3, 85.8, 86.0), _bar(9, 85.6, 89.5, 85.4, 89.2)])
        # 14. Bearish Engulfing
        self._assert_candle_detected("Bearish Engulfing", self._prefix("UP") + [_bar(8, 112.0, 114.2, 111.8, 114.0), _bar(9, 114.4, 114.6, 110.8, 111.0)])
        # 15. Bullish Harami
        self._assert_candle_detected("Bullish Harami", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 84.8, 85.0), _bar(9, 86.2, 87.6, 86.0, 87.4)])
        # 16. Bearish Harami
        self._assert_candle_detected("Bearish Harami", self._prefix("UP") + [_bar(8, 111.0, 115.2, 110.8, 115.0), _bar(9, 113.8, 114.0, 112.4, 112.6)])
        # 17. Piercing Line
        self._assert_candle_detected("Piercing Line", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 84.8, 85.0), _bar(9, 84.0, 88.0, 83.8, 87.8)])
        # 18. Dark Cloud Cover
        self._assert_candle_detected("Dark Cloud Cover", self._prefix("UP") + [_bar(8, 111.0, 115.2, 110.8, 115.0), _bar(9, 116.0, 116.2, 112.0, 112.2)])
        # 19. Tweezer Bottom
        self._assert_candle_detected("Tweezer Bottom", self._prefix("DOWN") + [_bar(8, 88.0, 88.2, 85.0, 85.5), _bar(9, 85.6, 88.4, 85.05, 88.0)])
        # 20. Tweezer Top
        self._assert_candle_detected("Tweezer Top", self._prefix("UP") + [_bar(8, 112.0, 115.0, 111.8, 114.5), _bar(9, 114.4, 114.95, 111.6, 112.0)])
        # 21. Bullish Kicker
        self._assert_candle_detected("Bullish Kicker", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 85.8, 86.0), _bar(9, 90.0, 93.8, 89.8, 93.5)])
        # 22. Bearish Kicker
        self._assert_candle_detected("Bearish Kicker", self._prefix("UP") + [_bar(8, 111.0, 114.2, 110.8, 114.0), _bar(9, 110.0, 110.2, 106.2, 106.5)])

    def test_c_three_candle_8(self) -> None:
        # 23. Morning Star
        self._assert_candle_detected("Morning Star", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 84.8, 85.0), _bar(9, 84.2, 85.0, 83.4, 84.7), _bar(10, 85.2, 89.0, 85.0, 88.6)])
        # 24. Evening Star
        self._assert_candle_detected("Evening Star", self._prefix("UP") + [_bar(8, 111.0, 115.2, 110.8, 115.0), _bar(9, 115.8, 116.6, 115.0, 115.3), _bar(10, 114.8, 115.0, 111.0, 111.4)])
        # 25. Morning Doji Star
        self._assert_candle_detected("Morning Doji Star", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 84.8, 85.0), _bar(9, 84.2, 85.0, 83.4, 84.25), _bar(10, 85.2, 89.0, 85.0, 88.6)])
        # 26. Evening Doji Star
        self._assert_candle_detected("Evening Doji Star", self._prefix("UP") + [_bar(8, 111.0, 115.2, 110.8, 115.0), _bar(9, 115.8, 116.6, 115.0, 115.85), _bar(10, 114.8, 115.0, 111.0, 111.4)])
        # 27. Three White Soldiers
        self._assert_candle_detected("Three White Soldiers", self._prefix("FLAT") + [_bar(8, 100.0, 103.2, 99.8, 103.0), _bar(9, 101.8, 105.4, 101.6, 105.2), _bar(10, 103.8, 107.6, 103.6, 107.4)])
        # 28. Three Black Crows
        self._assert_candle_detected("Three Black Crows", self._prefix("FLAT") + [_bar(8, 108.0, 108.2, 104.8, 105.0), _bar(9, 106.2, 106.4, 102.6, 102.8), _bar(10, 104.2, 104.4, 100.4, 100.6)])
        # 29. Three Inside Up
        self._assert_candle_detected("Three Inside Up", self._prefix("DOWN") + [_bar(8, 89.0, 89.2, 84.8, 85.0), _bar(9, 86.0, 87.8, 85.8, 87.5), _bar(10, 87.6, 90.8, 87.4, 90.5)])
        # 30. Three Inside Down
        self._assert_candle_detected("Three Inside Down", self._prefix("UP") + [_bar(8, 111.0, 115.2, 110.8, 115.0), _bar(9, 114.0, 114.2, 112.2, 112.5), _bar(10, 112.4, 112.6, 109.2, 109.5)])


class TestLifecycleAndMTFValidation(unittest.TestCase):
    def _build_double_bottom_payload(
        self,
        last_bar: dict,
        weekly_trend: str = "UP",
        monthly_trend: str = "UP",
        l2_book: dict | None = None,
    ) -> dict:
        base_closes = _interp_path([(0, 120), (5, 100), (10, 115), (15, 101), (18, 112)])
        daily = [
            {
                "timestamp": f"2026-10-{i + 1:02d}T00:00:00Z",
                "open": b.open,
                "high": b.high,
                "low": b.low,
                "close": b.close,
                "volume": 1_000_000,
            }
            for i, b in enumerate(_bars_from_closes(base_closes, spread=0.005))
        ]
        daily.append(last_bar)

        w_step = 2.0 if weekly_trend == "UP" else -2.0
        m_step = 3.0 if monthly_trend == "UP" else -3.0
        weekly = [
            {"timestamp": f"2026-01-{i + 1:02d}T00:00:00Z", "open": 90 + i * w_step, "high": 92 + i * w_step, "low": 88 + i * w_step, "close": 91 + i * w_step, "volume": 5_000_000}
            for i in range(25)
        ]
        monthly = [
            {"timestamp": f"2025-{(i % 12) + 1:02d}-01T00:00:00Z", "open": 80 + i * m_step, "high": 83 + i * m_step, "low": 78 + i * m_step, "close": 82 + i * m_step, "volume": 20_000_000}
            for i in range(15)
        ]
        return {
            "symbol": "NVDA",
            "as_of": "2026-11-25T16:00:00-05:00",
            "live_price": last_bar["close"],
            "market_value": 115.0,
            "daily": daily,
            "weekly": weekly,
            "monthly": monthly,
            "l2_book": l2_book,
        }

    def test_four_lifecycle_states_and_live_cap(self) -> None:
        coord = TradingChartCoordinator()

        # 1. FORMING (below neckline $115.58)
        r_form = coord.run_scan(
            self._build_double_bottom_payload(
                {"timestamp": "2026-10-20T00:00:00Z", "open": 112.0, "high": 114.0, "low": 111.5, "close": 113.5, "volume": 900_000}
            )
        )
        db_form = next(d for d in r_form.detections if d.candidate.name == "Double Bottom (W)" and d.candidate.timeframe == Timeframe.DAILY)
        self.assertEqual(db_form.lifecycle_state, PatternLifecycleState.FORMING)
        self.assertLessEqual(db_form.validation.total_score, 78.0)

        # 2. CONFIRMED BREAKOUT (completed close > neckline + 1.8x volume + L2 Bid Wall + Full MTF UP)
        r_conf = coord.run_scan(
            self._build_double_bottom_payload(
                {"timestamp": "2026-10-20T00:00:00Z", "open": 113.0, "high": 120.0, "low": 112.8, "close": 119.5, "volume": 2_000_000},
                l2_book={"bids": [{"price": 114.0, "shares": 200_000}], "asks": [{"price": 135.0, "shares": 50_000}]},
            )
        )
        db_conf = next(d for d in r_conf.detections if d.candidate.name == "Double Bottom (W)" and d.candidate.timeframe == Timeframe.DAILY)
        self.assertEqual(db_conf.lifecycle_state, PatternLifecycleState.CONFIRMED_BREAKOUT)
        self.assertGreaterEqual(db_conf.validation.total_score, 85.0)

        # 3. LIVE INCOMPLETE BAR CAP (same breakout price, but bar still open -> MUST STAY FORMING!)
        r_live = coord.run_scan(
            self._build_double_bottom_payload(
                {"timestamp": "2026-10-20T00:00:00Z", "open": 113.0, "high": 120.0, "low": 112.8, "close": 119.5, "volume": 2_000_000, "is_live_incomplete": True}
            )
        )
        db_live = next(d for d in r_live.detections if d.candidate.name == "Double Bottom (W)" and d.candidate.timeframe == Timeframe.DAILY)
        self.assertEqual(db_live.lifecycle_state, PatternLifecycleState.FORMING)
        self.assertTrue(db_live.is_live_incomplete_capped)

        # 4. FAILED BREAKOUT (intraday spike above neckline $118, rejected and closed back inside at $112.5)
        r_fail = coord.run_scan(
            self._build_double_bottom_payload(
                {"timestamp": "2026-10-20T00:00:00Z", "open": 113.0, "high": 118.5, "low": 112.0, "close": 112.5, "volume": 950_000}
            )
        )
        db_fail = next(d for d in r_fail.detections if d.candidate.name == "Double Bottom (W)" and d.candidate.timeframe == Timeframe.DAILY)
        self.assertEqual(db_fail.lifecycle_state, PatternLifecycleState.FAILED_BREAKOUT)
        self.assertLessEqual(db_fail.validation.total_score, 45.0)

        # 5. INVALIDATED (closed below $99 invalidation floor)
        r_inv = coord.run_scan(
            self._build_double_bottom_payload(
                {"timestamp": "2026-10-20T00:00:00Z", "open": 102.0, "high": 102.5, "low": 94.0, "close": 95.0, "volume": 2_100_000}
            )
        )
        db_inv = next(d for d in r_inv.detections if d.candidate.name == "Double Bottom (W)" and d.candidate.timeframe == Timeframe.DAILY)
        self.assertEqual(db_inv.lifecycle_state, PatternLifecycleState.INVALIDATED)
        self.assertLessEqual(db_inv.validation.total_score, 25.0)

        # Verify Markdown & Canvas overlay exports cleanly
        md = coord.format_markdown(r_conf)
        self.assertIn("Double Bottom (W)", md)
        self.assertIn("Confirmed Breakout", md)
        self.assertIn("Daily", r_conf.canvas_overlays)

    def test_bilateral_bearish_breakout_flips_target_and_stop(self) -> None:
        coord = TradingChartCoordinator()
        rect_closes = _interp_path([(0, 110), (4, 120), (8, 105), (12, 120), (16, 105), (20, 120), (23, 108)])
        daily = [
            {"timestamp": f"2026-10-{i + 1:02d}T00:00:00Z", "open": b.open, "high": b.high, "low": b.low, "close": b.close, "volume": 1_000_000}
            for i, b in enumerate(_bars_from_closes(rect_closes, spread=0.004))
        ]
        # Clean volume breakdown below $105 floor
        daily.append({"timestamp": "2026-10-25T00:00:00Z", "open": 106.0, "high": 106.5, "low": 99.0, "close": 100.0, "volume": 2_200_000})
        report = coord.run_scan({"symbol": "TEST", "daily": daily})
        rect = next(d for d in report.detections if d.candidate.name == "Rectangle / Trading Range")
        self.assertEqual(rect.lifecycle_state, PatternLifecycleState.CONFIRMED_BREAKOUT)
        self.assertEqual(rect.resolved_bias.value, "Bearish")
        self.assertLess(rect.candidate.target_price, rect.candidate.breakout_level)
        self.assertGreater(rect.candidate.invalidation_level, rect.candidate.breakout_level)

    def test_reusable_html_renderer_zero_leaks_and_contract_keys(self) -> None:
        coord = TradingChartCoordinator()
        payload = self._build_double_bottom_payload(
            {"timestamp": "2026-10-20T00:00:00Z", "open": 113.0, "high": 120.0, "low": 112.8, "close": 119.5, "volume": 2_000_000},
            l2_book={"bids": [{"price": 114.0, "shares": 200_000}], "asks": [{"price": 135.0, "shares": 50_000}]},
        )
        payload["symbol"] = "ACME"
        report, ctx = coord.run_scan_with_context(payload)
        html_out = coord.render_html(report, ctx)
        for required in (
            "ACME", 'data-tf="TODAY"', 'data-tf="2D"', 'data-tf="1D"', 'data-tf="1W"', 'data-tf="1M"',
            'id="ctrlStrip"', 'id="coachStrip"', 'id="viewA"', 'id="viewB"', 'id="viewC"',
            "actionHeader", "actionTake", "lastRenderedPills", "hoveredPillIdx",
            "Corporate Events", "Layer 9", "••••3782", "Simple Kid-Level Summary",
            "TODAY_BARS", "TWO_DAY_BARS", "DAILY_BARS", "WEEKLY_BARS", "HORIZONS",
        ):
            self.assertIn(required, html_out, f"Missing required chart contract key: {required}")
        # Verify zero foreign ticker template leakage
        for banned in ("SPCX", "NVDA", "NBIS", "SOFI", "CRWV"):
            self.assertNotIn(banned, html_out, f"Foreign ticker leak found in reusable renderer: {banned}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
