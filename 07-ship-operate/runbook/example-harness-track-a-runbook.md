---
title: "Harness runbook: validator and Track A stack"
chapter: 07
status: reference
tags: [runbook, harness-meta, validator, track-a]
service: project-harness-dev
environment: local
updated: 2026-06-23
---

# Runbook — harness-meta (this book repo)

Worked **harness-meta** example: operating the book harness locally —
markdown validator, pre-commit gate, and Track A execution stack. Not a
production SaaS runbook; shows the template filled for a real repo.

## Service overview

| Field | Value |
| :---- | :---- |
| **Owner** | Human orchestrator (reader) |
| **Purpose** | Keep canon clean and Track A stack available for agent tasks |
| **Dependencies** | Python 3, Docker, OpenRouter account (Track A only) |
| **Repo** | `project-harness` on session branch |

## Deploy log

| Date | Version / commit | Action | Approved by |
| :---- | :---- | :---- | :---- |
| *(example)* | `main` @ session merge | Merge session branch after `validate_md.py --all` green | human |

**Promotion rule:** no merge to `main` without validator 0 failures (D-001:
git on Windows only).

## Health checks

| Check | Command | Pass when | Frequency |
| :---- | :---- | :---- | :---- |
| Markdown validator | `python scripts/validate_md.py --all` | `0 failed` | pre-commit, pre-merge |
| Context loader tests | `python scripts/test_context_loader.py` | all pass | after `context/` edits |
| Task context tests | `python scripts/test_task_context.py` | all pass | after task template edits |
| Track A stack | `docker compose -f 05-build/execution-tools/track-a/docker-compose.yml ps` | services `running` | before OpenHands task |
| LiteLLM proxy | `curl http://127.0.0.1:4000/health/liveliness` | HTTP 200 | before OpenHands task |
| OpenHands UI | browser `http://127.0.0.1:3000` | UI loads | before OpenHands task |

## Incident playbook

### INC-1 — Validator fails on merge

| Step | Action |
| :---- | :---- |
| 1 | Read failure path in output — budget WARN vs hard FAIL |
| 2 | Fix canon file or renegotiate budget per [DEBT-LEDGER](../../06-learn/DEBT-LEDGER.md) |
| 3 | Re-run `validate_md.py --all` |
| 4 | If near-miss caught pre-merge → optional post-mortem in `06-learn/post-mortems/` |

### INC-2 — Track A stack won't start

| Step | Action |
| :---- | :---- |
| 1 | Check Docker daemon: `docker version` |
| 2 | Check `.env` in `track-a/` — keys present, not committed |
| 3 | `docker compose ... logs litellm` / `openhands` |
| 4 | See [track-a-setup](../../05-build/execution-tools/track-a-setup.md) troubleshooting; log blocker ADR if upstream break |

### INC-3 — Stale file bytes from sandbox (D-001)

| Step | Action |
| :---- | :---- |
| 1 | **Do not** `git commit` from agent sandbox if Windows wrote the file |
| 2 | Run git on Windows PowerShell only |
| 3 | If NUL-padding seen → strip and re-run validator |

## Recurring tasks

| Task | Cadence | Procedure |
| :---- | :---- | :---- |
| Session close validator | every session | `validate_md.py --all` before merge offer |
| STATE + dashboard sync | every session | [harness-session-close-checklist](../../06-learn/boilerplate/specs/harness-session-close-checklist.md) |
| Track A `.env` key rotation | quarterly or on leak | OpenRouter revoke + reissue; update local `.env` only |
| Dependency pin review | quarterly | `docker-compose.yml` image tags; [constraints/project](../../03-plan/constraints/project.md) Models table |

## Docker hygiene (Track A compose)

Production patterns applied to `05-build/execution-tools/track-a/docker-compose.yml`
(S47 promotion). Check on quarterly pin review or after upstream image bumps:

| Pattern | Where in compose | Pass when | When NOT to apply |
| :---- | :---- | :---- | :---- |
| Layer ordering | N/A (images, not build) | Image tags pinned; not `:latest` in prod forks | Product uses only managed PaaS — no compose |
| Health + depends_on | `db`, `litellm`, Langfuse stack | `docker compose ps` shows healthy before OpenHands | Single-container dev without dependencies |
| Resource limits | `deploy.resources.limits` on services | No OOM during normal dev session | Local-only throwaway experiment |
| Log rotation | `logging.options max-size/max-file` | Disk stable after week of use | Ephemeral CI runner torn down hourly |
| Host bind | `127.0.0.1:` on exposed ports | Services not reachable from LAN | Deliberate LAN demo with firewall rules |
| Secrets | `.env` only; `${VAR:?}` for Langfuse boot keys | No keys in git; `.env` in `.gitignore` | Org secret manager replaces `.env` in prod |
| Privilege | `security_opt: no-new-privileges` on app services | Present on `litellm`, `openhands` | Root-required legacy image — replace image instead |

**Reader fork:** multi-stage Dockerfile guidance lives in inbox archive; this
harness uses upstream images — apply build-stage patterns when you containerize
your product app.

## Retirement notes

When **retiring** a harness capability (not whole-repo sunset — see Ch. 08):

- Document deprecate → migrate → remove per [ADR-003-removal-vocabulary](../../02-design/decisions/ADR-003-removal-vocabulary.md)
- Example: retiring Track B-only path while keeping Track A — update
  `05-build/README.md` and runbook health checks; post-mortem if users
  depended on removed path

## Contacts and escalation

| Role | This harness |
| :---- | :---- |
| Operator | human reader |
| Agent execution | [dev-agent](../../04-your-agents/agents/dev-agent.yaml) via [openhands](../../05-build/execution-tools/openhands.md) |
| Escalation | human gate — no unattended prod (N/A for local harness) |

## Change log

| Date | Change | Author |
| :---- | :---- | :---- |
| 2026-06-23 | Initial harness-meta example (S24) | session-24 |
