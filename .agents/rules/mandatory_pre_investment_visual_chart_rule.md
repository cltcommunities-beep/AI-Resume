---
trigger: model_decision
description: >-
  Mandatory 9-Layer Stock + 5-Layer Broad Market Chart Creation & 10/10
  Validation Standard for interactive HTML/Canvas <agent-embed> charts. Load via
  stock-chart-builder skill whenever creating, updating, or auditing any chart.
---

# 📊 MANDATORY FULL CHART CREATION STANDARD (`TODAY / 2D / 1D / 1W` HYBRID)

> [!IMPORTANT]
> **Modular Task Routing (Under `24 KB` Limit):** Whenever creating, updating, or auditing any chart (`"[TICKER] chart"`, `"market chart"`, `"balance sheet chart"`), activate the **[stock-chart-builder](file:///Users/karthik/Desktop/AI%20Resume/.agents/skills/stock-chart-builder/SKILL.md)** skill and load its full detailed specifications:
> * [stock_9layer_spec.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/skills/stock-chart-builder/references/stock_9layer_spec.md)
> * [market_5layer_spec.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/skills/stock-chart-builder/references/market_5layer_spec.md)
> * [validate_chart_contract.py](file:///Users/karthik/Desktop/AI%20Resume/.agents/skills/stock-chart-builder/scripts/validate_chart_contract.py)

---

## 🛑 1. Core Prohibitions (Non-Negotiable Across Every Chart)
* **NEVER** reuse residual text, slider bounds, narrative copy, or prices from a prior stock template (e.g., `BE` inside `NBIS`). Every variable, label, pill dictionary, preset, and card must originate 100% from the target ticker's fresh live bundle.
* **NEVER** strip any of the **4 Timeframe Tabs** (`● Today (5m)`, `2D (Prior+Today)`, `1D Daily (46d)`, `1W Weekly (52w)`) or **3 View Tabs** (`Chart`, `Simple 4-Step Graph`, `4-Step Explanation`).
* **NEVER** let the **Purple Dashed Target Line (`★ $XX.XX`)** vanish on zoomed intraday tabs (pin at top/bottom edge with `▲/▼` badge when out of range).
* **NEVER** invent OHLC bars, VWAPs, or options IV; ingest live Robinhood MCP + 3 orthogonal web searches in the current turn.
* **NEVER** embed with `file=...`, `height=...`, or `title=...` — ALWAYS use `<agent-embed src="file:///..."></agent-embed>` plus clickable markdown link, writing updates to a fresh anti-cache filename (`*_v2.html`).
* **NEVER** conflate a prior-day session low with a live L2 Bid Floor (label prior lows accurately as e.g. `$80.7 FRI LOW / $79 BASE`, and quote live L2 Bid/Ask depth transparently).

---

## 🧩 2. Required 8-Row Architecture & 9-Layer / 5-Layer Parity

1. **MVVMC Plan First (Rules 3 & 4):** Write a `<ticker>_chart_plan.md` artifact before HTML generation.
2. **Streamlined 4-Row Widget UI (Zero `:root` CSS overrides, Zero raw backticks inside HTML/JS, allowlisted `gstatic` Tailwind CDN, Light/Dark adaptive canvas):**
   * **Separation of Concerns:** Bloated top banners (Row 0 Red Alert/Cash-Vault, Row 1B Market Value banner, and Row 2B Target Slider & Presets) are **EXCLUDED from the chart UI** to prevent clutter and template leaks. All macro weather, inflation trinity, calendar gates, and valuation data are delivered directly in the written text report.
   * **Row 1 (Header Bar):** `[TICKER]`, 4 Timeframe Switchers (`● Today 5m`, `2D`, `1D Daily 46d`, `1W Weekly 52w`), Live Tape Price/Change, 3 View Tabs (`Chart`, `Simple 4-Step Graph`, `4-Step Explanation`) + `🌓` theme toggle.
   * **Row 2 (`#ctrlStrip` & `#coachStrip`):** Contextual overlay checkboxes (VWAP, Moving Averages, Support/Resistance Zones, Target Line) + Synchronized Coach Strip responding live to pill hovers.
   * **Row 3 (`#viewA`, `#viewB`, `#viewC`):** View A candlestick canvas (Live Robinhood L2 Bid Floor with exact share depth from `get_equity_price_book`, S1/S2/S3 Support Floors, VWAP, Pivot, 52W Low/High, `9:30–9:45 BAN`, `9:45–10:30 WIN`, Options Cones, Direct Pill-Hover Guidance Engine, `relaxPills`), View B 4-Step Graph (`1->4`), View C `2x2` Explanation Cards + Layer 7 Corporate Events + Layer 8 Risk Ticket + Layer 9 3–5 Peer Matrix + `🧸 Kid-Level Summary`.
   * **Row 4:** Masked Account `••••3782` Footer Strip + `52W` range.
3. **6-Zone L2 Order Flow Parity:** Show Bid/Ask shares, `$M` depth, level counts, and `±15%` ratio across Row 0, Row 2, Row 2B Presets, Row 3 Checkboxes, View A (ALL 4 TFs), and View B/C — noting transparently when pre-market/overnight L2 books show `0B/0A` levels.
4. **9 Individual Stock Layers (`stock_9layer_spec.md`):** `(1)` Market Weather First, `(2)` Live News & 3-Link Ecosystem, `(3)` Company Health & Cyan Mkt Value, `(4)` 4-TF Technicals & `12M` Gaps (`252d` `200-SMA`), `(5)` Live L2 Order Flow & Options Odds, `(6)` Account `••••3782` Reality, `(7)` Corporate Events & Catalyst Calendar, `(8)` Risk Management & Trade Validation (`Entry/Stop/T1–T3/R:R/Size/MaxLoss/Invalidation`), `(9)` Sector & 3–5 Competitor Matrix.
5. **5 Broad Market Macro Layers for `SPY`/`QQQ` (`market_5layer_spec.md`):** `(1)` Breadth (`A/D`, `% > 50/200 SMA`, `52W H/L`, `RSP` vs `SPY`), `(2)` Liquidity & Credit (`2Y/10Y`, `HYG/JNK` vs `TLT`, Fed QE/QT, TGA/RRP), `(3)` Volatility/Sentiment (`VIX`, `VVIX`, Put/Call, Term Structure, Fear & Greed), `(4)` Global Confirmation (`DXY/UUP`, `GLD`, `USO`, `EFA`, `EEM`), `(5)` Leadership & Rotation (`VUG/VTV`, `IWM/SPY`, `XLK/SPY`, Defensive vs Cyclical).

---

## ✅ 3. Mandatory Pre-Delivery Validation Gate (`10/10 PASS` + `jsc exit 0`)
Run [validate_chart_contract.py](file:///Users/karthik/Desktop/AI%20Resume/.agents/skills/stock-chart-builder/scripts/validate_chart_contract.py) on every generated HTML file before responding:
```bash
python3 "/Users/karthik/Desktop/AI Resume/.agents/skills/stock-chart-builder/scripts/validate_chart_contract.py" "<chart.html>" "<TICKER>" --peers "<PEER1,PEER2>"
```
Do **NOT** deliver any chart unless ALL 10 automated checks, zero foreign-ticker leaks, and macOS `jsc` syntax validation exit `0`! Always pair `<agent-embed src="file:///..."></agent-embed>` with the companion 9-Layer summary, Split Fair Decision, Green/Red Bullets (`Live Price` beside `Wall St Market Value`), and 30s Kid Summary.
