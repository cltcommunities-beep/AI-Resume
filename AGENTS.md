# 🏛️ PROJECT MASTER BRIEFING & CONTEXT ANCHOR (AGENTS.md)

## 🎯 Executive Mission
This workspace permanently governs the **Robinhood Account `••••3782` 6-Month $10,000 to $20,000 Capital Compounding Engine** (October 2026 – April 2027). 

Every agent session, chat turn, and subagent invocation in this workspace MUST automatically load and strictly adhere to this persistent context, the **45+ institutional rules in `.agents/rules/`**, and the live Robinhood MCP toolchain.

### 📋 Mandatory Response Format: Green Dot (To Follow) & Red Dot (NOT to Follow)
In **EVERY** response, analysis, review, or strategic update, the assistant MUST unconditionally structure the action checklist using color-coded dots:
* 🟢 **GREEN BULLETS (To Follow by You):** Exact, positive actions to execute (orders to stage or maintain, confirmed setups, risk compliance, and profit targets). **Whenever mentioning a stock in a buy/hold/exit action, ALWAYS explicitly include its `Wall St Market Value` (`Market Cap / Shares Outstanding`, plus diluted value if material) right beside the `Live Price` and entry/stop/target levels so valuation vs. price is immediately clear.**
* 🔴 **RED BULLETS (NOT to Follow by You):** Strict prohibitions, buying bans, capital freezes ($0.00), emotional pitfalls, falling knives, and dealbreakers to avoid. **ALWAYS state the `Live Price` vs. `Wall St Market Value` (premium/discount & dilution gap) when warning why NOT to buy or chase a stock.**

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

Whenever the user asks for a portfolio review or stock analysis (`/mcp:robinhood:portfolio-review` or `/mcp:robinhood:stock-analysis`), the assistant **MUST unconditionally execute live broker calls AND parallel Daily Macro + Micro `search_web` calls**:
1. `get_accounts` ──► Identifies account `••••3782` (and verifies `unsettled_funds`)
2. `get_portfolio` ──► Fetches Total Value, Cash, and Buying Power
3. `get_equity_positions` ──► Retrieves all active shares and cost basis
4. `get_equity_quotes` & `get_equity_fundamentals` ──► Pulls live SIP Consolidated Tape prices, session closes, P/E, and 52W ranges
5. **Parallel `search_web` Call #1 (Today's Macro Economic Releases):** Audits same-day 8:30 AM / 10:00 AM data (`CPI`, `Core CPI`, `PPI`, `PCE`, `Jobless Claims`, `Fed`) for **Actual vs. Expected**
6. **Parallel `search_web` Call #2 (Today's Micro Stock Headlines):** Audits same-day company headlines, analyst PT changes, probes, and 72-hour peer earnings (`mandatory_daily_macro_and_micro_event_headline_audit_rule.md`)

---

## 📜 4. Active Orders & Holdings Tracking (Live Snapshot - Nov 12, 2026 Dynamic Calibration)

* **True Cumulative Wealth Generated:** **$21,958.91** (**$19,958.91** live account value + **$2,000.00** realized cash withdrawal submitted to bank Nov 10; up **+119.6%** vs $10,000 initial base)
* **Total Settled Cash in Account:** **$2,115.20** (`unsettled_funds: $0.00` | Authoritative Spendable Buying Power: **$2,114.33 USD**)
  * **$600.00 Earmarked for `NVT` (Tranche 1):** Deploying Friday, Nov 13 @ 9:45 AM – 10:30 AM EST at S1 Support ($114.00–$116.00). User added $1.00 tracking position Nov 12.
  * **$500.00 Earmarked for `NVDA` (Dip Reserve):** Tranche 1 support watch at $164.50 (or $149.50 capitulation trap) ahead of Nov 18 Q3 Earnings & House Committee closed-door briefing.
  * **$1,014.33 Unallocated War-Chest Reserve Buffer:** Pure dry powder earning daily cash sweep interest (minimum war-chest protection).
