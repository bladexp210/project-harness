---
title: "Snippet: What lives here table"
chapter: template
status: template
tags: [template, obsidian, table]
---

# Snippet — "What lives here" table (chapter READMEs)

Copy into chapter READMEs under `## What lives here`. **Do not** use
`[[target|alias]]` in table rows — the inner `|` breaks GFM columns.

## Option A — stem-only links (simplest)

```markdown
## What lives here

| Path | Purpose |
| :---- | :---- |
| [[your-folder/README]] | One-line description |
| `_templates/your-template.md` | Blank template (repo root) |
| [[your-folder/example-name]] | Worked example |
```

## Option B — aliased links (escape the pipe)

```markdown
| Path | Purpose |
| :---- | :---- |
| [[your-folder/README\|your-folder/]] | One-line description |
```

Rule: [book-architecture](../context/system/book-architecture.md) § Wiki-links inside Markdown tables.
Enforced by `validate_md.py` on every commit.
