# 📊 Individual Stock 9-Layer Full Chart UI & Data Spec (Task 1 Reference)

This reference preserves the complete verbatim specification from `mandatory_pre_investment_visual_chart_rule.md` (`Sections 1–2D & 3–4`) for **Individual Stock / ETF Charts**.

---

## 🛠️ 1. Mandatory Live Multi-Timeframe & All-Prediction Data Ingestion Pipeline

Before writing any chart HTML, execute ALL live data fetches (zero static memory):

1. **Real-Time Tape, Safe-Haven Weather & Index Divergence (`get_equity_quotes`):**
   * Fetch `[TICKER]`, `SPY`, `QQQ`, `IWM`, `XLK`, `XLP`, `WMT`, `IAU`, `TLT`, `SHY`, `SGOV`, `HYG`.
   * Record live price (`Regular` / `Pre-Market` / `After-Hours`), `Bid / Ask`, official prior-session close, `>= 1.5%` relative index divergence check, **Beginner Weather Light (`💻 Tech XLK` vs `🛒 Groceries XLP/WMT` vs `🏦 Piggy Bank TLT/SHY/SGOV`)**, and **Credit Spread (`HYG` vs `TLT`)**.
2. **Intraday Live Bars for `● Today (5m)` & `2D` Tabs (`get_equity_historicals`):**
   * **Today (`24/5` 1-Minute -> Aggregated 5-Minute):** Call `interval: "minute"`, `bounds: "24_5"`, `start_time: "<TODAY>T00:00:00-05:00"`. Aggregate non-interpolated bars into **5-minute candlesticks** with session flags (`OVN`, `PRE`, `RTH`, `AH`) and compute **exact session-reset cumulative Intraday VWAP** for every bar.
   * **2-Day Context (`Prior Day + Today`):** Call `interval: "5minute"`, `bounds: "extended"`, starting at prior trading day `09:30 AM ET`. Aggregate to **10-minute candlesticks** (`~70–85` bars) with day-reset VWAP.
3. **12-Month Daily & 52-Week Weekly History (`get_equity_historicals` + `get_equity_fundamentals` + `get_equity_technical_indicators`):**
   * **Daily (`interval: "day"`, `>= 15 months` warm-up):** Compute `20-SMA`, `50-SMA`, `200-SMA`, `14-Day RSI`, and **Classic Pivot Points (`Pivot / S1–S3 / R1–R3`)**; append today's live `*` candle; display the cleanest **`45–46` recent daily bars** in `1D Daily`.
   * **Weekly (`interval: "week"`, `>= 2 years` warm-up):** Compute Weekly `20-SMA` & `50-SMA`; display **`52` weekly bars** (including live `*` week) in `1W Weekly`.
   * **Programmatic 12M Open-Gap Audit:** Scan all ~252 daily bars to list every unfilled **Lower Open Gap** (downside magnet) and **Upper Open Gap** (resistance/pull target).
   * **Fundamentals & Solvency (`get_equity_fundamentals` + `get_financials`):** Extract `52W High/Low + Dates`, trailing/forward `P/E`, **Wall St Market Stock Value (`Market Cap / Shares Outstanding`)** (plus **Diluted Fair Value** if share count expanded `> 3%`), latest quarter **Cash, Gross Debt, Net Debt, OCF, FCF, and Buybacks vs. Dilution**.
4. **Live Volatility, L2 Depth & Multi-Horizon Options Chain (`0DTE` + `1M / 4M / 7M / 14M`):**
   * `get_index_quotes` (`VIX`, `SPX`, `NDX`, plus Brent `e316e480-6263-4c8c-8687-114fd4381b49` & Gold `aee755c2-b2b2-4a9b-984f-e66d383b9980`).
   * `preview_scan` (`ivRank`, `frontIV`, `backIV`, `optionsPutDayVolume`, `optionsCallDayVolume`, `Put/Call OI`).
   * `get_equity_price_book` (`[TICKER]` and `SPY` -> Total Bid/Ask Levels, near-tape `±15%` Bid vs. Ask total shares & `$M` depth & ratio, Top 5 Bid Walls + Top 5 Ask Walls; note transparently that L2 reports aggregate resting shares per price level, not private buyer IDs).
   * `get_option_chains` + `get_option_instruments` + `get_option_quotes`: Fetch **LIVE ATM + key strike quotes** across **`Today 0D` / Nearest Weekly**, **`1M`**, **`4M`**, **`7M`**, **`14M`**.
   * Account & Catalyst Suite: `get_portfolio`, `get_equity_positions`, `get_equity_orders` (`••••3782`), `get_earnings_calendar`, `get_earnings_results`, `get_equity_analyst_ratings`, `get_politician_trades`, plus **3 orthogonal live `search_web` queries**.

