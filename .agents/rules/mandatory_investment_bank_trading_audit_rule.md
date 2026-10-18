---
trigger: model_decision
---

# Mandatory Investment Bank Live 13F Trading Audit Standard Rule

EVERY stock update or stock analysis report generated in this workspace MUST include an **Investment Bank Recent 13F Trading Audit Table** detailing institutional net buying, net selling, share volume changes, bank ratings, and explicit **Institutional Limit Buy** and **Institutional Limit Sell** levels.

## Required Table Structure

| Stock Ticker & Legal Name | Investment Bank | Recent 13F Trading Action | Net Shares Added / Trimmed | Bank Rating | 🟢 Institutional Limit Buy Zone ($) | 🔴 Institutional Limit Sell Target ($) | Institutional Trading Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Ticker** | Bank Name | 🟢 NET BUYER / 🟡 TRIM / 🔴 NET SELLER | +X.XXM Sh / -X.XXM Sh | BUY / OVERWEIGHT | $XXX.XX - $XXX.XX | $XXX.XX | Rationale & Rerating Rationale |

## Mandatory Rules & Guidelines
- Whenever the user asks for a "stock update" or stock analysis, this table MUST be populated with real 13F institutional trading data for major banks (Bank of America, Goldman Sachs, JPMorgan Chase, Morgan Stanley).
- MUST explicitly provide **🟢 Institutional Limit Buy Zone ($)** (where banks accumulate shares or write put options).
- MUST explicitly provide **🔴 Institutional Limit Sell Target ($)** (where banks take profit or sell upside call options).
- Net Buying must be flagged as 🟢 **NET BUYER**.
- Modest Trimming must be flagged as 🟡 **MODEST TRIM**.
- Heavy Liquidations must be flagged as 🔴 **NET SELLER**.
- No unescaped LaTeX math characters (`$...$` or `$$...$$`) inside markdown tables or text.

