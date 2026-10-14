---
title: Bare repo and worktrees
chapter: 05
status: in-progress
audience: [novice, seasoned, both]
tags: [execution, git, worktree, isolation]
---

# Bare repo + worktrees — shared git layout

Set up one git layout that both **Track A** ([openhands](openhands.md)) and **Track B**
([track-b-checklist](track-b-checklist.md)) use. A **bare hub** holds objects; **worktrees** give
each session or agent its own checkout, branch, and index.

> [!LEARN] Learn It
> **Why bare + worktrees:** git isolates blast radius at Layer 2 in the
> [overview](../../context/system/overview.md) stack. Docker (Track A) isolates process at Layer 3. They stack —
> worktrees are not Track B-only. See [ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md).

> [!TIP] Fast Track
> Not ready for bare yet? Use a **single clone** on `session-NN/<topic>` — valid
> ramp. Upgrade to bare + worktrees before parallel agents or OpenHands mounts.
> Jump to [Single-clone ramp](#single-clone-ramp).

## Maturity levels

| Level | Layout | When |
| :---- | :----- | :--- |
| **Ramp** | One normal clone, session branch | First tasks; harness authoring today |
| **Target (one worktree)** | Bare hub + one session worktree | First Track A run; IDE opens worktree root |
| **Target (full)** | Bare hub + N worktrees (+ N Docker mounts for Track A) | Parallel agents; each branch in its own directory |

Track B does not change when you adopt bare + worktrees — you still open **one
worktree** in the IDE and run git on Windows (D-001). Track A **adds** mounting
that same worktree into OpenHands.

## Directory layout (target)

```text
Host (Windows — git author per D-001)
├── my-project.git/           ← bare hub (object store only)
└── worktrees/
    ├── orchestrator/         ← human review / merge (optional)
    ├── session-19-topic/     ← Track B: IDE workspace
    └── agent-task-01/        ← Track A: OpenHands mount
```

*This shows where each checkout lives so agents and humans never share one working tree.*

Git rule: **one branch cannot be checked out in two worktrees at once.**

## Scaffold path — bare hub + first worktree

Replace `my-project` and paths with your project name and parent folder.

| Step | Action |
| :--: | :----- |
| 1 | Create parent folder and initialize bare hub |
| 2 | Add first worktree on `main` |
| 3 | Add session worktree on `session-NN/<topic>` |
| 4 | Open the **session worktree** in IDE or mount in OpenHands — never the bare hub |

```powershell
# 1 — parent folder + bare hub
New-Item -ItemType Directory -Path C:\Projects\my-project -Force | Out-Null
Set-Location C:\Projects\my-project
git init --bare my-project.git

# 2 — orchestrator worktree (optional; human merge/review)
git -C my-project.git worktree add worktrees\orchestrator main

# 3 — session worktree (Track B IDE or Track A mount)
git -C my-project.git worktree add worktrees\session-19-topic -b session-19/ch05-worktree-doc

# 4 — verify
git -C worktrees\session-19-topic status
git -C my-project.git worktree list
```

**Pass when:** `worktree list` shows each path and branch; `git status` in the
session worktree shows the expected branch only.

### Add another worktree later

```powershell
git -C my-project.git worktree add worktrees\agent-task-02 -b agent/task-02
```

Remove when done (discards uncommitted changes in that worktree):

```powershell
git -C my-project.git worktree remove worktrees\agent-task-02
```

## Single-clone ramp

Use this when bare setup feels heavy. Same session discipline applies.

| Step | Action |
| :--: | :----- |
| 1 | Clone once: `git clone <url> my-project` |
| 2 | `git checkout -b session-NN/<topic>` |
| 3 | Open **that clone folder** in IDE; mount **that folder** in OpenHands |
| 4 | Plan upgrade to bare + worktrees before parallel agents |

The ramp is **documented**, not the ideal end state — see pre-mortem in
[ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md).

## Session worktree workflow

Every session uses one branch in one worktree per [session-workflow](../../context/system/session-workflow.md):

| Phase | Git action |
| :---- | :----------- |
| Open | Create or checkout `session-NN/<topic>` in a dedicated worktree |
| Build | Agent edits only on that branch; human reviews diff |
| Close | Merge session branch → `main` on Windows (D-001); remove worktree if disposable |

Never commit session work directly to `main` without the close ritual.

## Track A — OpenHands mount

| Rule | Detail |
| :---- | :----- |
| Workspace root | **One worktree directory** — not the bare hub |
| Branch | Session branch checked out in that worktree |
| Parallel agents | One container per worktree; each mounts a different path |
| Git writes | Human runs on Windows host (D-001) — not inside the container |

See [openhands](openhands.md) for Docker setup and prompt assembly.

## Track B — IDE workspace

| Rule | Detail |
| :---- | :----- |
| Workspace root | **Session worktree folder** — not `my-project.git` |
| Branch | `session-NN/<topic>` checked out in that worktree |
| Git writes | Windows PowerShell only (D-001) |

See [track-b-checklist](track-b-checklist.md) §1 — workspace steps unchanged; this doc supplies
the target layout they reference.

## Common mistakes

| Mistake | Fix |
| :------ | :-- |
| IDE opens bare hub | Point workspace at `worktrees/<name>/` |
| Same branch in two worktrees | `git worktree list`; remove or switch one checkout |
| Agent commits from sandbox terminal | All `git add` / `commit` / `merge` on Windows (D-001) |
| OpenHands mounts repo root with wrong branch | Mount the worktree path where the session branch is checked out |

## When not to use bare + worktrees yet

| Situation | Stay on ramp |
| :-------- | :----------- |
| First hour with git | Single clone + session branch |
| One agent, one session | Ramp is enough |
| Reader has not finished Ch. 00 git basics | Complete clone workflow first |

## Reference

- Decision: [ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md) — git layout section
- Track A: [openhands](openhands.md)
- Track B: [track-b-checklist](track-b-checklist.md)
- Session ritual: [session-workflow](../../context/system/session-workflow.md)
- Blast-radius stack: [overview](../../context/system/overview.md)
