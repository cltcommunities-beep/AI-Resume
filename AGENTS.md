# 🏛️ PROJECT MASTER BRIEFING & CONTEXT ANCHOR (AGENTS.md)

## 🎯 Executive Mission
This workspace permanently governs the **Robinhood Account `••••3782` 6-Month $10,000 to $20,000 Capital Compounding Engine** (October 2026 – April 2027). 

Every agent session, chat turn, and subagent invocation in this workspace MUST automatically load and strictly adhere to this persistent context, the **45+ institutional rules in `.agents/rules/`**, and the live Robinhood MCP toolchain.

### 📋 Mandatory Response Format: Green Dot (To Follow) & Red Dot (NOT to Follow)
In **EVERY** response, analysis, review, or strategic update, the assistant MUST unconditionally structure the action checklist using color-coded dots:
* 🟢 **GREEN BULLETS (To Follow by You):** Exact, positive actions to execute (orders to stage or maintain, confirmed setups, risk compliance, and profit targets).
* 🔴 **RED BULLETS (NOT to Follow by You):** Strict prohibitions, buying bans, capital freezes ($0.00), emotional pitfalls, falling knives, and dealbreakers to avoid.

---

## 📌 1. Persistent Account & Portfolio Architecture

* **Brokerage Accounts:**
  * **Primary Default Account:** Robinhood Margin Account `••••3782`
  * **Agentic Trading Account:** Cash Account `••••6246` (Nickname: "Agentic")
* **Account Privacy:** Never display unmasked account numbers. Always format as `••••3782` or `••••6246`.
* **The 3-Bucket Capital Allocation Framework ($10,000 Base Engine):**
  * **Bucket A: Anchor Monopolies (40% = $4,000):** `NVDA` (Primary), `SPCX`, `GOOG`
  * **Bucket B: High-Velocity Growth Swings (45% = $4,500):** `AMKR`, `NBIS`, `CRWV`, `INTC`, `BE`, `SOFI`
  * **Bucket C: Liquid War-Chest Dry Powder (15% = $1,500 Minimum):** Pure Cash Buying Power (Earning daily interest in Robinhood Cash Sweep)

---

## 🔄 2. Daily Standard Operating Procedure (SOP)

Every morning when the user opens the project, the assistant must follow this disciplined timeline:

1. **8:00 AM – 9:00 AM EDT (Pre-Market Macro Audit):**
   * Check the **6 Macro Pressure Gauges** per `mandatory_macro_market_down_pressure_signals_rule.md` (Brent Crude, 10Y Yield, QQQ, SPY, IWM, Binary Events).
   * Review the day's high-impact economic calendar (CPI, PPI, Fed speakers, TSMC earnings).
2. **9:30 AM – 9:45 AM EDT (Observe Market Direction):**
   * **Strict Buying Ban:** Observe market direction only. Avoid impulsive entries, opening-spike chasing, or panic selling.
3. **9:45 AM – 10:30 AM EDT (⚡ The Confirmed Setup Morning Window):**
   * Enforce `mandatory_intraday_reality_and_morning_dip_rule.md`.
   * **The Golden Law:** Never enter simply because the clock is within this window. Only enter if price action confirms **support holding, price stabilization, and improving buying volume**.
   * **Pre-Entry Audit:** Check trend, option premium, defined risk, and maximum loss.
   * **Iron Law:** **No confirmation = No trade.** Missing a trade is 100x better than forcing one.
4. **10:30 AM – 3:30 PM EDT (Intraday Absorption & Cutoff):**
   * **Hard Cutoff:** Stop initiating new dip-buying trades after 10:30 AM EDT. Hold and monitor.
5. **3:30 PM – 4:00 PM EDT (Power Hour & Profit Recycling):**
   * Audit closing performance and review active limit sell orders at **R1 / R2 Resistance Targets**. Zero new market buys.

---

## 🛠️ 3. Mandatory Robinhood MCP Tool Pipeline

