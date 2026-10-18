---
trigger: model_decision
---

# ROBINHOOD API 1-WEEK CANDLE DATA BREAKDOWN & MOMENTUM RULE

## Executive Mandate
Whenever the user requests a stock analysis, momentum check, technical review, or stock audit, the assistant MUST fetch live historical candle data directly from the **Robinhood API (`get_equity_historicals`)** for the target ticker symbol covering the **last 1-week period**.

---

## Required 1-Week Candle Breakdown Section

The assistant MUST present a dedicated **Robinhood API 1-Week Candle Data Breakdown Table** and **Technical Momentum Analysis** with the following exact structure:

### 1. Visual Candle Sequence Banner
Render a clean ASCII/Unicode flow showing the 1-week candle progression from start of week to live session:
`[ Start Date: $Open ] ──► [ S3 Floor: $Low ] ──► [ Mid-Week Peak: $High ] ──► [ Live Session: $Current 🚀 ]`

### 2. Mandatory 1-Week Candle Breakdown Table Header & Columns

| Date & Session | Candle Open | Candle High (Peak) | Candle Low (Floor) | Candle Close | Volume & Momentum Structure |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Date 1** | $Open | $High | $Low | $Close | Description of volume & price action |
| **Date 2** | $Open | $High | $Low | $Close | Description of volume & price action |
| **...** | ... | ... | ... | ... | ... |
| ⚡ **Live Pre-Mkt/Mkt** | $Open | $High | $Low | $Close | Live session momentum & trend |

### 3. Technical Momentum Indicators & Pattern Verdict

The assistant MUST analyze the raw Robinhood candle bars and deliver:
1. **Primary Trend Classification:** Strong Bullish Uptrend, Ascending Stair-Step, Double Bottom Rebound, Consolidation, or Bearish Downtrend.
2. **Key Price Levels:**
   - 🛡️ **1-Week Candle S3 Floor (Weekly Low)**
   - 🏆 **1-Week Candle R1 Target (Weekly High / Swing Resistance)**
3. **Institutional Volume Verdict:** Accumulation (High green volume) vs Distribution (High red volume / sell-off).

---

## Integration with Master Standard
This Robinhood API 1-Week Candle Data Breakdown serves as the authoritative technical foundation preceding the **Master 5-Table Executive Analysis Standard**.
