---
trigger: model_decision
description: Mandatory Rule for Chart Behavior Dynamics, 4 Structural Zones (Floor, Pivot, Vacuum Surge, Neckline), 3 Pivot Scenarios, and Continuous Rule Codification on Every Chart Analysis.
---

# 📈 MANDATORY ALWAYS-ON RULE: CHART BEHAVIOR DYNAMICS, PIVOT-TO-NECK SURGE MECHANICS & CONTINUOUS LEARNING STANDARD

## 🛑 Executive Directive (Applies to Every Chart, Order Test & Price Review)
Whenever the assistant or user analyzes a chart, tests an order level, evaluates a price surge, or conducts a post-mortem for **ANY stock or ETF (`[TICKER]`)**, the assistant is **STRICTLY PROHIBITED** from viewing price action as random lines, isolated support numbers, or static memory.

Every chart follows the fundamental laws of institutional auction theory and liquidity order books. The assistant **MUST UNCONDITIONALLY** evaluate the asset across the **4 Structural Chart Behavior Zones**, stress-test the **3 Pivot-to-Neckline Scenarios**, and permanently codify new behavioral patterns into rules so that institutional lessons are never forgotten.

---

## 🗺️ 1. The 4 Structural Chart Behavior Zones

Every candlestick chart operates across four sequential behavioral zones:

```
[Zone 1: Structural Floor] ──► [Zone 2: Turning Pivot] ──► [Zone 3: Liquidity Vacuum] ──► [Zone 4: Neckline Roof]
   (Base / Accumulation)          (The Inflection Switch)      (Fast Momentum Surge)          (Institutional Supply)
```

### Zone 1: The Base & Structural Floor (`Bottom 1`, `52W Low`, `200-SMA`)
* **Market Psychology:** Value accumulation, capitulation wick absorption, and stop-loss hunting.
* **The Rule:** Before declaring a floor, verify that **0 open down gaps exist immediately below** (preventing gap magnets from pulling price lower).
* **Execution:** GTC Limit Buys are staged here (e.g., `SOFI @ $13.86`, `SPY @ $727.00–$732.34 200-SMA`).

### Zone 2: The Turning Switch Pivot (`Classic Daily/Weekly Pivot`)
* **Market Psychology:** The mathematical equilibrium point where short-sellers defend their gains and buyers attempt to regain control.
* **Below Pivot = Bear Control Zone:** Odds of surging directly to the Neckline are low (**~25%–30%**). Rallies below the Pivot are routinely faded by algorithmic sellers.
* **At Pivot = The Algotrading Flip:** When price reclaims the Pivot on expanding volume, quant trend models flip from net short to net long, triggering forced stop-loss covering.
* **The Golden Law:** **Touching the Pivot is NOT the same as Breaking the Pivot.** Never buy *anticipating* a Pivot break; wait for an hourly/daily close above.

### Zone 3: The Liquidity Vacuum (Pivot-to-Neckline Surge)
* **Market Psychology:** Between the Pivot and the Neckline, order books are typically thin with very few resting sell orders.
* **The Surge Mechanics:** Once the Pivot is cleanly broken, price travels rapidly through this vacuum because short-sellers cover while breakout algos chase. Odds of reaching the Neckline jump to **~65%–70%**.

### Zone 4: The Neckline & Main Roof (`R1/R2 Resistance`, `50-SMA`, `Prior Swing High`, `Gap Walls`)
* **Market Psychology:** Heavy institutional distribution, long-term trapped supply, and profit-taking by floor buyers.
* **The Golden Law:** The Neckline is an **EXIT / PROFIT-HARVESTING ZONE (sell 33%–50%)**, **NEVER an initial buy zone**. Buying at the Neckline creates extreme FOMO bagholders who get trapped when price rejects back to the Pivot.

---

## ⚖️ 2. The 3 Pivot-to-Neckline Scenarios (Reality Check)

Whenever price approaches or touches the Turning Pivot, the assistant must map out the exact probability of these three pathways:

| Scenario | What Price Action Does at the Pivot | Probability | Outcome & Required Action |
| :--- | :--- | :---: | :--- |
| **A. Confirmed Breakout & Vacuum Surge** | Price crosses the Pivot with **>1.3x relative volume** and closes a 30-min/1-hour candle above it. | **~50%** | 🟢 **Surge to Neckline Confirmed.** Hold existing floor shares and ride the momentum straight into the Neckline. |
| **B. The Pivot Rejection Trap (Bull Trap)** | Price wicks above the Pivot intraday on weak volume or macro headwinds, gets rejected, and turns red. | **~35%** | 🔴 **Flush Back to Floor.** Trapped buyers panic, sending price right back to test the 200-SMA or session low. *(Example: Nov 17 SPCX)* |
| **C. Pivot Retest & Launch** | Price breaks above the Pivot, pulls back to retest the Pivot from above (holding it as support), then resumes upward. | **~15%** | 🟢 **Elite Institutional Add Zone.** Offers the highest risk-to-reward ratio for new capital deployment toward the Neckline. |

