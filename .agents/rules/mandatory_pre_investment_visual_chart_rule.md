---
trigger: model_decision
description: Mandatory Pre-Investment Visual Chart Rule — Draw a clean, non-confusing interactive live Robinhood 1D Dual-Scenario & Step-by-Step Ladder chart before recommending or staging any stock buy or investment.
---

# 📊 MANDATORY RULE: PRE-INVESTMENT VISUAL CHART STANDARD (CLEAN, LIVE & NON-CONFUSING)

## 🛑 Executive Directive
Whenever the assistant evaluates, recommends, proposes, or prepares to stage a **buy, add, dip-buy, or rebalance trade** for **ANY stock or ETF (`[TICKER]`)** — or whenever the user asks to draw/explain a chart — the assistant MUST generate and embed a **clean, interactive live-data visual chart (`<agent-embed>`) FIRST**, before finalizing any investment decision.

**Core Principle ("Visual Clarity Before Capital"):** Never commit buying power blind from numbers alone, AND never clutter a chart with 15 overlapping lines or unexplained jargon. Every chart must make the exact **Floor**, **Step 1 Pivot**, **Step 2 Neckline**, **Open Gaps**, and **Dual Scenario Risk Paths** unmistakable in 10 seconds.

---

## 🛠️ 1. Mandatory 12-Month Live Robinhood MCP Data Pipeline (Zero Guessed Candles)

Every pre-investment chart MUST be built strictly from real-time session calls in that turn — static memory or invented OHLC bars are strictly forbidden:
1. **`get_equity_quotes` (`[TICKER], SPY, QQQ`):** Real-time `last_trade_price`, `Bid/Ask`, official prior close, and index relative divergence.
2. **`get_equity_fundamentals` (`[TICKER]`, `bounds: "regular"`):** Today's live intraday bar (`open`, `high`, `low`, `volume`), `52W` high/low, and `market_cap / shares_outstanding` (`Wall St Market Value`).
3. **`get_equity_historicals` (`[TICKER]`, `interval: "day"` — MANDATORY 12-MONTH FETCH):** ALWAYS pull **`12 months` (`365` calendar days / `~252` completed regular daily OHLCV bars**; or maximum available post-IPO history if listed `< 12` months, explicitly noted) ending yesterday, then append today's live intraday candle cleanly tagged `*`.
4. **`get_equity_technical_indicators` (`[TICKER]`):** Pull **`sma` (`20`, `50`, `200` — integer periods, using `>= 15 months` start_time warm-up so `200-SMA` computes cleanly)**, `rsi` (`14`), and `pivot_points` (`classic`).
5. **Full 12-Month Gap, Swing & Pattern Verification:** Run programmatic/explicit scan across the **entire 12-month (`~252`-bar) history** for:
   * **Unfilled Gaps (`Open` vs. `Already Filled`):** `low[i] > high[i-1]` (gap up) or `high[i] < low[i-1]` (gap down) checked against all subsequent highs/lows across the full year.
   * **12-Month Major Support/Resistance (`S1/S2/S3` & Macro Base) & Fibonacci Grid (`0.50` & `0.618–0.65` Golden Pocket):** Calculated directly from verified 12-month / dominant swing highs and lows so critical older floors or gaps are never hidden off-screen.

---

## 🎨 2. Two Approved Interactive Chart Views (Keep It Clean & Non-Confusing)

All widgets MUST follow `generative_ui` HTML/Canvas standards (`<= 450px` total height, `>= 12px` text, `ResizeObserver`, `themechange` light/dark sync, and **automatic right-axis pill separation `>= 16px` so labels NEVER overlap**):

