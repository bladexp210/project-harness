---
title: Reader product skeleton
chapter: 06
status: reference
audience: [novice, seasoned, both]
tags: [boilerplate, skeleton, fork, context]
---

# Reader product skeleton

Empty template for **your product repo** — not this harness. Mirrors the
three-layer `context/` tree from Ch. 04 (S22 worked example) plus a trimmed
`setup/` for git layout and design-tool choice.

> [!LEARN] Learn It
> The harness repo teaches with **harness-meta** context (`context/` in this
> book). Your product replaces Layer 2 and Layer 3 with distillations from
> [[02-design/layers/data|Ch. 02 layer designs]]. Layer 1 (`context/system/`)
> holds cross-cutting notes agents load on most tasks.

> [!TIP] Fast Track
> Copy this folder to a new repo root → fill the four architecture files →
> add one `implementation/<feature>/` file per bounded task → wire
> `context_load:` in task frontmatter.

## Fork steps

| Step | Action |
| :--: | :----- |
| 1 | Create a new directory (or git repo) for your product — separate from the book harness |
| 2 | Copy **everything** under `reader-skeleton/` to that repo root (`context/`, `constraints/`, `setup/`, `_templates/`, this README) |
| 3 | Fill `constraints/host.md` — OS, shell, copy-paste block language (D-001) |
| 4 | Read `setup/design-tools/README.md` — pick one design tool for Ch. 01–04 |
| 5 | Fill `_templates/tooling-manifest.md` — execution product adapters (Track B hub) |
| 6 | Read `setup/execution-tools/README.md` — VS Code hub + Track A when ready |
| 7 | Rename `README.md` to your project README or merge its sections into your own |
| 8 | Fill `context/architecture/*` from your Ch. 02 layer files (one file per domain) |
| 9 | Add `context/implementation/<feature>/` when a task needs narrow context beyond architecture |
| 10 | Copy agent yaml + `_templates/new-task.md` from the book; list paths in each task's `context_load:` |
| 11 | Follow `setup/README.md` for git layout (single clone ramp → bare + worktrees when ready) |
| 12 | Open `_views/project/index.html` in browser for project status; copy `arc/_template/roadmap.html` when starting a multi-session arc |

## Layout (mirrors S22)

```text
your-product/
├── README.md              ← project identity + how to run (you write)
├── _views/                ← HTML project dashboard, arc/session templates, gates
├── constraints/
│   └── host.md            ← machine + shell (D-001 instance)
├── _templates/
│   ├── tooling-manifest.md ← Track B product seam
│   └── host-profile.md    ← optional; or use constraints/host.md only
├── setup/
│   ├── README.md          ← git layout (trimmed from bare-worktree doc)
│   ├── design-tools/
│   │   └── README.md      ← design-tool choice (Ch. 01–04)
│   └── execution-tools/
│       └── README.md      ← VS Code hub checklist (Ch. 05+)
└── context/
    ├── README.md          ← layer map + wiring
    ├── system/            ← cross-cutting orientation
    ├── architecture/
    │   ├── data/          ← Ch. 02 data layer distillation
    │   ├── application/
    │   ├── communication/
    │   └── ux/
    └── implementation/
        └── <feature>/     ← one folder per bounded feature or task slice
```

## What stays empty vs what you fill

| Path | Skeleton provides | You provide |
| :---- | :---- | :---- |
| `context/architecture/*` | One-line hint per domain | Full distillation from Ch. 02 |
| `context/system/` | Placeholder README | Glossary, conventions, constraint pointers |
| `context/implementation/` | `_example-feature/` slot | Real feature folders as tasks multiply |
| `setup/` | Ramp + target git layout; design + execution tool checklists | Your paths, manifest fill, tool choice |
| `constraints/host.md` | Concern rows (empty product column) | OS, shell, block language |
| `_templates/tooling-manifest.md` | Concern rows (empty product column) | Your IDE, extensions, CLI agent names |
| App code, runbooks, decommission | — | Ch. 05–08 product work in your repo |

## Verify wiring

After your first task file exists:

```powershell
# From the book harness (if you copied scripts) or your CI later:
python scripts/task_context.py path/to/your-task.md
```

Preview stripped context before sending to an agent. See
[[context/README|context/README.md]] in the harness for the full layer map.

## Reference in this book

| Topic | Where |
| :---- | :---- |
| Context tree pattern | `context/README.md` (harness-meta example) |
| Engineering handoff | [[engineering-handoff-checklist]] |
| Populate context (task 03) | [[tasks/03-populate-context-tree]] |
| Git bare + worktrees (full) | [[bare-worktree-setup]] |
| Agent contracts | Ch. 04 `agents/*.yaml` |