Whenever the user asks for a portfolio review or invokes `/mcp:robinhood:portfolio-review`, the assistant **MUST unconditionally execute live broker calls**:
1. `get_accounts` ──► Identifies account `••••3782`
2. `get_portfolio` ──► Fetches Total Value, Cash, and Buying Power
3. `get_equity_positions` ──► Retrieves all active shares and cost basis
4. `get_equity_quotes` ──► Pulls live SIP Consolidated Tape prices and session closes

---

## 📜 4. Active Orders & Holdings Tracking (Live Snapshot - Oct 21, 2026 Audit)

* **Total Portfolio Value:** **$25,721.76** (All-Time High; up **+157.2%** vs $10,000 initial base)
* **Total Liquid Cash:** **$2,367.87**
* **Spendable Buying Power:** **$1,206.07**
* **Gold Hedge (IAU):** **59.65 Shares** (~$4,628.84 value, $84.43 cost) held as permanent geopolitical & inflation shield.
* **Core Active Holdings & Executions:**
  * **NVDA (Bucket A):** **20.00 Shares** (Avg Cost $228.70, Current $221.30). Filled 4.00 sh @ $213.80 on Oct 20.
  * **SPCX (Bucket A):** **11.01 Shares** (Avg Cost $162.48, Current $158.18). Filled 2.00 sh @ $143.50 on Oct 20. Surging on TSLA/SpaceX news.
  * **AMKR (Bucket B):** **66.80 Shares** (Avg Cost $51.38, Current $43.81). Q3 Earnings Oct 26. Active GTC Limit SELL order for **20.00 shares @ $56.50** ($1,130 cash harvest).
  * **NBIS (Bucket B):** **11.00 Shares** (Avg Cost $236.47, Current $172.85). Active GTC Limit BUY order for **5.00 shares @ $160.00** (reserves $800.00; drops avg cost to $212.57 upon fill).
  * **SMCI:** Active GTC Limit BUY orders for **4.00 shares @ $33.85** ($135.40) and **2.00 shares @ $33.20** ($66.40).
  * **INTC (21.41 Shares) & CRWV (39.01 Shares):** Hold current shares; 100% Capital Allocation Freeze ($0.00).



---

## 🛡️ 5. The "Never Repeat" Mistake Rule
Whenever any market surprise, bad entry, or drawdown occurs, the assistant and user MUST immediately perform a post-mortem and permanently write the lesson into a new markdown rule under `.agents/rules/` to ensure the mistake is never repeated.
* **Core Enforced Standard:** [buy_the_dip_vs_falling_knife_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buy_the_dip_vs_falling_knife_rule.md) (The 5 Golden Rules of Dip-Buying vs Falling Knives).
* **Forensic Dilution & Debt Standard:** [mandatory_debt_and_dilution_forensic_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_debt_and_dilution_forensic_audit_rule.md) (The 3-Gate Screen for Active ATM Programs, Distressed >12% Bond Yields, and 15% Interest Burden).
* **Upfront Dealbreaker Standard:** [mandatory_why_not_to_invest_bullet_points_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_why_not_to_invest_bullet_points_rule.md) (Mandatory 5-Bullet Red Flag Screen exposing why NOT to invest before committing any capital).
* **Dual-Scenario Technical Matrix Standard:** [mandatory_dual_scenario_technical_matrix_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_dual_scenario_technical_matrix_rule.md) (Mandatory Mapping of Resistance Ceilings, Inflection Pivots, 0.65 Fib Golden Pockets, and If/Then Dual Pathways).
* **Buffett & Quantitative Algo Standard:** [buffett_and_quantitative_algorithm_hybrid_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buffett_and_quantitative_algorithm_hybrid_rule.md) (The Dual-Brain Standard: Buffett Value & Cash Fortress combined with Algorithmic Fibonacci & Timing Execution).
* **Headline Spike Fade & Dynamic Harvest Standard:** [headline_spike_fade_and_dynamic_harvest_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/headline_spike_fade_and_dynamic_harvest_rule.md) (The SPCX Oct 21 Post-Mortem: Dynamic Profit-Taking and Breakeven Stops on Headline Pops into Hostile Macro Tapes).