### View A: Dual-Scenario `1D` Candlestick Chart (Default Pre-Investment View)
* **Clean Display Window (`35 – 60` Candles Shown):** Slice and plot the most recent **`35 – 60` regular daily bars (`~1.5 – 3 months`)** plus the live `*` candle so every candlestick stays wide and clear — while automatically projecting key **`6–12 month` floors, `200-SMA`, and older open gaps** as labeled horizontal lines. *(When a multi-year macro view is requested, render `1-Week` candles over `1–3 years` instead of squishing `250+` daily needles.)*
* Interactive toggles (`checkboxes`) so the user can isolate layers without visual clutter:
  1. `Gaps & SMAs` (`20/50/200-SMA` + shaded Open/Filled gaps)
  2. `Pattern, Channel & Fib` (Ascending/Descending channel rails, `S-H-S` or `W-Bottom` arcs, `0.50` & `0.618–0.65` Golden Pocket)
  3. `Dual Scenario Paths` (Bullish higher-low reclaim arrow vs. Bearish breakdown arrow)
* Interactive hover crosshair tooltip displaying `Date | O / H / L / C | Vol`.

### View B: Ultra-Simple 4-Step Interactive Ladder (`1 → 2 → 3 → 4` Buttons)
* Required whenever explaining a setup in plain English or whenever the user asks `"what is Pivot / Neckline?"` or expresses confusion:
  * **Button 1 — `The Shape`:** Shows only the clean price curve and simple bottom/top landmarks (e.g., `Left Shoulder`, `Head`, `Right Shoulder` or `"W" Double-Bottom`).
  * **Button 2 — `Neckline (Main Roof / Water Line)`:** Shows ONLY the pattern breakout ceiling (`Step 2 Gate`) required to confirm a full trend reversal.
  * **Button 3 — `Pivot (Step 1 Turning Switch)`:** Shows ONLY the short-term battle hinge (`20-SMA` / `Classic Pivot`) inside the pattern.
  * **Button 4 — `Full Ladder`:** Displays the plain-English hierarchy: **`🟢 Floor → 🟠 Step 1 Pivot → 🔴 Step 2 Neckline → 🚀 Target / Open Gaps`**.

---

## 🪜 3. Plain-English Rules Every Pre-Investment Chart Must Enforce

Before recommending ANY buy order (`S1/S2/S3` limit or breakout), verify all 4 visual gates on the chart:
1. **Define Floor vs. Pivot vs. Neckline Honestly:**
   * **🟢 Support Floor (`S1 / S2 / Base`):** Where buyers previously stepped in; staying above keeps the bullish base alive.
   * **🟠 Pivot (`Step 1 Turning Switch`):** Short-term trend flip line (`20-SMA` / `Classic Pivot`). **CRITICAL TRUTH:** Crossing a Pivot only *improves odds* of testing the Neckline — it is **NEVER a "no way to drop" guarantee** (intraday wicks and macro shocks can still reject back below it). Require a **confirmed daily close (and/or retest)** above the Pivot.
   * **🔴 Neckline (`Step 2 Main Ceiling`):** Full pattern reversal gate (`50-SMA` / `S-H-S` peak / `"W"` middle peak). Breaking & holding above unlocks measured-move targets.
2. **Pre-Buy Visual Veto (`$0.00` Freeze Triggers):**
   * **NEVER buy directly underneath an unconfirmed Pivot or Neckline resistance lid** (`mandatory_dual_scenario_technical_matrix_rule.md`).
   * **NEVER chase vertical green spikes into `R1/R2` resistance** or initiate trades outside the `9:45 AM – 10:30 AM EDT` confirmed setup window (`mandatory_intraday_reality_and_morning_dip_rule.md`).
   * If a lower **open gap** sits underneath current price during a red macro tape (`10Y` yield `> 5.0%` or `SPY/QQQ` red), treat the open gap as an active downside magnet and wait/stage only at lower `S2` / `0.65 Golden Pocket` support (once Macro & Event gates pass).
3. **Mandatory Output Pairing:**
   * Embed `<agent-embed>` + clickable `[chart.html](file://...)` link, pair with the **4-Gate Macro + Micro Scorecard**, **Dual-Scenario Table**, and **Fair Decision 🟢 GREEN / 🔴 RED bullets** (explicitly stating `Live Price` vs. `Wall St Market Value` (`Market Cap / Shares Outstanding`) and masked `••••3782` account context; zero LaTeX math blocks).