* **Core Active Holdings & Confirmed Open Orders (Verified Nov 12, 2026):**
  * **NVDA (Bucket A):** **25.004289 Shares** (Avg Cost $220.50 | Nov 12 Live $164.74). Resting on S1 Support ($164.50). House Committee closed-door briefing Nov 18; Q3 Earnings Nov 18.
  * **NBIS (Bucket B — Frozen Post-Earnings):** **17.003932 Shares** (Avg Cost $209.49 | Nov 12 Live $127.40). Reported Q3 Nov 12 AM: Rev beat $980.8M (+571% YoY), Adj. EBITDA +$465.8M, but full-year 2026 guidance trimmed to $3.0B and CapEx raised to $27B on data center/power capacity delays pushing deployments into H1 2027. **Fail Protocol Officially Triggered: 100% Capital Allocation Freeze ($0.00) on new cash; HOLD existing 17.00 shares.**
  * **NVT (Tier-2 Industrial Datacenter Compounder):** **Active $1.00 Tracking Slice** (Live $115.47 | Market Cap $18.66B / 161.59M shares). Approved Tier-2 non-tech compounder (+44% Q3 sales, $268M FCF, debt-safe). Staged for $600.00 Tranche 1 Friday Nov 13 morning.
  * **OKLO (Thematic Energy):** **41.023452 Shares** (Avg Cost $33.26 | Nov 12 Live $24.83). Current weight 5.07% maxes out 5.0% single-stock ceiling on pre-commercial assets. **100% Capital Allocation Freeze ($0.00) on adding shares; HOLD existing 41.02 shares.**
  * **SMR (NuScale Power):** Forensic audit Nov 12: **100% Capital Allocation Freeze ($0.00)** due to 429.9M share dilution, -$401.4M 9-month cash burn, and Nov 2026 class action lawsuits.
  * **CRWV (Bucket B — Frozen):** **39.011664 Shares** (Avg Cost $76.00 | Nov 12 Live $51.50). Reported Q3 Nov 10 PM: $3.661B Rev beat, but $846M quarterly interest bleed keeps 100% Capital Allocation Freeze ($0.00) active.
  * **AMKR (Bucket B):** **80.167016 Shares** (Avg Cost $49.18 | Nov 12 Live $37.17). Active GTC Limit SELL order for **20.00 shares @ $54.00** (`id: 6ae38580-0ae4-4e3b-aac4-c8f6238ad079`, confirmed).
  * **APLD (Speculative Legacy):** **12.67 Shares** (Avg Cost $33.13). Active GTC Limit SELL order for **12.00 shares @ $35.00** (`id: 6a8b2a22-ecad-42bb-897b-d8c611e7a0ce`, confirmed).
  * **SPCX (Bucket A):** **11.007110 Shares** (Avg Cost $162.48 | Nov 12 Live $141.81). Space defense proxy.
  * **INTC (21.41 Shares @ $111.94) & MRVL (0.15 Shares @ $238.45):** 100% Capital Allocation Freeze ($0.00).
  * **Crypto (`BCH`):** **2.128298 BCH** (Cost Basis `$702.19` / Avg `$329.93` | Live `$225.56` / Value `$480.06`). Repair-and-exit only; support watch at `$217.00`.

### 🚨 Completed Tracker: Super Thursday `NBIS` Credit & Permitting Gate (Nov 12 @ 8:00 AM EST)
* **Outcome: FAIL PROTOCOL TRIGGERED.** While Q3 revenues surged +571% ($980.8M) and EBITDA swung positive ($465.8M), management explicitly disclosed data center power and capacity delays pushing rollouts into H1 2027 and raised CapEx to $27B.
* **Enforced Action:** Strict **$0.00 Capital Allocation Freeze on `NBIS`**. Zero new cash deployed. Existing 17.00 shares held for 2027 recovery. Earmarked buying power rotated into Tier-2 non-tech compounder **`NVT`** for Friday, Nov 13.
* **Macro Catalyst Ahead:** **Friday, Nov 13 @ 8:30 AM EST October PPI** (Consensus: 0.4% MoM / 0.3% Core; Headline YoY expected at 6.6%).



