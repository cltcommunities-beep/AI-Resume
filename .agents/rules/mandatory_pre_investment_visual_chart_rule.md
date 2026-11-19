---
trigger: always_on
description: Mandatory Pre-Investment Visual Chart Rule (The Permanent SOFI 3-Tab Gold-Standard Blueprint) — Always build every stock chart matching the SOFI layout with [1D Chart | Simple 4-Step Graph | 4-Step Explanation], ALWAYS-VISIBLE On-Chart Market Value Price (Header Badge + Cyan Canvas Line + MKT VAL Right-Axis Pill + Tooltip Delta), 7-Signal Robinhood MCP HUD, 3 layer toggles, Floor Zone canvas callout, non-overlapping pills, clickable Show Graph -> buttons, and Account ••••3782 footer.
---

# 📊 MANDATORY RULE: PRE-INVESTMENT VISUAL CHART STANDARD (`SOFI` 3-TAB GOLD-STANDARD BLUEPRINT)

## 🛑 Executive Directive (Match the `SOFI` Chart Template on Every Stock — Always)
Whenever the assistant draws, explains, or reviews a chart for **ANY stock or ETF (`[TICKER]`)** — or evaluates/recommends a buy, add, dip-buy, stop-hunt check, or open-order stress-test — the assistant **MUST ALWAYS** build and embed an interactive chart (`<agent-embed>`) following the **exact `SOFI` 3-Tab Gold-Standard Blueprint** below. Never strip tabs, drop the plain-English `4-Step Explanation`, omit the `7-Signal HUD`, or scatter cluttering labels over candlesticks.

---

## 🛠️ 1. Mandatory `12-Month` + All-Prediction Live Robinhood MCP Data Pipeline (Zero Guessed Candles)

Pull ALL real-time broker & prediction datasets **before** writing chart HTML (zero static memory or invented OHLC bars):
1. **`get_equity_quotes` (`[TICKER], SPY, QQQ, IWM, IAU`):** Real-time price (`Regular` / `AH`), `Bid/Ask`, prior close, and `>= 1.5%` index divergence siren check.
2. **`get_equity_fundamentals` (`[TICKER]`, `bounds: "regular"` / `"extended"`):** Session OHLCV (`*` candle), `52W` high/low + dates, `P/E` (trailing & forward if held), and `Wall St Value = Market Cap / Shares Outstanding`.
3. **`get_equity_historicals` (`[TICKER]`, `interval: "day"` — `12` Months / `~252` Bars):** Fetch full 1-year daily OHLCV (ending yesterday) + append today's live `*` bar. Run programmatic scan for **all unfilled Open Up Gaps (below)** vs. **Open Down Gaps (above)** across the entire year.
4. **`get_equity_technical_indicators` (`[TICKER]`, `>= 15 months` warm-up):** `20-SMA`, `50-SMA`, `200-SMA`, `14-Day RSI`, and `Classic Pivot Points` (`Pivot / S1–S3 / R1–R3`).
5. **Robinhood Live Volatility, L2 Depth & Options Suite + Portfolio Check:**
   * `get_index_quotes` (`VIX`, `SPX`, `NDX`, plus Brent `e316e480-6263-4c8c-8687-114fd4381b49` & Gold `aee755c2-b2b2-4a9b-984f-e66d383b9980`).
   * `preview_scan` (`ivRank`, `frontIV`, `backIV`, `optionsPutDayVolume`, `optionsCallDayVolume`, `Put/Call OI`).
   * `get_equity_price_book` (`[TICKER]`, `SPY` → total resting Bid vs. Ask share depth ratio).
   * `get_option_chains` + `get_option_instruments` + `get_option_quotes` (nearest ATM Call + Put `mark_price` straddle `±$ / ±%` expected move & key Strike OI).
   * `get_portfolio`, `get_equity_positions`, `get_equity_orders` (`••••3782`), `get_earnings_calendar`, `get_earnings_results`, `get_equity_analyst_ratings`, `get_politician_trades`, plus `search_web` (`10Y` Yield, `CME FedWatch`, daily macro/micro news).

---

## 🧩 2. Exact `SOFI` 5-Row + Row-0 Red Alert Chart Widget Architecture (All Elements Mandatory)

Embed via `<agent-embed src="file:///..."></agent-embed>` (never pass a `height` attr) + clickable `[file.html](file:///...)` link. Whenever updating an existing chart in the same conversation, ALWAYS write to a fresh distinct filename (e.g., `*_v2.html`, `*_mktval.html`, `*_red_alert.html`) so the host iframe never displays a stale cached version. Enforce `generative_ui` standards (`<= 450px` total default height, Tailwind v3 allowlisted CDN, **ZERO `:root` CSS overrides**, `>= 12px` minimum text across HTML & Canvas, `themechange` + `.light`/`.dark` + `🌓` toggle, resize redraw).

