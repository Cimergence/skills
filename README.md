# Claude Skills

A curated collection of skills, prompts, and techniques for getting the most out of [Anthropic Claude](https://www.anthropic.com/claude).

## What is this?

This repository stores useful Claude skills — patterns, prompt templates, and techniques that are practical and interesting. Each skill is documented with a description, example prompt, and sample output so you can understand and reuse them quickly.

## Skills by Category

| Category | Description |
|----------|-------------|
| [Coding](skills/coding/) | Code generation, review, debugging, and refactoring |
| [Writing](skills/writing/) | Drafting, editing, summarising, and style transformation |
| [Analysis](skills/analysis/) | Data interpretation, document analysis, and critical thinking |
| [Productivity](skills/productivity/) | Task planning, note-taking, meeting summaries, and checklists |
| [Reasoning](skills/reasoning/) | Step-by-step problem solving, logic, and decision support |

## Repository Structure

```
.                           ← Repository root
├── README.md               ← You are here
└── skills/
    ├── coding/             ← Programming-related skills
    ├── writing/            ← Writing and communication skills
    ├── analysis/           ← Analysis and research skills
    ├── productivity/       ← Productivity and organisation skills
    └── reasoning/          ← Reasoning and problem-solving skills
```

## How to Use a Skill

1. Browse the category folder that matches your need.
2. Open the skill's `.md` file to read the description and example prompt.
3. Copy the prompt template, fill in the `[placeholders]`, and send it to Claude.

## Contributing

Found a useful skill? Feel free to open a PR:

1. Pick the right category folder (or create one if it doesn't exist).
2. Add a new `.md` file named after the skill (e.g., `code-review.md`).
3. Follow the template below.

### Skill File Template

```markdown
# Skill Name

**Category:** <category>
**Tags:** tag1, tag2

## Description

A short description of what this skill does and when to use it.

## Prompt Template

\```
Your prompt goes here. Use [PLACEHOLDER] for parts the user fills in.
\```

## Example

**Input:**
> [Example filled-in prompt]

**Output:**
> [Example Claude response]

## Notes

Any extra tips, variations, or caveats.
```

## License

This collection is released for personal and educational use. Feel free to adapt any skill for your own workflows.
