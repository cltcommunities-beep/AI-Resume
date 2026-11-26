"""5-Factor Institutional Pattern Validator & Strict 4-State Lifecycle State Machine."""

from __future__ import annotations

from dataclasses import replace

from .models import (
    L2OrderBookSnapshot,
    PatternBias,
    PatternKind,
    PatternLifecycleState,
    RawPatternCandidate,
    Timeframe,
    TimeframeSeries,
    ValidatedPattern,
    ValidationBreakdown,
)


class InstitutionalPatternValidator:
    """Implements PatternValidatorProtocol with Volume, Breakout, S/R+L2, Trend & MTF checks."""

    def validate(
        self,
        candidate: RawPatternCandidate,
        series: TimeframeSeries,
        all_series: dict[Timeframe, TimeframeSeries],
        sr_levels: tuple[list[float], list[float]],
        l2_book: L2OrderBookSnapshot | None,
    ) -> ValidatedPattern:
        bars = series.bars
        last_bar = bars[-1]
        is_live_incomplete = last_bar.is_live_incomplete

        # Identify most recent completed bar for strict breakout confirmation
        completed_bars = [b for b in bars if not b.is_live_incomplete]
        eval_bar = completed_bars[-1] if completed_bars else last_bar
        eval_idx = len(completed_bars) - 1 if completed_bars else len(bars) - 1
        atr = series.atr14[eval_idx] if series.atr14 and eval_idx < len(series.atr14) else series.latest_atr
        vol_avg = (
            series.vol_sma20[eval_idx]
            if series.vol_sma20 and eval_idx < len(series.vol_sma20)
            else max(eval_bar.volume, 1.0)
        )
        vol_ratio = eval_bar.volume / max(vol_avg, 1.0)

        # 1. Classify Lifecycle State & Resolve Bilateral Bias
        state, resolved_bias, buffer_atr, capped = self._classify_lifecycle(
            candidate, bars, completed_bars, eval_bar, atr, vol_ratio, is_live_incomplete
        )

        # If a bilateral pattern resolved Bearish, flip trigger/invalidation/target to the downside rail
        effective_candidate = candidate
        if (
            candidate.bias == PatternBias.NEUTRAL
            and candidate.secondary_breakout_level is not None
            and resolved_bias == PatternBias.BEARISH
        ):
            upper = max(candidate.breakout_level, candidate.secondary_breakout_level)
            lower = min(candidate.breakout_level, candidate.secondary_breakout_level)
            span = max(upper - lower, atr)
            effective_candidate = replace(
                candidate,
                breakout_level=lower,
                invalidation_level=upper,
                target_price=max(0.01, lower - span),
            )

        # 2. Factor 1 — Geometry (0-20)
        geom_score = min(20.0, max(0.0, candidate.geometry_score))

        # 3. Factor 2 — Volume Confirmation (0-20)
        if vol_ratio >= 1.8:
            vol_score = 20.0
        elif vol_ratio >= 1.5:
            vol_score = 18.0
        elif vol_ratio >= 1.3:
            vol_score = 15.5
        elif vol_ratio >= 1.0:
            vol_score = 11.5
        elif vol_ratio >= 0.75:
            vol_score = 8.0
        else:
            vol_score = 5.0

        # 4. Factor 3 — Breakout & Close Confirmation (0-20)
        if state == PatternLifecycleState.CONFIRMED_BREAKOUT:
            brk_score = min(20.0, 16.5 + min(abs(buffer_atr), 1.4) * 2.5)
        elif state == PatternLifecycleState.FORMING:
            brk_score = 12.0 if not capped else 10.5
        elif state == PatternLifecycleState.FAILED_BREAKOUT:
            brk_score = 4.0
        else:  # INVALIDATED
            brk_score = 0.0

        # 5. Factor 4 — Support/Resistance & Live Robinhood L2 Alignment (0-20)
        sr_l2_score, l2_note = self._score_sr_and_l2(
            effective_candidate, resolved_bias, eval_bar.close, atr, sr_levels, l2_book
        )

        # 6. Factor 5 — Trend Direction & Multi-Timeframe (D/W/M) Confluence (0-20)
        mtf_score, mtf_note = self._score_mtf_confluence(
            candidate, resolved_bias, series, all_series
        )

        raw_total = geom_score + vol_score + brk_score + sr_l2_score + mtf_score
        # Enforce strict lifecycle score ceilings so unconfirmed or failed patterns never look "90/100 Bullish"
        if state == PatternLifecycleState.INVALIDATED:
            total = min(raw_total, 25.0)
        elif state == PatternLifecycleState.FAILED_BREAKOUT:
            total = min(raw_total, 45.0)
        elif state == PatternLifecycleState.FORMING:
            total = min(raw_total, 78.0)
        else:
            total = min(100.0, raw_total)

        breakdown = ValidationBreakdown(
            geometry_score=geom_score,
            volume_score=vol_score,
            breakout_score=brk_score,
            sr_l2_score=sr_l2_score,
            mtf_trend_score=mtf_score,
            total_score=total,
            volume_ratio=vol_ratio,
            breakout_buffer_atr=buffer_atr,
            l2_alignment_note=l2_note,
            mtf_note=mtf_note,
        )

        action = self._build_action_summary(effective_candidate, state, resolved_bias, vol_ratio, capped)
        return ValidatedPattern(
            candidate=effective_candidate,
            lifecycle_state=state,
            resolved_bias=resolved_bias,
            validation=breakdown,
            is_live_incomplete_capped=capped,
            action_summary=action,
        )

    def _classify_lifecycle(
        self,
        c: RawPatternCandidate,
        bars: tuple,
        completed_bars: list,
        eval_bar,
        atr: float,
        vol_ratio: float,
        is_live_incomplete: bool,
    ) -> tuple[PatternLifecycleState, PatternBias, float, bool]:
        min_buf = min(0.20 * atr, max(c.breakout_level * 0.0025, 1e-6))
        recent_slice = completed_bars[-3:] if len(completed_bars) >= 3 else completed_bars

        # Bilateral / Neutral patterns can break EITHER upper rail or lower rail
        if c.bias == PatternBias.NEUTRAL and c.secondary_breakout_level is not None:
            upper = max(c.breakout_level, c.secondary_breakout_level)
            lower = min(c.breakout_level, c.secondary_breakout_level)

            # Check if live bar poked outside while unclosed
            if is_live_incomplete and (bars[-1].close > upper + min_buf or bars[-1].close < lower - min_buf):
                if lower <= eval_bar.close <= upper:
                    return PatternLifecycleState.FORMING, PatternBias.NEUTRAL, 0.0, True

            if eval_bar.close >= upper + min_buf:
                buf_atr = (eval_bar.close - upper) / max(atr, 1e-6)
                if vol_ratio >= 1.30:
                    return PatternLifecycleState.CONFIRMED_BREAKOUT, PatternBias.BULLISH, buf_atr, False
                return PatternLifecycleState.FORMING, PatternBias.BULLISH, buf_atr, False

            if eval_bar.close <= lower - min_buf:
                buf_atr = (lower - eval_bar.close) / max(atr, 1e-6)
                if vol_ratio >= 1.30:
                    return PatternLifecycleState.CONFIRMED_BREAKOUT, PatternBias.BEARISH, buf_atr, False
                return PatternLifecycleState.FORMING, PatternBias.BEARISH, buf_atr, False

            # Failed breakout check on either rail
            for b in recent_slice:
                if b.high > upper + min_buf and eval_bar.close < upper:
                    return PatternLifecycleState.FAILED_BREAKOUT, PatternBias.NEUTRAL, (eval_bar.close - upper) / max(atr, 1e-6), False
                if b.low < lower - min_buf and eval_bar.close > lower:
                    return PatternLifecycleState.FAILED_BREAKOUT, PatternBias.NEUTRAL, (lower - eval_bar.close) / max(atr, 1e-6), False

            return PatternLifecycleState.FORMING, PatternBias.NEUTRAL, 0.0, False

        # Directional patterns (BULLISH or BEARISH)
        if c.bias == PatternBias.BULLISH:
            # 1. Invalidated check on completed bar
            if eval_bar.close < c.invalidation_level:
                buf = (eval_bar.close - c.invalidation_level) / max(atr, 1e-6)
                return PatternLifecycleState.INVALIDATED, PatternBias.BULLISH, buf, False

            # 2. Live unclosed bar guardrail: cap ONLY when the breakout has NOT yet occurred on a completed bar!
            if is_live_incomplete and eval_bar.close < c.breakout_level + min_buf:
                if c.kind == PatternKind.CANDLESTICK and c.end_idx == len(bars) - 1:
                    return PatternLifecycleState.FORMING, PatternBias.BULLISH, 0.0, True
                if bars[-1].close >= c.breakout_level + min_buf:
                    return PatternLifecycleState.FORMING, PatternBias.BULLISH, (bars[-1].close - c.breakout_level) / max(atr, 1e-6), True

            # 3. Confirmed Breakout on completed bar with volume expansion
            if eval_bar.close >= c.breakout_level + min_buf:
                buf = (eval_bar.close - c.breakout_level) / max(atr, 1e-6)
                if vol_ratio >= 1.30:
                    return PatternLifecycleState.CONFIRMED_BREAKOUT, PatternBias.BULLISH, buf, False
                return PatternLifecycleState.FORMING, PatternBias.BULLISH, buf, False

            # For strong completed candlestick confirmation patterns that closed near their own high on heavy volume
            if (
                c.kind == PatternKind.CANDLESTICK
                and c.end_idx < len(completed_bars) - 1
                and eval_bar.close > c.breakout_level
                and vol_ratio >= 1.30
            ):
                buf = (eval_bar.close - c.breakout_level) / max(atr, 1e-6)
                return PatternLifecycleState.CONFIRMED_BREAKOUT, PatternBias.BULLISH, buf, False

            # 4. Failed Breakout check (bull trap wick / rejected breakout)
            for b in recent_slice:
                if b.high > c.breakout_level + min_buf and eval_bar.close < c.breakout_level:
                    return PatternLifecycleState.FAILED_BREAKOUT, PatternBias.BULLISH, (eval_bar.close - c.breakout_level) / max(atr, 1e-6), False

            return PatternLifecycleState.FORMING, PatternBias.BULLISH, (eval_bar.close - c.breakout_level) / max(atr, 1e-6), False

        # BEARISH directional
        if eval_bar.close > c.invalidation_level:
            buf = (eval_bar.close - c.invalidation_level) / max(atr, 1e-6)
            return PatternLifecycleState.INVALIDATED, PatternBias.BEARISH, buf, False

        if is_live_incomplete and eval_bar.close > c.breakout_level - min_buf:
            if c.kind == PatternKind.CANDLESTICK and c.end_idx == len(bars) - 1:
                return PatternLifecycleState.FORMING, PatternBias.BEARISH, 0.0, True
            if bars[-1].close <= c.breakout_level - min_buf:
                return PatternLifecycleState.FORMING, PatternBias.BEARISH, (c.breakout_level - bars[-1].close) / max(atr, 1e-6), True

        if eval_bar.close <= c.breakout_level - min_buf:
            buf = (c.breakout_level - eval_bar.close) / max(atr, 1e-6)
            if vol_ratio >= 1.30:
                return PatternLifecycleState.CONFIRMED_BREAKOUT, PatternBias.BEARISH, buf, False
            return PatternLifecycleState.FORMING, PatternBias.BEARISH, buf, False

        for b in recent_slice:
            if b.low < c.breakout_level - min_buf and eval_bar.close > c.breakout_level:
                return PatternLifecycleState.FAILED_BREAKOUT, PatternBias.BEARISH, (c.breakout_level - eval_bar.close) / max(atr, 1e-6), False

        return PatternLifecycleState.FORMING, PatternBias.BEARISH, (c.breakout_level - eval_bar.close) / max(atr, 1e-6), False

    @staticmethod
    def _score_sr_and_l2(
        c: RawPatternCandidate,
        bias: PatternBias,
        spot: float,
        atr: float,
        sr_levels: tuple[list[float], list[float]],
        l2_book: L2OrderBookSnapshot | None,
    ) -> tuple[float, str]:
        supports, resistances = sr_levels
        score = 12.0
        notes: list[str] = []
        near_tol = max(1.25 * atr, spot * 0.025)

        if bias == PatternBias.BULLISH:
            if any(abs(c.invalidation_level - s) <= near_tol for s in supports):
                score += 4.0
                notes.append("Floor aligns w/ swing S/R")
            if l2_book:
                near_bids = [w for w in l2_book.bid_walls if 0 < (spot - w.price) / max(spot, 1e-6) <= 0.08]
                blocking_asks = [w for w in l2_book.ask_walls if 0 < (w.price - spot) / max(spot, 1e-6) <= 0.025 and w.notional_usd >= 5_000_000]
                if near_bids and l2_book.bid_ask_ratio >= 1.15:
                    score += 4.0
                    notes.append(f"L2 Bid-heavy ({l2_book.bid_ask_ratio:.2f}x, top ${near_bids[0].price:.2f})")
                if blocking_asks:
                    score -= 5.0
                    notes.append(f"Ask Wall cap @ ${blocking_asks[0].price:.2f} (${blocking_asks[0].notional_usd/1e6:.1f}M)")
        elif bias == PatternBias.BEARISH:
            if any(abs(c.invalidation_level - r) <= near_tol for r in resistances):
                score += 4.0
                notes.append("Roof aligns w/ swing resistance")
            if l2_book:
                near_asks = [w for w in l2_book.ask_walls if 0 < (w.price - spot) / max(spot, 1e-6) <= 0.08]
                blocking_bids = [w for w in l2_book.bid_walls if 0 < (spot - w.price) / max(spot, 1e-6) <= 0.025 and w.notional_usd >= 5_000_000]
                if near_asks and l2_book.bid_ask_ratio <= 0.85:
                    score += 4.0
                    notes.append(f"L2 Ask-heavy ({l2_book.bid_ask_ratio:.2f}x, top ${near_asks[0].price:.2f})")
                if blocking_bids:
                    score -= 5.0
                    notes.append(f"Bid Wall cushion @ ${blocking_bids[0].price:.2f} (${blocking_bids[0].notional_usd/1e6:.1f}M)")
        else:
            if supports and resistances:
                score += 3.0
                notes.append(f"Bounded by S/R ${supports[0]:.2f}–${resistances[0]:.2f}")
            if l2_book:
                notes.append(f"L2 ratio {l2_book.bid_ask_ratio:.2f}x")

        if not notes:
            notes.append("Standard swing S/R context (no L2 snapshot)")
        return min(20.0, max(2.0, score)), "; ".join(notes)

    @staticmethod
    def _score_mtf_confluence(
        c: RawPatternCandidate,
        bias: PatternBias,
        series: TimeframeSeries,
        all_series: dict[Timeframe, TimeframeSeries],
    ) -> tuple[float, str]:
        tf_trends = {tf.value: s.trend_direction for tf, s in all_series.items()}
        summary = " / ".join(f"{k}:{v[:2]}" for k, v in tf_trends.items())

        if bias == PatternBias.NEUTRAL:
            return 13.0, f"Bilateral awaiting direction ({summary})"

        wanted = "UPTREND" if bias == PatternBias.BULLISH else "DOWNTREND"
        opposing = "DOWNTREND" if bias == PatternBias.BULLISH else "UPTREND"
        higher_tfs = []
        if series.timeframe == Timeframe.DAILY:
            higher_tfs = [all_series[tf] for tf in (Timeframe.WEEKLY, Timeframe.MONTHLY) if tf in all_series]
        elif series.timeframe == Timeframe.WEEKLY:
            higher_tfs = [all_series[tf] for tf in (Timeframe.MONTHLY,) if tf in all_series]

        # Reversal patterns naturally form against the local trend, but higher-TF support/confluence still matters
        is_reversal = "Reversal" in c.category or c.kind == PatternKind.CANDLESTICK
        if not higher_tfs:
            if series.trend_direction == wanted:
                return 16.5, f"Aligned w/ {series.timeframe.value} {wanted}"
            if is_reversal:
                return 13.5, f"Reversal setup vs {series.timeframe.value} {series.trend_direction}"
            return 9.0, f"Counter-trend vs {series.timeframe.value} {series.trend_direction}"

        aligned_htf = sum(1 for h in higher_tfs if h.trend_direction == wanted)
        opposed_htf = sum(1 for h in higher_tfs if h.trend_direction == opposing)

        if aligned_htf == len(higher_tfs):
            return 20.0, f"Full MTF Confluence ({summary})"
        if aligned_htf > 0 and opposed_htf == 0:
            return 16.5, f"Constructive MTF ({summary})"
        if opposed_htf == len(higher_tfs):
            score = 10.0 if is_reversal else 6.0
            return score, f"Counter-HTF warning ({summary})"
        return 13.0, f"Mixed MTF ({summary})"

    @staticmethod
    def _build_action_summary(
        c: RawPatternCandidate,
        state: PatternLifecycleState,
        bias: PatternBias,
        vol_ratio: float,
        capped: bool,
    ) -> str:
        if state == PatternLifecycleState.CONFIRMED_BREAKOUT:
            return f"CONFIRMED {bias.value} breakout ({vol_ratio:.2f}x vol); stop ${c.invalidation_level:.2f}, target ${c.target_price:.2f} (check Tier-0 Weather/Macro Gate)."
        if state == PatternLifecycleState.FAILED_BREAKOUT:
            return f"TRAP WARNING: Failed breakout at ${c.breakout_level:.2f}; do not chase — watch snapback toward ${c.invalidation_level:.2f}."
        if state == PatternLifecycleState.INVALIDATED:
            return f"INVALIDATED: Structural stop ${c.invalidation_level:.2f} breached; discard setup."
        live_tag = " [Live unclosed bar — wait for close]" if capped else ""
        return f"FORMING: Awaiting volume-backed close beyond ${c.breakout_level:.2f} (>=1.3x vol; now {vol_ratio:.2f}x); stop ${c.invalidation_level:.2f}.{live_tag}"
