---
trigger: model_decision
description: Mandatory Chart Market Prediction & Downside Risk HUD Rule — Ingests ALL live Robinhood MCP prediction data (VIX, Brent/Gold, Scanner IV Rank/Front-Back IV/Put-Call flow, Level-2 Order Book imbalance, ATM Options Expected Move, 31-day Earnings Calendar, Analyst/Politician flow, 12M Gaps) alongside FedWatch & 10Y yields to display downside risk directly on every chart without cluttering candlesticks.
---

# 🧭 MANDATORY RULE: ALL-ROBINHOOD-MCP ON-CHART MARKET PREDICTION & DOWNSIDE RISK HUD STANDARD

## 🛑 Executive Directive (Why the Nov 13 `NVT` `$116.00` Fill Happened — Never Repeat)
Looking at a stock's candlesticks alone hides market-wide and options-market downside risk. On Friday, Nov 13, `NVT` looked steady at `$116.00`, yet `10Y` bond yields (`> 5.0%`), pre-weekend de-grossing ahead of `NVDA` earnings + `FOMC`, elevated `VIX`/options `IV Rank` fear, and an **unfilled lower gap (`$107.65–$108.79`)** pulled it straight down to `$106.09` within two sessions.

Therefore, EVERY interactive stock chart (`<agent-embed>`) generated under [mandatory_pre_investment_visual_chart_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_investment_visual_chart_rule.md) MUST unconditionally pull **ALL available Robinhood MCP predictive datasets** *before* creating the chart and render a clean, non-cluttering **Market Prediction & Downside Risk HUD** directly on the widget.

**Honesty Mandate:** "Market Prediction" on a chart NEVER claims `100%` certainty. It displays **objective probability tilt** (`Downside Risk Score`) backed by live broker volatility, order-book supply/demand walls, options-implied ranges, macro yields/FedWatch, and `12-Month` gap magnets.

---

## 📡 1. Mandatory Pre-Chart Robinhood MCP Prediction Data Pulls (Pull ALL Before Charting)

Before calculating the HUD score or writing any chart HTML, execute these Robinhood MCP predictive calls in parallel (paired with `search_web` ONLY for external items Robinhood MCP does not expose directly: `10Y` Treasury yield, `CME FedWatch` rate-hike odds, and daily CPI/Fed news):

1. **Macro Fear & Commodity Tide (`get_index_quotes`):**
   * `symbols: ["VIX", "SPX", "NDX"]` → Live CBOE Fear Index (`VIX >= 20.0` elevated fear; `>= 25.0` panic hedging), `SPX`, and `NDX`.
   * Pass exact `instrument_ids` from `get_indexes` (`"e316e480-6263-4c8c-8687-114fd4381b49"` for `Brent Oil`, `"aee755c2-b2b2-4a9b-984f-e66d383b9980"` for `Spot Gold`; note passing commodity string names via `symbols` returns `not_found`, so always use `instrument_ids`).
2. **Options IV Regime & Put/Call Flow (`preview_scan`):**
   * Screen `expression: "symbol"`, `predicate: "ANY_OF"`, `values: ["[TICKER]", "SPY", "QQQ"]` with columns `ivRank`, `frontIV`, `backIV`, `optionsPutDayVolume`, `optionsCallDayVolume`, `optionsPutOpenInterest`, `optionsCallOpenInterest`.
   * Check for **`IV Rank >= 0.80` (`80%+` fear)**, **Inverted Term Structure (`frontIV > backIV`)** signaling imminent catalyst fear, and **Put/Call Volume or OI skew (`>= 1.0x`)**.
3. **Live Level-2 Order Book Supply/Demand (`get_equity_price_book`):**
   * Pull `[TICKER]` and `SPY` bid/ask order books and sum total resting bid shares vs. ask shares.
   * Flag **`Ask Overhang >= 1.25x`** (heavier overhead sell walls than dip bids) vs. **`Bid Support >= 1.25x`**.
4. **ATM Options Implied Move (`get_option_chains` + `get_option_instruments` + `get_option_quotes`):**
   * Required whenever the stock (or direct peer) has a `<= 72h` binary event or high `IV`: sum nearest ATM Call + Put `mark_price` to derive exact **Wall Street Expected Move (`±$ / ±%`)** and check Call vs. Put `open_interest` and `chance_of_profit_long`. Plot the Bear/Bull expected-move targets cleanly on the chart!
