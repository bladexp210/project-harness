---
title: Getting started
chapter: 00
status: in-progress
audience: [novice, seasoned, both]
tags: [orientation, setup, onboarding]
updated: 2026-07-03
---

# Getting started

**Purpose:** Get from clone to first working session in one sitting — without
reading the whole book first.

> [!TIP] Fast Track
> Clone → open Obsidian → read [[manifesto]] → pick a path below → run the
> **Day 1 checklist** → stop when the success check passes.

---

## Step 1 — Choose your path

You need exactly one path. Mixing them on day one causes confusion.

| Path | You want to… | Start in | Done when… |
| :---- | :----------- | :------- | :--------- |
| **A — Learn the method** | Study how the book works using its own examples | This repo (harness) | You finish Ch. 01 with the book's sample roles and use cases |
| **B — Build your product** | Apply the method to *your* software | [[06-learn/boilerplate/reader-skeleton\|reader-skeleton]] (copy to a new repo) | You run one bounded task and commit a real change in *your* repo |

| Path | Do **not** do on day one |
| :---- | :----------------------- |
| A | Fork `reader-skeleton`, fill arc42, or learn session-NN workflow |
| B | Read all of Ch. 02–04 before writing one task file |

**Harness-meta vs your product:** This repo documents *itself* as the worked
example. Path A explores that. Path B copies the empty template and replaces
book examples with your decisions.

---

## Step 2 — Install prerequisites

| Tool | Required | Why |
| :---- | :------- | :-- |
| **Git** | Yes | Every change stays reversible |
| **Obsidian** | Yes (Path A); recommended (Path B) | Wiki-links, callouts, and Mermaid render correctly |
| **Python 3** | Yes | Validator and task-context scripts |
| **One AI editor or agent** | Yes | Design and build work (see default stack below) |

Open the clone as an **Obsidian vault** (the repo root folder). GitHub's web
view shows markdown but breaks `[[wiki-links]]` — that is expected.

**Verify Python and git:**

```powershell
python --version
git --version
```

Use your host shell for git writes. See `_templates/host-profile.md` when you
fill `constraints/host.md` for your machine (Path B).

---

## Step 3 — Default stack (recommended)

You can change tools later. Pick one default now to avoid paralysis.

| Layer | Default | Alternative |
| :---- | :------ | :------------ |
| **Design (Ch. 01–04)** | Cursor (same window as code) | [[setup/design-tools/cowork\|Cowork]], [[setup/design-tools/antigravity\|Antigravity]] |
| **Build (Ch. 05+)** | Track B — IDE/CLI agent in your editor | Track A — OpenHands + Docker ([[05-build/execution-tools/track-a-setup\|track-a-setup]]) |
| **Git layout** | Single clone + session branch | Bare repo + worktrees ([[bare-worktree-setup]]) — defer until parallel agents |

Full tool indexes (when you outgrow the default):

- Design: [[setup/design-tools/README|design-tools index]]
- Build: [[setup/execution-tools/README|execution-tools index]]

---

## Path A — Learn the method (this repo)

### Day 1 checklist

| # | Do | Pass when |
| :-: | :--- | :-------- |
| 1 | Clone the repo and open it as an Obsidian vault | Wiki-links resolve; Mermaid renders in Ch. 00 |
| 2 | Read [[manifesto]] (one page) | You can state who owns decisions vs who executes |
| 3 | Run the validator | Command exits 0 (see below) |
| 4 | Read [[01-understand/user-roles\|user-roles]] and [[01-understand/use-cases\|use-cases]] | You see how the *book* filled its own examples |
| 5 | Skim [[Agents.md]] only if you use an AI co-author in this repo | You know agents load [[STATE]], not every file |

**Validator (from repo root):**

```powershell
python scripts/validate_md.py --all
```

**Optional — preview how agents load context:**

```powershell
python scripts/task_context.py 04-your-agents/tasks/01-threat-model-premortem.md
```

Review the output: teaching callouts (`[!LEARN]`, `[!TIP]`) should be stripped.

### What to defer (Path A)

| Defer until… | Topic |
| :----------- | :---- |
| You maintain the book repo | [[STATE]], dashboard, session-NN branches, [[context/system/session-workflow\|session-workflow]] |
| You run parallel agents | [[bare-worktree-setup]] |
| Ch. 02 in earnest | arc42, threat model, full ADR set |
| Ch. 05 | Track A Docker stack |

Maintainer orientation: [[maintainers|For book maintainers]].

### Path A — success check

You are set up when all three are true:

