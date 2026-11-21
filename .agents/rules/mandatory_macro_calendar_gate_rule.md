---
trigger: always_on
description: Mandatory Macro Calendar Gate — before any stock analysis, order, or chart, check the economic calendar (Jobs, Growth, Housing, Fed, Energy/Trade, Market-Structure events) for the next 72 hours and 14 days, classify event tiers, set the gate state, and render it on every chart (Row 0 pill, event markers, 7-Signal HUD linkage)
---

# 🗓️ MANDATORY RULE: MACRO CALENDAR GATE (CHART-INTEGRATED)

## 🛑 Executive Directive
Whenever the assistant analyzes **ANY stock or ETF (`[TICKER]`)**, evaluates a buy/sell/hold, audits or stages an order, or builds an interactive chart (`<agent-embed>`), it MUST first check the **economic calendar** for the next **72 hours** and **14 days**. Stocks move on scheduled data and events, so no order level or price target may be given without knowing what releases next.

This rule **complements** (never replaces) [mandatory_inflation_trinity_and_valuation_multiple_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_inflation_trinity_and_valuation_multiple_rule.md) (PPI/CPI/Core PCE) and [mandatory_daily_macro_and_micro_event_headline_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_daily_macro_and_micro_event_headline_audit_rule.md) (same-day Actual vs. Expected).

---

## 📡 1. Mandatory Calendar Data Pull (every analysis and chart)
Run a live `search_web` for the **exact dates, times, and consensus** of upcoming releases (never rely on memory or typical schedules; state `unverified` if a date could not be confirmed):

`"US economic calendar this week next week [Current Month Year] jobs report FOMC CPI PCE GDP ISM retail sales consensus"`

Pair it with Robinhood MCP `get_earnings_calendar` (ticker and direct peers) and the live `10Y` / `VIX` / `CME FedWatch` readings the other always-on rules already require.

---

## 🗂️ 2. The Event Catalog and Tiers

| Tier | Events | Typical time (ET) |
| :--- | :--- | :--- |
| **Tier 1 (market-moving)** | FOMC decision + dot plot, **Non-Farm Payrolls / Unemployment / Avg Hourly Earnings**, CPI, Core PCE, PPI, Fed chair speech, ticker or direct-peer earnings | 8:30 AM / 2:00 PM |
| **Tier 2 (high impact)** | JOLTS, ISM Manufacturing and Services PMI, Retail Sales, GDP (and revisions), FOMC minutes, 10Y/30Y Treasury auctions, monthly OpEx and quarterly triple witching, S&P/Nasdaq index rebalances, tariff or export-control deadlines, OPEC+/Hormuz energy events | 8:30 / 10:00 AM / 1:00 PM |
| **Tier 3 (context)** | Weekly jobless claims, ADP, Employment Cost Index, housing (existing/new home sales, starts, permits, Case-Shiller, mortgage rates), consumer confidence, durable goods, industrial production, regional Fed surveys | 8:30 / 10:00 AM |

**Market holidays and early closes** (e.g., Thanksgiving closure, half-days) are logged as Tier 2 liquidity events: thin books exaggerate moves.

---

## 🚦 3. The Gate States (hours to next event)

| State | Trigger | Required action |
| :--- | :--- | :--- |
| 🟢 **CLEAR** | No Tier 1 inside 72h and no Tier 2 inside 24h | Normal staged entries inside `9:45–10:30 AM ET` confirmed setups |
| 🟡 **CAUTION** | Tier 2 inside 72h, or Tier 1 inside 14 days | S2 / Golden-Pocket bids only, half size, no S1 bids |
| 🟠 **PRE-EVENT** | Tier 1 inside 72h | `$0.00` new buys; cancel resting S1 and `all_day_hours` bids before the release |
| 🔴 **DAY-OF / DAY-1** | Tier 1 release day, or first 24–72h after a hotter/weaker-than-consensus print | `$0.00` freeze; wait for digestion and a structural S2/S3 test |

