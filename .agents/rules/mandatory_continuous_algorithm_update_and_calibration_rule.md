---
trigger: model_decision
description: Mandatory Continuous Algorithm Update, Dynamic Model Recalibration, and Technical Freshness Standard
---

# 🔄 MANDATORY RULE: CONTINUOUS ALGORITHM UPDATE & DYNAMIC CALIBRATION MANDATE

## 🚨 Executive Directive: Zero Tolerance for Stale Trading Algorithms
This rule is a **PERMANENT INSTITUTIONAL DIRECTIVE** governing all automated, agentic, and algorithmic trading systems for Robinhood Account `••••3782` and Cash Account `••••6246` ("Agentic").

Trading on outdated models, static support levels, obsolete stock rosters, or uncalibrated macro baselines causes systemic capital destruction. **All quantitative models, technical parameters, stock rosters, and algorithmic rules MUST be continuously updated, calibrated, and verified fresh before staging or executing any trade. NO EXCEPTIONS PERMITTED.**

---

## 🛡️ 1. The 4-Tier Continuous Algorithm Calibration Framework

### Tier 1: Real-Time Intraday Technical Calibration (Daily Recalculation)
* **Dynamic Levels Only:** Technical support floors ($S_1, S_2, S_3$) and resistance targets ($R_1, R_2$) are **time-decaying metrics**. They must be re-computed dynamically using live Robinhood API Consolidated Tape data for each trading session.
* **Moving Average Alignment (20MFA / 50MFA):** The 20-day and 50-day moving average floors must be recalculated against the latest daily session closes.
* **Strict Ban on Stale Levels:** Never reuse support/resistance figures from previous weeks or past turns without verifying them against active session candles.

### Tier 2: Daily Pre-Market Macro Recalibration (8:00 AM – 9:00 AM EDT)
* **Macro Baseline Adjustments:** Recalibrate the 6 Macro Pressure Gauges (Brent Crude, 10-Year Treasury Yield, QQQ, SPY, IWM, VIX) every morning prior to market open.
* **Threshold Shifting:** As the Federal Reserve rate cycle, Treasury issuance, and global supply lines evolve, adjust what constitutes an "inflation shock" or "yield breakout" so algorithmic triggers stay calibrated to current reality.

### Tier 3: Stock Roster & Valuation Refresh (Monthly / Post-Earnings)
* **Bucket B Growth Swings:** Every stock in the active roster (`best_stocks_roster_and_entry_timing_rule.md`) must be re-scored following quarterly 10-Q earnings releases, analyst consensus shifts, and backlog revisions.
* **Solvency Re-computation:** Free Cash Flow, cash burn runway, and share dilution metrics must be refreshed dynamically after every quarterly filing. Companies failing the 4-Point Fundamental Gate must be pruned from the active buying algorithm immediately.

### Tier 4: The Adaptive Feedback Loop ("Never Repeat" Engine)
* **Post-Mortem Rule Patching:** Any unexpected slippage, retail stop-hunt shakeout, or drawdown must trigger an immediate algorithmic post-mortem.
* **Permanent Rule Hardening:** The root cause must be codified into `.agents/rules/` to ensure the system’s logic evolves and never makes the same mistake twice.

---

## 🚫 2. Immediate Capital Allocation Freeze for Stale Logic
If at any point:
1. Technical support levels have not been recalculated for the current session, OR
2. Macro gauge thresholds have not been audited within 24 hours, OR
3. A stock's quarterly earnings or solvency numbers are outdated:

👉 **THE ASSISTANT MUST ENFORCE AN IMMEDIATE 100% CAPITAL ALLOCATION FREEZE ($0.00).** No limit buy orders may be staged until all algorithmic inputs are confirmed fully up-to-date.

---

## 📋 3. Pre-Trade Algorithm Freshness Checklist
Before any limit order is recommended or staged, verify:
- [ ] Are current prices and technical indicators pulled from live SIP tape (not cached)? ──► **MUST BE YES.**
- [ ] Have $S_1, S_2, S_3$ and $R_1, R_2$ levels been recalculated for the active session? ──► **MUST BE YES.**
- [ ] Are the 6 Macro Pressure Gauges verified against today's macro conditions? ──► **MUST BE YES.**
- [ ] Has the stock's fundamental solvency and dilution standing been validated against the latest filing? ──► **MUST BE YES.**
- [ ] Does this order honor all post-mortem rules codified in `.agents/rules/`? ──► **MUST BE YES.**
