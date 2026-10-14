---
title: Git setup (reader skeleton)
chapter: 06
status: template
audience: [novice, seasoned, both]
tags: [git, worktree, setup, skeleton]
---

# Git layout — reader product

Trimmed from [bare-worktree-setup](../../../../05-build/execution-tools/bare-worktree-setup.md). Replace `my-project` with your product
name and paths with your host folders.

## Maturity levels

| Level | Layout | When |
| :---- | :----- | :--- |
| **Ramp** | One normal clone, session branch `session-NN/<topic>` | First tasks; solo authoring |
| **Target (one worktree)** | Bare hub + one session worktree | First Track A run or parallel IDE + agent |
| **Target (full)** | Bare hub + N worktrees | Parallel agents; each branch in its own directory |

## Directory layout (target)

```text
Host
├── my-project.git/           ← bare hub (object store only)
└── worktrees/
    ├── main-review/          ← optional human merge checkout
    └── session-NN-topic/     ← IDE or OpenHands mount
```

**Rule:** one branch cannot be checked out in two worktrees at once.

## Scaffold path — bare hub + first worktree

| Step | PowerShell (edit paths) |
| :--: | :---- |
| 1 | `mkdir C:\Projects\my-project-hub; cd C:\Projects\my-project-hub` |
| 2 | `git init --bare my-project.git` |
| 3 | `git clone C:\Projects\my-project-hub\my-project.git C:\Projects\worktrees\my-project-main` |
| 4 | Session branch: `git checkout -b session-01/first-feature` in the worktree |

## Single-clone ramp (start here)

Valid until you need parallel checkouts or Track A Docker mounts:

```powershell
git clone <your-remote-or-path> my-product
cd my-product
git checkout -b session-01/first-feature
```

Upgrade to bare + worktrees before parallel agents share one working tree.

## Protected branch

Keep `main` merge-only after human review — same session ritual as the book
([session-workflow](../../../../context/system/session-workflow.md)). Commits on session branches; merge when the task closes.
