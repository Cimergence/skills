# Code Review

**Category:** Coding
**Tags:** code review, best practices, pull request, quality

## Description

Ask Claude to review a block of code and provide structured feedback covering correctness, readability, performance, and security. Ideal for self-review before opening a pull request or when onboarding to an unfamiliar codebase.

## Prompt Template

```
Please review the following [LANGUAGE] code. Focus on:
1. Correctness — are there any bugs or edge cases?
2. Readability — is the code clear and well-structured?
3. Performance — are there any obvious inefficiencies?
4. Security — are there any vulnerabilities or risky patterns?

Provide your feedback as a numbered list grouped by these four areas. If everything looks good in a category, say so briefly.

```[LANGUAGE]
[PASTE YOUR CODE HERE]
```
```

## Example

**Input:**
> Please review the following Python code. Focus on correctness, readability, performance, and security.
>
> ```python
> import sqlite3
>
> def get_user(username):
>     conn = sqlite3.connect("users.db")
>     cursor = conn.cursor()
>     cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
>     return cursor.fetchone()
> ```

**Output:**
> **1. Correctness**
> - The function does not close the database connection or cursor after use, which can lead to resource leaks.
>
> **2. Readability**
> - The function is concise but lacks a docstring explaining its purpose and return value.
>
> **3. Performance**
> - Opening a new connection on every call is expensive. Consider using a connection pool or passing a shared connection.
>
> **4. Security** ⚠️
> - The query uses an f-string to interpolate `username` directly, making it vulnerable to SQL injection. Use parameterised queries instead:
>   ```python
>   cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
>   ```

## Notes

- For large files, paste only the relevant function or class to keep the review focused.
- You can add language-specific concerns (e.g., "Also check for Pythonic idioms" or "Check for memory safety in Rust").
- Works well combined with the [Refactor Code](refactor-code.md) skill to act on the feedback.
