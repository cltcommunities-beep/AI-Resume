---
trigger: model_decision
---

# MANDATORY BREAKING MARKET & GEOPOLITICAL HEADLINES TABLE RULE

## Executive Directive
Whenever the assistant provides an audit for an individual stock or market analysis, **Table 1 MUST ALWAYS be titled EXACTLY as: `### 1. Official Breaking Market & Geopolitical Headlines Table`** and MUST be formatted inside a clean Markdown Table using a strict 2-Tier Priority Hierarchy. Rendering headlines as plain text is strictly prohibited.

---

## Strict 2-Tier Priority Hierarchy for Table 1

When auditing any individual stock or market update, Table 1 MUST follow this exact row ordering:

### Priority Tier 1: Stock-Specific & Market News FIRST (Rows 1 & 2)
1. **Earnings & Guidance:** Quarterly revenue, EPS beats/misses, and management guidance updates.
2. **Analyst Actions & Price Targets:** Upgrades, downgrades, and Wall Street price target revisions.
3. **Corporate Catalysts:** Product launches, management changes, litigation, patents, mergers/acquisitions, and unusual price/volume surges.

### Priority Tier 2: Relevant Geopolitical & Macro News SECOND (Rows 3 & 4)
- **Direct Operational Impact ONLY:** Geopolitical developments (tariffs, trade embargoes, sanctions, currency shifts, commodity spikes) that **DIRECTLY affect that specific company's** supply chain, regulation, raw materials, or end-market demand.
- **Irrelevant Macro Excluded:** Generic macro news unrelated to the company's business model MUST be excluded.

---

## Mandatory Table 1 Schema (6 Columns)

Table 1 Header MUST BE EXACTLY: `### 1. Official Breaking Market & Geopolitical Headlines Table`

| # | Priority Tier & News Category | Breaking Headline / Event | Impact Level (High / Med / Low) | Live Company & Market Facts | Portfolio Strategy Directive |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1️⃣ | 📊 **Priority 1: Stock Catalyst** | **[Earnings Beat / Guidance Raise / Product Launch]** | 🔴 HIGH / 🟡 MED / 🟢 LOW | Live facts, earnings numbers, and volume spikes | Immediate stock directive |
| 2️⃣ | 🎯 **Priority 1: Analyst & Company** | **[Analyst Upgrades / Price Target / Contract]** | 🔴 HIGH / 🟡 MED / 🟢 LOW | Wall Street targets and major customer deals | Position target exit adjustment |
| 3️⃣ | 🌐 **Priority 2: Relevant Geopolitical** | **[Tariffs / Supply Chain / Import Ban / Sanctions]** | 🔴 HIGH / 🟡 MED / 🟢 LOW | Specific impact on company's supply chain or materials | Risk mitigation & moat assessment |
| 4️⃣ | 🛢️ **Priority 2: Macro & Commodity** | **[Raw Material Spikes / Energy / Regulation]** | 🔴 HIGH / 🟡 MED / 🟢 LOW | Direct cost or demand impact on company's operations | Long-term solvency directive |

---

## Rules of Execution
1. **Exact Table Title:** Header MUST be `### 1. Official Breaking Market & Geopolitical Headlines Table`.
2. **Always Stock-Specific FIRST:** Rows 1 & 2 MUST be stock-specific company news.
3. **Relevant Geopolitical SECOND:** Rows 3 & 4 MUST be geopolitical/macro news that directly impacts the target company.
4. **No LaTeX Math Blocks:** Plain text inside tables only (`no_latex_math_blocks_rule.md`).
