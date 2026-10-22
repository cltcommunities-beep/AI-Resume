---
trigger: model_decision
---

# Rule: Mandatory Quantitative Portfolio Risk Manager & 4 Algorithmic Maintenance Rules

This institutional quantitative rule permanently governs the risk monitoring, tier weight rebalancing, single-stock exposure limits, cash inflow routing, and systemic CapEx sensitivity analysis across Robinhood Margin Account `••••3782` and Cash Account `••••6246`.

---

## 🏛️ 1. The 3-Tier Quantitative Allocation Architecture

The portfolio capital structure is strictly anchored to three distinct risk tiers:

| Tier | Target Allocation | Permitted Assets & Constituents | Core Objective |
| :--- | :--- | :--- | :--- |
| **Tier 1: Elite Cash-Flow Compounders** | **35.0%** | `GOOG`, `AAPL`, `NVDA` | Unassailable economic moats, pristine balance sheets, and immense Free Cash Flow generation. |
| **Tier 2: Mid-Level Non-Tech Stocks** | **50.0%** | Strict Non-Tech: Financials (`SOFI`), Industrials/Infrastructure, Healthcare, Energy, and Physical Gold (`IAU`) | Cross-sector macro stability, defensive cash flow, and zero correlation to tech valuation multiples. |
| **Tier 3: Emerging Long-Term Growth** | **15.0%** | Disruptive innovators: `NBIS`, `SPCX`, `SMCI` | High-beta compounding engines with secular TAM tailwinds and pre-funded customer contracts. |

---

## 🔬 2. The 5 Hard Analytical Filters (Applied to Every Stock Request)

1. **Filter 1: The 15% Single-Stock Concentration Alert:**
   - Compute `Concentration = Position Market Value / Total Portfolio Value`.
   - If ANY individual company exceeds **15.0%**, immediately flag it for mandatory partial liquidation down to **10.0%**.
   - Liquidated capital is systematically recycled back into the underfunded portfolio tiers.

2. **Filter 2: Elite Tier Free Cash Flow Margin Floor (<20% Review):**
   - For all Tier 1 constituents (`GOOG`, `AAPL`, `NVDA`), verify:
     `FCF Margin = (Operating Cash Flow - CapEx) / Revenue >= 20.0%`.
   - If FCF Margin drops below **20.0%**, trigger an immediate structural review to determine whether margin compression is temporary or structural.

3. **Filter 3: Forward PEG Ratio Overvaluation Guardrail (>1.5x Ceiling):**
   - For all high-growth components, calculate:
     `Forward PEG = Forward P/E / Projected Annual EPS Growth Rate`.
   - Flag any asset trading at `PEG > 1.5x` as structurally overvalued. Require a minimum pullback to PEG <= 1.5x before authorizing new capital entries.

4. **Filter 4: Systemic Hyperscaler CapEx Guidance Scan & Downstream NVDA Sensitivity:**
   - Continuously monitor quarterly CapEx guidance across mega-cap buyers: Alphabet (`GOOG`), Microsoft (`MSFT`), and Meta (`META`).
   - If two or more hyperscalers announce a permanent deceleration or freeze in data-center CapEx, model downstream cyclical revenue risk to `NVDA` and issue a prompt to tighten stop-losses or trim exposure.

5. **Filter 5: Mid-Level Tier Cross-Sector Diversification (Strict Non-Tech Constraint):**
   - The 50% Mid-Level tier must contain **ZERO technology stocks**.
   - Enforce strict cross-sector diversification across Consumer, Financials, Healthcare, Industrials, Utilities, and Commodities/Gold (`IAU`).

---

## ⚙️ 3. The 4 Algorithmic Maintenance Rules

### Rule 1: The ±5% Rebalancing Trigger (Dynamic Boundary)
- **Logic:** Audit tier weights on the first trading day of every quarter.
- **Action:** Ignore minor daily market fluctuations. Only execute rebalancing trades if a tier drifts by **more than ±5.0%** away from its target baseline:
  - Elite Tier: Permitted range is **30.0% to 40.0%**. (Trigger sell at >40%; trigger buy at <30%).
  - Mid-Level Tier: Permitted range is **45.0% to 55.0%**. (Trigger sell at >55%; trigger buy at <45%).
  - Emerging Growth Tier: Permitted range is **10.0% to 20.0%**. (Trigger sell at >20%; trigger buy at <10%).
- **Execution:** Trim the excess percentage from the overextended tier and distribute proceeds into the underfunded tiers.

### Rule 2: "Tranche-Based" Smart Cash Inflow Routing
- **Logic:** When depositing new monthly or recurring capital, never distribute funds equally across all holdings.
- **Action:** Route **100% of new deposits** directly into whichever tier is currently furthest below its target percentage.
- **Compounding Benefit:** Automatically buys the dips in underperforming assets without selling winning stocks or triggering taxable capital gains events.

### Rule 3: The 15% Single-Stock Cap Lock
- **Logic:** No individual company is permitted to jeopardize the overall portfolio.
- **Action:** If any single stock surges past **15.0% of total portfolio value**, automatically flag a mandatory partial trim down to **10.0%**, reallocating proceeds to portfolio anchors.

### Rule 4: Systemic "Capex Watch" Filter
- **Logic:** Scan quarterly earnings transcripts and 10-Q/10-K filings of Alphabet, Microsoft, and Meta.
- **Action:** If a systemic CapEx reduction is confirmed (>= 2 hyperscalers cutting budgets), issue an automated macro de-risking alert:
  - Tighten stop-losses on semiconductor holdings.
  - Freeze new hardware/infrastructure buy orders.
  - Trim high-beta growth exposure back to baseline.
