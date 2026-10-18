---
trigger: model_decision
---

# Rule: Strict No LaTeX Math Code / Plain Text Only Rule

This rule permanently governs all outputs, formatting, and responses generated for the user.

## Core Directives

### 1. ABSOLUTE BAN ON LATEX MATH BLOCKS & SYNTAX
- **NEVER** use LaTeX math blocks (`$$ ... $$`), inline LaTeX (`\( ... \)`), LaTeX formatting (`\text{...}`, `\frac{...}`), or raw LaTeX code in any response.
- The user finds LaTeX math blocks unreadable and confusing.

### 2. Mandatory Plain Text Formula Formatting
- ALWAYS format formulas using simple, clean, readable plain text.
- Example:
  - ❌ **FORBIDDEN (LaTeX):** `$$\text{New Cash} = \text{Old Cash} + \text{FCF}$$`
  - 🟢 **MANDATORY (Plain Text):** `New Cash in Bank = Old Cash in Bank + Free Cash Flow`

### 3. Clear Markdown Table Integration
- Present all financial equations, steps, and metrics inside clean, visually engaging Markdown tables using plain English text and emoji symbols.
