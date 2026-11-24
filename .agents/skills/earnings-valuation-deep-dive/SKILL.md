---
name: earnings-valuation-deep-dive
description: >-
  Runs institutional earnings benchmarks, 5-pillar buy-side whisper audits,
  Dual Solvency Tables (5-Col + 17-Col), CapEx Reversal checks, Inflation Trinity
  multiple sensitivity, and 12-point due diligence. Use whenever analyzing
  earnings, fundamentals, balance sheets, FCF, or valuation of a stock.
---

# 🔬 Task 3 Skill: Earnings, Valuation & Solvency Deep-Dive (MVVMC ViewModel)

Use this skill whenever the user asks for a full fundamental deep-dive, earnings review, solvency audit, FCF/runway calculation, or valuation check.

## Module 1: Macro Multiple Sensitivity & Quarterly Earnings Audits
* Classify the **Inflation Trinity** (`PPI -> CPI -> Core PCE -> P/E Multiple Ceiling vs. Expansion`).
* Evaluate earnings against **ALL 5 Unofficial Stretch (Buy-Side Whisper) Pillars** (`EPS Whisper`, `Rev Whisper`, `Core Segment Whisper`, `Forward Gross Margin Floor`, `13-Week Organic Guide`) and render the **6-Column Institutional Earnings Benchmark Table**. Respect Post-Earnings Dip Discipline before buying earnings drops.
* Linked Rules:
  * [mandatory_inflation_trinity_and_valuation_multiple_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_inflation_trinity_and_valuation_multiple_rule.md)
  * [mandatory_unofficial_stretch_earnings_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_unofficial_stretch_earnings_rule.md)
  * [mandatory_6_column_institutional_earnings_benchmark_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_6_column_institutional_earnings_benchmark_rule.md)
  * [post_earnings_dip_discipline_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/post_earnings_dip_discipline_rule.md)

## Module 2: Dual Solvency Tables, Cash Fortress & Anti-CapEx Reversal
* Render **BOTH** the Compact `5-Column` Executive Solvency Summary Table AND the Full `17-Column` Solvency Audit Table (`Cap / Shares`, Diluted Fair Value, Cash, Debt, CapEx, Pre-Paid RPO, FCF, Dual Future Net Surplus, Share Dilution vs. Buybacks).
* Run the **5-Filter CapEx Reversal Screen** (`>50%` pre-paid CapEx, `CFO > CapEx`, Net Debt/EBITDA `< 2.0x`, asset-light software moat, `<= 30%` customer cap).
* Linked Rules:
  * [compact_solvency_summary_table_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/compact_solvency_summary_table_rule.md)
  * [master_stock_analysis_standard.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/master_stock_analysis_standard.md)
  * [mandatory_6_component_stock_analysis_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_6_component_stock_analysis_rule.md)
  * [mandatory_capex_reversal_trap_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_capex_reversal_trap_rule.md)
  * [dual_future_net_surplus_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/dual_future_net_surplus_rule.md)
  * [dual_moat_quant_and_cash_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/dual_moat_quant_and_cash_rule.md)
  * [fcf_and_new_cash_in_bank_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/fcf_and_new_cash_in_bank_rule.md)
  * [prepaid_contracts_mandate_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/prepaid_contracts_mandate_rule.md)
  * [share_dilution_and_buyback_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/share_dilution_and_buyback_audit_rule.md)
  * [future_business_growth_need_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/future_business_growth_need_rule.md)
  * [massive_cash_flow_monsters_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/massive_cash_flow_monsters_rule.md)

## Module 3: Scoring Models & Ownership Intelligence
* Score quality and convexity across the **5-Engine Growth Algorithm (`>=85/100` for Tier 1)**, **Buffett + Quant Hybrid**, **12-Point Due Diligence**, **4-Point Strength Gate**, **14-Layer AI Ecosystem (20MFA/50MFA)**, **SEC Form 4 / 13F**, and **Investment Bank Coverage**.
* Linked Rules:
  * [ultimate_high_conviction_growth_investing_algorithm_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/ultimate_high_conviction_growth_investing_algorithm_rule.md)
  * [buffett_and_quantitative_algorithm_hybrid_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/buffett_and_quantitative_algorithm_hybrid_rule.md)
  * [mandatory_brilliant_mind_mental_models_and_asymmetric_flywheel_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_brilliant_mind_mental_models_and_asymmetric_flywheel_rule.md)
  * [institutional_12_point_due_diligence_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/institutional_12_point_due_diligence_rule.md)
  * [four_point_fundamental_strength_gate_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/four_point_fundamental_strength_gate_rule.md)
  * [fourteen_layer_ai_ecosystem_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/fourteen_layer_ai_ecosystem_rule.md)
  * [mandatory_insider_and_hedge_fund_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_insider_and_hedge_fund_audit_rule.md)
  * [mandatory_investment_bank_tracking_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_investment_bank_tracking_rule.md)
