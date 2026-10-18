---
trigger: model_decision
---

# PRE-MARKET NEWS SCANNER EXCLUSION RULE

## Directive
When executing the daily 8:15 AM EST Pre-Market High-Surging News Scanner, the assistant and background scripts MUST EXCLUDE all existing portfolio holdings (`GOOG`, `NFLX`, `SECZ`, `UAMY`, `SIDU`, `ASTS`, `SPCX`, `XE`, `INTC`, `ET`).

## Purpose
The Pre-Market News Scanner is dedicated exclusively to discovering NEW external high-surging stocks across the broader market gapping >10% with >1M pre-market volume on fresh corporate news catalysts (SEC 8-K filings, FDA approvals, contract wins).

## Implementation
1. Maintain an active exclusion set of current portfolio ticker symbols.
2. Filter out any pre-market gapper matching a ticker in the portfolio exclusion set.
3. Deliver pre-market Telegram news alerts ONLY for newly discovered external stocks.
