# Pros and Cons

**Category:** Reasoning
**Tags:** decision making, trade-offs, evaluation, pros, cons

## Description

Ask Claude to generate a balanced pros and cons list for a decision, idea, or action. Useful for reality-checking your thinking, surfacing blind spots, and preparing to present a decision to others.

## Prompt Template

```
Generate a balanced pros and cons list for the following:

Decision / idea: [DESCRIBE THE DECISION OR IDEA IN ONE OR TWO SENTENCES]

My context: [BRIEF DESCRIPTION OF YOUR SITUATION — e.g. "I'm a freelancer considering moving to a product role at a startup"]

List at least [N] pros and [N] cons. For each point, include a brief explanation (one sentence) of why it matters. After the list, give a short neutral summary of the key tension or trade-off I should focus on when making this decision.
```

## Example

**Input:**
> Generate a balanced pros and cons list for the following:
>
> Decision: Switching from a monolithic Rails app to a microservices architecture.
>
> My context: We're a 6-person engineering team at a growing SaaS startup. Our monolith is becoming harder to deploy but is stable and well-understood.
>
> List at least 4 pros and 4 cons, with a brief explanation for each. Then summarise the key trade-off.

**Output:**
> **Pros**
> - **Independent deployability** — Each service can be deployed separately, reducing the risk that one change breaks the entire system.
> - **Team scalability** — As the team grows, separate services allow squads to own and ship their domain without stepping on each other.
> - **Technology flexibility** — Different services can use different languages or databases best suited to their workload.
> - **Fault isolation** — A failure in one service does not necessarily bring down the whole product.
>
> **Cons**
> - **Significant operational complexity** — You'll need service discovery, distributed tracing, inter-service authentication, and more sophisticated deployment pipelines.
> - **Distributed systems problems** — Network failures, data consistency across services, and debugging across service boundaries are genuinely hard.
> - **High upfront investment** — Decomposing a stable monolith takes months of careful work with little visible user-facing value in the short term.
> - **Overhead for a small team** — Six engineers operating many services may spend more time on infrastructure than on product features.
>
> **Key trade-off to focus on:**
> The core tension is *short-term productivity vs long-term scalability*. Your monolith is stable and your team knows it — migrating to microservices will slow you down for months and introduce new failure modes. The question is whether your current pain (deployment difficulty) is serious enough to justify that cost *now*, or whether you can defer the decision until the team and product are larger.

## Notes

- Ask for a specific number of pros and cons to force Claude to think beyond the obvious first answers.
- Follow up with [Compare Options](../analysis/compare-options.md) if you want to weigh multiple alternatives rather than a single binary decision.
- Ask Claude to argue strongly for one side: "Now make the strongest possible case *for* the switch" — useful for stress-testing your thinking.