5. **12-Month Structure, Technicals & Catalysts:**
   * `get_equity_historicals` (`12M` daily bars) + `get_equity_technical_indicators` (`20/50/200-SMA`, `rsi` `14`, `pivot_points` `classic`) → Full 1-year open gap scan (`gap magnets` above & below).
   * `get_earnings_calendar` (`days: 7` or `14`, `filter: "high_market_cap"`), `get_earnings_results`, `get_equity_analyst_ratings`, and `get_politician_trades`.

---

## 🚦 2. Leading 5-Pillar Early-Warning Trap Radar + 7-Signal Robinhood MCP Score

### 🚨 Part A — The 5 True Leading Trap Signals (Placed in Row 0 Top-of-Chart Red Alert Banner)
To stop getting caught reloading Dip #1 after booking bull-market profits (Nov 2026 lesson: `+$2,520` booked Jul–Oct 9, then reloaded into `10Y > 5.0%` rate-hike hurricane), EVERY chart MUST evaluate these **5 Leading Early-Warning Signals** (`move BEFORE stocks crash`) and surface exact **Trap Instructions** right at the **top of the chart**:

| # | True Leading Trap Signal | Early-Warning Trigger | Never-Miss Trap Instruction |
| :--- | :--- | :--- | :--- |
| **1. Bonds & Fed Shock** | `10Y Yield`, `TLT`, `CME FedWatch` | `10Y > 4.75%–5.0%` OR Fed flips hawkish / hike odds | **Trap #1 (Buying Trap):** NEVER forget bond yields or buy Dip #1 into surging rates. |
| **2. Credit / Junk Cracks** | `HYG` ETF & Single-Stock Bond Yields | `HYG` breaks 20/50-SMA OR issuer bond yield `> 10%–12%` | **Credit Veto:** `$0.00` hard buying ban on distressed borrowers (`> 12%` yields like `CRWV`). |
| **3. `VIX` & IV Panic Skew** | `VIX` (`get_index_quotes`) + `Front IV > Back IV` | `VIX >= 20` (Watch) · `>= 22` (Orange) · `>= 25` (Panic) | **Fear Gauge:** Do NOT chase green pops when `VIX >= 22`; do NOT panic-sell debt-free quality (`NVDA`) at `VIX >= 25` 52W lows (**Trap #2**). |
| **4. `SPY 200-SMA` & L2 Wall** | `SPY` vs `200-SMA` + `get_equity_price_book` | `SPY < 200-SMA` OR morning pop into `>= 1.25x–1.5x` Ask Wall | **Morning Fade Trap:** Cancel `all_day_hours` & `S1` bids before `9:30 AM`; treat morning spikes under `200-SMA` as institutional exit liquidity. |
| **5. Profit-Lock Cash Vault** | Realized Profits vs. Free Cash (`••••3782`) | Any Level 1–3 Red Alert active after taking profits | **No-Reload-on-Dip-1 Rule:** Lock **`50%`** of profit proceeds in cash under **L1 Yellow**, **`100%`** under **L2/L3 Orange–Red** until `SPY > 200-SMA` & `VIX < 22`. |

**3-Level Action Playbook Displayed on Row 0 Banner:**
* 🟢 **`L0 CLEAR (0–1 Leading Red)`:** Normal staged buys allowed (`9:45–10:30 AM ET`); normal profit reloading permitted.
* 🟡 **`L1 YELLOW WATCH (2 Leading Red)`:** Ban breakouts/`S1` bids; **Lock `50%` of profit-taking proceeds in cash**; trim `20%–25%` of high-debt stocks into green resistance.
* 🟠 **`L2 ORANGE DE-RISK (3 Leading Red)`:** **`$0.00` New Buys**; **cancel `all_day_hours` & `S1` resting bids before `9:30 AM`**; **Lock `100%` of profits in cash**; build `25%–35%` cash on morning bounces.
* 🔴 **`L3 RED LOCKDOWN (4–5 Leading Red)`:** Strict **`$0.00` Buying Ban** + **Lock `100%` Cash Vault** + **Anti-Panic Fence** (never panic-sell debt-free quality into 52W lows; trim leveraged borrowers only on relief bounces).

### 📊 Part B — Live 7-Signal Robinhood MCP + Macro HUD Score (`0 to 7 Red`)

Score every chart from live telemetry before rendering:

| Signal # | Data Source | 🟢 Tailwind (`0 Red`) | 🔴 Downside Pressure (`+1 Red`) |
| :--- | :--- | :--- | :--- |
| **1. Rates & FedWatch** | `search_web` (`10Y Yield`, `FedWatch`) | `10Y < 4.8%` & no imminent hike shock | **`10Y >= 5.0%`** OR **`>= 70%` near-term Fed hike risk** |
| **2. Index & Fear (`VIX`)** | `get_equity_quotes` + `get_index_quotes` | `SPY`/`QQQ` green & `VIX < 20` | **`SPY <= -0.4%`**, **`QQQ <= -0.5%`**, OR **`VIX >= 20.0`** |
| **3. `IV` Fear & Put/Call** | Robinhood `preview_scan` | `IV Rank < 0.70` & `frontIV <= backIV` | **`IV Rank >= 0.80`**, **`frontIV > backIV`**, OR **Put Vol > Call Vol** |
| **4. L2 Order Book Walls** | `get_equity_price_book` | Bid shares >= Ask shares (`Bid >= 1.0x`) | **`Ask Shares / Bid Shares >= 1.25x`** (heavy sell wall overhead) |
| **5. `72h` Binary Catalyst** | `get_earnings_calendar` / `results` / `FOMC` | Zero Fed/CPI/peer/company catalyst `<= 72h` | **FOMC / CPI / PPI / `NVDA` / ticker or peer earnings `<= 72h`** |
| **6. Trend & Lower Gap** | `12M` OHLCV + `20/50/200-SMA` | Price `> 20-SMA` & **zero open gaps below** | Price **below `20/50-SMA`** OR **open gap sits below live price** |
| **7. Clock & Friday Trap** | Current ET time & Day of Week | Inside `9:45–10:30 AM EDT` (Mon–Thu clean) | **Pre-market / `> 10:30 AM ET`**, OR **Pre-Catalyst Friday** |

### Verdict Mapping Displayed on Chart:
* 🟢 **`0–1 Red Signals` → `TIDE: FAVORABLE`:** Normal staged `S1/S2` or Pivot-reclaim setups permitted inside `9:45–10:30 AM EDT`.
* 🟡 **`2–3 Red Signals` → `TIDE: CAUTION`:** Downgrade limit bids strictly to **`S2` / `0.65` Golden Pocket** or **below any lower open gap**; ban `S1` bids.
* 🔴 **`4+ Red Signals` (or active `<=72h` binary / `10Y >= 5.0%`) → `TIDE: HIGH DOWNSIDE RISK → BUY BAN ($0.00)`:** Display prominent **`BUY BAN ($0.00)`** strip; show ATM Options Bear Target / lower open gap as primary risk zone.

---

## 🖥️ 3. Exact Visual Layout Inside Every Chart Widget (Keep Candlesticks Clean!)

To protect the **"Never Confusing"** design (`<= 450px` total widget height, `>= 12px` text, zero overlapping labels), place prediction data into **3 lightweight, non-overlapping zones**:

1. **Top Prediction Status HUD (`Below Title Header`):**
   * Compact wrap-safe bar showing Score Badge + compact live Robinhood telemetry pills:
     * Example: `MARKET PREDICTION: 🔴 7/7 DOWNSIDE RISK → BUY BAN ($0.00)` + compact pills: `10Y 5.14%` · `VIX 25.3` · `IV Rank 100% (74%v67%)` · `L2 Asks 1.46x` · `ATM ±9.9%` · `Lower Gaps: ✓ 0`
2. **Lower Open Gap & ATM Options Range Callouts (`On Canvas`):**
   * Shade any **open unfilled gap BELOW live price** in translucent amber/rose with clear label (`⚠️ Gap Magnet $XX–$YY`). If zero lower gaps exist, state `12M Scan: Zero open gaps < $Floor` cleanly in clear space.
   * When a `<72h` catalyst has `get_option_quotes` ATM pricing, plot the **ATM Options Bear Target** cleanly in the forecast zone alongside **Bull Target**.
3. **Weighted Dual-Scenario Arrows + Honest Tilt (`Forecast Zone`):**
   * Show the honest condition & probability tilt (never `100%` certainty), explicitly referencing invalidation levels (`Step 1 Pivot`, `Step 2 Neckline`, or `12M Base`).

---

## 🛡️ 4. Mandatory Pre-Buy Chart Gate Enforcement

1. **Zero Unchecked Charts:** Generating any chart without pulling Robinhood's live `VIX`, `preview_scan` volatility/put-call, `get_equity_price_book` Level-2 book, and `12M` gap scan is an automatic rule violation.
2. **Sync With Existing Rules:** All `$0.00` freezes, Friday `S1` bans ([mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md)), and Macro Tide vetoes ([mandatory_macro_market_down_pressure_signals_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_macro_market_down_pressure_signals_rule.md)) remain strictly enforced and surfaced inside the chart HUD.
