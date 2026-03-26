# Meeting Notes to Action Items

**Category:** Productivity
**Tags:** meetings, action items, follow-up, notes, summary

## Description

Paste raw meeting notes or a transcript and ask Claude to extract a clean summary, decisions made, and a list of action items with owners and deadlines. Eliminates the time spent manually parsing long notes after a meeting.

## Prompt Template

```
Here are notes from a [MEETING TYPE: team standup / project kickoff / client call / retrospective].

Please extract:
1. **Summary** — 2–4 sentences describing what was discussed and the overall outcome.
2. **Decisions made** — a bullet list of any decisions or agreements reached.
3. **Action items** — a table with columns: Action | Owner | Due Date. Use "TBD" if owner or date was not mentioned.

---
[PASTE MEETING NOTES OR TRANSCRIPT HERE]
```

## Example

**Input:**
> Here are notes from a project kickoff meeting.
>
> ---
> Attendees: Sarah (PM), Dev (Engineering lead), Priya (Designer), Tom (QA)
>
> Sarah opened — this is the kickoff for the new onboarding redesign. Goal is to launch by end of Q2.
> Dev said the backend API is ready, frontend work needs to start asap. He'll share API docs by Friday.
> Priya has wireframes 80% done, will send for review Monday.
> Tom asked about test environments — Dev to set up staging by next Wednesday.
> Sarah will send a project brief to everyone today.
> Next meeting: weekly sync, every Tuesday 10am.

**Output:**
> **Summary:**
> The team held a kickoff meeting for the onboarding redesign project, targeting a Q2 launch. The backend API is complete and frontend work is ready to begin. Wireframes and documentation are both nearly ready, with key assets expected by early next week.
>
> **Decisions made:**
> - Target launch date: end of Q2.
> - Weekly sync scheduled for Tuesdays at 10am.
>
> **Action items:**
>
> | Action | Owner | Due Date |
> |--------|-------|----------|
> | Share API documentation | Dev | Friday |
> | Send wireframes for review | Priya | Monday |
> | Set up staging environment | Dev | Next Wednesday |
> | Send project brief to team | Sarah | Today |

## Notes

- Works well with both bullet-point notes and raw transcripts.
- If the transcript is very long, tell Claude to focus on specific topics: "Focus only on action items related to the frontend team."
- Ask Claude to format the output as Markdown so you can paste it directly into Notion, Confluence, or a GitHub issue.
