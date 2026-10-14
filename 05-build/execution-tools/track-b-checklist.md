---
title: Track B execution checklist
chapter: 05
status: in-progress
audience: [novice, seasoned, both]
tags: [execution, track-b, checklist]
---

# Track B — generic execution checklist

Use this when **Track B** applies per [[ADR-007-dual-execution-tracks]]: you
run tasks through an IDE or CLI agent (Cursor, Claude Code, Codex, OpenCode,
Jules, Antigravity, or any successor product) instead of OpenHands.

The book documents **one execution contract**. Your tool adapts it — rules
files, @-mentions, MCP, project memory, whatever that product calls the same
concerns.

> [!LEARN] Learn It
> Track A ([[openhands]]) is **ideal** — Docker sandbox + LiteLLM/OpenRouter.
> Track B is **fallback** when setup confidence or subscription billing fits
> better today. The harness does not change: same task files, same gates.

> [!TIP] Fast Track
> Worktree on session branch → `task_context.py` → paste into agent with role
> + scope → review diff → `validate_md.py --all` → commit on Windows (D-001).
> Map each step to your product's docs in [§7 Adapter](#7-adapter-map-the-checklist-to-your-tool).

## Before you start

| Check                    | Pass when                                                                                                                       |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| Track B is honest choice | [[ADR-007-dual-execution-tracks]] drivers say you are not ready for Track A yet, or you are doing harness meta-work on the ramp |
| Tool picked              | One IDE/CLI agent; you know where its **rules**, **context**, and **diff UI** live                                              |
| Git layout               | Session branch checked out in a **worktree** — [[bare-worktree-setup]]                                                          |

## 1. Workspace — isolate git state

|  #  | Do                                                                                                          | Secure against                           |
| :-: | :---------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
| 1.1 | Open the repo in **one worktree** on branch `session-NN/<topic>`                                            | Editing on `main` by accident            |
| 1.2 | Confirm `git status` shows only expected files before the agent runs                                        | Stray changes from another session       |
| 1.3 | List every path you will allow edits on **before** prompting (from task **Scope — modify**)                 | Scope creep into Layer 1/2 context files |
| 1.4 | Prefer bare repo + worktrees when ready — [[bare-worktree-setup]]; a single clone is an acceptable **ramp** | Parallel checkouts of the same branch    |

**Adapter hint:** point the IDE workspace root at the worktree directory, not
the bare hub.

## 2. Context — stripped inputs only

| # | Do | Secure against |
| :-: | :--- | :------------- |
| 2.1 | Run `python scripts/task_context.py <task.md>` | Loading raw dual-purpose chapter files (ADR-006 bloat) |
| 2.2 | Paste loader output into the agent **or** attach it and state it overrides raw files | Agent reading `[!LEARN]` / `[!TEACH]` prose as instructions |
| 2.3 | Include the task markdown (or path) in the prompt | Missing scope or Gherkin |
| 2.4 | Verify teaching callouts are absent from pasted context | Token waste and contradictory guidance |

```powershell
New-Item -ItemType Directory -Force -Path .build-context | Out-Null
python scripts/task_context.py 04-your-agents/tasks/01-threat-model-premortem.md `
  > .build-context/task-context.md
