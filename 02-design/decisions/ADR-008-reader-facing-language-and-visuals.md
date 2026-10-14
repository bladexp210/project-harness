---
title: "ADR-008: Reader-facing language and visuals"
chapter: 2
status: accepted
date: 2026-06-17
tags:
  - decision
  - conventions
  - legibility
---

# ADR-008 — Reader-facing language and visuals

**Status:** accepted — 2026-06-17, Session 14.

## Context

The book serves **complete novices and seasoned designers** ([Agents](../../Agents.md)).
Many readers use English as a second or third language. Experts still lose time
when prose hides structure behind jargon, long sentences, or in-group shorthand
("human gate," "canon home," "stub expansion").

ADR-006 solved **machine** legibility (strip teaching blocks for agents). This ADR
solves **human** legibility: lower decode cost so capacity goes to competence and
problem-solving — not to deciphering book-culture.

The [manifesto](../../00-start-here/manifesto.md) already commits to trust and hand-off readability. Session 14
human direction: adopt the same standard in co-author chat and in every
reader-facing file.

## Decision

### 1. Default section shape

Every teaching section in dual-purpose chapter files follows this order:

| Step | What | Why |
| :--: | :--- | :-- |
| 1 | **One-sentence purpose** — what this is and what you do | Orients before detail |
| 2 | **Visual or table** — diagram, checklist table, or comparison table | Compresses structure |
| 3 | **Steps** — numbered, imperative ("Run…", "Open…") | Action without parsing |
| 4 | **Exceptions / when not** — short bullet list | Stops wrong-path drift |

Pure reference files (ADRs, `context/system/*`) may invert 1 and 2 when the
table *is* the decision — but still open with a plain summary sentence.

### 2. Language rules

| Rule | Do | Don't |
| :--- | :--- | :---- |
| **Short sentences** | One idea per sentence. Active voice. | Nested clauses; passive hedging ("it may be considered") |
| **Direct address** | "You run…", "Your task file lists…" | "The reader should…", "One might…" |
| **Plain words first** | "Confirm the table is correct" | "Approve the matrix at the human gate" |
| **Project terms** | Define once per chapter; then `[[wiki-link]]` | Repeat mystique; assume prior session memory |
| **Industry fog** | Delete or replace | "Leverage," "synergy," "best-in-class," undefined "canon" |
| **Lead with the point** | Answer "what / where / next" in the first line | Bury the action under context |

**Project terms** (allowed after first definition): Track A/B, worktree, ADR,
Gherkin, ICOM+, D-001, etc. **Chat shorthand** for humans and agents: replace
with the plain phrase in reader-facing text.

### 3. Visuals — when and how

| Question type | Use | Budget |
| :------------ | :-- | :----- |
| Parts and connections | Mermaid `flowchart` | ADR-002: ≤ 20 nodes |
| Order of handoffs | Mermaid `sequenceDiagram` | Same |
| Compare two paths | Markdown table (2+ columns) | Prefer over prose paragraphs |
| Repeatable procedure | Numbered checklist table | See [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) |
| States | `stateDiagram-v2` | When status matters |

Every diagram gets **one caption line** under it — fill in for the reader job:

> *This shows the workflow so you can pick Track A or Track B.*

No diagram without a stated reader job. **Markdown tables:** pipe rows must be
**consecutive** (no blank lines inside a table); checked by
`md_checks/markdown_structure.py`.

### 4. Dual path unchanged

[book-architecture](../../context/system/book-architecture.md) scaffold + fast track stays. ADR-008 tightens **both**
paths — not dumber content, less ceremony:

- `[!LEARN]` — full section shape (purpose → visual → steps → exceptions)
- `[!TIP]` — purpose line + command/table only; reader owns outcome

### 5. Reader checkpoint (optional callout)

At section end, when a decision or skill should be confirmed:

```markdown
> [!NOTE] Reader checkpoint
> You should be able to answer: (your verification question here)
```

Use for "stop and verify" — not for general tips (those stay `[!TIP]`).

**Human gate pages** (task review, session close, merge approval) follow the
six-step shape in [Agents](../../Agents.md) § How to communicate. Full templates
below. Confirmed Session 15 (task 01 pre-mortem review).

#### Step 1 — What your review will decide (future tense, **start**)

