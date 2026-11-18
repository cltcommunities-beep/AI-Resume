---
trigger: model_decision
description: Mandatory Unofficial Stretch & Buy-Side Whisper Earnings Benchmark Rule — Requires auditing the 5 Mandatory Whisper Data Pillars (EPS, Revenue, Core Segment, Forward Gross Margin, and 13-Week Organic Guidance) on every earnings review.
---

# 🔴 RED-TAG MANDATORY RULE: UNOFFICIAL STRETCH & BUY-SIDE WHISPER EARNINGS BENCHMARK

## 🚨 MANDATORY EXECUTIVE DIRECTIVE
Whenever the user asks about **earnings, financial results, quarterly reports, revenue/EPS beats or misses, or guidance for ANY stock**, the assistant is **STRICTLY PROHIBITED** from simply reporting whether the company beat the official Wall Street sell-side consensus.

The assistant **MUST UNCONDITIONALLY DETERMINE AND CLEARLY STATE** whether the company **beat or missed the 🔬 Unofficial Stretch Result (The Buy-Side Whisper Target)** held privately by hedge funds and institutional trading desks. **NO EXCEPTIONS PERMITTED.**

---

## 🏛️ 1. Why This Rule Exists: The Retail Earnings Trap

Retail investors frequently get trapped buying post-earnings "beats" because public financial media (Yahoo Finance, CNBC, Robinhood) reports that a company beat the public sell-side consensus (e.g. Netflix beating $0.82 EPS by printing $0.87, or Nvidia reporting a headline revenue beat).

However, hedge funds and algorithmic market makers trade against **Buy-Side Whisper Expectations (The 🔬 Unofficial Stretch Guess)**:
1. If a company beats the public estimate but **misses the 🔬 Unofficial Stretch Target** (especially on forward gross margins or organic guidance), institutions immediately dump the stock or fade the pop.
2. If a company beats both the public estimate **AND all 5 Unofficial Stretch Data Pillars**, it receives the **🏆 BEAT ALL 5 (TROPHY)**, fueling a multi-week institutional melt-up.

---

## 🔬 2. The 5 Mandatory Data Pillars Needed for Unofficial Stretch Verification

Before declaring whether an earnings report beat or missed the Unofficial Stretch, the assistant **MUST UNCONDITIONALLY audit all 5 of the following mandatory data pillars** via live broker tools and targeted `search_web` calls (`"[TICKER]" "whisper number" OR "whisper" revenue EPS QX [Current Year] trading desk`):

### 1️⃣ Pillar 1: Backward-Looking EPS Whisper
* **Data Needed:** Non-GAAP diluted EPS whisper figure tracked by trading desks and whisper indexes (e.g. `thewhispernumber.com`, buy-side pre-market notes).
* **Requirement:** Must determine the exact delta between consensus ($2.47), whisper target ($2.60), and reported actual ($2.68).

### 2️⃣ Pillar 2: Backward-Looking Revenue Whisper
* **Data Needed:** Total net revenue whisper target held by buy-side funds, which is almost always 2% to 5% higher than published sell-side consensus.
* **Requirement:** State the exact dollar gap (e.g. Consensus $109.0B vs Whisper $114.0B–$115.0B vs Reported $115.8B).

### 3️⃣ Pillar 3: Core Segment & Engine Driver Whisper
* **Data Needed:** The single most critical business segment that justifies the stock's valuation multiple (e.g. Nvidia Data Center, SpaceX Starlink Recurring Subs/ARPU, Microsoft Azure, Amazon AWS, Tesla Auto Gross Margin ex-regulatory credits).
* **Requirement:** A top-line beat accompanied by a core segment miss triggers an automatic warning.

### 4️⃣ Pillar 4: Forward Gross Margin Guidance Whisper (The Nitpick Trap)
* **Data Needed:** Forward quarterly gross margin percentage expectation held by institutional models.
* **The Iron Law:** **Beating revenue while guiding forward gross margins down (e.g. Nvidia guiding Q4 gross margin down -300 to -400 bps to 71%–72% due to new architecture ramps) is an automatic 🔴 MISSED STRETCH flag.** Gross margin dilution directly reduces future cash flow quality.

