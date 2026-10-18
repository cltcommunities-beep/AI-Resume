---
trigger: model_decision
description: Mandatory Rules to Follow Every Time While Investing & Placing Agentic Trades
---

# MANDATORY RULES TO FOLLOW EVERY TIME WHILE INVESTING

## Executive Directive
This rule permanently governs all automated, agentic, and manual investment decisions, order staging, position sizing, risk controls, and profit taking across all brokerage accounts.

Every single investment recommendation, analysis, or order execution MUST strictly pass through this 7-Step Protocol. **NO EXCEPTIONS PERMITTED.**

---

## 🛡️ The Mandatory Investment Execution Rules

### Rule 0: Mandatory Pre-Investment Market Audit Gate (Top-Down Execution Funnel)
- **Directive:** NEVER recommend, audit, or stage a buy order for ANY individual stock without FIRST running the **Pre-Investment Market Audit Gate**.
- **Protocol:** Enforce `mandatory_pre_investment_market_audit_gate_rule.md`. Pass through the 4-Tier Funnel:
  1. **Tier 1 (Macro Tide):** Scan Brent Crude, SPY, QQQ, TLT (Yields), and Macro Events. If 3 or more Downward Pressure signals are active, enforce **ABSOLUTE 100% CAPITAL ALLOCATION FREEZE ($0.00)** under `mandatory_macro_tide_absolute_veto_rule.md`. Macro strictly vetoes micro; zero S1, S2, or S3 buying permitted.
  2. **Tier 2 (Sector Flow):** Audit institutional capital flow into the target sector.
  3. **Tier 3 (Intraday Timing Window):** Verify the **Golden Morning Dip Window (9:45 AM – 10:30 AM EDT)**. Strict ban on open/pre-market/afternoon market buys.
  4. **Tier 4 (Company Solvency):** Audit 4-Point Fundamental Strength Gate and 3-tranche limit order levels.

### Rule 1: Live API Streaming & Continuous Algorithm Calibration Verification (Zero Stale Data)
- **Directive:** Never use cached, remembered, or static stock prices, and never trade on uncalibrated models or stale support levels.
- **Protocol:** Enforce [mandatory_continuous_algorithm_update_and_calibration_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_continuous_algorithm_update_and_calibration_rule.md). ALWAYS query live Robinhood quotes (`get_equity_quotes`) and recalculate $S_1/S_2/S_3$ floors and 20MFA/50MFA baselines before calculating entry prices, market capitalizations, or allocation percentages. Include live session timestamps in all reviews. If models or levels are stale, enforce a 100% Capital Allocation Freeze ($0.00).

### Rule 2: Anti-FOMO, Floor-Only Entry & Morning Dip Window Mandate
- **Directive:** NEVER recommend or execute a buy order on a stock that is extended or surging intraday, nor at the prior day's close without waiting for the morning liquidity flush.
- **Protocol:** All buy orders MUST be staged as **Limit Orders** placed strictly at verified **S1/S2/S3 Support Floors** during the **Golden Morning Dip Window (9:45 AM – 10:30 AM EDT)**. Never execute market buys at 9:30 AM open or in pre-market. Enforce `mandatory_intraday_reality_and_morning_dip_rule.md`. If price runs away, let it go; do not chase.

### Rule 3: Institutional Solvency & Dilution Gate
- **Directive:** Never invest in companies facing cash exhaustion or massive unissued share overhangs.
- **Criteria:**
  1. **Solvency Runway:** Liquid cash / annual cash burn must be `>= 4.0 Years` (or positive Free Cash Flow).
  2. **Dilution Check:** If unissued authorized shares exceed 50% of charter capacity, trade strictly as a swing with a hard stop-loss.
  3. **Failed Gate:** If a stock fails solvency, allocate **$0.00 capital**.

### Rule 4: Strict Position Sizing & Cash War-Chest Reserve
- **Directive:** Prevent over-concentration and preserve dry powder for market-wide pullbacks.
- **Allocation Limits:**
  - **Category A (Fortress Monopolies - NVDA, SPCX, GOOG):** Max **10% to 15%** of portfolio equity.
  - **Category B (Growth Swings - CRWV, BE, SOFI, AMKR):** Max **3% to 5%** of portfolio equity.
  - **Dry Powder Mandate:** ALWAYS maintain at least **10% to 15% of total portfolio value in liquid cash/buying power** to exploit unexpected flash drops.

### Rule 5: Retail Trap Protection & Deep Value Reload Protocol
- **Directive:** Eliminate automated retail stop-loss shakeouts on fundamentally bulletproof companies.
- **Protocol:** Enforce `mandatory_retail_trap_and_stop_hunt_protection_rule.md`:
  - **4/4 Gate Stocks (Fortress Compounders, e.g. AMKR, NVDA, SOFI):** STRICT BAN on open automated stop-loss orders in retail trap zones (e.g. $48.50 – $50.00). Reclassify deep dips below S3 as **Tranche 3 Deep Value Reload Zones (Accumulate, Do Not Sell)**. Exits are triggered ONLY by **Fundamental Invalidation** (contract loss, negative net income, or insolvency).
  - **Speculative Stocks (<3/4 Gates):** Maintain strict stop-loss orders -2% to -3% below S3 to prevent catastrophic capital loss.

### Rule 6: Systematic 3-Tranche Profit Recycling
- **Directive:** Lock in gains systematically; never let green trades turn into red losses.
- **Protocol:**
  - **Tranche 1 (R1 Target):** Sell 30% to 33% of position to lock in principal + profit.
  - **Tranche 2 (R2 Target):** Sell 30% to 33% of position; trail stop to break-even on the rest.
  - **Capital Recycling:** Harvested cash automatically flows back into spendable buying power for the next S1/S2 opportunity.

### Rule 7: Mandatory Order Ticket Schema & Explicit User Confirmation
- **Directive:** Never execute unverified or blind market orders.
- **Protocol:** For every proposed trade, the assistant MUST generate a standardized **Order Ticket**:
  1. **Brokerage Account:** Masked (e.g. `••••3782` or `••••6246`)
  2. **Action:** Buy / Sell
  3. **Order Type:** Limit Order (strictly no blind market orders for entries)
  4. **Limit Price:** Exact dollar limit
  5. **Share Quantity:** Exact share count
  6. **Capital Required:** Exact dollar amount
  7. **Time in Force:** GTC (Good-Til-Cancelled) or GFD (Good-For-Day)
  8. **Stop-Loss Level:** S3 Floor - 2.5%
  9. **Profit Target:** TradingView R1 / R2 Target
  - Always wait for the user's manual review and confirmation before firing live orders into the market!

---

## 🚫 Prohibited Actions
1. **NO Blind Market Orders** on buys during market open or after-hours volatility.
2. **NO Unmasked Account Numbers** (must always display `••••3782`, `••••6246`, `••••6538`).
3. **NO LaTeX Math Blocks** in responses or tables (plain text markdown only).
4. **NO Auto-Committing / Auto-Pushing Git** without user confirmation.
