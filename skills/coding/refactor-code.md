# Refactor Code

**Category:** Coding
**Tags:** refactoring, clean code, maintainability, best practices

## Description

Ask Claude to refactor a piece of code to improve its structure, readability, or adherence to best practices — without changing its external behaviour.

## Prompt Template

```
Refactor the following [LANGUAGE] code to improve [GOAL: readability / performance / testability / idiomatic style].

Requirements:
- Do not change the external behaviour or API.
- [ANY ADDITIONAL CONSTRAINTS, e.g. "Keep it compatible with Python 3.8" or "Avoid adding new dependencies"]

After the refactored code, include a short summary of the changes you made and why.

```[LANGUAGE]
[PASTE YOUR CODE HERE]
```
```

## Example

**Input:**
> Refactor the following Python code to improve readability and idiomatic style. Do not change the external behaviour.
>
> ```python
> def process(items):
>     result = []
>     for i in range(len(items)):
>         if items[i] % 2 == 0:
>             result.append(items[i] * 2)
>     return result
> ```

**Output:**
> ```python
> def process(items):
>     return [item * 2 for item in items if item % 2 == 0]
> ```
>
> **Changes made:**
> - Replaced the index-based `for i in range(len(items))` loop with a direct iteration over `items`.
> - Consolidated the filtering and transformation into a single list comprehension, which is the idiomatic Python approach and easier to read at a glance.

## Notes

- Specify the goal clearly (readability, performance, testability) so Claude targets the right kind of refactoring.
- For larger files, refactor one function or class at a time to keep changes reviewable.
- Follow up with the [Code Review](code-review.md) skill to validate the refactored result.
