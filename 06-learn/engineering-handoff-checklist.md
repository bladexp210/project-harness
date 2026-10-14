---
title: Engineering handoff checklist
chapter: 06
status: reference
updated: 2026-07-02 18:14
session: 47
tags: [handoff, poc, engineering]
---

# Engineering handoff checklist

Solo POC → engineering day-1. Complete before inviting a second contributor
or forking to a product repo. Complements per-session
[session close checklist](boilerplate/specs/harness-session-close-checklist.md).

## When to use

- End of S41–S47 post-arc42 arc (this harness)
- Before copying [reader-skeleton](boilerplate/reader-skeleton/README.md) to a new repo
- Before granting write access to engineering

## Checklist

| # | Area | Action | Pass when |
| :-: | :---- | :------- | :-------- |
| 1 | **Governance** | Reader has `Agents.md`, `STATE.md`, dashboard L1–L3 | Session loop documented; validator green |
| 2 | **Architecture** | `02-design/arc42/` §1–§12 + ADRs 001–011 | Engineering can answer "why" without chat history |
| 3 | **Plan** | `03-plan/PROJECT-PLAN.md`, golden tasks, constraints | Bounded tasks + regression fixtures exist |
| 4 | **Agents** | Five role yaml + `context/` tree + tasks 01–04 done | `context_loader.py` resolves paths |
| 5 | **Build** | Track A compose + Track B hub + Path C hooks | Smoke trace passed (Langfuse + session log) |
| 6 | **Learn** | Post-mortem template + RCA picker + boilerplate | Failure loop closes to constraints |
| 7 | **Operate** | Runbook example + Docker hygiene table | Local stack recovery documented |
| 8 | **Sunset** | Decommission template + decision tree | Kill criteria priced at design time |
| 9 | **CI** | GitHub Actions runs `validate_md.py --all` on push | Actions green on `main` |
| 10 | **Remote** | `origin` on work GitHub; local git identity set | `git push` succeeds (D-001 host shell) |
| 11 | **Fork path** | `reader-skeleton/` copied or linked | Product repo has own `constraints/host.md` |
| 12 | **Observability** | ADR-009 Paths A/B/C documented; Path C live | Process trace (STATE/git) + Langfuse replay |
| 13 | **Inbox** | S41 triage executed; `_inbox/` consumed or deferred | No orphan promote rows |
| 14 | **Secrets** | `.env` never committed; keys rotated if exposed | `git log` clean for credentials |
| 15 | **HTML views** | `_views/project/index.html` opens in browser | Mission, phase, milestones visible; arc template ready |

## Fork quick path

| Step | Command / path |
| :--: | :---- |
| 1 | Copy `06-learn/boilerplate/reader-skeleton/` to new repo root |
| 2 | Fill `constraints/host.md` + `_templates/tooling-manifest.md` |
| 3 | Wire CI from `.github/workflows/validate-md.yml` (adjust paths if needed) |
| 4 | Create GitHub repo; set local `user.name` / `user.email` for that org |
| 5 | First session: `Agents.md` equivalent + `STATE.md` bootstrap |

## Out of scope at handoff (by design)

| Item | Why deferred |
| :---- | :---- |
| Branch protection / required reviews | Solo until team scale |
| Multi-team Langfuse routing | Post-handoff infra |
| Reader product runbooks (Ch. 07 Type A) | Engineering fills for product |
| arc42 CLI / SaaS product fork | Post-handoff polish |

## Reference map

| Question | Start here |
| :---- | :---- |
| What is this repo? | `00/README.md`, `_index/dashboard/01-context.md` |
| How do sessions work? | [session-workflow](../context/system/session-workflow.md), `STATE.md` |
| How do I run agents? | [vscode-hub](../05-build/execution-tools/vscode-hub.md), `04-your-agents/` |
| How do I trace failures? | [ADR-009-observability-paths-abc](../02-design/decisions/ADR-009-observability-paths-abc.md), `06-learn/post-mortems/README.md` |
| How do I shut down cleanly? | `08-sunset/README.md` |
