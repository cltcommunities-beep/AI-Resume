---
trigger: model_decision
description: Dual Solvency Table Rule - Render BOTH the Compact 5-Column Executive Solvency Summary Table AND the Full 17-Column Solvency Audit Table in all stock analyses
---

# MANDATORY DUAL SOLVENCY TABLE RULE (COMPACT SUMMARY + FULL 17-COLUMN AUDIT)

## Executive Directive
Whenever the assistant performs a stock analysis, market audit, or due diligence report, the assistant **MUST INCLUDE BOTH SOLVENCY TABLES**:
1. ⚡ **Table 4: Compact Executive Solvency Summary Table (5 Columns)** — For fast, high-level executive reading and 3-bullet takeaway explanations.
2. 📊 **Table 5: Full 17-Column Solvency Audit Table** — For complete, granular institutional due diligence and formula audits.

---

## 🔁 Sequential Master Structure

Every full stock audit report MUST follow this exact sequence:

1. 🚩 **Visual Candle Sequence Banner**
2. 📊 **Robinhood API 1-Week Candle Data Breakdown Table** & Technical Momentum Verdict
3. 📰 `### 1. Official Breaking Market & Geopolitical Headlines Table`
4. 📅 `### 2. Official Weekly Market-Moving Catalysts Table`
5. 🛡️ `### 3. 4-Point Fundamental Strength Gate Table`
6. ⚡ `### 4. Compact Executive Solvency Summary Table` (5 Columns + 3-Bullet Takeaway)
7. 📊 `### 5. 17-Column Solvency Audit Table` (Full 17-Column Deep-Dive Matrix)
8. 📊 `### 6. Official Earnings Expected vs Actual Table`
9. 🔮 `### 🔮 Future Business Growth Need & 3-5 Year Industry Expansion Analysis`

---

## 📊 Table 4: Compact 5-Column Executive Solvency Summary Schema

| Metric Category | Key Parameter | Live Audit Data & Formula | Solvency & Safety Verdict | Tactical Trade Directive |
| :--- | :--- | :--- | :--- | :--- |
| 🚀 **Price & Valuation** | Live Execution Price | `🚀 $XX.XX ($XX.XX Wall St Value = Market Cap / Total Shares)` | Valuation Benchmark | **Recommended Buy Zone:** `$XX.XX – $XX.XX` |
| 🛡️ **Technical Moat** | Support Floors | `S1: $XX.XX \| S2: $XX.XX \| S3: $XX.XX` | Candle Floor Integrity | **Stop-Loss Buffer:** `$XX.XX` (-3% below S3) |
| 🏦 **Cash & Solvency** | Cash vs Total Debt | `$XX.XB Cash \| $XX.XB Total Debt` | Net Solvency Position | **Solvency Runway:** `>4.0 Years` |
| 🧮 **Net Surplus** | Standard & F1/F2 Surplus | `New Cash = Old + FCF \| F1/F2 Surplus = +$XX.XB` | 100% Debt Coverage | **4/4 Gate Score:** `PASSED` |
| 🔴 **Dilution & Risk** | Share Dilution & Exit Target | `Dilution Status \| Unissued Authorized Shares` | Corporate Action Audit | **🎯 R1 Target Exit:** `$XX.XX` |

### 📝 Mandatory 3-Bullet Executive Explanation
1. 💡 **Price & Support Takeaway:** Concise breakdown of current price vs S1/S2/S3 support floors and recommended buy range.
2. 🏦 **Solvency & Cash Flow Takeaway:** Clear summary of cash reserves, total debt, and 100% debt clearance capability via F1/F2 net surplus.
3. 🎯 **Risk Management & Exit Directive:** Clear summary of stop-loss buffer, position sizing, and target exit price.

---

## 📊 Table 5: Full 17-Column Solvency Audit Schema
Column 2 MUST format price as: `🚀 $XX.XX ($XX.XX Wall St Value = Market Cap / Total Shares)`.

---

## Rules of Execution
1. **Never Omit Either Table:** BOTH the 5-column summary table AND the 17-column table MUST be presented.
2. **No LaTeX Math Blocks:** Plain text formatting inside markdown tables only (`no_latex_math_blocks_rule.md`).