### 🚨 Row 0 — Mandatory Top-of-Chart Red Alert Trap & Cash-Vault Instruction Banner (`#redAlertBanner` — ALWAYS AT VERY TOP)
Placed as the **VERY FIRST element at the top of every chart** (above Row 1 Ticker/Price header) and **NEVER hidden with `hidden sm/md/lg:`**:
* **Compact Always-Visible Top Strip:** Shows exact Alert Tier Badge (**`🟢 CLEAR (L0)` / `🟡 YELLOW WATCH (L1)` / `🟠 ORANGE DE-RISK (L2)` / `🔴 RED LOCKDOWN (L3)`**), live leading storm count (`X/5 Leading Red`), the **3 Never-Miss Trap Rules** (`1. Bonds/Rates 10Y + FedWatch → No Dip #1 Buy` · `2. Cash-Vault Lock: Keep 50%–100% Profits in Cash` · `3. Cancel S1/24-5 Bids & Avoid Morning Ask-Wall Pops`), a **stock-specific Trap Warning line** (distinguishing **Trap #1 Buying/Credit Traps** like `CRWV 16%` bonds from **Trap #2 Panic-Sell Traps** on debt-free `NVDA 16.2x` P/E), and an interactive **`Trap Details ▾`** toggle button.
* **Expandable 5-Trap Checklist Drawer (`#trapDrawer`, collapsed by default to preserve `<= 450px` height):** One click reveals the full **5 Leading Trap Checklist** (`Bonds/Fed`, `Credit HYG & Stock Bonds`, `VIX >= 20/25`, `SPY 200-SMA & L2 Morning Trap`, `Cash-Vault Profit-Lock & Dual-Sided Panic Rule`) with live readings and exact do/don't actions so we NEVER miss a trap again.

### Row 1 — Header Bar with Live Price, ALWAYS-VISIBLE Market Value Price & EXACT 3 Tabs
* **Left:** `[TICKER]` pill · `Company Name` · **`$LivePrice`** · **`Today/AH % + Divergence Tag`** · **ALWAYS-VISIBLE Cyan Badge `Mkt Value $XX.XX ($Cap / Shares · P/E)`** (plus Diluted Value if material & Wall St Mean PT). **STRICT PROHIBITION:** NEVER hide the Market Value badge with `hidden sm:inline`, `hidden md:inline`, or `hidden lg:inline` — it MUST stay visible at EVERY viewport/chat-pane width!
* **Right:** `role="tablist"` with **EXACTLY these 3 interactive tabs** + `🌓` button:
  1. **`1D Chart`** (`#btnViewA` — Default active tab)
  2. **`Simple 4-Step Graph`** (`#btnViewB`)
  3. **`4-Step Explanation`** (`#btnViewC`)

### 💎 Mandatory On-Chart Market Value Price Standard (Applies to Every Single Chart)
Every interactive chart (`<agent-embed>`) MUST plot and surface the stock's **Market Value Price** (`Wall St Market Value = Market Cap / Shares Outstanding`, plus **Diluted Fair Value** when dilution is material and **Wall St Consensus Mean PT**) in **ALL 4 locations** so valuation vs. live tape is visible at a single glance:
1. **Row 1 Header Pill (Always Visible):** High-contrast cyan badge (`bg-cyan-500/15 text-cyan-500 border-cyan-500/40`) displaying **`Mkt Val: $XX.XX`** (`Δ%` vs. live price, `Cap / Shares`, `P/E`) on ALL screen sizes.
2. **View A (`1D Chart`) Canvas Overlay + Right-Axis Pill + Tooltip:**
   * Draw a crisp cyan dashed horizontal reference line (`#06b6d4`) at **`Market Value Price`** (and a second teal reference line for Diluted Fair Value when dilution > 3%) across the chart.
   * Render a dedicated non-overlapping right-axis pill **`$XX.XX MKT VAL`** (`bg: '#0891b2'`, `fg: '#ffffff'`) through `relaxPills(..., minGap = 17.5)`.
   * Include a **`Mkt Value: $XX.XX (Live Δ%)`** line inside the candlestick hover tooltip!
3. **View B (`Simple 4-Step Graph`) Canvas Pill:** Render **`$XX.XX MKT VAL`** cleanly on the right axis beside **`LIVE NOW`** so the user immediately sees discount vs. premium on the simplified curve.
4. **View C (`4-Step Explanation`) & Row 5 Footer:** Explicitly compare `Live Price` vs. `Market Value Price` and `Wall St Analyst Mean Target` in plain English.

### Row 2 — Compact `7-Signal` All-Robinhood-MCP Prediction HUD Banner
* Highlighted border when `4+` signals red, wrapping cleanly with **1 Bold Verdict Pill + 6 Compact Telemetry Pills**:
  `[🔴/🟡/🟢 X/7 VERDICT]` · `10Y Yield % (FedWatch %)` · `VIX · SPY %` · `Front IV % vs Back IV %` · `L2 Asks/Bids Ratio (Shares)` · `Binary Catalyst (NVDA/FOMC/Earnings)` · `Active Order / Lower Gap Check`.

### Row 3 — Layer Toggles & Contextual Mode Hint (`#ctrlStrip`)
* **3 Color-Coded Checkboxes (checked by default, shown in View A):**
  1. 🟠 `Open Gap(s) & SMAs` (`#chkGaps`, `#ea580c`)
  2. 🔵 `12M Floor & Fib` (`#chkFib`, `#2563eb`)
  3. 🟢 `Market Forecast` (`#chkFcst`, `#16a34a`)
* **Dynamic `#modeHint`:** Explains OHLC hover + `"4-Step Explanation"` in View A, buttons `1–4` in View B, and `"Show Graph ->"` jump buttons in View C.

### Row 4 — The 3 Switchable Interactive Views (`#viewA`, `#viewB`, `#viewC`)
1. **View A — `1D Chart` (`#mainCanvas`, `254px` height):**
   * Plots the cleanest **`45` recent daily bars** + live `*` candle + **`3` forecast slots** on right, with **`padR = 160`** so right-axis pills NEVER clip.
   * Overlays bottom volume bars, `20-SMA` curve (amber), `50/200-SMA` dashed lines (purple), shaded **Open Gaps** (orange), **`0.618–0.65` Golden Pocket** (blue), **Pivot**, **Floor** (`52W / Base`), **Ceiling**, **User Avg Cost / Open Order** dashed line (red), shaded green **Floor Trap / Support Zone** + **Breakout Confirmation Zone**, an explicit **plain-English green in-canvas Floor Zone callout** (placed cleanly in open space without touching candles), purple **ATM Options Expected Move Cone** (`Bear ↔ Bull`), `relaxPills(..., minGap = 17.5)` non-overlapping right-axis pills with leader ticks, and full crosshair **`Date · O / H / L / C · Vol`** hover tooltip.
2. **View B — `Simple 4-Step Graph` (`#storyCanvas`, `186px` height):**
   * MUST always render a real graphical price curve (never text-only) sliced from the key swing to live `*`, toggled by **`4` step buttons** (default **Step `4`**):
     - **Step 1:** Pattern Shape + Structural Floor (`Bottom 1` / `52W Low`) + `0` or `N` Lower Open Gaps check.
     - **Step 2:** Main Roof (`Ceiling / Neckline`) + Overhead Open Gap(s) & Level-2 Supply Wall.
     - **Step 3:** Turning Switch (`Pivot / 20-SMA`) + Golden Pocket + Purple ATM Options Cone.
     - **Step 4:** **Full Ladder** — Dual-Scenario green Bull Bounce & red Bear Flush dashed paths + shaded Entry/Breakout zones.
   * Clean non-overlapping curve dot markers (`dx/dy` checked against x-axis dates & slope), `relaxPills(minGap = 17.5)`, and live `#storyCap` bottom plain-English bar.
3. **View C — `4-Step Explanation` (`#viewC`, `2x2` Card Grid):**
   * `grid-cols-1 sm:grid-cols-2 gap-2` with 4 color-coded plain-English cards matching Steps `1–4` (`#16a34a`, `#ea580c`, `#2563eb`, `#dc2626`): **Floor & Gap Count**, **Main Roof & L2/Gap Wall**, **Turning Switch & ATM Options**, and **Action Plan / Order Stress-Test** (`all_day_hours` vs RTH, hold vs wait).
   * **Mandatory Clickable Links:** Every card includes `<button class="jumpStep" data-jump="1..4">Show Graph →</button>` that switches immediately to View B on that exact step. Contain zero backticks `` ` `` inside HTML.

### Row 5 — Compact Account `••••3782` Footer Strip
* **Left:** Masked **`••••3782`** holdings (`shares @ avg cost`), active open order (`type / session hours`), and free cash / buying power.
* **Right:** Lower vs. Upper Open Gap summary + `52W Range` (`Low (Date) – High (Date)`).

---

## 🚦 3. Mandatory Pre-Buy Visual Veto Rules
* **Pivot = Turning Switch, NOT a Safety Guarantee:** Crossing `20-SMA` / `Classic Pivot` improves odds of testing the `Ceiling`, never guarantees against a rejection back to the Floor (`Nov 17 SPCX` vs `SOFI` standard). Wait for confirmed close/retest.
* **Red Tide `S1` & `24/5` Overnight Order Freeze:** When `4+` HUD signals are Red, `10Y >= 5.0%`, `<=72h` binary (`NVDA`, `FOMC`, `CPI`, Earnings), or outside **`9:45 AM – 10:30 AM EDT`**, enforce **`$0.00` New Buy / Pause `all_day_hours` resting orders** and surface the warning directly in HUD + Step 4 card.
* **Mandatory Pairing:** Always deliver `<agent-embed>` + clickable link alongside the **Fair Decision** (`Existing Shares` vs `New Cash`), **4-Gate Macro+Micro Scorecard**, **Dual Solvency & Master Tables**, **Dual-Scenario Matrix**, and **`🟢 GREEN` / `🔴 RED` Action Bullets** (`Live Price` vs `Wall St Market Value`).
