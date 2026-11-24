---
name: stock-chart-builder
description: >-
  Builds, validates, and embeds interactive 9-Layer Stock/ETF charts, 5-Layer
  Broad Market charts (SPY/QQQ), and on-demand Balance Sheet Column charts. Use
  whenever the user asks for a chart (e.g., "NBIS chart", "BE chart", "market
  chart", "balance sheet chart") or when auditing technical zones and L2 walls.
---

# 📊 Task 1 Skill: Stock & Market Chart Builder (MVVMC ViewModel)

Follow this modular workflow strictly whenever generating or updating any chart artifact. Never reuse prose or price constants from another ticker's chart!

## Linked Institutional References & Contracts
* **Individual Stock 9-Layer & 6-Zone L2 Spec:** [stock_9layer_spec.md](./references/stock_9layer_spec.md)
* **Broad Market (`SPY`/`QQQ`) 5-Layer Macro Overlay:** [market_5layer_spec.md](./references/market_5layer_spec.md)
* **Core Workspace Chart Rules (`7` Rules Preserved):**
  * [mandatory_pre_investment_visual_chart_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pre_investment_visual_chart_rule.md)
  * [mandatory_chart_market_prediction_overlay_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_chart_market_prediction_overlay_rule.md)
  * [mandatory_pill_hover_and_zero_loss_chart_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_pill_hover_and_zero_loss_chart_rule.md)
  * [mandatory_chart_behavior_and_continuous_learning_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_chart_behavior_and_continuous_learning_rule.md)
  * [on_demand_balance_sheet_column_chart_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/on_demand_balance_sheet_column_chart_rule.md)
  * [robinhood_api_1week_candle_breakdown_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/robinhood_api_1week_candle_breakdown_rule.md)
  * [image_generation_style_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/image_generation_style_rule.md)

## Execution Steps

1. **Plan First (Rules 3 & 4):** Write/update a concise `<ticker>_chart_plan.md` artifact showing the MVVMC data-to-view flow before coding HTML.
2. **Ingest Live Data (`100%` Fresh — Zero Legacy Copying):**
   * Robinhood MCP: `get_equity_quotes` (`[TICKER]`, `SPY`, `QQQ`, `IWM`, `XLK`, `XLP`, `WMT`, `SGOV`, `SHY`, `TLT`, `HYG`, `IAU`, peers), `get_index_quotes` (`VIX`, `SPX`, `NDX`, Brent, Gold), `get_equity_historicals` (`minute/24_5`, `5minute/extended`, `day/year+`, `week/2y+`), `get_equity_fundamentals`, `get_financials`, `get_equity_price_book`, `get_option_chains` + `get_option_quotes` (`0D/1M/4M/7M/14M`), `get_earnings_calendar`, `get_earnings_results`, `get_equity_analyst_ratings`, plus `get_portfolio`/`get_equity_positions`/`get_equity_orders` (`868333782` masked as `••••3782`).
   * **3 Orthogonal `search_web` Queries:** (a) Same-day Macro + Upcoming 14-day Calendar/FedWatch/10Y, (b) Unfiltered Wire Breaking News, (c) Adversarial/Regulatory/Balance-Sheet Sweep.
3. **Compile & Isolate Ticker Data (Streamlined 4-Row Canvas Architecture):**
   * Store raw bars and computed levels (`SPOT`, `PREV_CLOSE`, `MKT_VAL`, `VWAP`, `PIVOT`, `SMA20/50/200`, `12M Gaps`, `HORIZONS`) in `<artifactDir>/scratch/<ticker>_bars_bundle.json`.
   * **Eliminated Bloat Standard:** Zero Row 0 Red Alert/Weather/Inflation banners, zero Row 1B Market Value banners, zero Row 2B Target Sliders/Preset buttons, and zero hardcoded prices in checkbox labels. All macro weather, calendar gates, and valuation multiples belong exclusively in the written text report, keeping the chart canvas clean, fast, and 100% focused on candlesticks, L2 order books, and interactive pill hovers.
   * Format strictly into 4 rows:
     * **Row 1:** Header & Horizon Bar (Ticker/Company pill, 4 Timeframe buttons, Live Price badge, View A/B/C tabs, Theme toggle).
     * **Row 2:** Clean Checkboxes & Coach Strip (Generic layer toggles without hardcoded price stamps, plus interactive coach tip).
     * **Row 3:** Interactive Views (View A Canvas with direct right-axis pill hover action popups; View B Simple 4-Step Graph; View C 4-Step plain-English card walkthrough).
     * **Row 4:** Account `••••3782` Footer (Masked holdings, cost basis, unrealized P&L, protective note).
   * Write to a fresh anti-cache filename (e.g., `<ticker>_live_9layer_clean_chart.html`) using `write_file` (`UserFacing: true`, `RequestFeedback: false`).
4. **Run Mandatory Validation Gate (`scripts/validate_chart_contract.py`):**
   * Run:
     ```bash
     python3 "/Users/karthik/Desktop/AI Resume/.agents/skills/stock-chart-builder/scripts/validate_chart_contract.py" "<chart.html>" "<TICKER>" --peers "<PEER1,PEER2>"
     ```
   * Enforces 8 strict checks: file existence, HTML/JS syntax via `jsc`, direct right-axis pill hover action dictionary, L2 order book wall badges, strict prohibition of foreign ticker price fingerprints (`FOREIGN_PRICE_SIGNATURES`), absolute price-range anomaly fence, and elimination of deprecated bloated banners/sliders.
5. **Embed Correctly (`generative_ui` Standard):**
   * Use `<agent-embed src="file:///..."></agent-embed>` ONLY — **NEVER** pass `file=`, `height=`, or `title=` attributes.
   * Pair with the clickable file link and full companion analysis (Weather Light, 4-Gate Scorecard, Macro Calendar Gate, 4 Structural Zones, Dual-Scenario/Peer Table, Split Fair Decision, Green/Red Bullets with `Live Price` beside `Wall St Market Value`, and 30s Kid Summary).