```

Review `.build-context/task-context.md` before sending.

## 3. Identity — same agent role as Ch. 04

| # | Do | Secure against |
| :-: | :--- | :------------- |
| 3.1 | Set prompt header: "You are the {role} from `agents/<name>.yaml`" | Generic "helpful coding assistant" drift |
| 3.2 | Name the task file and agent yaml explicitly | Wrong mandate or model persona |
| 3.3 | Treat yaml `model` as advisory unless wired to LiteLLM | Assuming subscription model matches yaml alias |

## 4. Execution — bounded transformation

|  #  | Do                                                                   | Secure against              |
| :-: | :------------------------------------------------------------------- | :-------------------------- |
| 4.1 | Restate **Scope — modify** and **read-only** lists in the prompt     | Files changed outside scope |
| 4.2 | Require Gherkin evidence: quote each `Then` with proof before "done" | False completion            |
| 4.3 | Escalate if a change would touch Layer 1/2 context or need an ADR    | Silent architecture edits   |
| 4.4 | One logical batch per review cycle (per [[session-workflow]])        | Mixed commits               |

## 5. Safety — gates the tool cannot override

| # | Do | Secure against |
| :-: | :--- | :------------- |
| 5.1 | **Disable or avoid** IDE auto-commit / auto-push to `main` | Bypassing human review |
| 5.2 | Run **all git write operations on the host shell** (D-001) — see [[host\|constraints/host]] | NUL-corrupted `.git` from sandbox terminals |
| 5.3 | Never paste secrets into chat; confirm `.env` is gitignored | Credential leakage |
| 5.4 | Do not use `--no-verify` unless you explicitly intend to skip hooks | Broken validator / gitleaks |
| 5.5 | Keep agent terminal out of git when the IDE runs in a remote sandbox | D-001 violation |

## 6. Close — human owns the commit

| # | Do | Secure against |
| :-: | :--- | :------------- |
| 6.1 | Review full diff in the IDE or Obsidian | Missed scope violations |
| 6.2 | `python scripts/validate_md.py --all` (or scoped paths for the batch) | Frontmatter / budget / NUL failures |
| 6.3 | Commit with Conventional Commits on **host shell**; agent suggests message only | Non-revertible batch commits |
| 6.4 | Update task status / dashboard when closing a session (if applicable) | STATE drift |

```powershell
python scripts/validate_md.py --all
git add <files>
git commit -m "type(scope): subject" -m "Body with why."
```

## 7. Adapter — map the checklist to your tool

The book stops at **concerns**. Fill `_templates/tooling-manifest.md` (copy to
your repo) with product names, then mirror one-line adapters into
`constraints/project.md`. See [[vscode-hub]] and [[ADR-010-vscode-hub-barbell]].

| Concern (this checklist) | Typical product feature names |
| :----------------------- | :---------------------------- |
| IDE shell | VS Code, Cursor, Windsurf — workspace root = worktree |
| Persistent rules | "Rules", "Instructions", `AGENTS.md`, `.cursor/rules/` |
| Scoped files | @-mentions, file picks, "codebase search" |
| Stripped context | Paste buffer, attached markdown, project docs |
| Diff review | Source control panel, inline diff |
| Model choice | Settings, subscription tier, API key |
| Automation hooks | `.cursor/hooks.json` → `langfuse_trace_bridge` | [[path-c-hook-contract]] |

**Your job:** for each row in §1–§6, write one line in the manifest and in
`constraints/project.md` that points your product at the harness artifact. When
the vendor renames a feature, update **your manifest and adapter lines** — not
the book.

## Prompt shell (copy and fill)

```markdown
You are the {role} for this project ({agent}.yaml).

## Task
{task file path or pasted task markdown}

## Loaded context (ADR-006 stripped — authoritative)
{paste task_context.py output}

## Rules
- Modify only: {Scope — modify list}
- Read-only: {read-only list}
- Quote each Gherkin Then clause with evidence before claiming done
- Escalate if a change would touch Layer 1/2 context files or need an ADR
```

## When to move to Track A

Re-read ADR-007 decision drivers. When Docker + LiteLLM/OpenRouter is viable,
run the next build task through [[openhands]] — same task file, same
`task_context.py`, different runtime.

## Reference

- Hub pattern: [[vscode-hub]]
- Host profile: [[host|constraints/host]]
- Tooling manifest: [[tooling-manifest|_templates/tooling-manifest.md]]
- Decisions: [[ADR-007-dual-execution-tracks]] · [[ADR-010-vscode-hub-barbell]]
- Path C hooks: [[path-c-hook-contract]]
- Track A guide: [[openhands]]
- Git layout: [[bare-worktree-setup]]
- ICOM+ Track B examples: [[icom-plus-examples-trackb]]