---

## 🛡️ 5. The "Never Repeat" Mistake Rule
Whenever any market surprise, bad entry, or drawdown occurs, the assistant and user MUST immediately perform a post-mortem and permanently write the lesson into a new markdown rule under `.agents/rules/` to ensure the mistake is never repeated.
* **Core Enforced Standard:** [buy_the_dip_vs_falling_knife_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buy_the_dip_vs_falling_knife_rule.md) (The 5 Golden Rules of Dip-Buying vs Falling Knives).
* **Forensic Dilution & Debt Standard:** [mandatory_debt_and_dilution_forensic_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_debt_and_dilution_forensic_audit_rule.md) (The 3-Gate Screen for Active ATM Programs, Distressed >12% Bond Yields, and 15% Interest Burden).
* **Upfront Dealbreaker Standard:** [mandatory_why_not_to_invest_bullet_points_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_why_not_to_invest_bullet_points_rule.md) (Mandatory 5-Bullet Red Flag Screen exposing why NOT to invest before committing any capital).
* **Dual-Scenario Technical Matrix Standard:** [mandatory_dual_scenario_technical_matrix_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_dual_scenario_technical_matrix_rule.md) (Mandatory Mapping of Resistance Ceilings, Inflection Pivots, 0.65 Fib Golden Pockets, and If/Then Dual Pathways).
* **Buffett & Quantitative Algo Standard:** [buffett_and_quantitative_algorithm_hybrid_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buffett_and_quantitative_algorithm_hybrid_rule.md) (The Dual-Brain Standard: Buffett Value & Cash Fortress combined with Algorithmic Fibonacci & Timing Execution).
* **Headline Spike Fade & Dynamic Harvest Standard:** [headline_spike_fade_and_dynamic_harvest_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/headline_spike_fade_and_dynamic_harvest_rule.md) (The SPCX Oct 21 Post-Mortem: Dynamic Profit-Taking and Breakeven Stops on Headline Pops into Hostile Macro Tapes).
* **Friday Pre-Catalyst De-Grossing & S1 Trap Standard:** [mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md) (The Nov 13 Post-Mortem: 4-Gate Pre-Order Forensic Friction Checklist banning S1 limit orders on pre-catalyst Fridays, mandating S2 Deep Capitulation Traps and zero intraday double-dipping).

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

---

## 📲 16. Mandatory Always Check with Robinhood Live APIs Standard (Zero Guesswork)
Whenever the user or assistant discusses stock prices, open/filled orders, portfolio balances, or cash buying power, executing real-time Robinhood MCP tool calls is UNCONDITIONALLY MANDATORY.
* **Core Enforced Standards:** [mandatory_always_check_robinhood_api_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_always_check_robinhood_api_rule.md), [mandatory_robinhood_mcp_portfolio_review_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_robinhood_mcp_portfolio_review_rule.md), and [no_static_stock_prices_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/no_static_stock_prices_rule.md).
* **The 4 Real-Time Triggers:**
  1. **Order Checks:** Call `get_equity_orders` (Account `868333782`) to verify exact order state (`filled` vs `confirmed`). Never guess based on price.
  2. **Live Ticks:** Call `get_equity_quotes` for real-time SIP consolidated tape prices and session closes.
  3. **Cash & Buying Power:** Call `get_portfolio` for authoritative spendable funds.
  4. **Positions & Basis:** Call `get_equity_positions` for exact share counts and average buy prices.
* **Zero Exceptions:** Relying on conversational memory, cached numbers, or static prices is strictly banned. The live broker state is the sole source of truth.

---

