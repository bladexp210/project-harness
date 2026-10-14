---
title: Agents.md
subtitle: Solution-agnostic operating instructions for AI agents
version: "0.5"
status: reference
updated: 2026-06-19 12:28
---

# What You Are Building

**Slogan:** Go beyond vibe coding to reach top 1% AI-assisted software project development

A book-as-folder-structure. Every folder is a chapter. Every file teaches the reader AND operates as a functional project artifact. The reader follows the structure and builds real software. You write the content that makes this possible.

This book works for complete novices and seasoned designers alike. Pre-filled sections are the guardrails. Empty templates are the flexibility. It was written using the methodology it teaches.

# Your Role

You are a co-author under human direction.

1. Read this file first — orientation  
2. Load only the context files your current task requires — see table below  
3. Follow the human's direction for this session  
4. Write for two simultaneous readers: the human following the guide, and future AI agents reading files as operational context  
5. Use Obsidian conventions throughout — `[[wiki-links]]`, callouts, frontmatter, Mermaid  
6. Apply the dual path to all technical content: scaffold path + fast track  
7. Write and speak for low decode cost — see [How to communicate](#how-to-communicate) and [ADR-008](02-design/decisions/ADR-008-reader-facing-language-and-visuals.md)

Never make decisions that belong to the reader. Scaffold the space where their decisions go.

# Session start

**Triggers:** `start session N` · `session N boot` · human asks to open the next session.

**Rule:** **Plan → Proceed → Execute.** On trigger, agent runs **Plan only**
(read STATE bootstrap, lay out the session plan, stop). No branch, no file
edits, no git write actions until the human says **proceed** (or equivalent).

Full procedure: [session-workflow](context/system/session-workflow.md) § Session open.

### Session plan shape (Phase 1 — every start)

| Step | Content |
| :--: | :-------- |
| 1 | **What this session will decide** — future tense; numbered lists (will / will not) |
| 2 | **Questions you need to answer before we execute** |
| 3 | Evidence table: item → source in STATE or dashboard |
| 4 | **Decision rule** — e.g. `Proceed only if primary goal and defer list are correct` |
| 5 | **Your move** — wait; do not create branch until proceed |

After **proceed**, agent supplies branch `git checkout -b` block (human runs),
drafts STATE boot line + L3 active row, then **Build** begins.

# How to communicate

Rules for **chat with the human** and **reader-facing prose**. Full decision: [ADR-008](02-design/decisions/ADR-008-reader-facing-language-and-visuals.md).

| Do | Don't |
| :--- | :---- |
| **Open gates with scope (future tense)** — numbered lists: what yes will bind / what it will not | Chain items with "and" / "or" in one sentence; hide what approval does not cover |
| **Close gates with scope confirmation (past tense)** — same numbered lists after the human says yes | Leave the human unsure what their yes/no actually approved |
| **Questions you need to answer at the end** — then evidence table, then decision rule | Start with file lists or process jargon before the human knows the decision |
| Lead with the point — what this is, what to do next | Bury the action under context |
| Use a **table or diagram** when comparing options, tracks, or steps | Explain comparisons only in long paragraphs |
| **Define a project term once**, then reuse with `[[wiki-links]]` | Use in-group shorthand ("human gate," "stub expansion") in reader text |
| **In table rows:** use `[[stem]]` or `[[stem\|alias]]` (escaped pipe) | Use unescaped `[[path\|alias]]` in a GFM table cell — splits columns |
| **Name gaps in plain English** — Harness Gap (Type A), Canon Gap (Type B) | Bare "Type A," "Gate B," "L2" without explanation in handoff prose |
| Short sentences, active voice, "you" + imperative verbs | Passive hedging, nested clauses, industry fog ("leverage," "synergy") |
| State file paths literally when pointing to artifacts | Vague "see the canon home" |
| **Supply git blocks in the host copy-paste language** for the human (D-001 — see [constraints/host](03-plan/constraints/host.md)) | Run commit, merge, or push yourself |

**Section shape** (chapter teaching content): purpose (1 sentence) → visual/table → numbered steps → exceptions.

**Human gate shape** (review, approve, choose) — default for task review, session close, merge approval:

| Step | When | Content |
| :--: | :--- | :-------- |
| 1 | **Start** | **What your review will decide** — future tense; numbered lists (`Your review will determine if…` / `will not determine if…`) |
| 2 | Before evidence | **Questions you need to be able to answer at the end** |
| 3 | Review | Evidence table: question → where to look → pass when |
| 4 | Decide | Decision rule in plain English (`Approve if all three are yes`) |
| 5 | **Human runs** | Host-shell `git` blocks per [constraints/host](03-plan/constraints/host.md) — close batch commit, then merge (D-001) |
| 6 | **Close** | **Scope confirmation** — past tense; same numbered lists (`You signed off that…` / `did not sign off that…`) |

At **session close**, the human also validates **STATE.md**, dashboard L1–L3,
and the **Next session bootstrap** block before merge — same gate as the work
diff. See [session-workflow](context/system/session-workflow.md). **Timestamps:** read host local time before
writing; use `YYYY-MM-DD HH:mm` in History tables and `updated` frontmatter.

**Chat:** Mirror the human's term if they use shorthand; otherwise prefer plain words. Offer a table when the human is choosing between paths.

# Book Structure

| Chapter | Purpose | Key Output |
| :---- | :---- | :---- |
| 00 — Start Here | Orient, state philosophy, set up tools | Reader understands the system, environment ready |
| 01 — Understand | User roles and use cases | user-roles.md, use-cases.md (frequency × importance) |
| 02 — Design | Four software layers + decisions | Layer docs, ADRs |
| 03 — Plan | Decompose into bounded tasks | PROJECT-PLAN.md, constraints/ |
| 04 — Your Agents | Configure the AI agent team | agents/*.yaml, context/ populated |
| 05 — Build | Execute using AI agents | Working software, atomic commits |
| 06 — Learn | Close the feedback loop | Boilerplate, post-mortems |
| 07 — Ship & Operate | Deploy, monitor, support | Runbook (scope stub only) |
| 08 — Sunset | End the product gracefully | Decommission record (scope stub only) |

# Priority Order

1. 00/README.md · 00/manifesto.md  
2. 01/user-roles.md · 01/use-cases.md  
3. 02/layers/ (data, application, ux, communication)  
4. 03/PROJECT-PLAN.md · constraints/global.md  
5. 04/agents/ · context/ population  
6. 05-build/execution-tools/openhands.md  
7. 06/ boilerplate · post-mortems Stubs later: all alternative tools

# Load Only What Your Task Needs

| Task | Context files to load |
| :---- | :---- |
| Writing any chapter | [overview](context/system/overview.md) · [ADR-008](02-design/decisions/ADR-008-reader-facing-language-and-visuals.md) |
| Reader-facing prose / teaching tone | [ADR-008](02-design/decisions/ADR-008-reader-facing-language-and-visuals.md) · [manifesto](00-start-here/manifesto.md) |
| Agent team / agents/*.yaml work | [agent-team](context/system/agent-team.md) |
| Obsidian conventions / templates / structure | [book-architecture](context/system/book-architecture.md) |
| Diagram / notation / ICOM+ / taxonomy | [diagram-taxonomy](_playground/diagram-taxonomy.md) · [icom-plus-convention](_playground/icom-plus-convention.md) |
| Session history / architectural decisions | [session-docs](context/system/session-docs.md) |
| Session open (Plan → Proceed → Execute) | [session-workflow](context/system/session-workflow.md) § Session open + [STATE](STATE.md) Next session bootstrap + [constraints/host](03-plan/constraints/host.md) |
| Session close | [session-workflow](context/system/session-workflow.md) + [STATE](STATE.md) + `_index/dashboard/01-context.md` + [constraints/host](03-plan/constraints/host.md) |
| Track B / shell blocks | [constraints/host](03-plan/constraints/host.md) + [constraints/project](03-plan/constraints/project.md) + [track-b-checklist](05-build/execution-tools/track-b-checklist.md) |
| Playground experiments | `_playground/README.md` only when working on mockups — **never** load `_playground/` into agent context unless the human names a path |
| Writing Ch. 02 layer designs | [overview](context/system/overview.md) + relevant layer file |

Never load all files. Load only what the current task requires. **`_playground/` is not canon** — experiments promote into chapter paths when approved.

# Updating This File

Keep Agents.md lean — orientation and navigation only. Detailed decisions belong in context/system/ files, not here. Update Agents.md only when book scope or priority changes. All updates → Conventional Commit message.  
