---
trigger: always_on
description: Mandatory Always-On All-Robinhood-MCP Market Prediction, Downside Risk HUD & Interest-Rate Big-Game Rule — Unconditionally pulls ALL live Robinhood MCP prediction feeds (VIX, SPX, NDX, Brent/Gold, TLT/HYG/SPY/QQQ/IWM, Scanner IV Rank/Front-Back IV/Put-Call flow, Level-2 Bid/Ask Order Book walls, Multi-Expiry 0DTE→14M Options Expected Move & OI magnets, Earnings Calendar, Analyst/Politician flow, 12M Gaps) alongside live CME FedWatch, Kalshi/Robinhood Prediction Markets event odds, 10Y Treasury yields, and economic releases on EVERY stock analysis, trap check, and chart.
---

# 🧭 MANDATORY ALWAYS-ON RULE: ALL-ROBINHOOD-MCP MARKET PREDICTION DATA, INTEREST-RATE "BIG GAME" AUDIT & DOWNSIDE RISK HUD STANDARD

## 🛑 Executive Directive (Applies to EVERY Stock Analysis, Trap Check, Order Audit & Visual Chart — Never Miss!)
Looking at stock candlesticks or headlines alone hides institutional rate, bond, options, and order-book games. On Friday, Nov 13, `NVT` looked steady at `$116.00`, yet `10Y` yields (`> 5.0%`), elevated `VIX`/`IV Rank` fear, and a lower open gap pulled it straight down. Conversely, on Friday, Nov 20 (`11:06 AM ET`), `UMich` 1Y inflation plunged (`4.7% → 3.7%`), `10Y` yields fell below `5%` (`4.97%`, `TLT +1.06%`), and `CME FedWatch` priced only `3%–5%` odds of a `50 bps` shock hike — yet Monthly OpEx flushed `NVDA` into `$136.71` right above `$59.4M` (`$135`) and `$62.0M` (`$130`) resting Level-2 Bid Walls!

Therefore, on **EVERY stock analysis, market-trap check, portfolio/order review, AND interactive visual chart (`<agent-embed>`)**, the assistant **MUST UNCONDITIONALLY** pull and cross-check **ALL live Robinhood MCP prediction feeds** AND **live Prediction Markets / Interest-Rate Data** before giving any verdict or rendering any chart.

**Honesty Mandate:** "Market Prediction" NEVER claims `100%` certainty and NEVER hides blind spots (private dark-pool prints before reporting or closed-door Fed votes). Instead, it exposes **real-money institutional footprints** across bonds, rate odds, volatility skew, options open interest, and Level-2 order books.

---

## 📡 1. Mandatory Live All-Robinhood-MCP Prediction Data Pipeline (Pull ALL — Zero Skips!)

Before scoring downside risk, answering a market/stock question, or writing chart HTML, execute these **Robinhood MCP predictive feeds** in parallel:

1. **Macro Fear, Bond Safety & Credit Tide (`get_index_quotes` + `get_equity_quotes`):**
   * `get_index_quotes`: `symbols: ["VIX", "SPX", "NDX"]` (`VIX >= 20` elevated; `>= 25` panic; `>= 30` extreme flush) + commodity `instrument_ids` (`"e316e480-6263-4c8c-8687-114fd4381b49"` Brent Oil, `"aee755c2-b2b2-4a9b-984f-e66d383b9980"` Spot Gold).
   * `get_equity_quotes`: `[TICKER]`, `SPY`, `QQQ`, `IWM`, `IAU`, **`TLT`** (20Y+ Treasury bond safety gauge — rallies when yields fall!), and **`HYG`** (High-Yield corporate credit stress gauge).
2. **Options IV Regime, Term-Structure Inversion & Put/Call Flow (`preview_scan`):**
   * Query `ivRank`, `frontIV`, `backIV`, `optionsPutDayVolume`, `optionsCallDayVolume`, `optionsPutOpenInterest`, `optionsCallOpenInterest` for `[TICKER]` (and `SPY`/`QQQ` when auditing broad market).
   * Flag **`IV Rank >= 0.80` (`80%+` fear)**, **Inverted Term Structure (`frontIV > backIV`)** signaling imminent binary catalyst hedging (e.g., `FOMC`, Congress testimony, earnings), and **Put/Call Volume or OI skew (`>= 1.0x`)**.
