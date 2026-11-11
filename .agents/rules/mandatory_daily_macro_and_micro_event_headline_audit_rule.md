---
trigger: always_on
description: Mandatory Daily Macro-Economic Data Release (Actual vs. Expected) and Micro-Company Event/Headline Dual-Audit Rule for Every Stock Analysis and Investment Decision
---

# 🌐📰 MANDATORY RULE: DAILY MACRO-ECONOMIC DATA RELEASE & MICRO-EVENT HEADLINE DUAL-AUDIT STANDARD

## 🛑 Executive Directive (Applies Every Day to Every Stock Analysis & Trade Decision)
Whenever the user invokes `/mcp:robinhood:stock-analysis`, `/mcp:robinhood:portfolio-review`, `/mcp:robinhood:market-overview`, or asks to analyze, check, or invest in **ANY stock (`[TICKER]`)**, the assistant is **STRICTLY PROHIBITED** from checking only stock prices or only company-level news in isolation.

Every single day, stock prices are driven by the collision of **TWO daily forces**:
1. **🌐 Daily Macro-Economic Data Releases (`8:30 AM / 10:00 AM / 2:00 PM EST`):** Same-day economic numbers (`Core CPI`, `Headline CPI`, `PPI`, `Core PCE`, `Initial Jobless Claims`, `Non-Farm Payrolls`, `GDP`, `ISM PMI`, `10-Year Treasury Yield`, and `FOMC / Fed Speakers`) where **`Actual vs. Expected`** dictates whether the entire market (`SPY`/`QQQ`) rallies or sells off.
2. **📰 Daily Micro Company-Specific Events & Headlines:** Same-day company headlines (`Analyst Price Target Cuts/Upgrades`, `Board/Regulatory Probes`, `Export Controls`, `New Customer Contracts`, `Dilution Filings`, and `Same-Day / 72-Hour Peer Earnings`).

Before outputting **any** stock analysis or investment plan, the assistant **MUST UNCONDITIONALLY** execute **THREE orthogonal, unbiased live web searches** in that turn (never cramming old-topic keywords into breaking-news queries) and synthesize them into the **4-Gate Daily Macro + Micro Event Scorecard**.

---

## 🏛️ 1. The 3 Mandatory Unbiased Parallel `search_web` Queries (Nov 11 Reuters H200 Post-Mortem Upgrade)

**🚨 Why 3 Orthogonal Queries Are Mandatory:** Cramming specific terms (like `"analyst price target"` or `"House letter"`) into a breaking-news query creates **Search Confirmation Bias** and hides orthogonal breaking wire scoops (such as Reuters export-control or PLA military procurement investigations). Every stock news audit MUST run three cleanly separated, unbiased searches:

### Query A: 🌐 Same-Day Macro Economic Release Audit (`Actual vs. Expected`)
* **Search Pattern:** `"US economic data release today CPI PPI jobless claims PCE Fed actual vs expected [Current Month Day Year]"`
* **What Must Be Verified & Stated:**
  1. What 8:30 AM EST or 10:00 AM EST economic data was released today? (e.g., **Core CPI `0.3%` Actual vs. `0.2%` Expected**; **Headline CPI `0.4%` Actual vs. `0.3%` Expected**).
  2. Did the data **Beat (Cooler/Bullish)**, **Meet (In-Line)**, or **Miss (Hotter/Bearish)** consensus expectations?
  3. How is the macro print impacting **10-Year Treasury Yields**, **Gold (`IAU`)**, and the broad indices (**`SPY` / `QQQ` / `IWM`**)?

### Query B: 📰 Pure Unfiltered Wire Breaking News (`Reuters / Bloomberg / FT / CNBC`)
* **Search Pattern:** `"[Company Name]" OR "[TICKER]" Reuters Bloomberg FT CNBC breaking news [Current Month Day Year]` *(Keep free of narrow topic adjectives so major wire scoops rank first).*
* **What Must Be Verified & Stated:**
  1. **Top-Tier Wire Scoops:** Any breaking Reuters, Bloomberg, WSJ, or FT investigative pieces over the last 24–48 hours.
  2. **Wall Street Analyst Actions Today:** Did any investment bank raise or cut its price target or rating today?
  3. **Today & 72-Hour Earnings Contagion:** Does the stock or its direct competitor (`CRWV` <-> `NBIS`) report earnings today or within 72 hours?

