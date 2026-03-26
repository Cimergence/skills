# Compare Options

**Category:** Analysis
**Tags:** decision making, trade-offs, comparison, evaluation

## Description

Ask Claude to systematically compare two or more options across a set of criteria and recommend the best choice given your priorities. Useful for product decisions, technology choices, vendor selection, and more.

## Prompt Template

```
Compare the following options on the criteria listed below. Present the comparison as a table, then provide a short recommendation based on my priorities.

Options:
- [OPTION A]
- [OPTION B]
- [OPTION C — optional]

Criteria (in order of importance to me):
1. [MOST IMPORTANT CRITERION]
2. [SECOND CRITERION]
3. [THIRD CRITERION]

My context: [A SENTENCE OR TWO ABOUT YOUR SITUATION, CONSTRAINTS, OR GOALS]
```

## Example

**Input:**
> Compare the following options on the criteria listed. Present as a table, then recommend.
>
> Options:
> - PostgreSQL
> - MongoDB
> - SQLite
>
> Criteria (in order of importance):
> 1. Ease of setup for a solo developer
> 2. Suitability for relational/structured data
> 3. Production scalability
>
> My context: I'm a solo developer building a side project that may eventually need to scale to thousands of users. The data is mostly structured with clear relationships.

**Output:**
> | Criterion | PostgreSQL | MongoDB | SQLite |
> |---|---|---|---|
> | Ease of setup | Moderate — needs a server process | Moderate — needs a server process | Very easy — single file, zero config |
> | Relational/structured data | Excellent — native relational model, foreign keys, joins | Fair — flexible schema, but relational queries are awkward | Good — full SQL support, good for structured data |
> | Production scalability | Excellent — battle-tested at scale | Good — scales well for document workloads | Limited — single-writer, not designed for high concurrency |
>
> **Recommendation: PostgreSQL**
> Given that your data is structured and relational, and you want a clear path to scale, PostgreSQL is the best fit. While SQLite is simpler to set up initially, you would likely need to migrate away from it as traffic grows. MongoDB's flexible schema is a poor match for strongly relational data. Most cloud providers (Supabase, Railway, Render) offer managed PostgreSQL with minimal setup overhead, reducing the operational burden for a solo developer.

## Notes

- The more specific your criteria and context, the better the recommendation.
- You can ask Claude to weight the criteria numerically (e.g., "score each out of 5") for a more quantitative comparison.
- If you disagree with the recommendation, share your objection and ask Claude to reconsider: "I'm concerned about X — does that change your recommendation?"