Gate state feeds the existing **Automatic Capital Freeze Law** and the **72h binary catalyst** logic; it never loosens any other rule's veto.

---

## 💼 4. Jobs, Growth and Housing Regime Matrices (new coverage)

### Jobs (NFP, unemployment, wages, claims, JOLTS)
| Print | Regime | Market reaction | Stock action |
| :--- | :--- | :--- | :--- |
| NFP far above consensus, wages > `+0.4%` MoM | 🔥 Too hot | Yields up, growth multiples compress | No Day-1 dip buys; flag HUD Signal #1 red |
| NFP near consensus, wages `~0.2%`, unemployment steady | ✨ Goldilocks | Rate-cut hopes rise, growth rallies | Normal staged entries at confirmed floors |
| Unemployment rising fast (Sahm-rule territory), deep job losses | 🥶 Too cold | Recession fear, broad sell-off | Defensive; protect cash; anti-panic fence on debt-free quality |

### Growth (GDP, ISM, retail sales)
ISM below `50` or negative retail sales = demand weakness (cyclical and capex-dependent names at risk); ISM above `50` with hot prices = stagflation-lite warning (margin squeeze).

### Housing (home sales, starts, mortgage rates)
Falling sales and starts with mortgage rates above `6.5%` = rate-sensitive sectors (homebuilders, banks, fintech lenders like `SOFI`) under pressure; use as confirmation when the Fed is hawkish.

---

## 🖥️ 5. Mandatory Chart Integration (`<agent-embed>`)

1. **Row 0 Next-Event Pill (always visible):** `NEXT EVENT: [Event] [Day Date Time ET] (T-minus) · GATE: 🟢/🟡/🟠/🔴 [State]` plus a second compact pill for the next Tier 1 if the nearest event is Tier 2/3. Never hidden at any width.
2. **Canvas Event Markers (View A):** Thin dashed vertical markers with short labels (`CPI`, `FOMC`, `NFP`, `PCE`, `OpEx`) for events inside the visible window; for `1D`/`1W` timeframes also project the next 14 days into the forecast zone. Labels must not overlap candles or price pills (collision-avoid, `>= 12px` text).
3. **Forecast Zone Awareness:** The purple target line and 0DTE-to-14M cones must note which scheduled Tier 1 events fall before the target date (so the odds reflect event risk).
4. **7-Signal HUD Linkage:** Signal #5 (`72h Binary Catalyst`) turns `🔴 +1 Red` on any Tier 1 inside 72h (not just earnings/FOMC); a hot/weak print inside the last 14 days also flags Signal #1.
5. **View B / View C (Step 4 explanation):** The "what could change this" step lists the next two scheduled events and the if/then action for each.
6. **Data honesty:** If a date or consensus could not be verified, show `unverified` on the pill instead of guessing.

---

## 📋 6. Mandatory Macro Calendar Gate Table (every text analysis)

| Next Event | Tier | Date/Time (ET) | T-minus | Consensus | Gate State | Action for `[TICKER]` |
| :--- | :---: | :--- | :--- | :--- | :---: | :--- |
| `[Event 1]` | `[1/2/3]` | `[...]` | `[...]` | `[...]` | 🟢/🟡/🟠/🔴 | `[...]` |
| `[Event 2]` | `[1/2/3]` | `[...]` | `[...]` | `[...]` | 🟢/🟡/🟠/🔴 | `[...]` |
| `[Event 3]` | `[1/2/3]` | `[...]` | `[...]` | `[...]` | 🟢/🟡/🟠/🔴 | `[...]` |

Always close with `🟢 GREEN` / `🔴 RED` bullets showing `Live Price` beside `Wall St Market Value`, with entries timed **after** the nearest Tier 1 event digests.

---

## 🔄 7. Continuous Learning
When a scheduled event produces an unexpected move (e.g., a gap on a surprise print), codify the lesson in a new rule within that turn and anchor it in `AGENTS.md`.