## 🧠 17. Mandatory Brilliant Mind Mental Models & Asymmetric Convexity Flywheel Standard
All trading decisions, position scaling, order staging, and capital preservation protocols must strictly operate under the 4 Brilliant Mind Mental Models (Stanley Druckenmiller asymmetry, Jim Simons quantitative mechanics, and Warren Buffett value fortress).
* **Core Enforced Standard:** [mandatory_brilliant_mind_mental_models_and_asymmetric_flywheel_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_brilliant_mind_mental_models_and_asymmetric_flywheel_rule.md).
* **The 4 Brilliant Pillars:**
  1. **Asymmetric Convexity Flywheel (Zero-Theta Synthetic Leverage):** Stage equity tranches at statistical moving average floors (20MFA / S3) instead of high-decay options to capture outsized +20% to +50% explosive rebounds with zero time decay.
  2. **Energy & Compute Bottleneck Front-Running:** Front-run the inevitable physical constraints of the AI revolution by owning clean nuclear energy (`OKLO`) and high-efficiency GPU datacenter infrastructure (`NBIS`).
  3. **Predatory Liquidity Staging:** Pre-stage GTC limit buy orders in the dark at key moving average floors, allowing panicking retail stop-outs to fill our orders at wholesale prices.
  4. **Dynamic Tranche Recycling Machine:** Bifurcate holdings into permanent Core Compounding Shares (60%–70%) and Tactical Velocity Tranches (30%–40%). Systematically harvest velocity tranches at R1/R2 resistance to continuously replenish the Liquid Cash War Chest.

---

## 🚨 18. Mandatory Universal Pre-Recommendation Live News, Divergence & Past/Future Catalyst Audit Standard (Applies to ALL Stocks)
Whenever ANY stock (`[ANY_TICKER]`) across the entire market is discussed, evaluated, compared, or considered for buying, selling, or holding, the assistant is STRICTLY PROHIBITED from relying solely on broker price quotes (`get_equity_quotes`) or past memory. The assistant MUST unconditionally execute a live `search_web` audit in that exact turn before naming or recommending any stock.
* **Core Enforced Standard:** [mandatory_pre_recommendation_news_and_divergence_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_recommendation_news_and_divergence_audit_rule.md).
* **The 4 Universal Pre-Recommendation Laws (For Every Stock):**
  1. **Mandatory Live `search_web` News Audit:** Before suggesting or evaluating any stock (`[TICKER]`), execute a live web search for breaking news, investigations, and catalysts in the current turn.
  2. **The Universal ≥1.5% Index Divergence Siren:** Calculate `Stock % Change - SPY/QQQ % Change`. If any stock underperforms the index by ≥1.5%, treat it as an active company-specific shock siren and identify the exact headline before calling it a technical dip.
  3. **Universal Past 7-Day Forensic News Audit:** Audit past 7 days for board/DOJ/SEC/Congressional probes, executive scandals, customer oversight/contract issues, analyst downgrades, or S-3/ATM dilution filings.
  4. **Universal Future 14-Day Fixed-Date & Catalyst Audit:** Verify via `get_earnings_results` and `search_web` all scheduled events in the next 14 days (exact earnings dates, direct peer earnings within 72 hours, and regulatory/Congressional deadlines).
* **Mandatory Proof Table & Automatic $0.00 Freeze:** Render the **3-Gate Proof Table** (Index Divergence, Past 7-Day News, Next 14-Day Fixed Dates) for every stock candidate. Any active Day-1/Day-2 probe (3-Day Stabilization Rule) or binary event within 72 hours triggers an automatic **100% Capital Allocation Freeze ($0.00)**.

---

