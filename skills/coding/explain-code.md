# Explain Code

**Category:** Coding
**Tags:** documentation, understanding, onboarding, learning

## Description

Ask Claude to explain what a piece of code does in plain language. Useful when reading an unfamiliar codebase, learning a new language, or preparing documentation.

## Prompt Template

```
Explain what the following [LANGUAGE] code does. Assume the reader is [AUDIENCE LEVEL: a beginner / a mid-level developer / a senior engineer unfamiliar with this library].

Describe:
1. The overall purpose of the code.
2. What each significant section or function does, step by step.
3. Any non-obvious patterns, algorithms, or library features used.

```[LANGUAGE]
[PASTE YOUR CODE HERE]
```
```

## Example

**Input:**
> Explain what the following Python code does. Assume the reader is a mid-level developer unfamiliar with this library.
>
> ```python
> from functools import lru_cache
>
> @lru_cache(maxsize=128)
> def fibonacci(n):
>     if n < 2:
>         return n
>     return fibonacci(n - 1) + fibonacci(n - 2)
> ```

**Output:**
> **Overall purpose:** This function computes the nth Fibonacci number using recursion with memoisation to avoid redundant calculations.
>
> **Step by step:**
> 1. `from functools import lru_cache` — imports a decorator from Python's standard library that caches function return values.
> 2. `@lru_cache(maxsize=128)` — decorates `fibonacci` so that up to 128 unique results are stored in memory. If the same `n` is requested again, the cached value is returned immediately instead of recomputing.
> 3. The base case `if n < 2: return n` returns `0` for `n=0` and `1` for `n=1`.
> 4. The recursive case `fibonacci(n-1) + fibonacci(n-2)` follows the standard Fibonacci definition.
>
> **Non-obvious detail:** Without `lru_cache`, this naive recursion would have O(2ⁿ) time complexity. With caching, it drops to O(n).

## Notes

- Adjust the audience level to get more or less technical explanations.
- For very long files, break them into logical sections and explain each one separately.
