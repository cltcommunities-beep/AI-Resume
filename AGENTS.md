# 🏛️ PROJECT MASTER BRIEFING & CONTEXT ANCHOR (AGENTS.md)

## 🎯 Executive Mission
This workspace permanently governs the **Robinhood Account `••••3782` 6-Month $10,000 to $20,000 Capital Compounding Engine** (October 2026 – April 2027). 

Every agent session, chat turn, and subagent invocation in this workspace MUST automatically load and strictly adhere to this persistent context, the **45+ institutional rules in `.agents/rules/`**, and the live Robinhood MCP toolchain.

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
2. **9:30 AM – 9:45 AM EDT (Opening Bell Patience):**
   * **Strict Buying Ban:** Do not chase opening bell spikes or panic-sell into retail stop-sweeps.
3. **9:45 AM – 10:30 AM EDT (⚡ The Golden Morning Dip Window):**
   * Enforce `mandatory_intraday_reality_and_morning_dip_rule.md`.
   * Execute staged limit buy orders strictly within this 45-minute window at confirmed **S1/S2/S3 Support Floors**.
4. **3:30 PM – 4:00 PM EDT (Daily Closing Audit & Profit Recycling):**
   * Audit closing performance and review active limit sell orders at **R1 / R2 Resistance Targets**.

---

## 🛠️ 3. Mandatory Robinhood MCP Tool Pipeline

Whenever the user asks for a portfolio review or invokes `/mcp:robinhood:portfolio-review`, the assistant **MUST unconditionally execute live broker calls**:
1. `get_accounts` ──► Identifies account `••••3782`
2. `get_portfolio` ──► Fetches Total Value, Cash, and Buying Power
3. `get_equity_positions` ──► Retrieves all active shares and cost basis
4. `get_equity_quotes` ──► Pulls live SIP Consolidated Tape prices and session closes

---

## 📜 4. Active Orders & Holdings Tracking (Live Snapshot - Oct 15, 2026 Audit)

* **Total Portfolio Value:** **$24,762.30** (Targeting $25,000 Milestone; up +147.6% vs $10,000 initial base)
* **Total Liquid Cash:** **$3,733.80** (Expanded via $2,000 external cash injection)
* **Spendable Buying Power:** **$3,577.81** (🟢 **Massive Dry Powder Surplus** — $2,077.81 above $1,500 minimum buffer!)
* **Gold Hedge (IAU):** **59.65 Shares** (~$4,653.90 value, $84.43 cost) held as a permanent geopolitical & inflation shield.
* **Core Active Directives & Executions:**
  * **NVDA (16.00 Shares, Avg Cost $232.43):** Accumulation complete. 16 shares working.
  * **AMKR (66.80 Shares, Avg Cost $51.38):** Pending directive to stage Limit SELL order at **$56.50** (20 shares = $1,130 cash harvest).
  * **NBIS (11.00 Shares):** Active GTC Limit BUY order set for 1.00 share @ **$155.99** (reserves $155.99; buying power $3,577.81).
  * **INTC (21.41 Shares) & CRWV (24.01 Shares):** Hold current shares; zero new capital allocated.
  * **APLD (12.67 Shares):** Active limit sell open for 12.0 shares @ $35.00 GTC.


---

## 🛡️ 5. The "Never Repeat" Mistake Rule
Whenever any market surprise, bad entry, or drawdown occurs, the assistant and user MUST immediately perform a post-mortem and permanently write the lesson into a new markdown rule under `.agents/rules/` to ensure the mistake is never repeated.
* **Core Enforced Standard:** [buy_the_dip_vs_falling_knife_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buy_the_dip_vs_falling_knife_rule.md) (The 5 Golden Rules of Dip-Buying vs Falling Knives).

---

## 🔄 6. Continuous Algorithm Update & Dynamic Calibration Mandate
All trading models, quantitative algorithms, technical support/resistance levels, macro gauges, and stock rosters must be continuously calibrated and kept 100% up-to-date.
* **Core Enforced Standard:** [mandatory_continuous_algorithm_update_and_calibration_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_continuous_algorithm_update_and_calibration_rule.md).
* **Strict Rule:** Trading on uncalibrated models or stale levels triggers an immediate **100% Capital Allocation Freeze ($0.00)**.