### Query C: 🛡️ Adversarial, Regulatory, Export-Control & Supply-Chain Sweep
* **Search Pattern:** `"[Company Name]" OR "[TICKER]" export China military DOJ SEC investigation lawsuit delay Reuters [Current Month Year]`
* **What Must Be Verified & Stated:**
  1. Government blacklists, third-party reseller / grey-market leaks (e.g., PLA-linked university procurement), DOJ/SEC subpoenas, or Congressional probes.
  2. Supply-chain bottlenecks, customer delays, or product defect headlines.

---

## 📋 2. Mandatory 4-Gate Daily Macro + Micro Event Scorecard Table

Every stock analysis MUST render this **4-Gate Daily Macro + Micro Event Scorecard Table** before giving any buy/sell/hold price target:

| Daily Audit Gate | Live Source Checked Today | Verified Today's Data / Headline (`Actual vs. Expected`) | Impact on Stock & Action Verdict |
| :--- | :--- | :--- | :---: |
| **1. 🌐 Today's Macro Data Release** | `search_web` (8:30 AM / 10:00 AM Data) | State exact print: e.g., `Core CPI 0.3% Actual vs 0.2% Expected` (`Headline 0.4% vs 0.3%`) | 🟢 Tailwind / 🔴 Macro Headwind |
| **2. 📉 Index & Yield Reaction** | `get_equity_quotes` (`SPY`, `QQQ`, `IWM`, `IAU`) | Compare `[TICKER]` % move vs `SPY`/`QQQ` % move (`≥1.5%` Divergence Check) | 🟢 In-Line / 🔴 Divergence Siren |
| **3. 📰 Today's Micro Stock Headlines** | `search_web` (`[TICKER]` Today) | Explicit summary of today's analyst PT changes, probes, contracts, or dilution | 🟢 Clean / 🟡 Noise / 🔴 Veto |
| **4. ⏰ Same-Day & 72h Binary Events** | `get_earnings_results` + Live Web | Exact time of today's/upcoming earnings, peer reports (`CRWV`/`NBIS`), or deadlines | 🟢 Clear / 🔴 72h Binary Freeze |

---

## 🛡️ 3. The 3 Automatic Execution Rules Based on Daily Macro + Micro Events

1. **Rule 1 — The "Hot Macro Print" Day-1 Digestion Law (e.g., Core CPI `0.3%` > `0.2%` Expected):**
   * Whenever a major 8:30 AM inflation or jobs report misses expectations (hotter CPI/PPI/PCE or spiking yields), algorithms spend the regular session (`9:30 AM – 4:00 PM EST`) repricing valuations downward.
   * **Strict Directive:** Never chase pre-market or opening-bell prices on a hot CPI/PPI day. Let the macro sell-off push target stocks down to **S1 / S2 / S3 support floors**, and either stage deep limit traps or wait until the next morning (`Day 2`) once the macro shock is fully digested.
2. **Rule 2 — Analyst Price Target Cut vs. Live Price Reality Filter:**
   * When an analyst trims a price target (e.g., Wells Fargo trimming `NVDA` from `$315` to `$300`, or Mizuho to `$250` while the stock trades at `$174`), always calculate the **Remaining Upside % to the New Target** (`($250 - $174) / $174 = +43.6%`) vs. when an analyst cuts a target *below* the user's cost basis (e.g., Morgan Stanley cutting `APLD` from `$41` to `$25` on debt/dilution risk).
3. **Rule 3 — Combined Macro + Micro Discount Harvesting:**
   * The single best institutional buying opportunities occur when a **temporary macro dip** (like a `0.3%` Core CPI pullback) coincides with **temporary micro headline noise** on a debt-free monopoly (`NVDA` or `NBIS`), pushing the stock right onto multi-month channel support (`S1`/`S2`) right before our scheduled execution day!