---

## 🔄 6. Continuous Algorithm Update & Dynamic Calibration Mandate
All trading models, quantitative algorithms, technical support/resistance levels, macro gauges, and stock rosters must be continuously calibrated and kept 100% up-to-date.
* **Core Enforced Standard:** [mandatory_continuous_algorithm_update_and_calibration_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_continuous_algorithm_update_and_calibration_rule.md).
* **Strict Rule:** Trading on uncalibrated models or stale levels triggers an immediate **100% Capital Allocation Freeze ($0.00)**.

---

## 🗳️ 7. U.S. Election Impact & Post-Election Surge Framework
All market evaluations during Midterm and Presidential election seasons must account for the 3-phase election cycle, peak pre-election volatility/de-grossing, and the historical 100% 12-month post-midterm rally track record.
* **Core Enforced Standard:** [us_election_market_impact_and_post_election_surge_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/us_election_market_impact_and_post_election_surge_rule.md).

## 🚀 8. The 5-Engine Quantitative Growth Compounding Algorithm
All growth stock evaluations, dip purchases, and capital allocations must pass the 5-Engine Quantitative Growth Model (Secular TAM, Operating Leverage & Cash Conversion, Anti-Dilution Balance Sheet, Valuation PEG Discipline, and Technical Support Staging).
* **Core Enforced Standard:** [ultimate_high_conviction_growth_investing_algorithm_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/ultimate_high_conviction_growth_investing_algorithm_rule.md).
* **Execution Threshold:** Minimum Composite Score of **85/100** required for Tier 1 capital allocation. Zero capital ($0.00) for scores below 70 or any hard dilution/cash burn veto.

---

## 🔬 9. Mandatory Unofficial Stretch & Buy-Side Whisper Earnings Benchmark
Whenever evaluating earnings, financial results, quarterly reports, or revenue/EPS beats/misses for ANY stock, the assistant MUST unconditionally determine and clearly state whether results beat or missed the **🔬 Unofficial Stretch Guess (The Buy-Side Whisper Target)** in addition to public consensus.
* **Core Enforced Standard:** [mandatory_unofficial_stretch_earnings_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_unofficial_stretch_earnings_rule.md).
* **Required Output:** 5-Level Horizontal Flow (`[Official] ──► [Consensus] ──► [Tier-1] ──► [🔬 Unofficial Stretch] ──► [Reported]`) and 6-Column Institutional Earnings Benchmark Table with `🏆 BEAT ALL 5` or `🔴 MISSED STRETCH` status coding.

---

## 🧱 10. Mandatory Elite Execution, Quality Business Checklist & Structural Safeguards Standard
All trade entries, position sizing calculations, stop-loss deployments, long-term portfolio rules, and exit triggers must strictly adhere to the Essential Execution Rules and 3-Pillar Pre-Buy Verification Checklist.
* **Core Enforced Standard:** [mandatory_elite_execution_and_structural_safeguards_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_elite_execution_and_structural_safeguards_rule.md).
* **Core Mandates:**
  * **1% Risk Allocation Law:** Sizing calculated so stop-loss distance equals exactly 1.0% account equity.
  * **2:1 Minimum R:R Ratio:** Upside target must be at least 2.0x the stop distance.
  * **Hard Automated Stop-Losses:** Never moved backward; honor weekend liquidity gaps.
  * **Anti-FOMO Staggered Tranches:** Allocate cash across 3 to 4 tranches rather than lump sums at highs.
  * **Elite Business Quality Gate:** Consistent ROIC > 15%, FCF Margin > 20%, unassailable economic moat, Net Debt-to-EBITDA < 2.0x, high insider ownership, Forward PEG < 1.5x.
  * **Portfolio Boundaries:** 40% Broad Core, 20% Dividend/Gold, 40% Individual Picks; 10%–15% single-stock ceiling.
  * **Forever Stock Sell Triggers:** Moat erosion, reckless debt-fueled M&A, extreme valuation (P/E > 100x).
  * **Daily Loss Limit:** Max 3.0% daily account drawdown; close platform and walk away if hit.
  * **3-Pillar Pre-Buy Verification:** Risk/Structural Setup, Technical/Trend Alignment, Macro/Catalyst Timing.

