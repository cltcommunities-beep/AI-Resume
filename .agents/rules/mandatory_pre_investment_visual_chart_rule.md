---
trigger: always_on
description: Mandatory Full Visual Chart Creation Standard — Every stock/ETF chart MUST include ALL 4 timeframes [Today (5m) | 2D (Prior+Today) | 1D Daily | 1W Weekly], ALL 3 views [Chart | Simple 4-Step Graph | 4-Step Explanation], Row 0 Red Alert Trap & Cash-Vault Banner, Always-Visible Cyan Market Stock Value (Banner + Line + Pill + Tooltip), 7-Signal Robinhood MCP HUD, Always-On Interactive 6-Factor Target-Price % Probability Bar (0DTE + 1M/4M/7M/14M) with Always-Visible Purple Dashed Target Line (edge-pinned if off intraday scale), Live VWAP & Event Clock on Today (5m), Mandatory Zero-Missing-Data 6-Zone L2 Bid/Ask Parity (Exact Shares + $M Dollar Values + Total Bid/Ask Level Counts on ALL 4 TFs & View B), Account ••••3782 Footer, and Mandatory Automated Completeness + jsc Syntax Verification.
---

# 📊 MANDATORY FULL CHART CREATION STANDARD (`TODAY / 2D / 1D / 1W` HYBRID + ALWAYS-ON TARGET LINE + 6-FACTOR `%` ODDS + RED ALERT BLUEPRINT)

## 🛑 Executive Directive (Applies Automatically Every Single Time a Chart Is Requested)
Whenever the user asks for a chart of **ANY stock, ETF, or index (`[TICKER]`)** — or whenever the assistant evaluates/recommends a buy, add, dip-buy, stop-hunt check, or open-order stress-test — the assistant **MUST UNCONDITIONALLY** build and embed an interactive HTML/Canvas chart (`<agent-embed>`) satisfying **100% of this Full Chart Creation Standard**.

**STRICT PROHIBITIONS:**
* NEVER strip any of the **4 Timeframe Tabs** (`● Today (5m)`, `2D`, `1D Daily`, `1W Weekly`) or any of the **3 View Tabs** (`Chart`, `Simple 4-Step Graph`, `4-Step Explanation`).
* NEVER omit the **Row 0 Red Alert Trap & Cash-Vault Banner**, the **Always-Visible Cyan Market Stock Value**, the **7-Signal Prediction HUD**, or the **6-Factor Target-Price `%` Probability Calculator**.
* NEVER let the **Purple Dashed Target Line (`★ $XX.XX`)** disappear on any timeframe tab (including zoomed intraday `Today 5m` / `2D` views!).
* NEVER invent or guess OHLC bars, VWAP values, options IV, or prices — every single candle and probability input MUST come from live Robinhood MCP + live web searches in that exact turn.

---

## 🛠️ 1. Mandatory Live Multi-Timeframe & All-Prediction Data Ingestion Pipeline

Before writing any chart HTML, execute ALL live data fetches (zero static memory):

1. **Real-Time Tape & Index Divergence (`get_equity_quotes`):**
   * Fetch `[TICKER]`, `SPY`, `QQQ`, `IWM`, `IAU`, `TLT`, `HYG`.
   * Record live price (`Regular` / `Pre-Market` / `After-Hours`), `Bid / Ask`, official prior-session close, and `>= 1.5%` relative index divergence check.
2. **Intraday Live Bars for `● Today (5m)` & `2D` Tabs (`get_equity_historicals`):**
   * **Today (`24/5` 1-Minute → Aggregated 5-Minute):** Call `interval: "minute"`, `bounds: "24_5"`, `start_time: "<TODAY>T00:00:00-05:00"`. Aggregate non-interpolated bars cleanly into crisp **5-minute candlesticks** with session flags (`OVN`, `PRE`, `RTH`, `AH`) and compute **exact session-reset cumulative Intraday VWAP** for every bar.
   * **2-Day Context (`Prior Day + Today`):** Call `interval: "5minute"`, `bounds: "extended"`, starting at prior trading day `09:30 AM ET`. Aggregate to crisp **10-minute candlesticks** (`~70–85` bars) with day-reset VWAP so yesterday's sell-off/rally flows directly into today's session.