### 5️⃣ Pillar 5: Organic Forward Guidance vs. Calendar/M&A Distortions
* **Data Needed:** Normalized 13-week organic revenue guidance.
* **The Distortion Screen:** Management frequently boosts headline guidance using extra calendar weeks (e.g. a 14-week fiscal quarter adding ~7% or ~$8.8B in optical revenue) or unclosed acquisitions. The assistant MUST strip out calendar/M&A distortions to evaluate the true organic forward whisper beat/miss.

---

## 📊 3. Mandatory 5-Level Horizontal Benchmark Flow

For every stock earnings evaluation, the assistant MUST render the horizontal progression showing how actual results compare across all 5 benchmark tiers:

```markdown
[ 📜 Official Mgmt Guide: $X ] ──► [ 📊 Wall St Consensus: $X ] ──► [ 🏛️ Tier-1 Banks: $X ] ──► [ 🔬 Unofficial Stretch (Whisper): $X ] ──► [ 🏆/🔴 Actual Reported: $X ]
```

---

## 📋 4. Mandatory 6-Column Institutional Earnings Benchmark Table

Every earnings analysis MUST include this standardized audit table:

| Financial Metric | 📜 Official Guidance | 📊 Wall St Consensus | 🔬 Unofficial Stretch (Whisper) | 🏆/🔴 Actual Reported | Status Flag & Institutional Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Quarterly Non-GAAP EPS** | $X.XX | $X.XX | **$X.XX** | **$X.XX** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |
| **Quarterly Total Revenue** | $X.XX B | $X.XX B | **$X.XX B** | **$X.XX B** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |
| **Core Engine / Segment Revenue** | $X.XX B | $X.XX B | **$X.XX B** | **$X.XX B** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |
| **Next-Quarter Headline Revenue Guide**| $X.XX B | $X.XX B | **$X.XX B** | **$X.XX B** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |
| **Next-Quarter Organic (13-Wk) Guide** | $X.XX B | $X.XX B | **$X.XX B** | **$X.XX B** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |
| **Next-Quarter Gross Margin Guide** | X.X% | X.X% | **≥ X.X%** | **X.X%** | 🏆 **BEAT ALL 5** or 🔴 **MISSED STRETCH** |

---

## 🏷️ 5. Standardized Status Coding & Nitpick Gap Analysis

1. 🏆 **`BEAT ALL 5 (TROPHY)`:**
   - **Condition:** The reported result beat Official Guidance, Wall Street Consensus, Tier-1 Banks, AND all 5 **🔬 Unofficial Stretch Data Pillars** (including forward gross margins and organic guidance).
   - **Meaning:** Authentic blow-out quarter; institutional green light.
2. 🔴 **`MISSED STRETCH (RED DOT)`:**
   - **Condition:** The reported result met or beat public consensus, but **failed to clear any of the 5 🔬 Unofficial Stretch Data Pillars** (e.g. forward gross margins guided down, or 13-week organic revenue below whisper).
   - **Meaning:** Hidden weakness; explains post-earnings sell-offs/fades and prevents retail dip-buying traps.
3. 🔍 **`Nitpick Gap Analysis`:**
   - Explicitly highlight the exact dollar or percentage gap between the **🔬 Unofficial Stretch Target** and the actual reported/guided number to decode institutional price action.

---

## 🚫 6. Strict Prohibitions
1. **NO Single-Number Claims:** Never answer "Did they beat earnings?" with a simple yes/no without breaking down the 5 Mandatory Whisper Data Pillars.
2. **NO LaTeX Math Blocks:** Plain text numbers inside tables and markdown only (`no_latex_math_blocks_rule.md`).
3. **NO Blind Dip Buying:** Never recommend buying a post-earnings dip on Day 1 before the Day 2 Morning Dip Window (9:45 AM – 10:30 AM EDT) confirms support.
