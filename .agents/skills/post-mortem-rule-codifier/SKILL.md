---
name: post-mortem-rule-codifier
description: >-
  Codifies new trading post-mortems into clean, non-redundant rules or skill
  references while enforcing Antigravity's 24 KB per-file cap, 20k-token
  always_on budget, and YAML trigger hygiene. Use when saving new lessons.
---

# 🔄 Task 6 Skill: Never-Repeat Rule Codifier & Budget Gate

Use this skill whenever the user or agent runs a market/trade post-mortem and needs to permanently codify a lesson without re-creating `always_on` budget overflow.

## Linked Governance Rule
* [mandatory_continuous_algorithm_update_and_calibration_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_continuous_algorithm_update_and_calibration_rule.md)

## Mandatory Codification Protocol
1. **Default to `trigger: model_decision` + Crisp `description:`:** Never mark a new narrow/domain rule `trigger: always_on`! Keep `always_on` reserved strictly for universal capital shields (`<= 5` rules, total combined with `AGENTS.md` `< 16,000` tokens).
2. **Route to the Right Task Module:** Link any new rule into the matching Task Skill under `.agents/skills/` (`stock-chart-builder`, `trade-entry-and-order-audit`, `earnings-valuation-deep-dive`, `portfolio-compounding-review`, or `breaking-news-crisis-audit`) and keep the file under `15 KB` (`24 KB` hard cap).
3. **Zero Static Prices in Rule Files:** Never save hardcoded portfolio share counts, cash balances, or spot prices inside `AGENTS.md` or rule files (`no_static_stock_prices_rule.md`).
4. **Run Budget & Hygiene Audit Script After Every Rule Edit:**
   ```bash
   python3 "/Users/karthik/Desktop/AI Resume/.agents/skills/post-mortem-rule-codifier/scripts/verify_task_wise_rules.py"
   ```