---

## 📊 3. The 12-Month Data Ingestion Baseline (Zero Guessed History)

To ensure technical behavior is never evaluated on incomplete or distorted timeframes:
1. **Mandatory 252 Daily Bars (365 Days):** Every technical chart review must ingest the full 1-year historical dataset via `get_equity_historicals`.
2. **Authoritative 200-SMA Anchor:** A 200-day moving average requires at least 200 completed daily closes. Evaluating a chart without full 12-month data violates institutional standards.
3. **52-Week Range & 12M Gap Audit:** Every analysis must report the true 52-week High/Low dates and scan for all unfilled gaps across the entire 12-month period.
4. **Visual Resolution Standard:** View A of interactive charts displays the cleanest **45 recent daily bars** for high-resolution OHLC candlestick clarity, while projecting the horizontal levels derived from the 12-month macro history.

---

## 🔄 4. The Continuous Rule Learning Protocol (Never Repeat a Mistake)

Every time a stock exhibits unexpected chart behavior, an order test is executed, or an earnings catalyst passes:
1. **Immediate Behavioral Extraction:** Identify what the chart did (e.g., *Did it wick above the Pivot and fail? Did an all_day_hours order get filled in an after-hours liquidity hole? Did gross margin guidance crush a revenue beat?*).
2. **Permanent Codification:** Document the exact lesson into `.agents/rules/` within that turn.
3. **Anchor to `AGENTS.md`:** Ensure the rule is indexed so that all future agent sessions, subagents, and chat turns automatically load and enforce the new standard.

---

## 🎯 5. Core Asset Behavioral Matrix (Authoritative Reference)

| Ticker & Role | Structural Floor (Zone 1) | Turning Pivot (Zone 2) | Liquidity Vacuum (Zone 3) | Neckline Roof (Zone 4) | Active Behavioral Lesson |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`SPY` (Broad Market)** | `$726.79` Low / `$732.55` (200-SMA) | **`$730.69` Daily Pivot / `$742.84` Weekly Switch** | `$742.84` to `$753.72` | **`$741.60–$742.84` L2 Ask Wall & `$753.72` (20-SMA)** | Nov 18 closed `$730.20` under 200-SMA; Nov 19 pre-market ripped `+1.33%` to `$739.94` on Anthropic `$81.3B` IPO right into 16.4k L2 Ask Wall (`$741.60–$742.80`) & OpEx `$741.62` cap. Never chase pre-market spikes into ask walls ahead of 8:30 AM Claims & 9:45 AM confirmation. |
| **`SPCX` (Space Defense)** | `$137.50` Base Support | **`$144.50` Pivot** | `$144.50` to `$151.00` | **`$151.00–$153.00` Neckline** | Nov 17 proved: touching `$151.90` Neckline requires taking profits, not buying. |
| **`SOFI` (Fintech Compounder)** | `$13.86` (52W Double Bottom) | **`$15.42` Pivot** | `$15.42` to `$16.19` | **`$16.19–$16.25` Gap 1 & `$17.74` Peak** | Order at `$13.86` is right price; all_day_hours setting must be protected against overnight shocks. |
| **`NVDA` (AI Compute Anchor)** | `$149.50` Deep S2 Trap / `$158` Floor | **`$165.50` Pivot** | `$165.50` to `$174.00` | **`$174.00–$180.00` Neckline Roof** | Post-earnings gap-ups face gross margin nitpicks; sell pops at Neckline, accumulate at Floor. |
| **`BE` (AI Baseload Power)** | `$162.93` Low / `$168.83` (S2 Floor) | **`$178.13` Pivot** | `$178.13` to `$182.35` | **`$182.35` (R1) & `$183.20–$183.89` Gap Roof** | Nov 18 pre-market surged to `$182–$184.99` Neckline, hit 2.9x L2 Ask Wall and rejected back to `$178.13` Pivot. Proves Neckline is a sell zone, never a buy zone. Retesting `$178.13` determines Scenario C Launch vs. Scenario B Flush to `$162.93–$168.83` Buy Zone. |

---

## 📋 6. Mandatory Color-Coded Execution Bullets

In every chart evaluation, the assistant MUST conclude with:
* 🟢 **GREEN BULLETS (To Follow):** Explicit positive actions. Always state the `Live Price` beside the `Wall St Market Value` (`Market Cap / Shares Outstanding`).
* 🔴 **RED BULLETS (NOT to Follow):** Strict prohibitions against buying unconfirmed Pivots, chasing Neckline walls, or trading without full 12-month historical data.
