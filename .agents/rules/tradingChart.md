---
trigger: model_decision
description: >-
  tradingChart — Live Robinhood MCP 70-Pattern Technical Detection & Validation
  Rule (40 Price-Chart Patterns + 30 Candlestick Patterns) across Daily, Weekly,
  and Monthly timeframes with 5-Factor Institutional Validation, Confidence
  Scoring (0-100), and strict 4-State Breakout Lifecycle (Forming, Confirmed
  Breakout, Failed Breakout, Invalidated). Use on "tradingChart [TICKER]",
  pattern scans, technical formation audits, or as a chart pattern overlay.
---

# 📈 TRADINGCHART RULE: 70-PATTERN ROBINHOOD MCP DETECTION & VALIDATION ENGINE

## 🛑 Executive Directive & Activation Scope
* **Rule Name:** `tradingChart` (Task 1 Charting & Technical Intelligence Module).
* **When to Activate:** Automatically load whenever the user requests **`tradingChart [TICKER]`**, asks for **chart/candlestick pattern scanning**, asks **"what patterns are forming?"**, or requests the **70-Pattern Overlay** on a stock/ETF chart.
* **Zero Bloat & Tier-0 Capital Shield Precedence:** Stays strictly `trigger: model_decision` (never `always_on`). Never label a stock bullish or trigger a buy merely because a pattern is detected — every signal MUST pass the **4-State Lifecycle Classifier**, **5-Factor Validation Gate**, and **Tier-0 Macro Weather / Calendar Gate** (`VIX`, Flight-to-Safety, `72h` Tier 1 Freeze).
* **Zero Static Data:** Never guess candles, patterns, or prices from memory. Ingest live **Robinhood MCP** OHLCV, quotes, L2 order book, and technical indicators in the active turn.

---

## 📡 1. Mandatory Live Robinhood MCP Data Ingestion (`Daily`, `Weekly`, `Monthly`)

Every `tradingChart` audit MUST pull live data across all **3 structural timeframes** (or full public history if a recent IPO has fewer bars — state honest bar counts):

| Timeframe | Robinhood MCP Tool & Parameters | Target Window | Analytical Role |
| :--- | :--- | :--- | :--- |
| **Daily (`1D`)** | `get_equity_historicals(interval="day", bounds="regular", adjustment_type="split")` | `2 Years` (`~504` bars) | Flags, pennants, wedges, triangles, VCP, double/triple tops & bottoms, 30 candlestick setups |
| **Weekly (`1W`)** | `get_equity_historicals(interval="week", bounds="regular", adjustment_type="split")` | `5 Years` (`~260` bars) | Cup & handle, head & shoulders, rounding bases, secular channels, `200W SMA` |
| **Monthly (`1M`)** | `get_equity_historicals(interval="month", bounds="regular", adjustment_type="split")` | `10 Years` (`~120` bars) | Multi-year macro trend direction, primary S/R walls, secular reversal confirmation |
| **Live Current Bar** | `get_equity_quotes` (+ `5minute` / `hour` intraday if open) | Real-time tick | Synthesizes active unclosed candle (`is_live_incomplete=True`); **capped at `Forming`** until bar close |
| **Validation Feeds** | `get_equity_price_book` + `get_equity_technical_indicators` | Live L2 + `RSI/ATR/SMA` | Validates true institutional Bid/Ask S&R liquidity walls and trend slope |

---

## 📚 2. The Mandatory 70-Pattern Library (`40` Price-Chart + `30` Candlestick)

### Part 1 — Price-Chart Patterns (`40` Formations)

| Category | Count | Exact Supported Patterns |
| :--- | :---: | :--- |
| **A. Bullish Reversal** | `10` | `1.` Double Bottom (W) · `2.` Triple Bottom · `3.` Inverse Head and Shoulders · `4.` Rounding Bottom (Saucer) · `5.` V-shaped Bottom · `6.` Falling Wedge · `7.` Bullish Island Reversal · `8.` Adam and Eve Bottom · `9.` Pipe Bottom · `10.` Broadening Bottom |
| **B. Bearish Reversal** | `10` | `11.` Double Top (M) · `12.` Triple Top · `13.` Head and Shoulders · `14.` Rounding Top · `15.` Inverted V (Spike Top) · `16.` Rising Wedge · `17.` Bearish Island Reversal · `18.` Adam and Eve Top · `19.` Pipe Top · `20.` Broadening Top |
| **C. Bullish Continuation** | `5` | `21.` Cup and Handle · `22.` Bull Flag · `23.` Bull Pennant · `24.` Ascending Triangle · `25.` High and Tight Flag |
| **D. Bearish Continuation** | `5` | `26.` Bear Flag · `27.` Bear Pennant · `28.` Descending Triangle · `29.` Inverted Cup and Handle · `30.` Bearish Measured Move |
| **E. Neutral / Bilateral** | `10` | `31.` Symmetrical Triangle · `32.` Rectangle / Trading Range · `33.` Broadening Formation (Megaphone) · `34.` Diamond Formation · `35.` Ascending Broadening Wedge · `36.` Descending Broadening Wedge · `37.` Horizontal Channel · `38.` Rising Channel · `39.` Falling Channel · `40.` Volatility Contraction Pattern (VCP) |