1. Obsidian opens the vault and links work.
2. `python scripts/validate_md.py --all` exits 0 on your clone.
3. You know your next file: [[01-understand/user-roles|Ch. 01 — user roles]].

---

## Path B — Build your product (reader-skeleton)

### Day 1 checklist

| # | Do | Pass when |
| :-: | :--- | :-------- |
| 1 | Create a **new** directory or git repo for your product | Separate from the book harness |
| 2 | Copy everything under `06-learn/boilerplate/reader-skeleton/` to that repo root | `context/`, `constraints/`, `setup/`, `_templates/` present |
| 3 | Fill `constraints/host.md` — OS, shell, copy-paste block language | Agent-supplied commands match your machine |
| 4 | Write a one-paragraph `README.md` — product name, one sentence on what it does | A stranger knows what you are building |
| 5 | Fill **one** file in `context/architecture/` (start with application or data) | One distillation from your intent — not empty placeholders |
| 6 | Copy `_templates/new-task.md` from the book; write **one** task under `tasks/` | Task has Scope — modify and Gherkin `Then` lines |
| 7 | Copy `scripts/task_context.py` and `scripts/context_loader.py` from the book (or run from harness path) | Loader runs on your task file |
| 8 | Run the task through your editor agent (Track B) | Diff stays inside Scope — modify |
| 9 | Commit on your host shell | One atomic commit with a clear message |

**Git ramp (single clone):**

```powershell
git clone <your-remote> my-product
cd my-product
git checkout -b session-01/first-feature
```

**Task context preview:**

```powershell
python scripts/task_context.py tasks/your-first-task.md
```

Execution ritual: [[05-build/execution-tools/track-b-checklist|Track B checklist]].

### What to defer (Path B)

| Defer until… | Topic |
| :----------- | :---- |
| Second parallel agent | Bare repo + worktrees ([[06-learn/boilerplate/reader-skeleton/setup/README\|skeleton git setup]]) |
| Ch. 02 complete | All four architecture files, arc42, threat model |
| Observability | Langfuse bridges, Path C hooks |
| HTML views | `_views/` dashboard — optional status UI |

Full fork reference: [[06-learn/boilerplate/reader-skeleton/README|reader-skeleton README]].

### Path B — success check

You are set up when all four are true:

1. Your product repo exists **outside** the book harness.
2. One task file has bounded scope and acceptance criteria.
3. `task_context.py` produces stripped context for that task.
4. One commit on a session branch contains a real change from that task.

---

## Step 4 — First session (both paths)

A **session** is one bounded unit of work — one task or one chapter section —
with a clear done state. You do not need the full 47-session apparatus on day one.

| Step | Action |
| :--: | :----- |
| 1 | Name what you will finish today (one sentence) |
| 2 | Open only the files that task touches |
| 3 | Work with your AI agent using stripped context (`task_context.py`) |
| 4 | Review the diff against Scope — modify |
| 5 | Run validator if you changed markdown in the harness repo |
| 6 | Commit on your **host shell** — not the agent sandbox if your host profile says so |

**Path A first session:** Complete [[01-understand/user-roles|user-roles]] exercises
for *your* hypothetical product — or study the book's filled examples if you are
still learning the shape.

**Path B first session:** Ship the smallest useful change from task 1 — a script,
an API stub, a test, one screen. Measure whether the method helped; note where
it got in the way.

---

## Step 5 — Prove it works (your experiment)

The method earns trust through outcomes, not prose. After your first session,
capture **one honest line**:

| Question | Your answer |
| :------- | :---------- |
| What shipped? | (file, feature, or learning artifact) |
| Did bounded tasks help? | yes / no / partly — where |
| Did context stripping help? | yes / no — token noise, wrong instructions |
| What ceremony got in the way? | (name it — defer or cut it) |

Keep this note in your product repo or a personal log. One external artifact beats
ten more process docs.

---

## Where to go next

| After day one | Link |
| :------------ | :--- |
| Philosophy | [[manifesto]] |
| Chapter journey | [[README\|Ch. 00 — Start Here]] |
| Plan your product | [[03-plan/PROJECT-PLAN\|PROJECT-PLAN]] |
| Configure agents | [[04-your-agents/README\|Ch. 04]] |
| Build | [[05-build/README\|Ch. 05]] |
| Known book compromises | [[06-learn/DEBT-LEDGER\|DEBT-LEDGER]] |

**Stuck?** Re-read [Step 1](#step-1--choose-your-path). Most day-one confusion
is picking both Path A and Path B at once.