## 🔗 19. Mandatory Stock Dependency, Competition & AI Infrastructure Basket Contagion Standard
No stock trades in isolation. Whenever ANY stock (`[TICKER]`)—especially inside the AI Infrastructure, Semiconductor, Neocloud, and Power Basket—is evaluated for buying, limit-order staging, holding, or selling, the assistant MUST audit its **3 Ecosystem Links**: (1) **⬆️ Upstream Suppliers**, (2) **⬇️ Downstream Customers**, and (3) **⚔️ Direct Competitors**.
* **Core Enforced Standard:** [mandatory_stock_dependency_competition_and_basket_contagion_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_stock_dependency_competition_and_basket_contagion_rule.md).
* **The 4 Contagion & Competition Laws:**
  1. **Upstream Supplier Shock Rule (`NVDA`/`TSM` -> `NBIS`/`CRWV`/`AMKR`):** Never place early limit buy orders on a dependent stock while its primary supplier is down ≥3.0% on regulatory probes or supply shocks (avoid 9:30 AM algorithmic basket selling).
  2. **Downstream Customer CapEx & Oversight Rule (`MSFT`/`META` -> `NBIS`/`NVDA`):** Verify whether customer contracts are pre-paid and binding vs. unfunded speculative capacity whenever a hyperscaler tightens oversight.
  3. **72-Hour Direct Competitor Earnings Contagion Rule (`CRWV` <-> `NBIS`):** Enforce an automatic **100% Capital Allocation Freeze ($0.00)** if a direct Tier-1 competitor reports earnings within 72 hours.
  4. **Fundamental Separation vs. Sympathy Drag Arbitrage:** Distinguish true supply-chain contagion from false algorithmic sympathy; accumulate the fundamentally insulated winner only after the 72-hour binary window clears.

---

## 📰 20. Mandatory Daily Macro-Economic Data Release & Micro-Event Headline Dual-Audit Standard
Whenever performing ANY stock analysis (`/mcp:robinhood:stock-analysis`), market overview, or investment evaluation, the assistant MUST unconditionally execute **two parallel live `search_web` audits** alongside Robinhood MCP calls: (1) **Today's Macro Economic Data Releases (`Actual vs. Expected` — e.g., Core CPI `0.3%` vs `0.2%`, Headline CPI, PPI, PCE, Jobless Claims, Fed)**, and (2) **Today's Micro Company-Specific Events & Headlines (Analyst PT changes, probes, contracts, 72h peer earnings)**.
* **Core Enforced Standard:** [mandatory_daily_macro_and_micro_event_headline_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_daily_macro_and_micro_event_headline_audit_rule.md).
* **Mandatory Output:** Render the **4-Gate Daily Macro + Micro Event Scorecard Table** in every stock analysis. If a same-day macro release prints hotter/worse than expected, enforce the **Day-1 Macro Digestion Hold** and wait for S1/S2/S3 support stabilization.

---

## ⚖️ 21. Mandatory Always-On Fair Decision Standard
Every response evaluating any stock, order, chart, or market event MUST deliver an unbiased, objective, plain-English **Fair Decision**—never flattering the user or cherry-picking one side of the story.
* **Core Enforced Standard (`trigger: always_on`):** [mandatory_fair_decision_always_needed_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_fair_decision_always_needed_rule.md).
* **The 5 Fair Decision Gates:**
  1. **Live Data Over Feelings:** Verify real-time quotes, `Cap / Shares` (plus actual diluted shares), live orders, and 1-minute opening bars (to prove when a missed low was a 60-second trap inside `9:30–9:45 AM`).
  2. **Unfiltered Both-Sides Truth:** Weigh real strengths (backlog, institutional support) alongside real dealbreakers (dilution, OCF burn, CapEx surge, macro yields, analyst cuts, scandals).
  3. **Time, Macro & Scandal Clearance:** Enforce the `9:30–9:45 AM` ban, `72h` binary freeze, and **3-Day Scandal Freeze**.
  4. **Split Verdict (`Existing Shares` vs. `New Cash`):** Always state separate **Hold/Trim** guidance for shares owned and **Deploy/Wait/`$0.00` Freeze** guidance for buying power.
  5. **Plain-English Clarity:** Short scannable bullets, simple tables, masked `••••3782`, and `🟢 GREEN` / `🔴 RED` bullets with `Live Price` vs `Wall St Market Value`.