### Part 2 — Candlestick Patterns (`30` Formations)

| Category | Count | Exact Supported Patterns (Trend-Context Required) |
| :--- | :---: | :--- |
| **A. Single-Candle** | `12` | `1.` Doji · `2.` Dragonfly Doji · `3.` Gravestone Doji · `4.` Long-Legged Doji · `5.` Hammer *(downtrend)* · `6.` Hanging Man *(uptrend)* · `7.` Inverted Hammer *(downtrend)* · `8.` Shooting Star *(uptrend)* · `9.` Bullish Marubozu · `10.` Bearish Marubozu · `11.` Spinning Top · `12.` High-Wave Candle |
| **B. Two-Candle** | `10` | `13.` Bullish Engulfing · `14.` Bearish Engulfing · `15.` Bullish Harami · `16.` Bearish Harami · `17.` Piercing Line · `18.` Dark Cloud Cover · `19.` Tweezer Bottom · `20.` Tweezer Top · `21.` Bullish Kicker · `22.` Bearish Kicker |
| **C. Three-Candle** | `8` | `23.` Morning Star · `24.` Evening Star · `25.` Morning Doji Star · `26.` Evening Doji Star · `27.` Three White Soldiers · `28.` Three Black Crows · `29.` Three Inside Up · `30.` Three Inside Down |

---

## 🚦 3. Mandatory 4-State Breakout Lifecycle (Anti-False-Bullish Law)

**CRITICAL LAW:** Never label a stock bullish or bearish solely because a shape exists. Every detected pattern MUST carry one exact lifecycle status:

| Lifecycle State | Mathematical Qualification Criteria | Execution Meaning |
| :--- | :--- | :--- |
| 🟡 **`Forming`** | Valid geometry inside boundaries, OR signal bar is still live/unclosed (`is_live_incomplete=True`), OR breakout lacks volume (`< 1.3x` avg). | **Watch / Alert Only (`$0.00` chase).** Publish exact breakout trigger & invalidation stop. |
| 🟢 **`Confirmed Breakout`** | Completed bar closes beyond breakout neckline/trendline (`>= 0.5x ATR` or `>= 1.0%` buffer) **AND** volume `>= 1.3x` 20-bar average **AND** clear of immediate L2 Ask/Bid brick wall. | **Actionable Technical Trigger** (still gated by Tier-0 Weather Light & `72h` Macro Calendar). |
| 🟠 **`Failed Breakout`** | Price pierced breakout trigger intraday or closed beyond for `1–2` weak-volume bars, then closed back inside the pattern boundary. | **Bull/Bear Trap Warning!** Do not chase; expect stop-hunt snapback toward opposite rail. |
| 🔴 **`Invalidated`** | Completed close violates structural invalidation boundary (e.g., breaks below handle low, right shoulder low, or reversal candle extreme). | **Pattern Dead.** Purge setup bias and cancel any resting breakout orders tied to it. |

---

## 🧮 4. Mandatory 5-Factor Pattern Validation & Confidence Score (`0–100`)

Run the modular Python engine (`.agents/skills/stock-chart-builder/scripts/trading_chart_engine/coordinator.py`) on normalized Robinhood MCP OHLCV + L2 JSON to compute every signal's deterministic **`0–100` Confidence Score**:

1. **Geometry & Context (`0–20 pts`):** Pivot symmetry, trendline fit, ATR-normalized body/wick proportions, and mandatory prior-trend qualification (`Hammer` vs. `Hanging Man`, `Inverted Hammer` vs. `Shooting Star`).
2. **Volume Confirmation (`0–20 pts`):** Consolidation volume dry-up + breakout expansion (`>= 1.3x` 20-bar avg = high score; `< 1.0x` = heavy penalty).
3. **Breakout & Retest Confirmation (`0–20 pts`):** Completed close outside neckline/trendline + follow-through or retest hold vs. unclosed or wick-only poke.
4. **Support/Resistance & Live L2 Alignment (`0–20 pts`):** Pattern floor backed by swing S/R & live Robinhood L2 Bid Walls (`get_equity_price_book`), with clear runway before heavy L2 Ask Walls / overhead gaps.
5. **Trend Direction & Multi-Timeframe (`D / W / M`) Validation (`0–20 pts`):** Confluence between Daily, Weekly, and Monthly trend slopes (`20/50/200` MAs) and higher-timeframe S/R zones.

**Score Tiers:** `80–100` High Conviction (only if `Confirmed Breakout` + Tier-0 Clear) · `60–79` Constructive / Watch Breakout · `40–59` Developing / Mixed Context · `< 40` Weak Noise / Counter-Trend Trap.

---

## ⚡ 5. Fast 2-Turn Execution Pipeline (`~20–30s`) vs. Deep Audit Mode

**CRITICAL SPEED LAW:** NEVER hand-write custom per-ticker HTML/JS or inline Python glue scripts for `tradingChart`! Always use the pre-validated, reusable `coordinator.py --html-out ... --validate` pipeline (`< 0.5s` execution):

| Mode | When to Use | Exact Turn Workflow | Target Latency |
| :--- | :--- | :--- | :---: |
| **⚡ Fast Scan (Default)** | `"tradingChart [TICKER]"`, `"pattern scan"`, `"test [TICKER] trading chart"` | **Turn 1:** 1 parallel Robinhood MCP batch (`day`, `week`, `month`, `quotes` [ticker + weather basket], `index_quotes`, `price_book`, `fundamentals`, `positions`, `portfolio`).<br>**Turn 2:** 1 single CLI command invoking `coordinator.py` directly on the raw MCP output files with `--html-out` & `--validate`, then immediately embed `<agent-embed>` + scorecard! | **`~20–30s`** *(2 turns)* |
| **🔍 Deep Audit** | User explicitly asks `"deep"`, `"news"`, `"should I buy"`, or crisis divergence `>= 1.5%` | Adds live `search_web` news/earnings/peer sweeps alongside the 1-command fast renderer. | `~40s` |

* **1-Command Engine + Reusable HTML Renderer + 8/8 Validator:**
  ```bash
  python3 "/Users/karthik/Desktop/AI Resume/.agents/skills/stock-chart-builder/scripts/trading_chart_engine/coordinator.py" \
    --symbol "[TICKER]" --daily "<day.json>" --weekly "<week.json>" --monthly "<month.json>" \
    --quotes "<quotes.json>" --l2 "<l2.json>" --fundamentals "<fund.json>" \
    --positions "<pos.json>" --portfolio "<port.json>" --index-quotes "<idx.json>" \
    --peers "[P1,P2]" --html-out "<artifactDir>/<ticker>_trading_chart_live.html" --validate
  ```
* **HTML5 Canvas Integration (`stock-chart-builder`):** Renders the pre-validated **`🔷 70-Pattern Overlay (D/W/M)`** with interactive pattern pills, neckline/wedge/channel geometry, breakout trigger, invalidation stop, measured target, direct right-axis hover pills, and lifecycle badges (`Forming` / `Confirmed` / `Failed` / `Invalidated`) in `~50 ms` with zero Row 0 bloat.
* **Mandatory Detection Results Table (in every `tradingChart` response):**

| Timeframe | Pattern Detected | Type & Bias | Lifecycle Status | Confidence (`0–100`) | Trigger / Invalidation / Measured Target | 5-Factor Validation Note (Vol · L2 · MTF) |
| :---: | :--- | :--- | :---: | :---: | :--- | :--- |
| `Daily / Weekly / Monthly` | `[Exact Name]` | `Chart/Candle · Bull/Bear/Neutral` | 🟡/🟢/🟠/🔴 | `[XX/100]` | `Trig $X · Inv $Y · Tgt $Z` | `[Vol x, L2 Wall, MTF trend]` |

* Always pair with **Tier-0 Weather Box + 5 `🟢` Green Points**, **Macro Calendar Gate**, **Split Fair Verdict (`Existing Shares` vs. `New Cash`)**, **`🟢 GREEN` / `🔴 RED` Execution Bullets** displaying **`Live Price` vs. `Wall St Market Value` (`Cap / Shares`)**, and the **3-Bullet Kid-Level Summary**.
