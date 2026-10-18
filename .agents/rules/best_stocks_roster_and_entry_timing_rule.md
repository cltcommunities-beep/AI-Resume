---
trigger: model_decision
description: Mandatory Best Stocks Roster & Entry Timing Rule for Semiconductors, AI Hardware, Power, and Key Growth Stocks
---

# MANDATORY BEST STOCKS ROSTER & ENTRY TIMING RULE

## Executive Directive
Whenever the user asks about **semiconductors ("semis stocks"), AI hardware, tech power infrastructure, or entry timing** for key growth stocks, the assistant MUST trigger this rule and evaluate the target stocks against the **Approved Best Stocks Roster**.

The assistant MUST determine precise **Entry Timing (Recommended Buy Zone, Support Floors S1/S2/S3, Stop-Loss Buffer, and Target Exit R1)** using live execution prices and the **Master 5-Table Executive Standard**.

---

## 🏆 The Approved Best Stocks Roster

| Category | Approved Best Tickers | Primary Investment Role | Entry Strategy |
| :--- | :--- | :--- | :--- |
| **Primary Semiconductors** | `NVDA`, `MRVL`, `INTC` | Dominant Chip Architecture & Foundry Turnaround | Accumulate at S1 Support; trim near R1 targets |
| **Advanced Packaging & Systems** | `AMKR`, `SMCI` | Chip Packaging & High-Density AI Server Rack Infrastructure | Buy on 4/4 Gate validation dips |
| **Enterprise AI & Compute Platforms** | `PLTR`, `NBIS`, `CRWV` | Enterprise AI OS, Cloud Hyperscalers, & High-Performance Compute | Accumulate on high-volume pullbacks |
| **AI Power & Fintech Infrastructure** | `BE`, `SOFI` | 24/7 Clean Energy Fuel Cells & High-Margin Digital Banking | Strong cash flow compounders |
| **Future Watchlist (Reserve)** | `OKLO` | Next-Gen Nuclear SMR AI Power | ⏳ **FUTURE RESERVE:** Wait for S1/S2 support floor pullback |

---

## 🎯 Mandatory Entry Timing Execution Protocol

For any ticker analyzed from this roster or semi stock query, the assistant MUST calculate:

1. **🚀 Live Execution Price & Wall St Market Value:**
   - Format: `🚀 $XX.XX ($XX.XX Wall St Value = Market Cap / Total Shares)`
2. **🛡️ Support Floor Mapping:**
   - `S1 Support Floor` (Immediate entry base)
   - `S2 Support Floor` (Secondary pullback floor)
   - `S3 Support Floor` (Capitulation value base)
3. **🎯 Recommended Buy Entry Directive:**
   - Explicitly state the exact buy range and timing window: `Recommended Buy: $XX.XX – $XX.XX (Execute strictly during 9:45 AM – 10:30 AM EDT Morning Dip Window at S2/S3 floor)`. Enforce `mandatory_intraday_reality_and_morning_dip_rule.md`.
4. **🛡️ 7 Risk Management Stop-Loss Buffer:**
   - Set Stop Loss **-2% to -3% BELOW S3 Floor** to prevent false intraday shakeouts.
5. **🏆 Target Exit & Profit Recycling:**
   - Set Limit Sell Order at `TradingView R1 Target`.
6. **⏳ OKLO Special Directive:**
   - Whenever `OKLO` is mentioned, mark as `⏳ FUTURE INVESTMENT — WAITING FOR OPTIMAL S1/S2 DIP CHANCE`.

---

## 📊 Integration with Master Standard
This rule works alongside:
- `mandatory_live_search_rule.md` (Independent search per ticker)
- `master_stock_analysis_standard.md` (Sequential 5-table standard)
- `7_risk_management_principles_rule.md` (Stop loss & position sizing)
- `no_latex_math_blocks_rule.md` (Plain text formatting inside markdown tables)
