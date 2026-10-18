---
trigger: model_decision
---

# MANDATORY PER-STOCK INDEPENDENT LIVE WEB SEARCH RULE

## Executive Directive
Whenever the user asks for stock analysis, portfolio reports, price updates, or due diligence tables, the assistant MUST execute a **SEPARATE, INDEPENDENT `search_web` OPERATION FOR EACH INDIVIDUAL STOCK**. 

Grouping multiple stocks into a single search query is STRICTLY FORBIDDEN. Every ticker analyzed MUST receive its own dedicated tool call to fetch un-cached, real-time market data directly from authoritative live sources before processing.

---

## Mandatory Execution Protocol

1. **Individual Search Call Per Ticker:**
   - For a query involving $N$ stocks, the assistant MUST execute $N$ distinct `search_web` tool calls.
   - Example for `[GOOG, SECZ, INTC]`:
     - Tool Call #1: `search_web` specifically for `GOOG`
     - Tool Call #2: `search_web` specifically for `SECZ`
     - Tool Call #3: `search_web` specifically for `INTC`

2. **Data Extraction & Processing Requirements:**
   - From each independent live search, extract:
     a. Exact Live / Friday Close / Premarket / Post-market Price.
     b. Exact Market Capitalization ($ Billions / $ Millions).
     c. Total Outstanding Shares & Diluted Share Count.
     d. Official Wall Street Market Value per Share (`Market Cap / Total Shares`).
     e. Dilution Proposal Date & Share Buyback Status.

3. **Dynamic Formula Processing:**
   - Dynamically calculate all per-share formulas (`Pure Cash / Share`, `Standard Surplus / Share`, `Formula 1 Surplus / Share`, `Formula 2 Surplus / Share`, `Real Operating Business Price`) strictly from the freshly retrieved independent search payload.

4. **Zero Cache Enforcement:**
   - Never pull prices from historical context, cached summaries, or previous turns. Every turn containing stock analysis MUST execute independent searches afresh.
