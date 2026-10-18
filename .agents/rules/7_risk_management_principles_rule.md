---
trigger: model_decision
---

# Rule: 7 Golden Institutional Risk Management Principles Rule

This priority rule permanently governs all stock selection, risk auditing, trade management, position sizing, stop-loss buffers, and portfolio evaluations for the user.

## The 7 Golden Institutional Risk Management Principles

### 1. Solvency Safety Runway Protection
- **Rule:** `Cash / Annual Cash Burn >= 4.0 Years`
- Never invest in companies facing cash exhaustion. Ensure liquid reserves provide at least 4+ to 10+ Years of Solvency Runway.

### 2. Retail Trap Protection & Deep Value Reload Floor
- **Rule:** `Bifurcate Stop-Loss vs Tranche 3 Deep Value Reload based on 4/4 Gate Status`
- **Speculative Stocks (Failing 4/4 Gate):** Place strict Stop-Loss -2% to -3% BELOW support to prevent fatal capital loss.
- **Fundamentally Strong Compounders (Passing 4/4 Gate, e.g. AMKR, NVDA):** **ZERO automated stop-loss orders in the retail trap zone (e.g. $48.50 – $50.00).** Dips below S3/50 SMA are designated as **Tranche 3 Deep Value Reload Zones (Accumulate, Do Not Sell)**. Enforce `mandatory_retail_trap_and_stop_hunt_protection_rule.md`.
- **Exit Condition for 4/4 Gate Stocks:** Governed strictly by **Fundamental Invalidation** (loss of anchor customer, 2 consecutive quarters of net loss, or insolvency), NEVER by technical retail-trap wicks!

### 3. Dilution Warning & Unissued Share Audit
- **Rule:** `Audit Unissued Authorized Shares (Column 13)`
- If unissued shares exceed 50% of total charter capacity (e.g. `NVTS` 506M or `APLD` 284M), **NEVER buy-and-hold forever; trade strictly as a short-term swing with a strict stop loss!**

### 4. Dual Net Surplus Solvency Verification
- **Formula 1:** `(New Cash + Upfront Prepayments) - Total Debt`
- **Formula 2:** `(New Cash + 3-Year CFO) - Total Debt`
- Verify that customer prepayments and operating cash flow cover 100% of corporate debt liabilities.

### 5. Upfront Pre-Paid Customer Contract Mandate
- **Rule:** `Prioritize Stocks with Upfront Cash Prepayments / Backlogs (Column 7)`
- Favor companies where customers pay cash upfront before product delivery (`NBIS` $9B, `GOOG` $18.5B, `SOFI` $45.5B deposits).

### 6. Recommended Buy Entry Sizing & Position Capital Limits
- **Category A Fortress Sizing:** Up to 10%–20% Portfolio Allocation ($500–$1,500 capital limit).
- **Category B Swing Sizing:** Max 2%–5% Portfolio Allocation ($70–$650 capital limit, e.g. 10 shares SOUN @ $7.07, 11 shares AMKR @ $59.01).
- **Recommended Buy Term Directive:** Always use the term **Recommended Buy** (e.g. `Recommended Buy: $53.33`).
- **Failed Stocks Sizing:** $0 Capital Allocation (No New Buy Orders!).

### 7. Fixed Target Exit & Cash Profit Recycling
- **Rule:** `Set Limit Sell Orders at TradingView R1 / R2`
- Take profit at pre-determined technical levels and recycle principal back into liquid bank cash war chest ($4,966.09 liquid cash).
