---
title: Book Architecture
layer: 1-system
status: reference
tags: [book, structure, obsidian, conventions]
---

# Book Architecture

Load this file when working on Obsidian conventions, templates, chapter structure, or publication workflow.

---

## Chapter Detail

### 00 — Start Here

Files: README.md, manifesto.md, setup/design-tools/*, setup/execution-tools/*

**README.md** opens with the slogan and explains what the book is, who it is for, and how to use it. No jargon. No assumptions.

**manifesto.md** states the philosophy explicitly:

This system is designed for durability, not just speed. AI is a multiplier — not a substitute for understanding. Every decision is documented. Every pattern is explained. When AI is unavailable or expensive, the documented system still runs. When you bring someone new onto the project, they can read, understand, and trust what was built and why.

**setup/** documents tools with the dual path. Design tools and execution tools are separate sub-folders. Each tool gets its own file. Primary tools get full scaffold + fast track. Alternatives get stubs.

Design tools: cowork.md (primary), cursor.md, antigravity.md. Execution tools:
[openhands](../../05-build/execution-tools/openhands.md) (Track A), [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) (Track B); Ch. 00 index only.

### 01 — Understand Your Project

Files: user-roles.md, use-cases.md

**user-roles.md** — template + guide. Defines who will use the software. Each role gets a brief description and primary goals. The AI agent helps the reader discover roles through questions.

**use-cases.md** — template + guide. For each user role, defines use cases with frequency × importance ratings. This matrix drives decomposition tree ordering in Ch. 03.

| Role | Use Case | Frequency | Importance | Priority |
| :---- | :---- | :---- | :---- | :---- |
| [Role] | [What they need to do] | Daily/Weekly/Rarely | Critical/High/Medium/Low | [derived] |

### 02 — Design Your System

Files: layers/data.md, layers/application.md, layers/ux.md, layers/communication.md, decisions/

Each layer file: explains what the layer is → why it matters → provides a design template → AI helps fill it in. Mermaid diagrams are mandatory (see below).

**decisions/** — ADR files land here as significant decisions are made. Format: ADR-NNN.md. Every ADR documents: what was decided, why, alternatives considered (red-teamed), what was left on the table.

Dead branches in PROJECT-PLAN.md reference their ADR with [PRUNED: reason] notation.

### 03 — Plan Your Build

Files: PROJECT-PLAN.md (template), constraints/global.md (pre-filled), constraints/project.md (template)

**PROJECT-PLAN.md** — the nested checklist decomposition tree. Ordered by use-case priority from Ch. 01. Each leaf points to its task file.

```
## [ ] Feature Name
  ### [ ] Layer Name
    #### [x] Task name → tasks/layer/task-name.md
    #### [PRUNED: constraint-reference] Branch name
    > Decision: Why. See: [[ADR-001]]
```

**constraints/global.md** — pre-filled with good software practices. These are the guardrails. Reader does not write this; they inherit it.

**constraints/project.md** — template. Reader fills in their project-specific rules.

### 04 — Your Agents

Files: agents/*.yaml (pre-configured), context/ (reader populates from Ch. 01-02 outputs)

This chapter is largely pre-filled. The agent definitions come ready. The reader's job: populate the context/ layers using their layer designs from Ch. 02.

### 05 — Build

Files: tasks/ (workspace), execution-tools/*.md

Primary: openhands.md (full scaffold + fast track) Alternatives as stubs: note key differentiator vs. primary. Jules stub note: cloud-hosted, async, no local Docker — most accessible for non-technical users.

### 06 — Learn and Improve

Files: boilerplate/ (living artifact), post-mortems/ (template + examples)

Boilerplate grows from the learning loop. Good agent outputs → candidate boilerplate → human reviews → promoted. The specialist library grows the same way: systematic gaps revealed by post-mortems → new specialist agent role.

---

## Obsidian Conventions

### Wiki-links (mandatory)

All internal references use `[[note-name]]`, not standard markdown links. The
graph view becomes the book's visual table of contents. **Table rows:**
`[[stem]]` or `[[stem\|alias]]` only — see [chapter-what-lives-here-table](../../_templates/chapter-what-lives-here-table.md).

```
Correct:   See [[data-layer]] for schema design guidance.
Incorrect: See [data layer](../02-design/layers/data.md)
```

### YAML Frontmatter (every file)

```
---
chapter: 02
layer: data
status: template | in-progress | complete
audience: [novice, seasoned, both]
tags: [design, data-layer]
---
```

### Mermaid Diagrams (mandatory per context)

| File | Required diagram type |
| :---- | :---- |
| 00 README | System overview |
| 02/data | ER diagrams, schema tables |
| 02/application | Sequence diagrams, state machines |
| 02/communication | API endpoint tables, event flows |
| 02/ux | User flow diagrams, component hierarchy |
| 03/PROJECT-PLAN | Task dependency graph |

Dialect is chosen by the *question* the diagram answers — see the
question→dialect table in [ADR-002-modeling-conventions](../../02-design/decisions/ADR-002-modeling-conventions.md). Size budget:
≤ 20 nodes per diagram; bigger means wrong zoom level, split C4-style.
Decision logic uses markdown decision tables (DMN-lite), not diagrams.

### Task model (ICOM + Gherkin)

Every task file in `tasks/` follows the ICOM frame from
[ADR-002-modeling-conventions](../../02-design/decisions/ADR-002-modeling-conventions.md): **Inputs** (Layer-3 context list),
**Controls** (inherited constraints + acceptance criteria), **Mechanisms**
(agent + execution tool), **Outputs** (required artifacts). Acceptance
criteria are Gherkin scenarios; each `Then` clause is one test the agent
must evidence at task closure.

### Tags (use consistently)

`#design` `#data` `#application` `#ux` `#communication` `#decision` `#task` `#constraint` `#boilerplate` `#post-mortem`

### Playground (experiments — not canon)

`_playground/` — safe exploration before promotion. Mockups, HTML ICOM visuals,
A/B task layouts. Each experiment folder carries `manifest.yaml` (`created`,
`updated`, `promote_to`, `status`). Stale experiments (`status: experiment`,
no edit for **4 days**) move to `_playground/_archive/` via
`scripts/playground_archive.py`. Distinct from `_inbox/` (external research
ingress). Agents do not load `_playground/` unless the human names a path.

### Project dashboard (provider-agnostic)

`_index/dashboard/` — three zoom levels (C4-inspired), plain markdown + Mermaid:

- `01-context.md` — product-lifecycle spine, validator health, open threads  
- `02-containers.md` — per-chapter status and major artifacts  
- `03-components.md` — current session focus and next actions  

Updated at every session close per [session-workflow](session-workflow.md). Optional future:
Dataview queries on top of the same files (Obsidian-only).

### Templater

`_templates/` — generates structured new notes. Files: new-task.md, new-decision.md, new-use-case.md, new-layer-design.md

---

## The Dual Path (implementation)

Every technically demanding section uses these callout blocks:

```
> [!LEARN] Learn It
> **What this is:** [one sentence]
> **Why it matters:** [connected to durability / top-1% goal]
>
> Step 1: ...
> Step 2: ...
> Step 3: ...
>
> **What's happening underneath:** [one honest paragraph]

> [!TIP] Fast Track
> Already know this? Here's the short version.
> `[command]`
> You own the outcome.
```

The fast track is never dismissive. It acknowledges expertise. "You own the outcome" is honest, not threatening.

---

## Writing Rules

**Every file has two jobs:** (1) Teach (explain what this is, why it matters, how to fill it in) and (2) Scaffold (provide the structure the reader fills in for their project).

**Tone:** Respectful (never condescending), Honest (state tradeoffs clearly), Direct (say what it is first), Not preachy, and Concrete (use real examples, e.g. "an e-commerce checkout").

**AI assistance prompts:** Include one per major template section (e.g., `> [!NOTE] Ask your AI agent "Help me define the user roles..."`).

---

## Publication Workflow

**Flow:** Cowork authors files → local folder (Obsidian vault) → Google Drive Desktop sync → Google Drive (backup/collab) → push when ready → GitHub repository (public) → Quartz site repo → GitHub Pages website.

**Quartz** (quartz.jzhao.xyz) can publish an Obsidian-style vault as a static site (wiki-links, callouts, Mermaid). This public copy does not include deploy credentials or a live site. See [Publish later](../../07-ship-operate/publish/README.md).
