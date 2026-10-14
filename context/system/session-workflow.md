---
title: Session Workflow
layer: 1-system
status: reference
updated: 2026-06-30 22:25
tags: [state, handoff, workflow]
---

# Session workflow — bootstrap, build, close

Mandatory procedure for human–agent sessions on this repo. Complements
[[STATE]] (current truth) and [[_index/dashboard/README|dashboard]] (visual
status at three zoom levels). Git writes stay on the **host shell** (D-001) per
[[host|constraints/host]].

## Roles

| Phase | Owner | Rule |
| :---- | :---- | :---- |
| **Plan** | Agent | Read canon; draft session plan from STATE bootstrap — **no branch, no edits** |
| **Proceed** | Human | Confirms plan (`proceed`, `start session N`, or edits scope) |
| **Execute** | Agent | Branch + STATE boot line + L3 focus; then build — **no commit** unless human asks |
| Build | Agent | Edit on branch; `validate_md.py --all` after each batch |
| Close draft | Agent | STATE + dashboard L1–L3 + S(N+1) bootstrap — **before merge is offered** |
| Validate | Human | Work diff **and** handoff docs (STATE + dashboard + bootstrap) |
| Merge | Human | Final `--all`; commit close batch if needed; merge → `main` (D-001 host shell) |

## Session open (Plan → Proceed → Execute)

**Triggers** (human): `start session N`, `session N boot`, or equivalent. Agent
**never** creates a branch or edits files on Plan alone.

### Phase 1 — Plan (agent, read-only)

1. Read [[Agents.md|Agents]] → [[STATE]] → `_index/dashboard/01-context.md`.
2. Copy **Next session bootstrap** from STATE into the plan (branch name,
   primary, load first, defer, human gate).
3. Reply using the **session plan shape** in [[Agents.md|Agents]] § Session
   start — scope future tense, questions, evidence table, decision rule.
4. **Stop.** Wait for human **proceed** or scope change.

Load only task-needed context per Agents.md — never the whole vault.

### Phase 2 — Execute (after human proceed)

1. Human runs branch creation (agent supplies PowerShell block):

   ```powershell
   git checkout main
   git checkout -b session-NN/<topic>
   ```

2. Agent appends boot line to STATE **Current position** (human commits later):

   `**Session NN (bootstrapped YYYY-MM-DD HH:mm — branch session-NN/<topic>):** <one sentence intent>.`

   Use host local time — see **Timestamps** below.

3. Agent updates `_index/dashboard/03-components.md` — active session row.
4. Agent begins **Build** on the session branch.

**Do not** commit bootstrap-only edits unless the human asks.

### Structured flow (state and evidence)

Dijkstra test for the harness session loop — answer: *current state, valid next
states, evidence of last transition.*

| State | Valid transitions | Evidence |
| :---- | :---------------- | :------- |
| Plan | → Proceed (human) | Session plan in chat |
| Execute (boot) | → Build | Boot line in STATE + L3 row |
| Build | → Close draft | Work diff + session artifact |
| Close draft | → Validate (human) | STATE + dashboard L1–L3 |
| Validate | → Merge (human) | `validate_md.py --all` green |

Human gates (Proceed, validate, merge) are **preconditions** for the next phase;
close draft is the **postcondition** evidence pass before merge is offered.

## Session close (agent draft → human validate → merge)

The agent completes the close checklist **before** suggesting merge. The human
validates **both** the session work **and** the handoff docs in one gate — then
runs git on the host shell (D-001) per [[host|constraints/host]]. **Never merge
with stale STATE or dashboard.**

### Order (non-negotiable)

| # | Who | Action |
| :-: | :--- | :------- |
| 1 | Agent | Close checklist A–D below (on session branch) |
| 2 | Agent | Supply PowerShell `git add` / `git commit` for close batch |
| 3 | Human | Validate work diff **and** STATE + dashboard L1–L3 + bootstrap |
| 4 | Human | `validate_md.py --all`; merge session branch → `main` |

Handoff docs are part of "done" — not a post-merge afterthought.

**Optional HTML gates:** For session loop gates, open `_views/gates/proceed.html`,
`_views/gates/validate.html`, or `_views/gates/merge.html` in a browser. Fill
the form, then **Copy as markdown** and paste into the session artifact or chat.
Markdown canon (`STATE.md`, dashboard, session artifacts) stays authoritative;
HTML is the review surface only.

