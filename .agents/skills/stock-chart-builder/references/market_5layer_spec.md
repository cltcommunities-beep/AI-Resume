# 🌐 Broad Market Chart (`SPY` / `QQQ`) 5-Layer Institutional Macro Overlay (Task 1 Reference)

This reference preserves Section `2E` and Broad Market validation rules from `mandatory_pre_investment_visual_chart_rule.md`.

Whenever building a **Broad Market Chart** (default **`SPY`**, or **`QQQ`**), fetch all equity/index quotes (`SPY`, `QQQ`, `IWM`, `RSP`, `HYG`, `JNK`, `TLT`, `SHY`, `SGOV`, `UUP`, `GLD`, `USO`, `EFA`, `EEM`, `VUG`, `VTV`, `XLK`, `XLP`, `XLV`, `XLU`, `XLY`, `XLI`, `XLF`, `XLE`, `VIX`) plus live `search_web` macro internals, and unconditionally render **ALL 5 Institutional Broad Market Layers** inside the HUD, `#viewC`, and the companion text report:

| Broad Market Layer | Required Live Telemetry & Signals | Live Source |
| :---: | :--- | :--- |
| **1. 📊 Market Breadth & Internal Strength** | **Advance/Decline Line**, **% of S&P 500 Above 50-SMA & 200-SMA**, **52-Week Highs vs. 52-Week Lows**, and **`RSP` (Equal-Weight) vs. `SPY` (Cap-Weight)** relative performance. | Robinhood MCP (`RSP`, `SPY`) + live `search_web` |
| **2. 💵 Liquidity & Credit Stress** | **`2Y` & `10Y` Treasury Yields (`2s10s` spread)**, **`HYG` / `JNK` vs. `TLT` Credit Spreads**, **Fed Balance Sheet (`QE` vs. `QT` trend)**, and **Treasury Liquidity / TGA / RRP status**. | Robinhood MCP (`HYG`, `JNK`, `TLT`, `SHY`, `SGOV`) + live `search_web` |
| **3. 📉 Volatility & Sentiment** | **`VIX`**, **`VVIX`** *(vol-of-vol)*, **Equity/Index Put/Call Ratio**, **`VIX` Term Structure** *(Contango = calm vs. Backwardation = panic)*, and **CNN Fear & Greed Index**. | Robinhood MCP (`VIX`, `preview_scan` P/C) + live `search_web` |
| **4. 🌎 Global Market Confirmation** | **`DXY` (U.S. Dollar Index / `UUP`)**, **`GLD` (Gold)**, **`USO` (Oil / Brent-WTI)**, **`EFA` (Developed Intl)**, and **`EEM` (Emerging Markets)**. | Robinhood MCP (`UUP`, `GLD`, `USO`, `EFA`, `EEM`) + live `search_web` (`DXY`) |
| **5. 🔄 Market Leadership & Capital Rotation** | **`VUG` vs. `VTV`** *(Growth vs. Value)*, **`IWM` vs. `SPY`** *(Small vs. Large)*, **`XLK` vs. `SPY`** *(Tech vs. Market)*, and **Defensive (`XLP`, `XLV`, `XLU`) vs. Cyclical (`XLY`, `XLI`, `XLF`, `XLE`) Sectors**. | Robinhood MCP (`VUG`, `VTV`, `IWM`, `SPY`, `XLK`, `XLP`, `XLV`, `XLU`, `XLY`, `XLI`, `XLF`, `XLE`) |

## Broad Market Pre-Delivery Verification
In addition to Rows 0–5, Pill-Hover, Always-On Purple Target, Masked `••••3782` Shield Footer, `🧸 Kid-Level Summary`, and `jsc` syntax check (`exit 0`), confirm ALL 5 Broad Market Layers above are populated with live same-turn data (never static or unverified prose — mark unconfirmed web metrics explicitly as `unverified`).
