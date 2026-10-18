---
trigger: model_decision
---

# Mandatory Investment Bank Analyst & Ownership Tracking Rule

EVERY stock analysis report generated in this workspace MUST include an **Investment Bank Coverage & Target Audit Table** detailing the exact ratings, price targets, and institutional ownership stakes from bulge-bracket investment banks.

## Required Table Structure

| Investment Bank | Lead Tech Analyst | Official Bank Rating | Price Target ($) | Expected Upside (%) | Bank's Core Investment Thesis |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Bank of America (BofA)** | Lead Analyst | BUY / NEUTRAL / SELL | $XXX.XX | +XX.X% | Thesis & Catalysts |
| **Goldman Sachs** | Lead Analyst | BUY / NEUTRAL / SELL | $XXX.XX | +XX.X% | Thesis & Catalysts |
| **JPMorgan Chase (JPM)** | Lead Analyst | BUY / NEUTRAL / SELL | $XXX.XX | +XX.X% | Thesis & Catalysts |
| **Morgan Stanley** | Lead Analyst | BUY / NEUTRAL / SELL | $XXX.XX | +XX.X% | Thesis & Catalysts |

## Compliance Rules
- Must track top bulge-bracket investment bank ratings (BofA, Goldman Sachs, JPMorgan, Morgan Stanley, Barclays).
- Must calculate exact distance (%) from live execution price to Bank Price Target.
- Must verify 13F institutional ownership percentages for major holdings.
- No unescaped LaTeX math characters (`$...$` or `$$...$$`) inside markdown tables or text.
