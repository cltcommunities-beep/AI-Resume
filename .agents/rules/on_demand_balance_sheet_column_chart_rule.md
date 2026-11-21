---
trigger: model_decision
description: On-Demand Balance Sheet Column Chart Standard — Render an interactive HTML5 Canvas Balance Sheet Column Chart (<agent-embed>) ONLY when the user explicitly requests a balance sheet chart or balance sheet column chart
---

# 📊 ON-DEMAND RULE: BALANCE SHEET COLUMN CHART STANDARD (RENDER ONLY WHEN EXPLICITLY REQUESTED)

## 🛑 Executive Trigger Directive (Strictly On-Demand — Never Auto-Render!)
1. **Strict On-Demand Gate:** The assistant must **ONLY** build and embed the **Balance Sheet Column Chart (`<agent-embed>`)** when the user **explicitly asks** for a balance sheet chart, balance sheet column chart, or solvency bar/column visual (e.g., `"balance sheet chart for [TICKER]"`, `"[TICKER] balance sheet column chart"`, `"show balance sheet columns"`).
2. **Zero Unsolicited Clutter on Price Chart Requests:** When the user asks for a normal stock chart (e.g., `"NVDA chart"`, `"SOFI chart"`, `"ANT chart"`), do **NOT** auto-generate the balance sheet column chart widget—keep normal stock chart requests focused on the 4-Timeframe Price/L2/Options Hybrid Chart and the tabular solvency summaries.

---

## 🏗️ 1. MVVM + MVVMC + Protocol-Oriented DI Architecture (When Triggered)

