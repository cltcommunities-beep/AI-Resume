---
trigger: model_decision
description: >-
  ON-DEMAND ONLY — Standalone 15-Section Stock Investment Checklist Rule. Use
  STRICTLY when the user explicitly wants to evaluate a stock to invest in
  (e.g., "I want to invest in [TICKER]", "should I invest in [TICKER]",
  "run the Stock Investment Checklist on [TICKER]", or full pre-investment
  research). NEVER trigger or load on daily regular market updates, quick
  price/news checks, breaking headlines, order checks, or general chat.
---

# ✅ ON-DEMAND RULE: 15-SECTION STOCK INVESTMENT CHECKLIST

## 🛑 Activation Boundary (Strict On-Demand — Zero Daily Clutter)
* **ACTIVATE ONLY WHEN:** The user explicitly states they want to **invest in a stock**, asks **"should I invest in `[TICKER]`?"**, or requests the **"Stock Investment Checklist"** for a specific ticker.
* **DO NOT ACTIVATE FOR:** Daily regular market check-ins (`"how is market?"`), quick price checks, single-day drop explanations, breaking geopolitical/macro headlines, routine order checks, or casual chat.
* **Zero Static Data Mandate:** NEVER use stale memory, hardcoded prices, or outdated financials. Pull **live Robinhood MCP** data (`get_equity_quotes`, `get_equity_fundamentals`, `get_financials`, `get_earnings_results`, `get_earnings_calendar`, `get_equity_analyst_ratings`, `get_sec_filing_index`, `get_sec_filing_facts`, `get_equity_historicals`, `get_equity_price_book`, `get_equity_technical_indicators`, `get_option_chains`) paired with **live `search_web`** verification in the active turn.
* **Zero Clutter Mandate:** Present all 15 sections in **one clean, scannable 15-Row Master Scorecard Table** (1–2 crisp bullets per row — never 15 long walls of text). Follow Tier 0 formatting: plain text only (zero LaTeX `$$` math blocks), backticked `$` prices, and masked account `••••3782`.

---

## 📋 The Mandatory 15-Section Stock Investment Checklist

Every time this rule is triggered for `[TICKER]`, audit **ALL 15 sections** in exact order using the live sources below and score each row `🟢 Strong`, `🟡 Mixed / Watch`, or `🔴 Red Flag`:

