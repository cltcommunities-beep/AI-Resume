---
trigger: always_on
description: Mandatory Rule for Direct Pill-Hover Action Guidance, Explicit L2 Ask Wall & Bid Floor Standards, and Zero-Missing-Data Anti-Loss Chart Creation across ALL Stocks.
---

# 🎯 MANDATORY ALWAYS-ON RULE: DIRECT PILL-HOVER ACTION GUIDANCE, EXPLICIT L2 ASK/BID LABELING & ZERO-MISSING-DATA ANTI-LOSS STANDARD

## 🛑 Executive Directive (Applies to Every Single Stock Chart without Exception)
Whenever the assistant creates, updates, or renders an interactive visual chart (`<agent-embed>`) for **ANY stock or ETF (`[TICKER]`)**, the assistant is **STRICTLY PROHIBITED** from generating charts with ambiguous labels, non-interactive price pills, or omitted order-book details.

In institutional trading, **missing even small pieces of data (omitting an Ask Wall, hiding resting order sizes, overlooking open down gaps, or failing to give clear actionable trade instructions) directly causes retail capital losses.**

Every chart MUST unconditionally include:
1. **The Direct Pill-Hover Action Guidance Engine:** Hovering over any right-axis price pill MUST highlight the pill and display a dedicated pointing callout card explaining in plain, simple English **EXACTLY WHAT ACTION TO TAKE**.
2. **Explicit "ASK WALL" & "BID FLOOR" Standards:** Prohibits generic gap labels alone; mandates explicit Level-2 resting dollar values and share sizes on right-axis pills and canvas badges.
3. **Synchronized Dual Action Feedback:** Both the floating Canvas Callout Card and the live **Coach Strip above the canvas** MUST update dynamically in matching high-contrast colors (Red, Green, Amber).
4. **The Zero-Missing-Data Anti-Loss Checklist:** Strict pre-delivery verification to eliminate analytical blind spots.

---

## 👆 1. The Direct Pill-Hover Action Guidance Engine

### A. The Hover Boundary Law
The canvas mousemove event listener MUST NOT restrict tracking solely to the candlestick area (`x <= padL + cw`). It **MUST actively track cursor coordinates across the right y-axis padding (`pxLeft - 10` to `rect.width`)** where price pills reside.

```javascript
// 1. FIRST: Check if cursor is directly hovering over any of the RIGHT-AXIS PILLS!
let pillFound = -1;
if (x >= pxLeft - 10 && x <= rect.width) {
  for (let i = 0; i < lastRenderedPills.length; i++) {
    const p = lastRenderedPills[i];
    if (y >= p.y1 - 4 && y <= p.y2 + 4) {
      pillFound = i;
      break;
    }
  }
}
```

### B. Visual Feedback upon Pill Hover
When `pillFound >= 0`:
1. **Cursor State:** Change cursor to `pointer` (`mainC.style.cursor = 'pointer'`).
2. **Pill Glow:** Draw an outer glowing white/yellow border around the pill (`ctx.strokeStyle = '#ffffff'; ctx.lineWidth = 1.8; ctx.strokeRect(pxLeft - 1, pillY - 1, pillW + 2, pillH + 2);`).
3. **Floating Callout Card with Pointer Arrow:** Render an interactive callout card positioned directly to the left of the pill (`pxLeft - cardW - 14`) with a triangular pointer arrow pointing right at the hovered pill.

---

## 📋 2. The Mandatory Pill Action Dictionary (Every Pill Must Carry Action Directives)

Every right-axis pill added to the `pills` collection MUST include these 6 core properties:
`{ text, y, bg, fg, actionHeader, actionDetails, actionTake, actionBg, actionBorder, actionColor }`.

| Pill Category | Label Syntax Example | Header & Order Book Details | Plain-English Action Directive (`actionTake`) |
| :--- | :--- | :--- | :--- |
| **🔴 Overhead Ask Wall** | **`$143.7 ASK WALL ($28.5M)`** | `🔴 OVERHEAD LIMIT SELL ASK WALL ($143.73–$145.98)`<br>`$28.5M in resting limit sell orders (200k+ trapped shares)` | **`👉 ACTION: TAKE PROFITS / TRIM 33%–50%. DO NOT BUY HERE!`**<br>Trapped buyers dump shares at breakeven; heavy resistance ceiling. |
| **🔴 Turning Switch Pivot** | **`$145.98 PIVOT ASK`** | `🔴 BREAKDOWN PIVOT & PRIOR CLOSE ($145.98)`<br>`Mathematical equilibrium switch between Bull & Bear quant models` | **`👉 ACTION: HARVEST PROFITS ON SPIKES.`**<br>Touching the pivot is NOT breaking it. Wait for daily close above before turning bullish. |
| **🟢 52-Week Low Floor** | **`$124.5 BID FLOOR ($10.6M)`** | `🟢 52-WEEK LOW BID FLOOR ($124.50 · $10.6M BIDS)`<br>`Absorbed capitulation selling · 0 unfilled lower open gaps below` | **`👉 ACTION: HOLD TIGHT / DO NOT PANIC-SELL!`**<br>RSI oversold extreme. Smart money accumulates at this floor. |
| **🟢 Institutional Bid Wall** | **`$120.0 BID WALL ($15.8M)`** | `🟢 INSTITUTIONAL BID WALL ($120.00 · $15.8M BIDS)`<br>`Outsized limit buy wall at attractive forward valuation multiple` | **`👉 ACTION: STAGE PATIENT ACCUMULATION LIMIT BUYS`** once scheduled Tier-1 macro releases digest. |
| **🟢 S2 Structural Floor** | **`$115.0 S2 FLOOR ($18.4M)`** | `🟢 S2 STRUCTURAL FLOOR ($115.00 · $18.4M BIDS)`<br>`Deep capitulation trap support with $44.8M total bid cushion` | **`👉 ACTION: MAXIMUM MARGIN OF SAFETY ENTRY`** during macro liquidity panics. |
| **💎 Market Stock Value** | **`$125.79 MKT VAL`** | `💎 WALL ST MARKET VALUE BASELINE ($125.79 · $3,094B CAP)`<br>`Fundamental baseline: Diluted Shares × P/E Multiple` | **`👉 ACTION: VALUE DEFENSE FLOOR.`**<br>Compare Live Price against Mkt Val to identify institutional mispricings. |
| **🟠 Intraday VWAP** | **`$133.99 VWAP`** | `🟠 INTRADAY VWAP BENCHMARK ($133.99)`<br>`Institutional volume equilibrium point across active trading` | **`👉 ACTION: BEARS IN CONTROL below VWAP.`**<br>Bulls must reclaim on expanding volume before chasing rallies. |
| **Moving Averages (1D/1W)** | **`$181.5 20-SMA`** / **`$203.4 200-SMA`** | `Overhead Moving Average Trend Resistance` | **`👉 ACTION: PROFIT EXIT TARGET on relief rallies.`**<br>Medium/long-term trend ceiling. Exit swing trades if rejected. |

