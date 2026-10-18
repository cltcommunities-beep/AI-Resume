---
trigger: model_decision
---

# MANDATORY EARNINGS & QUARTERLY RESULTS REPORT TABLE RULE

## Executive Directive
The assistant MUST include the **6-Column Institutional Benchmark Category Table** whenever analyzing a stock's financial performance, earnings reports, or quarterly results.

This table MUST accompany Table 1 (Breaking Market Headlines), Table 2 (Weekly Market Catalysts), Table 3 (4-Point Fundamental Strength Gate), and Table 4 (17-Column Solvency Audit Table).

---

## Mandatory 6-Column Institutional Benchmark Category Table Schema

| Benchmark Category | Source & Institution Group | Expected Benchmark Figure | Reported Actual Result | Variance / Delta | Audit Status Flag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 📦 **Official Management Guidance** | Corporate SEC 8-K Outlook *(CEO/CFO)* | Expected Guidance | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT GUIDANCE or 🔴 MISSED GUIDANCE |
| 📊 **Wall Street Overall Expected** | Blended Consensus Average *(FactSet / Bloomberg / LSEG Aggregate)* | Expected Consensus | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT WALL STREET or 🔴 MISSED WALL STREET |
| 🏛️ **Tier-1 Bank Consensus** | Bulge-Bracket Investment Banks *(Goldman Sachs, JPM, Morgan Stanley, BofA, Citi)* | Expected Tier-1 Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT TIER-1 or 🔴 MISSED TIER-1 |
| 🏛️ **Tier-2 Bank Consensus** | Middle-Market / Regional Desks *(KeyBanc, Mizuho, Stifel, Piper Sandler, Needham)* | Expected Tier-2 Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT TIER-2 or 🔴 MISSED TIER-2 |
| 🔬 **Unofficial Stretch Guess** | Buy-Side Whisper Targets *(Hedge Fund & Trading Desk Expectations)* | Expected Stretch Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT ALL 5 (TROPHY) or 🔴 MISSED STRETCH |

---

## Rules of Execution
1. **Mandatory 6-Column Format:** Always render the 6 columns exactly as shown.
2. **Audit Flag Logic:**
   - 🏆 **`BEAT ALL 5 (TROPHY)`:** Reserve ONLY when the reported result beats all expectations including the 🔬 Unofficial Stretch Guess!
   - 🔴 **`MISSED STRETCH (RED DOT)`:** Mark with a Red Dot whenever the reported result fails to beat the 🔬 Unofficial Stretch Guess.
3. **No LaTeX Math Blocks:** Plain text inside tables only (`no_latex_math_blocks_rule.md`).