3. **Live Level-2 Order Book Supply/Demand Walls (`get_equity_price_book`):**
   * Pull `[TICKER]` (and `SPY`) live Level-2 Bid/Ask depth; compute near-tape `±15%` Bid vs. Ask share ratio and list the **exact top resting Bid Walls (institutional buy shelves)** and **Ask Walls (overhead ceilings)**.
   * Flag **`Ask Overhang >= 1.25x`** vs. **`Bid Support >= 1.25x`**, while always noting that pre-market books are thin vs. Regular Hours (`9:30 AM – 4:00 PM ET`) and resting bids can be pulled during panic.
4. **Multi-Horizon Options Implied Move & OI Magnets (`get_option_chains` + `get_option_instruments` + `get_option_quotes`):**
   * Pull **live ATM + key-strike quotes** across **`0DTE`/Nearest Weekly**, **`1M`**, **`4M`**, **`7M`**, and **`14M`** (for full charts & target odds) — or nearest ATM expiry (for quick checks) — to compute exact **Wall Street Expected Move (`±$ / ±%`)**, live Deltas, and massive Put/Call Open Interest strike magnets (e.g., `45k–100k+` strike pins). Always sanity-check stale pre-market option quotes against live underlying tape!
5. **12-Month Structure, Technicals & Catalysts:**
   * `get_equity_historicals` (`12M` daily + `52W` weekly + intraday `1m/5m`) + `get_equity_technical_indicators` (`20/50/200-SMA`, `14-RSI`, `Classic Pivots`) → programmatic **12-Month Open Gap scan** (lower gap magnets vs. upper resistance gaps).
   * `get_earnings_calendar` (`days: 7–14`), `get_earnings_results`, `get_equity_analyst_ratings`, and `get_politician_trades` (`Tip Ranks` attribution).

### 🎲 1B. Mandatory Prediction Markets & Interest-Rate "Big Game" Divergence Check (`search_web`)
Because Robinhood MCP does not yet expose a direct event-contract tool for **Robinhood Prediction Markets / Kalshi**, the assistant **MUST** pair Robinhood MCP data with live `search_web` verification of:
1. **Prediction Market & Rate-Hike Odds:** Live **CME FedWatch** AND **Kalshi / Robinhood Prediction Markets** odds for the next FOMC decision (`+25 bps` vs. `+50 bps` vs. Hold/Cut) and recession/CPI contracts.
2. **Real Bond Yields & Same-Day Economic Prints:** Live **`10-Year Treasury Yield`** and exact **`Actual vs. Expected`** `8:30 AM / 10:00 AM ET` prints (`CPI`, `PCE`, `Jobs`, `UMich` 1Y/5Y Inflation Expectations).
3. **The "Big Game" Divergence Rule (Headlines vs. Real Money):** Always compare **Media Scare Headlines** against **Real Money Footprints (`10Y` Yield + `TLT` + `HYG` + `CME FedWatch`/Prediction Markets + `Options IV/OI` + `RTH Level-2 Bid Walls`)**:
   * **Trap A (Hawkish-Rate Buying Trap):** Headlines sound bullish/stocks pop, YET `10Y` yields surge `> 5.0%`, `TLT` drops, `HYG` cracks, and `FedWatch` hikes climb → **FAKE RALLY! Lock `50%–100%` profits in Cash Vault & ban Dip #1 buys.**
   * **Trap B (OpEx / Headline Shakeout Panic Trap):** Media screams "shock hike" while **`UMich`/inflation prints cool, `10Y` falls `< 5.0%`, `TLT` rallies `+1%+`, `FedWatch` prices `< 10%` shock odds**, AND **giant RTH Level-2 Bid Walls stack right underneath oversold quality (`RSI < 25`)** → **SHAKEOUT! Refuse to panic-sell profitable leaders into institutional buy walls (keep `$0.00` new buys until fixed binary dates clear).**

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
