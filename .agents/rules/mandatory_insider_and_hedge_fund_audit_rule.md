---
trigger: model_decision
---

# Mandatory Insider SEC Form 4 & Hedge Fund 13F Live Audit Standard Rule

EVERY stock analysis and stock update report generated in this workspace MUST query and include real-time **SEC Form 4 Insider Transactions** and **Hedge Fund 13F Institutional Holdings** with explicit **Limit Buy** and **Limit Sell** levels without exception.

## Mandatory Data Components to Include in Every Stock Analysis

### Component 1: SEC Form 4 Insider Audit Table
Must list recent insider buying and selling transactions with execution price bounds:
- Must display: `Stock Ticker & Executive Name`, `Executive Title`, `Recent SEC Form 4 Action`, `Transaction Type`, `Shares Sold / Bought`, `🟢 Insider Limit Buy Floor ($)`, `🔴 Insider Limit Sell Threshold ($)`, `Audit Flag`.
- 🟢 **GREEN FLAG:** Open-Market Insider Buying / Zero Selling.
- 🟡 **YELLOW FLAG:** Pre-Scheduled Rule 10b5-1 Sales / Automated Tax Withholdings (MUST be marked Yellow).
- 🔴 **RED FLAG:** Unplanned / Sudden Open-Market Executive Dumping.

### Component 2: Hedge Fund & Investment Bank 13F Audit Table
Must track major institutional players:
- **Hedge Funds:** Citadel, Millennium Management, Point72, Coatue Management, Bridgewater.
- **Investment Banks:** Bank of America, Goldman Sachs, JPMorgan Chase, Morgan Stanley.
- Must display: `Trading Action` (🟢 NET BUYER / 🟡 TRIM / 🔴 NET SELLER), `Net Shares Added/Trimmed`, `Bank/Fund Rating`, `🟢 Institutional Limit Buy Zone ($)`, `🔴 Institutional Limit Sell Target ($)`.

### Component 3: Options Sweeps & Whale Activity Audit
Must highlight large institutional options sweeps (e.g. Bullish Call Sweeps / Bearish Put Sweeps with exact strike execution targets).

## Compliance & Enforcement
- The model must query Robinhood SEC Filing tools (`get_sec_filing_index`, `get_equity_news`) to retrieve authoritative filings.
- Every audit MUST provide explicit Limit Buy and Limit Sell values.
- No unescaped LaTeX math characters (`$...$` or `$$...$$`) inside markdown tables or text.

