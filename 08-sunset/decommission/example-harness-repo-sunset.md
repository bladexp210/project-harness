---
title: "Harness decommission: book repo wind-down"
chapter: 08
status: reference
tags: [decommission, harness-meta, example]
product: project-harness
decision_date: 2026-06-23
final_shutdown: "(example — not executed)"
owner: human reader
---

# Decommission record — harness-meta (this book repo)

> **Training artifact only** — illustrates `_templates/decommission-record.md`
> for a **whole-repo sunset**. This book is active; no shutdown is planned.

## Decision summary

| Field | Value |
| :---- | :---- |
| **Decision date** | *(example)* 2026-06-23 |
| **Kill criteria triggered** | *(example)* strategic pivot — reader ships own product using method only |
| **Approving authority** | human reader |
| **Final shutdown date** | *(example)* 2026-07-31 |

**Rationale:** *(fictional)* Harness book repo served its purpose once the
reader's product repo is self-sufficient; maintaining dual canon costs more
than archiving the teaching copy.

## Pre-registered kill criteria (reference)

| Signal | Threshold | Actual at decision | Met? |
| :---- | :---- | :---- | :--: |
| Reader product self-sufficient | Own PROJECT-PLAN + context/ populated | yes | ✓ |
| Harness maintenance cost | > 4h/month with no book updates | 6h/month | ✓ |
| External readers | 0 outside author for 12 months | 0 | ✓ |

## User notification

| Milestone | Date | Channel | Owner |
| :---- | :---- | :---- | :---- |
| Internal decision | 2026-06-23 | STATE.md note | human |
| Public archive notice | 2026-07-01 | README banner on `main` | human |
| Export window opens | 2026-07-01 | GitHub archive + vault zip | human |
| Export window closes | 2026-07-15 | — | human |
| Repo read-only | 2026-07-31 | GitHub archive mode | human |

## Export and migration

| Data class | Export format | Location / tool | Verified |
| :---- | :---- | :---- | :--: |
| Full vault | git bundle + Obsidian zip | `archive/project-harness-2026-07.zip` | *(example)* |
| Session history | STATE + `context/system/sessions/` | included in bundle | ✓ |
| Track A secrets | none exported | `.env` destroyed locally | ✓ |

**Migration path:** Method lives on in reader's product repo; book is reference
archive only.

## Gate F — decommission checklist

| # | Gate | Evidence | Date | Owner |
| :-: | :---- | :---- | :---- | :---- |
| F1 | User access disabled | GitHub collaborators removed | *(example)* | human |
| F2 | Credentials revoked | OpenRouter key revoked; Docker `.env` deleted | *(example)* | human |
| F3 | Data retention executed | Inbox `_inbox/` purged or archived per class | *(example)* | human |
| F4 | Vendors terminated | OpenRouter project key deleted | *(example)* | human |
| F5 | Infrastructure torn down | `track-a` compose down; volumes removed | *(example)* | human |
| F6 | Dependencies cleared | No scheduled CI on archived repo | *(example)* | human |
| F7 | Archive searchable | Tagged release `sunset-2026-07-31` on read-only repo | *(example)* | human |
| F8 | No unowned obligations | No open support queue | *(example)* | human |

## Archive locations

| Artifact | Path or URI | Retention |
| :---- | :---- | :---- |
| Code mirror | `github.com/.../project-harness` (archived) | indefinite read-only |
| This record | `08-sunset/decommission/example-harness-repo-sunset.md` | with archive |
| Final post-mortem | `06-learn/post-mortems/POSTMORTEM-2026-07-sunset.md` | *(example)* |

## Final post-mortem

| Field | Value |
| :---- | :---- |
| **File** | *(example)* product shutdown post-mortem |
| **Completed** | within 2 weeks of F8 |
| **Reusable capabilities** | validator scripts, session workflow, agent yaml patterns → reader product |

## Change log

| Date | Update | Author |
| :---- | :---- | :---- |
| 2026-06-23 | Initial harness-meta example (S25) | session-25 |