---

## ⚠️ 11. Mandatory "Capex Reversal" Trap & Hyperscaler Digestion Audit Standard
All semiconductor, AI datacenter, infrastructure, and hardware stocks must pass the 5-Filter Anti-Capex Reversal Screen to protect the portfolio from catastrophic cyclical digestion crashes.
* **Core Enforced Standard:** [mandatory_capex_reversal_trap_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_capex_reversal_trap_rule.md).
* **The 5 Mandatory Filters:**
  1. **Upfront Pre-Paid Customer Contracts:** >50% expansion CapEx pre-funded by cash prepayments (`NBIS` standard).
  2. **Self-Funding CapEx Rule:** CFO must exceed total CapEx; zero debt-dependent infrastructure builds.
  3. **Balance Sheet Fortress:** Net Debt-to-EBITDA < 2.0x with positive Net Cash Surplus after debt.
  4. **Asset-Light & Software Moat:** Fabless architecture and proprietary software lock-in (`NVDA` CUDA) over asset-heavy physical fabs (`INTC`).
  5. **Customer Concentration Ceiling:** Max 30% revenue from any single customer.
* **Veto Enforcement:** Stocks in a CapEx Reversal trap (`INTC`, `CRWV`) trigger an immediate **100% Capital Allocation Freeze ($0.00)**.

---

## 📐 12. Mandatory Quantitative Portfolio Risk Manager & 4 Algorithmic Maintenance Rules
Governs institutional tier allocations, dynamic rebalancing triggers, smart cash routing, and single-stock cap locks across Account `••••3782`.
* **Core Enforced Standard:** [mandatory_quantitative_portfolio_risk_manager_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_quantitative_portfolio_risk_manager_rule.md).
* **Target Tier Allocations:**
  * **Tier 1: Elite Cash-Flow Compounders (35%):** `GOOG`, `AAPL`, `NVDA`
  * **Tier 2: Mid-Level Non-Tech Stocks (50%):** Strict non-tech cross-sector stability (Financials, Industrials, Healthcare, Gold `IAU`)
  * **Tier 3: Emerging Long-Term Growth (15%):** Disruptive high-beta compounders (`NBIS`, `SPCX`, `SMCI`)
* **The 5 Hard Analytical Filters:**
  1. **15% Single-Stock Cap:** Flag immediate partial liquidation down to 10% if any stock exceeds 15% net worth.
  2. **FCF Margin Floor:** Minimum 20% FCF margin for Elite Tier; trigger structural review if breached.
  3. **Forward PEG Guardrail:** Ceiling at 1.5x; flag assets with PEG > 1.5x as structurally overvalued.
  4. **Systemic CapEx Watch:** Monitor Alphabet, Microsoft, Meta; if $\ge 2$ cut CapEx, calculate NVDA downstream revenue risk.
  5. **Non-Tech Mid-Tier:** Strictly enforce zero tech stocks in the 50% Mid-Level tier.
* **The 4 Algorithmic Rules:**
  * **Rule 1 (±5% Rebalancing Trigger):** Quarterly check; only rebalance if a tier drifts > ±5% from baseline.
  * **Rule 2 (Smart Cash Inflow):** 100% of new deposits route directly into whichever tier is furthest below target.
  * **Rule 3 (15% Single-Stock Cap Lock):** Automatic liquidation alert down to 10% on excessive concentration.
  * **Rule 4 (Systemic CapEx Watch Filter):** Macro de-risking alert and stop-loss tightening upon hyperscaler CapEx cuts.

