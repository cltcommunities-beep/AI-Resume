# 📲 Institutional Rule: Always Check with Robinhood Live APIs First
**Rule Name:** `mandatory_always_check_robinhood_api_rule.md`  
**Governing Authority:** Robinhood Margin Account `••••3782` Compounding Engine ($10,000 to $20,000 Milestone Architecture)  
**Standard:** Zero-Hallucination & Authoritative Live Broker Verification Standard  

---

## 🎯 Executive Mandate & Purpose
This rule permanently establishes that **the live Robinhood brokerage API is the SOLE authoritative source of truth** for Account `••••3782`.

Relying on conversational memory, cached numbers, estimates, or static assumptions for ANY stock price, account balance, cash figure, position size, or order status is **STRICTLY PROHIBITED**. The assistant MUST execute real-time Robinhood MCP tool calls before responding.

---

## 🔬 1. The 4 Mandatory API Call Triggers

Whenever the user or assistant initiates any of the following 4 actions, a live Robinhood API call is **UNCONDITIONALLY MANDATORY**:

| User Intent / Action | Required Robinhood MCP Tool | Authoritative Data Retrieved |
| :--- | :--- | :--- |
| **Check Active / Filled Orders** | `get_equity_orders` (Account `868333782`) | Live order states (`filled`, `confirmed`, `cancelled`), execution timestamps, fill prices, and reserved cash. |
| **Check Stock Price / Day Change** | `get_equity_quotes` (symbols array) | Real-time SIP consolidated tape prices (`last_trade_price` / `last_non_reg_trade_price`), bid/ask spreads, and previous close. |
| **Check Cash / Buying Power / Value** | `get_portfolio` (Account `868333782`) | Authoritative `total_value`, `cash`, `buying_power.buying_power`, and `equity_value`. |
| **Check Shares Owned / Cost Basis** | `get_equity_positions` (Account `868333782`) | Live `quantity`, `shares_available_for_sells`, and official Robinhood `average_buy_price`. |

---

## 🛡️ 2. The 4 Rules of Broker Verification

1. **The 'Zero Guessing' Law:** If the user asks *"check my NVDA order"*, *"what is OKLO at?"*, or *"how much cash do I have?"*, the assistant must NEVER answer from previous messages. A live tool call must be executed immediately in that exact turn.
2. **Order Execution Validation:** Never assume an order has or has not filled based on price alone. Verify the order's exact state (`state: "filled"` vs `state: "confirmed"`) from `get_equity_orders`.
3. **Transparent Live Timestamps:** When presenting prices or order statuses, state the real-time execution timestamp from the venue/broker (e.g. `Filled @ 9:29:58 AM EDT via Robinhood API`).
4. **Account Privacy Standard:** Always pass the unmasked account number `868333782` to Robinhood MCP tools, but display it masked as `••••3782` in all user-facing markdown responses.

---

## 📋 3. Post-Response Compliance Checklist

In every response involving account numbers, orders, or stock prices:
* 🟢 **GREEN BULLETS:** Did we call `get_equity_orders` to verify order status? Did we call `get_equity_quotes` for live prices? Did we call `get_portfolio` for cash/buying power?
* 🔴 **RED BULLETS:** Did we guess an order status? Did we quote a stale price from a previous message? Did we calculate cash balance by hand instead of querying `get_portfolio`?
