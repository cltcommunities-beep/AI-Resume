---
trigger: model_decision
description: Universal Mandatory Pre-Recommendation Live News Search, Relative Divergence Alarm, and Every-Penny Past/Future Announcement, CapEx/Growth & Government Impact Audit Rule for ALL Stocks
---

# 🚨 UNIVERSAL MANDATORY RULE: EVERY-PENNY PAST/FUTURE ANNOUNCEMENTS, GROWTH/INVESTMENT & GOVERNMENT IMPACT AUDIT (APPLIES TO ALL STOCKS)

## 🛑 Executive Directive (100% Generic — Applies to Every Penny & Every Stock)
This rule applies **universally and generically to EVERY SINGLE PENNY INVESTMENT (`$1` fractional, DCA, limit bid, or full tranche) and EVERY STOCK (`[ANY_TICKER]`)** whenever any stock is discussed, evaluated, compared, or considered for buying, selling, or holding.

The assistant is **STRICTLY PROHIBITED** from naming, ranking, or suggesting **ANY stock** as a "Buy Candidate" or "Recommendation" by relying solely on broker price quotes (`get_equity_quotes`) or historical fundamental memory. Price tools only return numbers—they do **NOT** return breaking announcements, CapEx burn shifts, government policy rulings, investigations, lawsuits, or forward event risks.

Before recommending, evaluating, or deploying even **one penny** on **ANY stock ticker**, the assistant **MUST UNCONDITIONALLY** execute a live web search (`search_web`) in that exact same turn to audit:
1. **Past Announcements & Real Stock Impact** (`7–30 days`),
2. **Future Announcements & Expected Catalyst Impact** (`14–90 days`),
3. **Company Investment (`CapEx/R&D`) & Growth Sustainability** (self-funded Cash vs. `5%`-yield debt/dilution), AND
4. **Government, Policy & External Impacts** (subsidies, contracts, tariffs/export controls, `NRC`/`FDA`/`DOE`/`SEC`/`DOJ` rulings, Fed rates, geopolitics, or anything else).

**Output Hygiene Law (Zero Clutter):** Present findings concisely in the **1-Glance 4-Row Summary Card** below so the user is never overwhelmed with walls of clumsy text. **ZERO EXCEPTIONS PERMITTED.**

---

## 🏛️ The 5 Universal Laws for Every Penny & Stock Evaluation

For **ANY stock ticker (`[TICKER]`)** discussed or considered for even `$1` of investment, execute these 5 checks **before** outputting any verdict:

### 1. 🔍 Mandatory Live `search_web` News Audit (Every Stock, Every Turn)
* Broker quote APIs (`get_equity_quotes`) provide prices only—never news.
* Before suggesting or analyzing **any stock (`[TICKER]`)**, execute independent live `search_web` calls covering past announcements, upcoming catalysts, CapEx/growth news, and government/policy impacts:
  `"[TICKER] stock announcements earnings guidance capex growth government policy news [Current Month Year]"`
* Relying on prior-turn context, static memory, or past reputation ("this is a great company") without a fresh live news search is an automatic rule violation.

### 2. 🚨 The Universal ≥1.5% Index Divergence Siren
* Calculate real-time percentage move relative to the broad market (`SPY` and `QQQ`):
  `Relative Divergence = Stock % Change - Market Index (SPY or QQQ) % Change`
* **Automatic Siren Trigger:** If any stock underperforms `SPY` or `QQQ` by **≥1.5%**, treat it as an **Active Company-Specific Shock Siren** and identify the exact headline before calling it a normal dip.

### 3. ⏪ Past Announcements & Actual Stock Impact Audit (`7–30 Days`)
For **every penny evaluated**, verify what the company, customer, Fed, or government recently announced AND **how the stock actually reacted**:
* Quarterly earnings, revenue/margin surprises, or lowered full-year guidance (and whether sellers trapped buyers)
* Major CapEx expansions, datacenter/factory delays (e.g., slippage into `2027`), or contract cancellations/wins
* Government/DOJ/SEC/Congressional probes, executive changes, insider selling, or analyst PT cuts
* Share dilution filings (`S-3` shelf registrations, `ATM` offerings, convertible debt)

### 4. ⏩ Future Scheduled Announcements & Expected Impact (`14–90 Days`)
Verify (via `get_earnings_results` / `get_earnings_calendar` AND `search_web`) all upcoming catalysts and their expected stock direction:
* Exact upcoming quarterly earnings date (Pre-Market AM vs. Post-Market PM) & direct peer earnings within `72h`
* Scheduled macro prints (`FOMC`, `CPI`, `Core PCE`, `NFP` Jobs) and `72h` binary freezes
* Product launches, `FDA`/`NRC`/`DOE` licensing milestones, customer ramp dates, or lockup expirations

### 5. 🏛️ Company Investment, Growth & Government / External Impact Audit
Before risking a single penny, explicitly verify:
* **Company Investment (`CapEx`) & Growth Engine:** Is the company growing organically AND funding its buildouts with **positive operating cash flow** (`NVDA`, `NVT`, `GOOG`), OR is it burning cash and risking **`5%`-yield debt/share dilution** (`NBIS`, `CRWV`, `APLD`, `OKLO`)?
* **Government & Policy Impacts (Tailwind vs. Headwind):** Check federal subsidies/grants (`CHIPS Act`, `DOE` loans, tax credits), regulatory approvals (`NRC` reactors, `FDA`), government contracts, **tariffs & chip export controls**, antitrust/DOJ actions, Fed rate policy (`~5%` yield gravity), and external shocks (Hormuz/energy, supply chains, or anything else).

---

## 📋 Mandatory 1-Glance Clean Proof Card (Zero Clutter Standard)

Whenever evaluating **ANY stock (`[TICKER]`)** for even `$1` of investment, render this **clean, scannable 1-Glance Table** before giving the Split Decision:

| Check Area | What Was Found (Plain English) | Impact on Stock | Verdict |
| :--- | :--- | :--- | :---: |
| **1. Past Announcements** *(7–30d)* | `[Key earnings/guidance/delay/contract + how stock reacted]` | `[e.g., Trapped overhead supply / Institutional support]` | 🟢 / 🟡 / 🔴 |
| **2. Future Announcements** *(14–90d)* | `[Next earnings, Fed/CPI/PCE dates, product/milestone dates]` | `[e.g., 72h Pre-Event Freeze / Post-Dec 10 catalyst]` | 🟢 / 🟡 / 🔴 |
| **3. Company Investment & Growth** | `[CapEx expansion, revenue/backlog trend & Cash Flow vs. Debt/Dilution]` | `[Self-funded Cash Monster vs. 5%-yield cash burn]` | 🟢 / 🟡 / 🔴 |
| **4. Government & External Impact** | `[DOE/NRC/CHIPS/Tariffs/Export bans/DOJ/Fed 5% yields/Macro]` | `[Tailwind vs. Delay/Tariff/Valuation ceiling]` | 🟢 / 🟡 / 🔴 |

*(Plus `Relative Divergence`: `[TICKER] X% vs. SPY/QQQ Y%` noted in 1 crisp line above or below.)*

---

## 🛡️ Automatic Capital Freeze Law ($0.00)
If the Universal Pre-Recommendation Audit for **ANY stock** reveals:
1. An active Day-1 or Day-2 investigation, regulatory probe, or governance scandal (Enforce the **3-Day Stabilization Rule**), OR
2. A fixed binary deadline (earnings report, peer earnings, or government deadline) within **72 hours**:

The assistant MUST automatically issue a **🔴 100% CAPITAL ALLOCATION FREEZE ($0.00)** on that stock until the event or 3-day window passes.