### A. Verify

- [ ] `python scripts/validate_md.py --all` — 0 failures
- [ ] Relevant unit tests green (e.g. `test_context_loader.py`,
      `test_task_context.py`, `test_playground_archive.py`, `test_md_checks.py`)

### B. STATE.md

- [ ] Replace boot line with **closed** paragraph (what shipped, branch, merge note)
- [ ] **Open threads** table accurate (close / compress rows as needed)
- [ ] **Last 3 decisions** updated
- [ ] **Current branch** → `main` after merge instructions
- [ ] **Current position** — update Snapshot + Milestones; replace **Last closed
      session**; prepend **Recent sessions** table (max **four** rows); shift
      fifth row to [[session-position-archive]]; never append narrative paragraphs

### C. Dashboard (`_index/dashboard/`)

Update all three zoom files in one pass (same timestamp — see **Timestamps**
below):

- [ ] `01-context.md` — spine, validator count, session #, thread summary;
      **Git branch** row (git checkout branch — not a zoom level name)
- [ ] `02-containers.md` — per-chapter status table
- [ ] `03-components.md` — current focus, next actions, pending human decisions
- [ ] Append one row per file to each **History** table (max 10 rows; archive
      older rows to `context/system/sessions/dashboard-history-archive.md`)

History column header is **When** (not Date). Values include time — see
**Timestamps**.

### Timestamps

Before writing any session timestamp:

1. Read **host local time** — never assume the chat date:

   ```powershell
   python -c "from datetime import datetime; print(datetime.now().strftime('%Y-%m-%d %H:%M'))"
   ```

2. Format: **`YYYY-MM-DD HH:mm`** (24-hour, host local).
3. Apply to: dashboard History **When** column; `updated` frontmatter on
   files touched at close; STATE closed-session lines; closed-thread **Closed**
   column when the close happens in this session.

### D. Next-session bootstrap block

Copy into STATE under `## Next session bootstrap` (agent overwrites each close):

```markdown
## Next session bootstrap

**Branch:** `session-(N+1)/<topic>`
**Primary:** <thread ID + one-line goal>
**Load first:** Agents.md, STATE.md, _index/dashboard/01-context.md, <task files>
**Defer:** <explicit out-of-scope>
**Human gate:** <what Alex reviews before merge — work diff plus STATE and dashboard L1–L3>
```

### E. Git (human)

- [ ] Conventional Commits on session branch (agent supplies PS blocks)
- [ ] `git checkout main && git merge session-NN/<topic> && git branch -d session-NN/<topic>`
- [ ] Set **Git branch** in `_index/dashboard/01-context.md` Signal table to
      `main` (this is the git checkout branch — not "L1" or a dashboard zoom
      name)

Canvas at session close is **optional** (`canvases/project-state.canvas.tsx`) —
dashboard + STATE are **mandatory**.

**Roadmap documents:** multi-session arcs require **Target snapshot (SNN end state)**
— see [[roadmap-document-shape]] (mandatory section order + close rules).

## Batch discipline during build

After each logical batch:

1. Run `validate_md.py --all` (or scoped paths if pre-merge sweep pending).
2. Output PowerShell `git add` / `git commit` blocks — **do not commit** unless
   the human explicitly asks.

**Markdown tables:** rows must be consecutive (no blank lines between `| … |`
lines). Broken tables fail `validate_md` — see [[book-architecture]].

## Failure modes

| Symptom | Likely cause | Fix |
| :---- | :---- | :---- |
| Next agent loads wrong chapter | STATE / dashboard stale (D-004) | Close checklist C skipped |
| Merged but handoff stale | Human merged before close draft | Agent must finish A–D before offering merge |
| "Where are we?" every session | No zoom-level view | Read dashboard L1 → L2 → L3 |
| Branch created before proceed | Old bootstrap habit | Plan phase is read-only until human confirms |
| Work started on `main` | Execute skipped | Branch must exist before any file edits |
| Teaching bloat in agent context | Dual-purpose file not retrofitted | ADR-006 + `load_task_context()` |

## Reference

Full session prose history: [[session-docs]]. Improvement analysis:
`project-harness-improvement-proposal.md` (vault root).