---

## 🎨 3. Explicit Canvas Badges & Shaded Resistance/Support Bands

Every chart MUST explicitly render on the canvas:
1. **🟢 Prominent In-Canvas Bid Floor Badge:**
   ```javascript
   const lbl = '🟢 L2 Bid Floor $XX.XX–$YY.YY ($YY.YY: XX.Xk=$XM · $XX.XX: $YM S2)';
   // Rendered with dark-emerald fill (#064e3b), emerald border (#10b981), and light-emerald text (#34d399)
   ```
2. **🔴 Prominent In-Canvas Ask Wall Badge:**
   ```javascript
   const askLbl = '🔴 L2 Ask Wall $AA.AA–$BB.BB ($BM Limit Sells · Gap Wall / Prior Close)';
   // Rendered with dark-rose fill (#4c0519), rose border (#f43f5e), and light-rose text (#fda4af)
   ```
3. **Shaded Bands with Dashed Borders:**
   - Translucent Green (`rgba(16, 185, 129, 0.16)`) spanning the Bid Floor zone.
   - Translucent Red (`rgba(239, 68, 68, 0.16)`) spanning the Ask Wall zone.

---

## ⚡ 4. Live Synchronized Coach Strip (`#coachStrip`)

Positioned directly above the canvas, the Coach Strip MUST dynamically respond to pill and zone hovers:
* **Default State:** Summarizes whether price is above/below VWAP and which structural level is being tested.
* **Hovering Ask Wall:** Changes to a high-contrast **Red Border & Red Tint** (`border-rose-500 bg-rose-500/20`), shouting:
  `🔴 ASK WALL ($AA–$BB): Cursor over Limit Sells ($BM) 👉 ACTION: TAKE PROFITS / TRIM 33%–50%. DO NOT BUY HERE!`
* **Hovering Bid Floor:** Changes to a high-contrast **Green Border & Green Tint** (`border-emerald-500 bg-emerald-500/20`), shouting:
  `🟢 BID FLOOR ($XX–$YY): Cursor over Limit Buys ($YM) 👉 ACTION: ACCUMULATE / STAGE BIDS. DO NOT PANIC-SELL!`
* **Hovering Vacuum:** Changes to an **Amber Border & Amber Tint** (`border-amber-500 bg-amber-500/20`), stating:
  `🟡 LIQUIDITY VACUUM: Cursor over Thin Book 👉 ACTION: HOLD & RIDE MOMENTUM toward Ask Wall.`

---

## 🛡️ 5. Zero-Missing-Data Anti-Loss Audit Checklist

Before embedding any chart, run this strict zero-missing-data checklist:
1. [ ] **12-Month Gaps Audit:** Verified exact count of unfilled Lower Gaps vs. Upper Gaps (confirm if 0 lower gaps exist).
2. [ ] **L2 Depth Parity:** Exact shares, dollar values ($M), and total level counts present in Row 0, Row 2 HUD, canvas badges, and right-axis pills.
3. [ ] **Explicit Ask Wall Labeling:** Pill on right axis says **`ASK WALL ($XM)`** (never generic gap label alone).
4. [ ] **Direct Pill-Hover Interaction:** Verified `lastRenderedPills` tracks pill hitboxes and renders callout cards on mousemove.
5. [ ] **Macro Calendar Gate Pill:** Row 0 displays the next Tier-1/2 event with T-minus countdown and Gate State (`🟠 PRE-EVENT`, etc.).
6. [ ] **Inflation Trinity Strip:** Row 0 displays PPI, CPI, Core PCE actuals and forward valuation multiple impact.
7. [ ] **Syntax & Sandbox Verification:** Validated via macOS JavaScriptCore (`jsc`) with **Exit Code 0**.
