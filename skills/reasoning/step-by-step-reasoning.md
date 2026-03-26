# Step-by-Step Reasoning

**Category:** Reasoning
**Tags:** problem solving, chain of thought, logic, debugging

## Description

Ask Claude to reason through a problem step by step before giving an answer. This technique — often called "chain of thought" prompting — dramatically improves accuracy on complex problems such as maths, logic puzzles, debugging, and multi-step decisions.

## Prompt Template

```
Think through the following problem step by step before giving your final answer. Show your reasoning clearly at each step.

Problem: [DESCRIBE THE PROBLEM]

[ANY ADDITIONAL CONTEXT OR CONSTRAINTS]
```

## Example

**Input:**
> Think through the following problem step by step before giving your final answer. Show your reasoning clearly at each step.
>
> Problem: A store sells apples at $1.20 each and oranges at $0.80 each. Alice buys a mix of apples and oranges and spends exactly $10.00. She buys more apples than oranges. How many of each did she buy?

**Output:**
> **Step 1 — Set up the equation.**
> Let `a` = number of apples, `o` = number of oranges.
> The constraint is: 1.20a + 0.80o = 10.00, and a > o, with a, o being positive integers.
>
> **Step 2 — Simplify.**
> Multiply through by 5 to eliminate decimals: 6a + 4o = 50, which simplifies to 3a + 2o = 25.
>
> **Step 3 — Solve for integer solutions.**
> From 3a + 2o = 25: 2o = 25 − 3a, so o = (25 − 3a) / 2.
> For o to be a positive integer, (25 − 3a) must be even and positive.
> 25 is odd, so 3a must be odd, so a must be odd.
> Try odd values of a:
> - a = 1: o = (25−3)/2 = 11. But a < o, violates a > o.
> - a = 3: o = (25−9)/2 = 8. Still a < o.
> - a = 5: o = (25−15)/2 = 5. Equal — violates a > o.
> - a = 7: o = (25−21)/2 = 2. ✓ a > o.
> - a = 9: o = (25−27)/2 = −1. Invalid (negative).
>
> **Step 4 — Verify.**
> 7 × $1.20 + 2 × $0.80 = $8.40 + $1.60 = $10.00 ✓
>
> **Answer:** Alice bought **7 apples** and **2 oranges**.

## Notes

- You can also use the phrase "Let's think through this carefully" at the end of a prompt to trigger step-by-step reasoning without a full template.
- Particularly useful for debugging: "Walk through this code execution step by step and find where it goes wrong."
- For very complex problems, ask Claude to first identify what type of problem it is and what strategy to apply.