---

## 🧩 2. Streamlined Modern Chart Architecture (Clean 4-Row Standard)

* **Delivery & Anti-Cache Rule:** Embed via `<agent-embed src="file:///..."></agent-embed>` (**NEVER pass a `height` or `file` attribute**) + clickable `[filename.html](file:///...)` link. Whenever revising/updating a chart, **ALWAYS write to a fresh distinct filename** (`*_v2.html`, etc.).
* **UI & Styling Standards:** Allowlisted Tailwind CDN (`https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js`), **ZERO `:root` CSS overrides**, **ZERO raw backticks** inside HTML/JS, Light/Dark adaptive canvas (`themechange` + `.light`/`.dark` + `🌓` toggle), `ResizeObserver` live redraw, crisp non-overlapping labels.
* **Separation of Concerns Mandate (No Bloated Banners in Chart):** Bloated top banners (Row 0 Red Alert/Cash Vault/Weather box, Row 1B Market Value banner, and Row 2B Target Slider & Presets) are **EXCLUDED from the chart UI**. They clutter the canvas and cause template leaks. Their data (Market Weather Light, Inflation Trinity, Macro Calendar Gate, and Valuation) is delivered directly in the written executive text report.

### Row 1 — Header Bar
* **Left:** `[TICKER]` badge + **4 Timeframe Buttons** (`● Today (5m)`, `2D (Prior+Today)`, `1D Daily (46d)`, `1W Weekly (52w)`) + live price/change/session timestamp.
* **Right:** `role="tablist"` with **`Chart`**, **`Simple 4-Step Graph`**, **`4-Step Explanation`** + `🌓` toggle.

### Row 2 — Contextual Controls & Live Coach Strip (`#ctrlStrip`, `#coachStrip`)
* Clean overlay toggles (VWAP & Moving Averages, Support Floors & Ask Walls, Target Line & Cones) without hardcoded prices in label strings.
* Synchronized Coach Strip (`#coachStrip`) above the canvas illuminates dynamically in Red/Green/Amber matching the hovered right-axis pill.

### Row 3 — The 3 Interactive Views (`#viewA`, `#viewB`, `#viewC`)
1. **View A (`#mainCanvas`, `padR = 176`):**
   * Intraday OVN/PRE/RTH shading, VWAP, Classic Pivot, 52W Low/High, `9:30–9:45 AM` `BAN` Strip, `9:45–10:30 AM` `WIN` Strip, Options Cones.
   * **Mandatory Support Floors (S1 / S2 / S3) & Live Robinhood L2 Bid Floor Engine:**
     - **Robinhood Live L2 Bid Floor:** Directly queried from Robinhood MCP `get_equity_price_book`. Identified as the largest resting bid cluster (e.g., `NBIS: $100.00 (18,020 shs)`), rendered as a distinct green horizontal bid shelf with exact share size and dollar depth, with a dedicated right-axis pill (e.g., `$100.0 L2 BID (18.0k)`).
     - **S1 Structural Floor:** First major structural support floor below price (e.g., breakout retest shelf or previous pivot). Rendered as horizontal line + pill: e.g., `$89.0 S1 FLOOR`.
     - **S2 Major Floor:** Major structural support floor (e.g., previous session low, 0.618 Fib Golden Pocket). Rendered as horizontal line + pill: e.g., `$80.7 S2 FLOOR`.
     - **S3 Macro Capitulation Floor:** Deep baseline support floor (e.g., 52-Week double bottom low). Rendered as horizontal line + pill: e.g., `$73.5 S3 FLOOR`.
   * **Always-On Purple Target Line Law (`★ $XX.XX`):** Drawn horizontally across `py(targetPrice)` when in `[minP, maxP]`, OR pinned cleanly along top (`▲ ★ TARGET ...`) / bottom (`▼ ★ TARGET ...`) when off zoom.
   * **Zero-Overlap Axes & Direct Pill-Hover Engine:** `relaxPills(pills, 15.0, padT + 7, padT + ch - 5)`, zero collisions. Hovering any pill on the right y-axis reveals instant pointer action card (`actionHeader`, `actionTake`, depth, and action badge).