Whenever the user requests a Balance Sheet Column Chart for `[TICKER]`, follow this modular architecture:
* **MVVMC Coordinator (`BalanceSheetChartCoordinator`):** Verifies explicit user intent, routes live Robinhood MCP + SEC 10-Q/10-K/S-1 data into the model, and selects the default column view.
* **Protocol Contracts:**
  * `BalanceSheetDataFetching`: Pulls `get_financials`, `get_sec_filing_facts`, `get_equity_fundamentals`, `get_equity_quotes`, plus live `search_web` verification of the latest 10-Q/10-K/S-1 balance sheet and diluted share count.
  * `SolvencyColumnCalculating`: Computes **Net Cash / (Net Debt)**, **F1/F2 Future Net Surplus (`Old Cash + FCF - Total Debt`)**, **Basic vs. Fully Diluted Fair Value per Share**, **Cash per Share**, **Debt per Share**, **Book Value per Share**, and the **3 Forensic Debt & Dilution Veto Gates** ([mandatory_debt_and_dilution_forensic_audit_rule.md](file:///Users/karthik/Desktop/AI%20Resume/.agents/rules/mandatory_debt_and_dilution_forensic_audit_rule.md)).
  * `ColumnChartRendering`: Draws clean, high-contrast grouped vertical columns on an HTML5 `<canvas>` (`<= 450px` total height, `>= 12px` font sizes, zero overlapping labels, value labels printed directly above every column, zero-line baseline for negative numbers like Net Debt or Operating Loss).

---

## 📊 2. The 4 Interactive Column Chart Modes Inside the Widget

Every On-Demand Balance Sheet Column Chart widget MUST include **4 interactive Column Mode tabs** + a **`🌓` Dark/Light theme button**:

1. **Tab 1: `Core Balance Sheet Columns ($B / $M)` (Default Active):**
   * Plots side-by-side vertical columns with exact dollar labels (`$B` or `$M`) printed above each bar:
     * **Column 1 — Total Cash & Short-Term Liquidity** (Emerald `#10b981`)
     * **Column 2 — Total Debt (`Short-Term + Long-Term Debt`)** (Rose `#f43f5e`)
     * **Column 3 — Net Cash / `(Net Debt)` Position** (Cyan `#06b6d4` if positive / Red `#ef4444` below zero line if negative)
     * **Column 4 — Operating Cash Flow (`OCF`) & Free Cash Flow (`FCF`)** (Blue `#3b82f6` / Teal `#14b8a6`)
     * **Column 5 — Total Assets vs. Total Liabilities vs. Stockholders' Equity** (Purple `#a855f7` / Amber `#f59e0b` / Indigo `#6366f1`)
     * **Column 6 — Next-12M Fixed Commitments & F1/F2 Net Surplus** (Slate/Gold)
2. **Tab 2: `Fixed Contracts: Inbound Customer RPO vs. Outbound Supplier Bills ($B & Years)`:**
   * Explicitly compares **how many years and dollars of fixed contracts customers are locked in to pay the company** (`Inbound RPO Backlog` & `Upfront Deferred Revenue`, with exact contract years e.g. `1–3 Yrs`) against **how many years and dollars of fixed contracts the company is locked in to pay suppliers/landlords** (`Next 12M Fixed Bills`, `4-Yr Fixed Bills`, `Partner-Specific Fixed Contracts` with exact years e.g. `7.25 Yrs / 10 Yrs`, and `Total Multi-Year Outbound Commitments` e.g. `19 Yrs through 2045`) plus the **Total Cash Pool** for visual coverage comparison.
3. **Tab 3: `Multi-Period Balance Sheet Trend (4Q / 3Y Columns)`:**
   * Grouped vertical columns across the last **4 Quarters (or 3 Fiscal Years)** comparing **Cash Pool vs. Total Debt vs. Revenue vs. Free Cash Flow (`FCF`)** so the user can see at a glance whether cash is compounding or burning.
4. **Tab 4: `Per-Share & Dilution Columns ($/Share)`:**
   * Vertical columns denominated in **`$/Share`**:
     * **Live Share Price (`$XX.XX`)**
     * **Basic Wall St Market Value (`Market Cap / Basic Shares`)**
     * **Fully Diluted Fair Value (`Market Cap / Fully Diluted Shares`)**
     * **Total Cash Per Share (`Cash / Shares`)**
     * **Total Debt Per Share (`Debt / Shares`)**
     * **Book Value Per Share (`Equity / Shares`)**

---

## 🛡️ 3. Mandatory 5-Row Widget Layout & Forensic Quality Gates

1. **Row 0 — Forensic Solvency Verdict Banner:** Displays **`🟢 FORTRESS BALANCE SHEET`**, **`🟡 LEVERAGED / DILUTION WATCH`**, or **`🔴 HARD FORENSIC VETO ($0.00)`** along with the 3 Forensic Gate results (**Gate 1:** Active ATM/Dilution `%`; **Gate 2:** Corporate Bond Yield `<8%` vs `>12%`; **Gate 3:** Quarterly Interest Expense as `%` of Revenue).
2. **Row 1 — Header Bar:** Ticker, Latest Filing Period (`Q3 2026 10-Q` / `S-1`), the 4 Column Mode Tabs (`Core Columns ($B)` | `Fixed Contracts (1–19 Yrs)` | `Multi-Period Trend` | `Per-Share & Dilution ($/sh)`), and `🌓`.
3. **Row 2 — 5-Pillar KPI Strip:** `Total Cash` · `Total Debt` · `Net Cash/(Debt)` · `TTM/9M FCF & Interest Coverage` · `Basic vs. Diluted Shares (±% Dilution Gap)`.
4. **Row 3 — Interactive HTML5 Canvas Column Chart + Floating Plain-English Tooltip Card:**
   * High-DPI canvas where hovering ANY column pops up a **large, high-contrast Floating Plain-English Tooltip Card right next to the column** (AND updates a bold bottom explanation banner) using **zero accounting jargon**.
   * **Mandatory 3-Line Simple-English Format for Every Column:**
     1. **`What This Money Is:`** Everyday explanation (e.g., *"Money already in the bank before IPO"*, *"Bills owed to lenders"*, *"Actual cash profit left over"*).
     2. **`Why It Is Good or Bad:`** Clear 1-sentence verdict (e.g., *"🟢 HUGE PLUS: 36x more cash than debt — zero bankruptcy risk!"* or *"🟡 CAUTION: Extra hidden shares lower true value to $64.70"*).
     3. **`Simple Rule for You:`** Direct takeaway for Account `••••3782`.
5. **Row 4 — Masked Account `••••3782` Footer & Mandatory Pre-Embed Verification:**
   * Must follow all HTML/JS safety rules (no `:root` override, no JS template backticks, fresh filename, macOS `jsc` syntax validation exit `0`, and no `height` attribute on `<agent-embed>`).