---

## 🏛️ 13. Mandatory "Great Company != Great Investment at Wrong Price" Standard
All entries into any asset—including Tier 1 / Bucket A Anchor Monopolies (`NVDA`, `SPCX`, `GOOG`, `MSFT`)—must strictly pass the Entry-Price Valuation Gate and Support-Floor Staging Standard.
* **Core Enforced Standard:** [mandatory_great_company_wrong_price_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_great_company_wrong_price_rule.md).
* **The 5 Core Mandates:**
  1. **Ban on Mid-Air Buying:** Purchases strictly banned >3% above 20MFA or >5% above 50MFA.
  2. **Support-Floor Staging Only:** GTC Limit Buys placed exclusively at verified S1/S2/S3 support floors.
  3. **3-Tranche Stagger Protocol:** Maximum 33% initial entry; never deploy 100% lump sums at highs.
  4. **Active Capital Recycling:** If a stock spikes on headlines into macro headwinds, sell 25%–50% into the pop and queue lower limit orders at support to reduce permanent cost basis.
  5. **Forward PEG Ceiling:** Ceiling at 1.5x; positive FCF conversion mandatory.

---

## 🌐 14. Mandatory Pre-Investment Macro-Impact Gate (No Trade Without Macro Clearance)
Before staging or recommending ANY buy order, limit staging, or capital allocation, the assistant MUST unconditionally audit the 5 Macro-Impact Pillars.
* **Core Enforced Standards:** [mandatory_pre_investment_market_audit_gate_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_investment_market_audit_gate_rule.md), [macroeconomic_catalysts_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/macroeconomic_catalysts_rule.md), and [weekly_market_moving_catalysts_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/weekly_market_moving_catalysts_table_rule.md).
* **The 5 Macro-Impact Pillars:**
  1. **Labor & Growth Data:** Weekly Initial Jobless Claims (e.g. 194K print), Non-Farm Payrolls, GDP Growth.
  2. **Inflation Metrics:** Core PCE Index (Federal Reserve's primary gauge), CPI, PPI.
  3. **Interest Rates & Yields:** 10-Year U.S. Treasury Yield (>5.0% = valuation compression).
  4. **Commodity Shocks:** Brent Crude Oil (>$100/bbl = margin compression).
  5. **Binary Event Window:** Scheduled FOMC meetings, Fed Chair speeches, and Mega-Cap earnings within 24–48 hours.
* **The Absolute Law:** **No Macro Clearance = $0.00 Capital Allocation.** Micro company quality NEVER overrides a macro storm.

---

## 📊 15. Mandatory Dual Solvency Table Standard (Compact 5-Column + Full 17-Column Solvency Audit Table)
Whenever the assistant performs a stock analysis, due diligence review, or investment evaluation, rendering BOTH solvency tables is UNCONDITIONALLY MANDATORY.
* **Core Enforced Standards:** [compact_solvency_summary_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/compact_solvency_summary_table_rule.md), [master_stock_analysis_standard.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/master_stock_analysis_standard.md), and [mandatory_executive_portfolio_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_executive_portfolio_table_rule.md).
* **The Dual Table Mandate:**
  1. **Table 4: Compact Executive Solvency Summary Table (5 Columns):** Fast executive reading with mandatory 3-bullet takeaway (Price & Support, Solvency & F1/F2 Net Surplus, Risk Management & Directives).
  2. **Table 5: Full 17-Column Solvency Audit Table:** The granular 17-metric institutional matrix auditing Column 2 Live Price vs Wall St Cap/Shares, Support S1/S2/S3, Moats, Cash, Debt, CapEx, Pre-Paid Backlog, New Cash, F1/F2 Net Surplus, Dilution/ATM headroom, Next Qtr Outlook, Risk Compliance, R1 Target, and Upside Chart.
* **Zero Exceptions:** Neither table may ever be omitted, altered, or replaced with plain text.