3. **12-Month Daily & 52-Week Weekly History (`get_equity_historicals` + `get_equity_fundamentals` + `get_equity_technical_indicators`):**
   * **Daily (`interval: "day"`, `>= 15 months` warm-up):** Compute `20-SMA`, `50-SMA`, `200-SMA`, `14-Day RSI`, and **Classic Pivot Points (`Pivot / S1–S3 / R1–R3`)**; append today's live `*` candle; display the cleanest **`45–46` recent daily bars** in `1D Daily`.
   * **Weekly (`interval: "week"`, `>= 2 years` warm-up):** Compute Weekly `20-SMA` & `50-SMA`; display **`52` weekly bars** (including live `*` week) in `1W Weekly`.
   * **Programmatic 12M Open-Gap Audit:** Scan all ~252 daily bars to list every unfilled **Lower Open Gap** (below live price = downside magnet) and **Upper Open Gap** (above live price = resistance/pull target).
   * **Fundamentals & Solvency (`get_equity_fundamentals` + `get_financials`):** Extract `52W High/Low + Dates`, trailing/forward `P/E`, **Wall St Market Stock Value (`Market Cap / Shares Outstanding`)** (plus **Diluted Fair Value** if share count expanded `> 3%`), latest quarter **Cash, Gross Debt, Net Debt, OCF, FCF, and Buybacks vs. Dilution**.
