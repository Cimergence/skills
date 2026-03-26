# Break Down a Task

**Category:** Productivity
**Tags:** planning, project management, task breakdown, GTD

## Description

Ask Claude to decompose a large, vague task into a clear, actionable checklist with sub-tasks. Helps overcome blank-page paralysis and makes it easier to estimate and delegate work.

## Prompt Template

```
Break down the following task into a detailed, actionable checklist.

Task: [DESCRIBE THE TASK IN ONE OR TWO SENTENCES]

Context:
- Who is doing this: [ROLE / SKILL LEVEL]
- Available tools / resources: [LIST KEY TOOLS OR CONSTRAINTS]
- Deadline or time budget: [DEADLINE OR HOURS AVAILABLE]
- Definition of done: [WHAT DOES COMPLETION LOOK LIKE?]

Group the sub-tasks into logical phases or sections if there are more than 5 steps.
```

## Example

**Input:**
> Break down the following task into a detailed, actionable checklist.
>
> Task: Launch a personal portfolio website.
>
> Context:
> - Who is doing this: Mid-level software developer, comfortable with HTML/CSS/JS
> - Available tools: GitHub Pages, a custom domain already purchased
> - Deadline: 2 weeks
> - Definition of done: Site is live at my custom domain, shows projects and contact info, works on mobile

**Output:**
> **Phase 1 — Content & Design Planning**
> - [ ] List 3–5 projects to feature, with descriptions and links
> - [ ] Write a short "About me" bio (2–3 sentences)
> - [ ] Choose a colour palette and font pairing
> - [ ] Sketch a rough wireframe (even on paper) for the layout
>
> **Phase 2 — Build**
> - [ ] Set up a new GitHub repository for the site
> - [ ] Create the HTML structure (index.html, projects section, contact section)
> - [ ] Apply CSS styling — responsive layout, typography, colours
> - [ ] Add project cards with screenshots, descriptions, and links
> - [ ] Add a contact section (email link or simple form)
> - [ ] Test on mobile using browser dev tools
>
> **Phase 3 — Deploy**
> - [ ] Enable GitHub Pages in the repository settings
> - [ ] Add a `CNAME` file pointing to your custom domain
> - [ ] Update your domain registrar's DNS to point to GitHub Pages IPs
> - [ ] Wait for DNS propagation (up to 24 hours) and verify the site is live
> - [ ] Test all links and the contact form on the live site

## Notes

- The more context you provide, the more tailored the breakdown.
- Ask Claude to estimate time for each phase: "Add a rough time estimate next to each phase."
- You can ask it to generate a Markdown checklist you can paste directly into a GitHub issue or Notion page.
