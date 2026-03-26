# Rewrite for Audience

**Category:** Writing
**Tags:** tone, audience, communication, editing, style

## Description

Ask Claude to rewrite a piece of text for a specific target audience or communication style — for example, turning a technical report into a plain-language email, or a casual note into a formal memo.

## Prompt Template

```
Rewrite the following text for [TARGET AUDIENCE: a non-technical executive / a 10-year-old / a legal audience / a social media post].

Tone: [TONE: formal / casual / enthusiastic / neutral]
Length: [LENGTH: keep roughly the same / shorten to ~[N] words / expand with more detail]

Preserve the core meaning and all important facts. Do not add information that is not in the original.

---
[PASTE ORIGINAL TEXT HERE]
```

## Example

**Input:**
> Rewrite the following text for a non-technical executive. Tone: formal. Length: keep roughly the same.
>
> ---
> The new caching layer reduces p99 API latency from 450ms to 35ms by serving frequent read queries from an in-memory Redis store rather than hitting the primary PostgreSQL database on every request.

**Output:**
> The new performance improvement has reduced response times for our slowest transactions by over 90% — from 450 milliseconds to 35 milliseconds. This was achieved by storing frequently accessed data temporarily in a fast in-memory system, so the main database is no longer queried on every customer request. The result is a significantly faster and more responsive product experience.

## Notes

- Being specific about the target audience ("CFO with no engineering background" vs "general non-technical reader") produces more tailored results.
- You can also specify what to cut: "Remove all acronyms" or "Avoid passive voice".
- Useful for translating internal engineering updates into stakeholder communications.
