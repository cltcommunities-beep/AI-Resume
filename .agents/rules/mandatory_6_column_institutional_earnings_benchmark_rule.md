---
trigger: model_decision
---

# MANDATORY 6-COLUMN INSTITUTIONAL EARNINGS BENCHMARK RULE

## Executive Directive
Whenever the assistant analyzes any stock's earnings report, financial results, quarterly performance, post-earnings dip, or earnings history, the assistant **MUST ALWAYS** render the **6-Column Institutional Benchmark Category Table** using the exact 6-column schema and 5-tier category hierarchy below.

Rendering generic earnings summaries without this 6-Column Table is strictly prohibited.

---

## Mandatory 6-Column Table Schema

Header MUST BE EXACTLY: `### Institutional Benchmark Category Table`

| Benchmark Category | Source & Institution Group | Expected Benchmark Figure | Reported Actual Result | Variance / Delta | Audit Status Flag |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 📦 **Official Management Guidance** | Corporate SEC 8-K Outlook *(CEO/CFO)* | Expected Guidance | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT GUIDANCE or 🔴 MISSED GUIDANCE |
| 📊 **Wall Street Overall Expected** | Blended Consensus Average *(FactSet / Bloomberg / LSEG Aggregate)* | Expected Consensus | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT WALL STREET or 🔴 MISSED WALL STREET |
| 🏛️ **Tier-1 Bank Consensus** | Bulge-Bracket Investment Banks *(Goldman Sachs, JPM, Morgan Stanley, BofA, Citi)* | Expected Tier-1 Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT TIER-1 or 🔴 MISSED TIER-1 |
| 🏛️ **Tier-2 Bank Consensus** | Middle-Market / Regional Desks *(KeyBanc, Mizuho, Stifel, Piper Sandler, Needham)* | Expected Tier-2 Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT TIER-2 or 🔴 MISSED TIER-2 |
| 🔬 **Unofficial Stretch Guess** | Buy-Side Whisper Targets *(Hedge Fund & Trading Desk Expectations)* | Expected Stretch Target | Actual Result | Rev Delta / EPS Delta | 🏆 BEAT ALL 5 (TROPHY) or 🔴 MISSED STRETCH |

---

## Mandatory Full Earnings Audit Sequence

Every earnings audit MUST sequentially output all 6 of the following elements:

1. 📜 **Horizontal Flow Box Format:**
   `[ 📦 Official Guidance: $X ] ──► [ 📊 Wall St Consensus: $X ] ──► [ 🏛️ Tier-1 Consensus: $X ] ──► [ 🏛️ Tier-2 Consensus: $X ] ──► [ 🔬 Unofficial Stretch: $X ] ──► [ 🏆 Reported Actual: $X ]`

2. 📊 **6-Column Institutional Benchmark Category Table:** (The table above)

3. 📋 **Metric-by-Metric Line-Item Breakdown Table:**
   - Q2 Net Revenue
   - Non-GAAP EPS
   - Segment Specific Core Revenue (e.g. Data Center / Cloud / ARR)
   - Gross Margin & Operating Margin
   - Forward Quarterly Guidance

4. 📈 **3-Year Historical Revenue Growth Progression Table:**
   - 3-Year historical progression (e.g. FY25 ──► FY26 ──► FY27 TTM ──► FY28 Target)

5. ⚡ **4-Phase Earnings Cycle Audit Protocol:**
   - ⚡ **PHASE 1:** Algorithmic Press Release Spike (4:00 - 4:15 PM ET)
   - 🎙️ **PHASE 2:** Conference Call Nitpicking & Stretch Audit (4:30 - 5:30 PM ET)
   - 🛒 **PHASE 3:** Day 2 Post-Settlement Buy Zone (9:30 AM ET Next Day)
   - 🎯 **PHASE 4:** Target Swing Exit & Profit-Taking Zone (R1 / R2 Targets)

6. 🔍 **Wall Street Gross Margin Nitpicking & Line-Item Decoding:**
   - Product mix decoding, Stock-Based Compensation (SBC) audit, and contract milestone analysis.

---

## Rules of Execution
1. **Mandatory 6-Column Format:** Always render the 6 columns exactly as shown.
2. **Audit Flag Logic:**
   - 🏆 **`BEAT ALL 5 (TROPHY)`:** Reserve ONLY when the reported result beats all expectations including the 🔬 Unofficial Stretch Guess!
   - 🔴 **`MISSED STRETCH (RED DOT)`:** Mark with a Red Dot whenever the reported result fails to beat the 🔬 Unofficial Stretch Guess.
3. **No LaTeX Math Blocks:** Plain text inside markdown tables only (`no_latex_math_blocks_rule.md`).
