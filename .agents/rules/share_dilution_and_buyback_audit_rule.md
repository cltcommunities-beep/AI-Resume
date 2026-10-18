---
trigger: model_decision
---

# Rule: Mandatory Share Dilution & Buyback Audit Rule

This rule permanently governs all stock analyses, due diligence reports, and table schemas executed for the user.

## Core Directives

### 1. Mandatory Dilution & Buyback News Audit
For EVERY stock analyzed, you MUST perform a live search to audit its share count trajectory, **exact Dilution Proposal / Offering Announcement Date**, and buyback status:
- **Dilution Proposal / Offering Announcement Date:** Audit SEC proxy statements (DEF 14A), S-3 shelf filings, and secondary equity offering press releases to identify the EXACT date dilution was proposed or priced (e.g., INTC proposed/priced Aug 10, 2026). This tells the user **EXACTLY WHEN to wait for dip buying at 50 SMA support floors**!
- **Share Buybacks:** Identify active share repurchase programs (e.g., Alphabet $70B buyback, Nvidia $50B buyback) that reduce share count.
- **Unissued Share Capacity:** Audit Column 13 (Unissued Authorized Shares Remaining) to verify open-market dilution risk.

### 2. Mandatory Column 12 Schema Standard
Column 12 in the Master Executive Portfolio Readiness Table MUST explicitly display:
`🔴 Share Dilution & Buyback Status (Proposal / Offering Date & Dip Buying Catalyst)`

### 3. Classification Standards
- **🟢 NON-DILUTIVE:** Net share repurchases actively shrinking float (e.g. GOOG, NVDA).
- **🟢 LOW DILUTION:** Annual share count expansion <2% with low unissued capacity.
- **🟡 MODERATE DILUTION:** Strategic capital raise backed by massive cash additions (e.g. INTC $20B raise expanding cash to $49.7B).
- **🔴 HIGH DILUTION:** Toxic dilution >10% per year or toxic convertible debt overhang (e.g. NVTS, APLD).
