---
trigger: model_decision
---

# 🔴 RED-TAG MANDATORY RULE: STRICT BAN ON STATIC STOCK PRICES & HARDCODED DATA

## 🚨 MANDATORY DIRECTIVE: DYNAMIC LIVE API DATA ONLY
This rule is a **RED-TAG MANDATORY DISCIPLINE RULE** governing all stock price retrieval, market valuation tables, and analysis outputs for this assistant. **NO EXCEPTIONS PERMITTED.**

---

### 🔴 1. ABSOLUTE BAN ON STATIC & HARDCODED STOCK DATA
- **STRICT BAN:** **NEVER MAINTAIN, STORE, OR OUTPUT HARDCODED OR STATIC STOCK PRICES IN RULE FILES, PROMPTS, OR SYSTEM MEMORY.**
- **ZERO STATIC MULTIPLES:** Never store static Market Caps, Forward P/E multiples, PEG ratios, or execution prices in text files or historical context.
- **ZERO STALE CACHING:** Never reuse stock prices from prior chat turns or past session logs.

---

### 📲 2. MANDATORY LIVE DYNAMIC ROBINHOOD & WEB API TOOL CALLS
Before rendering ANY stock price, valuation table, comparison chart, or analysis response:
1. **ROBINHOOD LIVE QUOTES FIRST:** The assistant MUST invoke live API tools (`get_equity_quotes` via Robinhood API or `search_web`) to retrieve the 100% real-time streaming market tick.
2. **DYNAMIC FORMULA RE-COMPUTATION:** Re-calculate all market capitalization formulas (`Market Cap / Total Shares`), 17-column solvency values, and upside percentages dynamically from the live streaming response.
3. **TRANSPARENT REAL-TIME TIMESTAMP:** State the exact live streaming price along with the live timestamp (e.g. `Robinhood API Live Quote @ 3:11 PM EDT`).

---

### 🛡️ 3. RULE COMPLIANCE CHECKLIST
- [ ] Is any static or hardcoded stock price stored in rule files? ──► **MUST BE NO.**
- [ ] Was a live API tool call (`get_equity_quotes` / `search_web`) executed in the current turn for EVERY stock analyzed? ──► **MUST BE YES.**
- [ ] Are all valuation numbers computed dynamically from real-time live data? ──► **MUST BE YES.**
