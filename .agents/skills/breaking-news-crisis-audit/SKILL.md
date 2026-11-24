---
name: breaking-news-crisis-audit
description: >-
  Executes 3 orthogonal unbiased live web searches, triggers >=1.5% index
  divergence sirens, enforces 3-day scandal stabilization freezes & order
  purges, and audits historical crisis analogs. Use when checking drops or news.
---

# 📰 Task 5 Skill: Breaking News, Divergence & Crisis Audit (MVVMC ViewModel)

Use this skill whenever any stock moves sharply (`>= 1.5%` divergence vs. `SPY`/`QQQ`), faces a headline/lawsuit/probe, or requires fresh daily macro + micro news verification. **Never rely on price quotes alone for news!**

## Step 1: Run 3 Orthogonal Live `search_web` Queries (Anti-Bias Protocol)
* **Query A (Same-Day Macro):** `Actual vs. Expected` for CPI, PPI, Core PCE, Claims, NFP, GDP, PMI, Fed Speakers.
* **Query B (Unfiltered Wire Scoops):** Reuters, Bloomberg, FT, CNBC, WSJ headlines free of narrow topic bias + analyst PT cuts & 72h peer earnings.
* **Query C (Adversarial, CapEx & Government Sweep):** Export controls, tariffs, CHIPS/DOE/NRC subsidies or approvals, DOJ/SEC/Congress probes, lawsuits, CapEx/guidance cuts, S-3/ATM dilution, Hormuz oil/geopolitics.
* Render the **1-Glance 4-Row Every-Penny Impact Card** (Past Announcements + Stock Impact, Future Catalysts, CapEx/Growth Funding, Government/External Impact) cleanly without clutter.
* Linked Rules:
  * [mandatory_daily_macro_and_micro_event_headline_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_daily_macro_and_micro_event_headline_audit_rule.md)
  * [mandatory_pre_recommendation_news_and_divergence_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_recommendation_news_and_divergence_audit_rule.md)
  * [breaking_market_headlines_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/breaking_market_headlines_table_rule.md)
  * [mandatory_live_search_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_live_search_rule.md)
  * [premarket_news_exclusion_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/premarket_news_exclusion_rule.md)
  * [strait_of_hormuz_geopolitical_monitor_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/strait_of_hormuz_geopolitical_monitor_rule.md)

## Step 2: 3-Day Escalating Scandal Freeze & Historical Analog Precedent
* If a Day-1/Day-2 probe, CEO scandal, or escalating multi-part whistleblower/Congressional shock ("Cockroach Theory") triggers, enforce an immediate **`$0.00` 3-Day Freeze** AND recommend purging resting GTC buy orders immediately.
* Search past historical analogs (comparable CEO ousters, DOJ/SEC investigations, restatements) before issuing any Hold/Trim/Buy verdict.
* Linked Rules:
  * [mandatory_escalating_scandal_and_resting_order_purge_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_escalating_scandal_and_resting_order_purge_rule.md)
  * [mandatory_historical_precedent_analog_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_historical_precedent_analog_audit_rule.md)