| # | Section | What to Analyze (Mandatory Scope) | Primary Live Data Sources |
| :-: | :--- | :--- | :--- |
| **1** | **Business Overview** | What does the company do? How does it make money (revenue segments & business model)? Who are its primary customers? | Robinhood `get_equity_fundamentals`, SEC 10-K/10-Q (`get_sec_filing_index`), live `search_web` |
| **2** | **Revenue & Earnings Growth** | YoY and quarterly revenue growth, EPS growth, gross/operating/net profit margins, beat/miss trend, and growth consistency across recent quarters. | Robinhood `get_financials`, `get_earnings_results`, `get_sec_filing_facts` |
| **3** | **Company-Specific Impact** | New contracts, backlog/RPO, customer wins or losses, product demand, production/supply capacity, and operational bottlenecks or business challenges. | Live `search_web` (`"[TICKER]" contracts backlog capacity demand`), latest earnings release |
| **4** | **Latest Innovation & Technology** | New products, R&D spend & pipeline, patents, AI developments, strategic partnerships, and recent or upcoming product launches. | Live `search_web` (`"[TICKER]" R&D new products AI partnership launch`), SEC 10-K |
| **5** | **Insider Activity** | Recent SEC Form 4 insider buying and selling, CEO/CFO/Director open-market transactions (vs. routine 10b5-1 sales), and management ownership stake. | Live `search_web` (`"[TICKER]" SEC Form 4 insider buying selling CEO CFO`) |
| **6** | **Institutional Investors** | Major hedge funds, mutual funds, top institutional holders, recent ownership accumulation/reductions, and latest SEC 13F filing shifts. | Live `search_web` (`"[TICKER]" 13F institutional ownership hedge fund buying selling`) |
| **7** | **Financial Health** | Operating cash flow (OCF), cash & short-term reserves, total/net debt, debt maturity/interest burden, operating margins, CapEx vs. OCF, and Free Cash Flow (FCF). | Robinhood `get_financials`, `get_sec_filing_facts` (Cash, Debt, OCF, CapEx, FCF) |
| **8** | **Competitive Position** | Direct competitors, market share, pricing power, switching-cost or tech moats, competitive advantages, and industry ranking. | Live `search_web` (`"[TICKER]" competitors market share moat pricing power`) |
| **9** | **Industry & Market Trends** | Is the underlying industry structurally growing or shrinking? Key secular tailwinds, TAM expansion, cycle phase, and emerging opportunities. | Live `search_web` (`"[Industry]" market growth trends TAM outlook`) |
| **10** | **Macroeconomic Impact** | Interest rates (`10Y` yield / Fed path), inflation (`PPI`/`CPI`/`Core PCE`), government policies, tariffs/export controls, FX/currency exposure, and broader economic conditions. | Live Robinhood macro quotes (`SPY`/`QQQ`/`TLT`/`VIX`), live `search_web` (`"[TICKER]" tariffs government policy rates macro`) |
| **11** | **Valuation** | Trailing P/E, Forward P/E, PEG ratio, Price-to-Sales (P/S), EV/EBITDA, **Wall St Market Value (`Market Cap / Shares Outstanding`, diluted if `> 3%`)**, and side-by-side comparison with 2–3 direct competitors. | Robinhood `get_equity_fundamentals`, `get_equity_quotes`, live `search_web` peer multiples |
| **12** | **Future Growth Catalysts** | Upcoming earnings dates, product releases, contract milestones, capacity/geographic expansion, and scheduled company or government events. | Robinhood `get_earnings_calendar`, live `search_web` (`"[TICKER]" upcoming catalysts roadmap guidance`) |
| **13** | **Risks & Red Flags** | Active lawsuits, regulatory/DOJ/SEC/Congress probes, customer concentration (`> 30%` single buyer), share dilution / ATM shelves, heavy debt, or declining demand. | Live `search_web` (`"[TICKER]" lawsuit probe risk dilution downgrade`), SEC 10-K/10-Q Risk Factors |
| **14** | **Analyst Expectations** | Consensus EPS & revenue estimates, Wall St Buy/Hold/Sell split, low/median/high price targets, and recent investment bank upgrades, downgrades, or target cuts. | Robinhood `get_equity_analyst_ratings`, live `search_web` (`"[TICKER]" analyst price target upgrade downgrade`) |
| **15** | **Stock Performance & Market Sentiment** | Live price vs. 52-week range & moving averages (`20`/`50`/`200`), relative performance vs. `SPY`/`QQQ`, RSI, volume & Level-2 bid/ask walls, options IV / Put-Call skew, and overall crowd/news sentiment. | Robinhood `get_equity_quotes`, `get_equity_historicals`, `get_equity_technical_indicators`, `get_equity_price_book`, `get_option_chains` |

---

## 🎯 Required Output Format (Clean, Fast-to-Read Decision Structure)

When this rule runs, deliver the response in this exact compact order (on top of the Tier 0 Top Weather Box & 5 `🟢` Green Points + Macro Calendar Gate Table):

1. **📊 15-Section Stock Investment Scorecard (`[TICKER]`):**
   * Render one clean 4-column table: `| # | Section | Live Verified Snapshot (Plain English) | Rating |` covering Sections `1` through `15` with `🟢` / `🟡` / `🔴` ratings.
   * Show the **Checklist Score Summary** directly beneath: `Score: X / 15 Green · Y / 15 Yellow · Z / 15 Red` (plus explicit **Dealbreaker Override** check: any severe active scandal, distressed debt, active ATM dilution, or 🔴 Storm macro veto overrides a high score and enforces `$0.00` wait).
2. **⚖️ Fair Split Investment Verdict (`Existing Shares` vs. `New Cash`):**
   * **Existing Shares Held (`••••3782`):** Clear `HOLD` / `TRIM` / `STOP-LOSS` call.
   * **New Cash Deployment:** Clear `BUY (Staged)` / `WAIT FOR FLOOR` / `$0.00 FREEZE` call with exact support levels (`S1` / `S2` / `S3`), respecting the `9:45–10:30 AM ET` confirmed window and Macro Calendar Gate.
3. **🟢 GREEN BULLETS (To Follow) & 🔴 RED BULLETS (NOT to Follow):**
   * State **`Live Price`** right beside **`Wall St Market Value`** (`Market Cap / Shares Outstanding`, noting diluted adjustment if `> 3%`).
4. **🧸 Simple Kid-Level Summary (30-Second Story):**
   * 3 short bullets answering: (1) Current market weather, (2) Is this company strong or broken?, and (3) Exact simple move right now.