2. **View B (`#storyCanvas`):** 4-Step graphical curve (`1->4`), S1/S2/S3 floor & gap zones, Purple Target Line + cone, `#storyCap`.
3. **View C (`#viewC`):** `2x2` plain-English cards with `Show Graph ->` buttons, Layer 7 Corporate Events, Layer 8 Risk Ticket, Layer 9 Competitor Matrix (`3–5` peers), and `🧸 Simple Kid-Level Summary`.

### Row 4 — Masked Account `••••3782` Footer Strip
* Holdings/realized P&L + Buying Power + `0DTE` range + Open Gaps + `52W Range`.

---

## 🔒 Zero-Missing-Data, 6-Zone L2 & Direct Pill-Hover Parity

* **6-Zone L2 Parity:** Display exact Bid/Ask shares + `$M` dollar depth + total Bid/Ask level counts across: `(1) Row 0 Banner`, `(2) Row 2 HUD`, `(3) Row 2B Presets`, `(4) Row 3 Checkbox`, `(5) View A ALL 4 TFs` (never omit Bid/Support pills on `1D`/`1W`), and `(6) View B & C`. When reporting prior-session lows (like Friday `$80.67`) separately from live L2 bids, label them transparently (e.g., `$80.7 FRI LOW / $79 BASE`) so live L2 bids and historical lows are never conflated.
* **Direct Pill-Hover Engine:** Track `mousemove` across right y-axis padding (`pxLeft - 10` to `rect.width`). Hovering highlights the pill, renders a pointer callout card (`Header`, `Depth`, `👉 EXACT ACTION`), and updates `#coachStrip`.

---

## 🧱 The 9 Mandatory Individual Stock Layers

| Layer | Name | Required Elements |
| :---: | :--- | :--- |
| **1** | **🌦️ Market Weather FIRST** | `SPY`/`QQQ`/`VIX`, Beginner Weather Light (`XLK` vs `XLP`/`WMT` vs `TLT`/`SGOV`), 1947 Regime, Seesaw, Macro Calendar Gate, Seasonal Window. |
| **2** | **📰 Live News & 3-Link Ecosystem** | 3 orthogonal web searches, `>= 1.5%` Divergence Siren, Suppliers -> Customers -> Competitors. |
| **3** | **💎 Company Health & True Value** | Always-Visible Cyan Mkt Value (`Cap / Shares`), Cash vs. Debt, FCF, Dilution vs. Buybacks, Analyst Targets. |
| **4** | **📈 4-TF Technicals & 12M Map** | `Today`, `2D`, `1D` (`252d` `200-SMA` + `12M` Gaps), `1W`, RSI, 4 Structural Zones (`Floor -> Pivot -> Vacuum -> Neckline`). |
| **5** | **🧱 Live Order Flow & Options Odds** | 6-Zone L2 + Pill-Hover Callouts, 5 Options Horizons (`0D/1M/4M/7M/14M`), Always-On Purple Target (`★`). |
| **6** | **💼 Your Account `••••3782` Reality** | Shares held, avg cost, buying power, open orders, Split Fair Decision (`Existing Shares` vs. `New Cash`). |
| **7** | **📅 Corporate Events & Catalyst Calendar** | Earnings dates, regulatory/FDA/NRC, launches, Form 4, S-3/ATM offerings, lockups, announcements. |
| **8** | **🛡️ Risk Management & Trade Validation** | Entry Price (or `$0.00` Freeze Trigger), Stop Loss, `T1/T2/T3`, `R:R`, Sizing (`$` & `%`), Max `$` Loss, Invalidation Rule. |
| **9** | **🏭 Sector & Competitor Intelligence** | 3–5 peers: YoY Rev Growth, Net/Op/FCF Margin, Valuation (`P/E`/`P/S`), Moat/Share, Relative Performance. |
