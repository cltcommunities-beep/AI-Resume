---
trigger: always_on
description: Universal Mandatory Pre-Recommendation Live News Search, Relative Divergence Alarm, and Past/Future Catalyst Audit Rule for ALL Stocks
---

# 🚨 UNIVERSAL MANDATORY RULE: PRE-RECOMMENDATION LIVE NEWS, DIVERGENCE & PAST/FUTURE CATALYST AUDIT (APPLIES TO ALL STOCKS)

## 🛑 Executive Directive (100% Generic — Applies to Every Stock on the Market)
This rule applies **universally and generically to EVERY SINGLE STOCK (`[ANY_TICKER]`)** across the entire market whenever any stock is discussed, evaluated, compared, or considered for buying, selling, or holding.

The assistant is **STRICTLY PROHIBITED** from naming, ranking, or suggesting **ANY stock** as a "Buy Candidate" or "Recommendation" by relying solely on broker price quotes (`get_equity_quotes`) or historical fundamental memory. Price tools only return numbers—they do **NOT** return breaking news, investigations, lawsuits, or forward event risks.

Before recommending, evaluating, or proposing **ANY stock ticker**, the assistant **MUST UNCONDITIONALLY** execute a live web search (`search_web`) in that exact same turn to audit both the **Past News** and **Future Fixed-Date Catalysts**. **ZERO EXCEPTIONS PERMITTED.**

---

## 🏛️ The 4 Universal Laws for Every Stock Analysis or Recommendation

For **ANY stock ticker (`[TICKER]`)** discussed or considered for investment, the assistant MUST execute these 4 steps **before** outputting any recommendation:

### 1. 🔍 Mandatory Live `search_web` News Audit (Every Stock, Every Turn)
* Broker quote APIs (`get_equity_quotes`) provide prices only—never news.
* Before suggesting or analyzing **any stock (`[TICKER]`)**, the assistant MUST execute an independent live `search_web` call:
  `"[TICKER] stock breaking news why dropping OR rising catalysts [Current Month Year]"`
* Relying on prior-turn context, static memory, or past reputation ("this is a great company") without a fresh live news search is an automatic rule violation.

### 2. 🚨 The Universal ≥1.5% Index Divergence Siren
* For **every stock** checked, the assistant must calculate its real-time percentage move relative to the broad market (`SPY` and `QQQ`):
  `Relative Divergence = Stock % Change - Market Index (SPY or QQQ) % Change`
* **Automatic Siren Trigger:** If any stock is underperforming `SPY` or `QQQ` by **≥1.5%** (for example, the market index is green/flat while the stock is down -2%, -3%, or -5%), the assistant MUST treat this as an **Active Company-Specific Shock Siren**.
* The assistant is strictly forbidden from calling a diverging drop a "normal technical dip to support" until it runs `search_web` and identifies the exact company-specific headline causing the divergence.

### 3. ⏪ Universal Past 7-Day Forensic News Audit (Why Did It Move?)
For **every stock** evaluated, the assistant must verify and explicitly state whether any of the following occurred in the **past 7 days**:
* Government, DOJ, SEC, Congressional, or Internal Board investigations, subpoenas, or regulatory probes
* Executive controversies, CEO/CFO resignations, or major insider selling
* Customer contract cancellations, tightened customer oversight, or order delays
* Analyst downgrades, price target cuts, or short-seller reports
* Share dilution filings (S-3 shelf registrations, ATM offerings, convertible debt)

### 4. ⏩ Universal Future 14-Day Fixed-Date & Catalyst Audit (What Is Coming Next?)
For **every stock** evaluated, the assistant must verify (via `get_earnings_results` AND `search_web`) and explicitly state all scheduled events in the **next 14 days**:
* Exact upcoming quarterly earnings date and timing (Pre-Market AM vs. Post-Market PM)
* Direct sector peer earnings occurring within the next 72 hours (sympathy sell-off risk)
* Regulatory, legal, or Congressional response deadlines and hearing dates
* Product launch deadlines, FDA/NRC milestones, or lockup expirations

---

## 📋 Mandatory Universal Pre-Recommendation Proof Table (4-Gate Macro + Micro Standard)

Whenever evaluating or proposing **ANY stock (`[TICKER]`)** as a buy, dip-buy, or reinvestment candidate, the assistant MUST render this standardized **4-Gate Macro + Micro Proof Table** before giving its verdict:

| Universal Audit Gate | Live Verification Source | Verified Finding for `[TICKER]` (Today's Macro + Past/Future Micro) | Clearance Verdict |
| :--- | :--- | :--- | :---: |
| **0. Today's Macro Data Release** | Live `search_web` (8:30 AM / 10:00 AM Data) | Exact `Actual vs. Expected` print (e.g., Core CPI `0.3%` vs `0.2%`, PPI, Jobs, Fed) | 🟢 Clear / 🔴 Macro Headwind |
| **1. Index Divergence Check** | `get_equity_quotes` vs `SPY`/`QQQ` | `[TICKER]`: X.XX% vs Index: Y.YY% (Divergence: Z.ZZ%) | 🟢 Clear / 🔴 Siren |
| **2. Past 7-Day & Today's Micro News** | Live `search_web` (Executed Now) | Explicit summary of today's analyst PT changes, probes, customer news, or dilution | 🟢 Clean / 🔴 Veto |
| **3. Next 14-Day Fixed Dates** | `get_earnings_results` + Live Web | Exact dates for earnings, peer reports (`CRWV`/`NBIS`), or legal/regulatory deadlines | 🟢 Safe / 🔴 Freeze |

---

## 🛡️ Automatic Capital Freeze Law ($0.00)
If the Universal Pre-Recommendation Audit for **ANY stock** reveals:
1. An active Day-1 or Day-2 investigation, regulatory probe, or governance scandal (Enforce the **3-Day Stabilization Rule**), OR
2. A fixed binary deadline (earnings report, peer earnings, or government deadline) within **72 hours**:

The assistant MUST automatically issue a **🔴 100% CAPITAL ALLOCATION FREEZE ($0.00)** on that stock until the event or 3-day window passes.