Open every gate with numbered lists — no chained "and" / "or" in one sentence:

```markdown
**Your review will determine if:**

1. …
2. …

**Your review will not determine if:**

1. …
2. …

If that is not the decision you want to make today, stop here.
```

Book callout (optional):

```markdown
> [!NOTE] What your review will decide
> **Your review will determine if:**
> 1. …
> **Your review will not determine if:**
> 1. …
```

#### Step 2 — Questions you need to be able to answer at the end

Plain yes/no or pick-one questions — title the section exactly this way in
co-author chat; use the same heading in book gate pages.

#### Steps 3–4 — Evidence and decision rule

Table: question → where to look → pass when. One decision rule line (`Approve
if all N are yes`).

#### Step 5 — Git (human only, D-001)

Agent supplies PowerShell blocks for **close batch commit** and **merge**; the
project owner runs both. Close docs must be committed on the session branch
**before** merge to `main`.

#### Step 6 — Scope confirmation (past tense, **close**)

After the human approves, restate the same numbered lists in past tense:

```markdown
> **You signed off that:**
> 1. …
> **You did not sign off that:**
> 1. …
```

Book callout (optional):

```markdown
> [!NOTE] What you approved
> **You signed off that:**
> 1. …
> **You did not sign off that:**
> 1. …
```

#### Worked example (Session 15 task 01)

**Start (future):** Your review will determine if: (1) pre-mortem record is
honest, (2) task ran within scope, (3) acceptance criteria met with evidence.
Will not determine if: (1) threat model finished, (2) pre-build design gate
cleared, (3) safe to build reader product.

**Close (past):** You signed off that: same three items. Did not sign off
that: same three exclusions.

Both bookends are mandatory in co-author chat; book gate pages use the same
shape with optional callouts at start and close.

### 6. Artifact zones stay strict

Per ADR-006, **outside** teaching callouts = project artifact. In artifact zones:

- No undefined metaphor
- No rhetorical questions without an answer
- Tables over prose for repeated structure
- File paths and commands literal (copy-paste ready)

Agents co-authoring with humans follow the same rules in chat: human gate
six-step shape; plain term on first use; no in-group shorthand unless the human
uses it first; git write actions as copy-paste blocks only (D-001).

### 7. Agent chat (co-author sessions)

Summarized in [Agents](../../Agents.md) § How to communicate. Full rules here.

## Why

Cognitive load is finite. Jargon and opaque structure act like an undeclared
prerequisite course. Visuals and tables are not "for beginners" — they let
experts see the problem structure immediately. ESL-friendly writing is a
**quality bar for everyone** tired, rushed, or new to the domain.

Pairs with ADR-006: agents get stripped artifacts; humans get scannable teaching.
Same legibility thesis as the manifesto addendum on plain language.

## Alternatives considered (red-teamed)

- **Simpler words only, no visuals** — rejected: tables/diagrams reduce load
  more than vocabulary swaps alone.
- **Separate "easy English" chapter** — rejected: ghettoizes ESL readers;
  bar applies everywhere.
- **Ban all technical terms** — rejected: precision matters; define once,
  link, reuse.
- **New `[!CHECK]` callout type** — rejected for now: `[!NOTE] Reader checkpoint`
  reuses Obsidian callout family (ADR-006 alignment).

## Pre-mortem

1. **Formulaic sections feel robotic** — mitigation: dual path; fast track stays
   terse; shape rule applies to Learn blocks, not every paragraph.
2. **Diagram caption boilerplate** — mitigation: caption must state reader job,
   not repeat the title.
3. **Agents ignore rules in chat** — mitigation: AGENTS.md § How to communicate;
   human can cite ADR-008 in session direction.

## Left on the table

- Lint rule: flag common fog words in artifact zones (T7 batch).
- Retrofit pass on dense chapter files (prioritize Ch. 05 execution paths).
- Illustrated figures (PNG/SVG) where Mermaid is insufficient — no pipeline yet.

## Consequences

- [Agents](../../Agents.md) gains § How to communicate (pointer here).
- [manifesto](../../00-start-here/manifesto.md) gains addendum § Plain language and visuals.
- New co-author and chapter work defaults to section shape + language rules.
- book-architecture execution-tools line already superseded by ADR-007
  (Track B checklist, not per-tool stubs) — update when that file is next edited.
