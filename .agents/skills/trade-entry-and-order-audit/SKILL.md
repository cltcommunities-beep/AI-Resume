---
name: trade-entry-and-order-audit
description: >-
  Audits stock trade setups, limit order staging, dip-buys vs falling knives,
  debt/dilution traps, Friday S1 de-grossing traps, ecosystem contagion, and
  1% risk sizing. Use whenever the user asks "should I buy?", "check my order",
  "stage a limit order", "sell or trim", or "is this a dip or falling knife?".
---

# 💰 Task 2 Skill: Trade Entry, Limit Staging & Order Audit (MVVMC ViewModel)

Execute these **4 Sequential Gates** before recommending or placing any buy, sell, or limit order on Account `••••3782` (`868333782`). **No confirmation = No trade (`$0.00` freeze).**

## Gate 1: Macro & Opening-Clock Veto
* Verify Today's Weather Light, Core Calendar Gate (`72h` Tier 1 freeze), Weekly Catalysts, and Active Macro Pressure Gauges (`10Y >= 5.0%`, `VIX >= 25`, Brent Oil).
* Enforce **`9:30–9:45 AM ET` Opening Ban** & **`10:30 AM ET` Cutoff** (`9:45–10:30 AM ET` confirmed setup window only).
* Linked Rules:
  * [mandatory_pre_investment_market_audit_gate_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_investment_market_audit_gate_rule.md)
  * [mandatory_macro_tide_absolute_veto_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_macro_tide_absolute_veto_rule.md)
  * [mandatory_macro_market_down_pressure_signals_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_macro_market_down_pressure_signals_rule.md)
  * [mandatory_intraday_reality_and_morning_dip_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_intraday_reality_and_morning_dip_rule.md)
  * [weekly_market_moving_catalysts_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/weekly_market_moving_catalysts_table_rule.md)
  * [macroeconomic_catalysts_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/macroeconomic_catalysts_rule.md)

## Gate 2: Upfront Dealbreakers, Past/Future Announcements, Government Impact & Debt/Dilution
* **Every-Penny Audit Mandate:** Even for `$1` fractional buys, run the **1-Glance 4-Pillar Check** (Past Announcements & Stock Reaction, Future Catalysts, CapEx/Growth Self-Funding vs. Dilution, and Government/Tariff/Regulatory/Fed Impacts).
* List Upfront "Why NOT to Invest" red flags first, run the **3-Gate Forensic Debt & Dilution Audit** (ATM/S-3 shelves, `>12%` distressed yields, `>15%` interest burden), and audit **3 Ecosystem Links** (Upstream `NVDA`/`TSM` -> Downstream `MSFT`/`META` -> 72h Direct Competitors).
* Linked Rules:
  * [mandatory_pre_recommendation_news_and_divergence_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_recommendation_news_and_divergence_audit_rule.md)
  * [mandatory_why_not_to_invest_bullet_points_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_why_not_to_invest_bullet_points_rule.md)
  * [mandatory_debt_and_dilution_forensic_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_debt_and_dilution_forensic_audit_rule.md)
  * [mandatory_stock_dependency_competition_and_basket_contagion_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_stock_dependency_competition_and_basket_contagion_rule.md)

## Gate 3: Technical Setup, Dip vs. Falling Knife & Trap Shield
* Validate **Buy the Dip vs. Falling Knife (5 Rules)**, ban mid-air buying (`>3%` above `20MFA` / `>5%` above `50MFA`), block pre-catalyst **Friday S1 Traps** (`S2`/`0.65` Golden Pocket only), protect against `all_day_hours` stop-hunts, and fade headline pops into R1/R2 walls.
* Linked Rules:
  * [buy_the_dip_vs_falling_knife_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buy_the_dip_vs_falling_knife_rule.md)
  * [mandatory_great_company_wrong_price_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_great_company_wrong_price_rule.md)
  * [mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_friday_pre_catalyst_degrossing_and_s1_trap_rule.md)
  * [headline_spike_fade_and_dynamic_harvest_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/headline_spike_fade_and_dynamic_harvest_rule.md)
  * [mandatory_dual_scenario_technical_matrix_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_dual_scenario_technical_matrix_rule.md)
  * [mandatory_retail_trap_and_stop_hunt_protection_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_retail_trap_and_stop_hunt_protection_rule.md)
  * [best_stocks_roster_and_entry_timing_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/best_stocks_roster_and_entry_timing_rule.md)

## Gate 4: Position Sizing & Live Broker Confirmation
* Enforce `1%` account risk allocation, `>= 2:1` R:R ratio, staggered `25%–33%` tranches, and **explicit user approval before any live `place_*_order`**.
* Linked Rules:
  * [mandatory_elite_execution_and_structural_safeguards_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_elite_execution_and_structural_safeguards_rule.md)
  * [mandatory_agentic_investment_rules.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_agentic_investment_rules.md)
  * [7_risk_management_principles_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/7_risk_management_principles_rule.md)
