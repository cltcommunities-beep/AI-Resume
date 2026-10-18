---
trigger: model_decision
---

# Mandatory SEC Form 4 Insider Transaction Audit Standard Rule

EVERY stock analysis report generated in this workspace MUST include an **SEC Form 4 Insider Transaction Audit Table** tracking executive buying, selling, and 10b5-1 pre-scheduled trades.

## Required Table Structure

| Insider Name & Title | Transaction Type | Shares Transacted | Transaction Price | Total Value ($) | Trade Mechanism / Filing Note | Audit Status Flag |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **Insider Name** | Buy / Sell / Grant | Quantity | $XXX.XX | $XX.XM | Filing Mechanism Note | Flag Indicator |

## Mandatory Audit Status Flag Rules
- 🟢 **GREEN FLAG:** Zero Insider Selling / Open-Market Insider Share Buying.
- 🟡 **YELLOW FLAG:** Pre-Scheduled Rule 10b5-1 Executive Sales / Automated Tax Withholding Sales upon RSU vesting (MUST be flagged as Yellow).
- 🔴 **RED FLAG:** Unplanned / Sudden Open-Market Executive Dumping or Insider Trimming.

## Compliance
- All SEC Form 4 filings must be audited for major holdings (`MRVL`, `ORCL`, `NVDA`, `PATH`, `CVX`).
- No unescaped LaTeX math characters (`$...$` or `$$...$$`) inside markdown tables or text.