4. **Live Volatility, L2 Depth & Multi-Horizon Options Chain (`0DTE` + `1M / 4M / 7M / 14M`):**
   * `get_index_quotes` (`VIX`, `SPX`, `NDX`, plus Brent `e316e480-6263-4c8c-8687-114fd4381b49` & Gold `aee755c2-b2b2-4a9b-984f-e66d383b9980`).
   * `preview_scan` (`ivRank`, `frontIV`, `backIV`, `optionsPutDayVolume`, `optionsCallDayVolume`, `Put/Call OI`).
   * `get_equity_price_book` (`[TICKER]` and `SPY` → extract **ALL** L2 fields: **Total Bid Price Levels (`len(bids)`)** & **Total Ask Price Levels (`len(asks)`)**, **Near-Tape `±15%` Bid vs. Ask total shares, total `$M` dollar depth, level counts, and Bid/Ask ratio**, AND **Top 5 resting Bid Walls + Top 5 resting Ask Walls with exact Price, Resting Shares, and `$M` Dollar Value**; note transparently that Robinhood L2 reports aggregate resting shares per price level, not private buyer IDs).
   * `get_option_chains` + `get_option_instruments` + `get_option_quotes`: Fetch **LIVE ATM + key strike quotes** across **5 horizons**:
     1. **`Today 0D` / Nearest Weekly** (exact intraday `±$` expected move & key OpEx strike OI)
     2. **`1M` (~30d)** · **`4M` (~120d)** · **`7M` (~210d)** · **`14M` (~12–14m LEAPS)**
   * Account & Catalyst Suite: `get_portfolio`, `get_equity_positions`, `get_equity_orders` (`••••3782`), `get_earnings_calendar`, `get_earnings_results`, `get_equity_analyst_ratings`, `get_politician_trades`, plus **3 orthogonal live `search_web` queries** (`10Y` Treasury Yield & FedWatch + Today's Macro/Fed Speakers, Unfiltered Wire Breaking News, Adversarial/Regulatory/Balance-Sheet Sweep).

---

## 🧩 2. Mandatory 8-Row Full Chart Widget Architecture (Every Element Required)

* **Delivery & Anti-Cache Rule:** Embed via `<agent-embed src="file:///..."></agent-embed>` (**NEVER pass a `height` attribute**) + clickable `[filename.html](file:///...)` link. Whenever revising/updating a chart in the same conversation, **ALWAYS write to a fresh distinct filename** (e.g., `*_v2.html`, `*_today_target_chart.html`) so the host iframe never renders a cached older version.
* **UI & Styling Standards:** Use allowlisted Tailwind CDN (`https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js`), **ZERO `:root` CSS overrides**, **ZERO raw backticks** inside HTML/JS, Light/Dark adaptive canvas (`themechange` + `.light`/`.dark` + `🌓` toggle), `ResizeObserver` live redraw, crisp non-overlapping labels.

### 🚨 Row 0 — Top-of-Chart Red Alert Trap & Cash-Vault Instruction Banner (`#redAlertBanner` — ALWAYS FIRST & NEVER HIDDEN)
* Placed as the **very first element** above Row 1 and **NEVER hidden with `hidden sm/md/lg:`**.
* **Always-Visible Compact Strip:** Alert Tier Badge (**`🟢 CLEAR (L0)` / `🟡 YELLOW WATCH (L1)` / `🟠 ORANGE DE-RISK (L2)` / `🔴 RED LOCKDOWN (L3)`**), live leading storm count (`X/5 Leading`), live `VIX` / `10Y` / Fed / OpEx alerts, **Cash-Vault Lock rule** (`50% L1` / `100% L2–L3`), **stock-specific Trap Check line** (separating Trap #1 Credit/Dilution/Ask-Wall traps from Trap #2 Panic-Sell traps), and clickable **`Trap Details ▾`** button.
* **Macro Calendar Gate Pill (additive):** Row 0 MUST also carry the **Next-Event Pill + Gate State** (`🟢 CLEAR / 🟡 CAUTION / 🟠 PRE-EVENT / 🔴 DAY-OF`) per [mandatory_macro_calendar_gate_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_macro_calendar_gate_rule.md), plus the **Inflation Trinity pill** per [mandatory_inflation_trinity_and_valuation_multiple_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_inflation_trinity_and_valuation_multiple_rule.md). View A draws dashed vertical event markers (`CPI`, `FOMC`, `NFP`, `PCE`, `OpEx`) for events in the visible window and projects the next 14 days in the forecast zone on `1D`/`1W`.
* **Expandable 5-Trap Checklist Drawer (`#trapDrawer`, collapsed by default):** Reveals all 5 traps (`Bonds & Fed`, `Cash-Vault Profit-Lock`, `Balance Sheet / Solvency Gate`, `Today Pivot / Ask-Wall / 0DTE Pin Trap`, and `How to Read Today's Chart / Target Line`).

### Row 1 — Header Bar: 4-Timeframe Switcher + Live Price + 3 Main View Tabs + `🌓`
* **Left:** `[TICKER]` badge + **4-Timeframe Switcher (`role="group"`):**
  1. **`● Today (5m)`** (`data-tf="TODAY"` — **Default Active** during active trading/pre-market/after-hours days, or toggleable anytime; emerald active accent!)
  2. **`2D (Prior+Today)`** (`data-tf="2D"`)
  3. **`1D Daily (46d)`** (`data-tf="1D"`)
  4. **`1W Weekly (52w)`** (`data-tf="1W"`)
  * Clicking ANY timeframe button while in View B or View C automatically switches back to View A (`Chart`).
  * Live price (`$XX.XX`, tabular-nums) + live `%` move + session timestamp + relative divergence vs `SPY`/`QQQ`.
* **Right:** `role="tablist"` with **EXACTLY these 3 view tabs** + `🌓` theme toggle:
  1. **`Chart`** (`#btnViewA` — Default active)
  2. **`Simple 4-Step Graph`** (`#btnViewB`)
  3. **`4-Step Explanation`** (`#btnViewC`)

### 💎 Row 1B — Always-Visible Cyan Market Stock Value Banner (`#mktValBanner` — NEVER HIDDEN AT ANY SCREEN WIDTH)
* **NEVER** hide with `hidden sm/md/lg:` classes. Displays **`💎 Market Stock Value: $XX.XX`** (`$Cap / Shares · P/E · Today VWAP $XX.XX`), **`Live vs Mkt Val: ±X.XX%`** pill (plus Diluted Fair Value if dilution `> 3%`), and **Wall St Mean PT (`$XX.XX`, `±X%`, Buy/Hold/Sell split)**.
* **On-Canvas Requirement (All 4 Timeframes + View B):** Always draw the **cyan dashed horizontal line (`#06b6d4`)** at `Market Value Price`, render **`$XX.XX MKT VAL`** right-axis pill (`#0891b2`), and display `💎 Mkt Val: $XX.XX (±X.X%)` in the hover tooltip.

### Row 2 — Compact 7-Signal All-Robinhood-MCP + Macro Prediction HUD (`#hudBar`)
* Horizontally scrollable single-row pill strip (highlighted rose border when `4+` signals Red):
  `[🔴/🟡/🟢 X/7 VERDICT]` · `VIX · SPY/QQQ % · 10Y/TLT` · `Today 0DTE Range (±$)` · `Pivot · Ask Wall · Key Strike OI` · `L2 Bid Walls & Ratio` · `Today Event Clock / Next Earnings` · `Lower vs Upper 12M Gaps`.

### 🎯 Row 2B — Interactive 6-Factor Target-Price `%` Probability Calculator (`#probBar`)
* **Interactive Controls:**
  * Live **Target Price Slider** (`#tgtSlider`) + **`$XX.XX`** readout.
  * **One-Click Target Presets** covering BOTH intraday and multi-month levels (e.g., `$Bid Floor`, `$Ask Wall`, `$Floor`, `$Gap 1`, `$Gap 2/3`, `$Wall St PT`), each tagging its optimal horizon (`data-hz`).
  * **5 Multi-Horizon Buttons:** **`Today 0D`**, **`1M`**, **`4M`**, **`7M`**, **`14M`** calibrated from live Robinhood option chains (VRP-adjusted barrier probability engine computing **Touch `%`**, **Close `≥/≤` `%`**, **Options Baseline `%`**, and **6-Factor Fundamental + Macro + News + Solvency Tilt `%`**).
* **Smart Timeframe ↔ Horizon Auto-Sync:** Switching between Intraday (`TODAY`/`2D`) and Interday (`1D`/`1W`) automatically syncs default horizon & target (`0D` + intraday wall ↔ `7M` + swing target) **unless** the user manually dragged the slider or clicked a preset (`userManualTarget = true`), in which case their exact target is strictly preserved!

### Row 3 — Contextual Layer Checkboxes & Live Coach Strip (`#ctrlStrip`)
* **3 Color-Coded Checkboxes (checked by default)** whose labels dynamically adapt to the active timeframe:
  * **Intraday (`TODAY` / `2D`):** 🟠 `VWAP & Pivot ($XX.XX)` · 🟢 `Bid Floor & Ask Wall` · 🟣 `Purple Target Line & 0DTE Cone`
  * **Interday (`1D` / `1W`):** 🟠 `Upper Gaps & SMAs` · 🟢 `L2 Bid Floor` · 🟣 `Purple Target Line & Options Cone`
* Dynamic `#modeHint` live coaching line explaining what to watch right now on the active tab.

### Row 4 — The 3 Interactive Views (`#viewA`, `#viewB`, `#viewC`)

#### 1. View A — Multi-Timeframe Candlestick Canvas (`#mainCanvas`, `~218px` height, `padR = 176`)
* **`● Today (5m)` Mode:**
  * Soft background shading separating **Overnight `24/5`** vs. **Pre-Market** vs. **Regular RTH** with crisp vertical session dividers.
  * **Amber Cumulative Intraday VWAP Curve** + **Blue Dashed Classic Pivot** + **Cyan Dashed Market Stock Value** + **Red Dotted 52W Low / Session Support** + **Green Shaded L2 Bid Floor** (with plain-English in-canvas badge) + **Red Shaded Overhead L2 Ask Wall**.
  * **Right-Side Live Event Clock Zone:** Vertical markers + tinted strips for upcoming macro/Fed speeches (e.g., `8:25` / `8:30`), **`9:30–9:45 AM` Red `BAN` Strip** (Opening Stop-Hunt Ban), and **`9:45–10:30 AM` Green `WIN` Strip** (Confirmed Window), overlaid with the **Live `0DTE` Purple Options Expected Move Cone**.
  * Key intraday turning-point dot callout (e.g., pre-market high stalled below Pivot).
* **`2D (Prior+Today)` Mode:**
  * Prior day RTH + After-Hours + Today Pre-Market/RTH 10-minute candles with clean session shading & day-reset Amber VWAP curves so cause-and-effect is unmistakable.
* **`1D Daily (46d)` & `1W Weekly (52w)` Modes:**
  * Full-scale candles + bottom volume bars + Amber `20-SMA` + `50/200-SMA` + shaded Orange **12M Open Gaps** + shaded Green **L2 Bid Floor / Golden Pocket** + **Live Multi-Horizon Purple Options Expected Move Cone** (`1M/4M/7M/14M`).
* **🟣 MANDATORY ALWAYS-ON PURPLE TARGET LINE LAW (ALL 4 TIMEFRAMES):**
  * Whenever `#chkFcst` is checked, **ALWAYS draw the bold Purple Dashed Target Line (`#8b5cf6`, `lineWidth = 2.2`)** AND its purple right-axis pill **`★ $XX.XX (YY%)`**:
    * **If `targetPrice` is inside `[minP, maxP]`:** Draw horizontally across the exact `py(targetPrice)` level.
    * **If `targetPrice > maxP` (off-scale above intraday zoom):** Pin the purple dashed line along the top edge (`padT + 2`) with an unmistakable purple callout box **`▲ ★ TARGET $XX.XX (YY% HZ) — Click 1D/1W for full scale`** + right-axis pill **`▲ ★ $XX.XX (YY%)`**.
    * **If `targetPrice < minP` (off-scale below intraday zoom):** Pin along the bottom edge (`padT + ch - 2`) with **`▼ ★ TARGET $XX.XX (YY% HZ) — Click 1D/1W for full scale`** + right-axis pill **`▼ ★ $XX.XX (YY%)`**.
  * **Smart Intraday Y-Axis Cushion:** If `targetPrice` is within `~$2` of the intraday range, gently expand `minP`/`maxP` to keep the line right on-canvas without squishing candles.
* **Zero-Overlap Axes & Smart Hover Tooltip:**
  * Run ALL right-axis pills through `relaxPills(pills, 15.0, padT + 7, padT + ch - 5)`.
  * Space x-axis time/date labels cleanly so the rightmost bar label NEVER collides with the purple forward timeline/horizon label.
  * Hover tooltip formats volume adaptively (`467`, `12.4k`, `38.02M`), displays **ET time + Session Name + VWAP delta + Pivot delta** on Intraday (`TODAY`/`2D`), and always includes **`💎 Mkt Val: $XX.XX (±X.X%)`**.

#### 2. View B — `Simple 4-Step Graph` (`#storyCanvas`, `154px` height)
* Real graphical swing-to-live curve controlled by **4 Step Buttons** (`1`–`4`, default Step `4`), displaying shaded Floor & Gap zones, Cyan Market Value dashed line + pill, **Purple Target Line + pill**, live Options Cone, and plain-English `#storyCap` bottom bar.

#### 3. View C — `4-Step Explanation` (`#viewC`, `2x2` Card Grid)
* `grid-cols-1 sm:grid-cols-2 gap-2` with 4 color-coded plain-English cards (`emerald`, `orange`, `purple`, `rose`) summarizing: **(1) Live Base, VWAP & Solvency**, **(2) Pivot, Ask Wall & Upper Gaps**, **(3) Target Line & Multi-Horizon Options Odds**, and **(4) Fair Decision & Watchlist Plan** — each with a clickable **`Show Graph →`** (`data-jump="1..4"`) button.

### Row 5 — Compact Masked Account `••••3782` Footer Strip
* **Left:** Masked `••••3782` holdings (`shares @ avg cost` or `0 sh Held` + prior realized P&L), Cyan `Mkt Val`, active open order, Buying Power, and today's buy verdict.
* **Right:** `0DTE` range, Lower vs. Upper Open Gaps summary, and `52W Range`.

---

## 🔒 2B. Mandatory Zero-Missing-Data & 6-Zone L2 Bid/Ask Parity Law (Never Drop Data Across Stocks!)

**Nov 20 `AMD` vs. `NVDA` Post-Mortem Lesson:** Showing exact `$M` Bid Walls (`$135: $63M · $130: $71M`) on `NVDA` while omitting `$M` sizes, total Bid/Ask price-level counts, `1D/1W`/View-B Bid pills, and the chat L2 Order-Book Table on `AMD` creates dangerous analytical blind spots (e.g., hiding that `AMD`'s `±15%` bid support `$78.1M` was nearly **5x thinner** than `NVDA`'s `$363.3M`).

Therefore, **EVERY chart for EVERY stock (`[TICKER]`) MUST display complete L2 Bid/Ask telemetry (`Exact Shares + Exact $M Dollar Values + Total Bid/Ask Price Levels + ±15% Ratio`) across ALL 6 mandatory chart locations — ZERO Omissions Allowed:**
1. **Row 0 Top-of-Chart Banner:** Cite top Bid Wall(s) with exact `$M` dollar size AND total Bid level count (or explicit Ask-Wall overhang when Asks dominate).
2. **Row 2 Prediction HUD Pill (`#hudBar`):** Display `RTH/PRE L2 Bids X.XXx ([BidLvls]B/[AskLvls]A lvls · $XM vs $YM · $Wall1: Xk=$XM · $Wall2: Xk=$XM)`.
3. **Row 2B Target Presets (`#probBar`):** Include at least one **Bid Wall `$M` preset** (e.g., `$400 ($13.5M)` / `$135 ($69M)`) alongside Ask Wall / VWAP / Gap / Mean PT presets.
4. **Row 3 Layer Checkbox (`#lblFib`):** Display exact `$M` dollar sizes in **BOTH** Intraday (`TODAY`/`2D`) AND Interday (`1D`/`1W`) checkbox labels (never generic `"Bids"` without `$M`!).
5. **View A Canvas (`ALL 4 Timeframes: Today 5m, 2D, 1D Daily, 1W Weekly`):**
   * **Intraday (`TODAY` & `2D`):** In-canvas green Bid Floor callout MUST list **both shares AND `$M` values**; right-axis pills MUST show exact shares or `$M` on BOTH Bid Walls (e.g., `$430 BIDS ($5.6M)`) AND Ask Walls (e.g., `$480 ASKS ($12.1M)`).
   * **Interday (`1D Daily` & `1W Weekly`):** NEVER drop the green Bid Wall layer or right-axis pill on `1D`/`1W`! Always render the green Bid Wall zone + in-canvas Bid Wall label (`Shares + $M`) + green right-axis pill (e.g., `$400–$430 BIDS ($25M)`).
6. **View B (`Simple 4-Step Graph`) & View C Cards:** View B right-axis pills MUST include the green L2 Bid Wall `$M` pill; View C Card 1 MUST state exact Bid/Ask level counts, `±15%` shares/`$M` depth, and top Bid Wall `$M` figures.

---

## ✅ 3. Mandatory Pre-Delivery Engineering & Zero-Missing-Data Verification Gate (Rule 2, Rule 3, Rule 4)

Before delivering ANY chart to the user, the assistant MUST pass ALL 6 automated checks in sequence (do NOT stop until ALL pass):
1. **Architecture Plan First (Rules 3 & 4):** Create/reference an MVVM + MVVMC Architecture & Implementation Plan diagram artifact (`*_plan.md`).
2. **Fresh Filename (Anti-Cache):** Save updated charts to a new distinct `.html` filename in the artifact directory.
3. **Static Rules Audit:** Programmatically assert **0 raw backticks**, **0 `:root` CSS overrides**, allowlisted `gstatic` Tailwind CDN, and presence of `redAlertBanner`, `mktValBanner`, `probBar`, and all 4 timeframe buttons (`TODAY`, `2D`, `1D`, `1W`).
4. **Automated Zero-Missing-Data & 6-Zone L2 Parity Audit:** Run a Python verification script asserting **zero missing data** across the generated HTML:
   * L2 Bid/Ask `$M` dollar values + share counts + total Bid/Ask level counts appear in Row 0, Row 2 HUD, Row 2B Presets, Row 3 Checkbox, View A Intraday (`drawIntraday`), View A Interday (`drawInterday` — `1D/1W` Bid pill MUST exist!), and View B (`drawStory` — Bid pill MUST exist!).
   * All core indicators present: Live RTH/Extended VWAP, Cyan Market Stock Value (`MKT VAL`), Always-On Purple Target Line (`★`), `0D/1M/4M/7M/14M` Horizons, `12M` Lower/Upper Open Gap count, Big-Game Bonds/Prediction Markets (`10Y`/`TLT`/`Kalshi` or `FedWatch`), Solvency metrics, and masked `••••3782` Footer.
5. **JavaScript Engine Syntax Test:** Extract the inline `<script>` block and execute a parse check via macOS JavaScriptCore (`/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`) confirming **exit code `0`**.
6. **Visual Math Sanity Check:** Verify right-axis pill count × `15px` fits cleanly within canvas `ch` (both View A and View B) and confirm zero x-axis label collisions before embedding `<agent-embed src="file:///..."></agent-embed>`.

---

## 🚦 4. Mandatory Pre-Buy Visual Veto & Response Pairing Rules
* **Pivot = Turning Switch, NOT a Safety Guarantee:** Touching Pivot or pre-market green is NOT a breakout — require post-`9:45 AM ET` confirmed hourly close + volume `> 1.3x`.
* **Red Tide `S1` & `24/5` Overnight Order Freeze:** When `4+` HUD signals are Red, `VIX >= 25`, `10Y >= 5.0%`, `<=72h` binary (`FOMC`, `CPI`, `OpEx`, Earnings), or outside **`9:45 AM – 10:30 AM ET`**, enforce **`$0.00` New Buy / Pause `all_day_hours` resting bids** directly in Row 0, HUD, and Step 4.
* **Mandatory Text Companion:** Always pair `<agent-embed>` + clickable links with the **4-Gate Daily Macro+Micro Scorecard**, **3-Link Dependency Audit**, **6-Factor `%` Probability Table**, **Executive Solvency & Forensic Debt/Dilution Audit**, **4 Structural Zones & 3 Pivot Scenarios**, **Fair Decision Split (`Existing Shares` vs. `New Cash`)**, and **`🟢 GREEN` / `🔴 RED` Action Bullets** (`Live Price` vs. `Wall St Market Value`).
