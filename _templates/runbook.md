---
title: "Runbook: [service name]"
chapter: 07
status: draft
service: "[service-id]"
environment: dev | staging | production
owner: "[role or name]"
updated: YYYY-MM-DD
tags: [runbook]
---

# Runbook — [service name]

## Service overview

| Field | Value |
| :---- | :---- |
| **Owner** | |
| **Purpose** | One sentence: what this service does for users |
| **Dependencies** | databases, queues, third-party APIs |
| **Repo / deploy target** | |

## Deploy log

| Date | Version / artifact | Action | Approved by |
| :---- | :---- | :---- | :---- |
| | | | |

**Rollback:** [how to revert this service to last known good — command or link]

## Health checks

| Check | Command or probe | Pass when | Frequency |
| :---- | :---- | :---- | :---- |
| | | | |

**Alert routing:** [where alerts land — pager, email, channel]

## Incident playbook

### INC-1 — [symptom title]

| Step | Action |
| :---- | :---- |
| 1 | |
| 2 | |
| 3 | |

### INC-2 — [symptom title]

| Step | Action |
| :---- | :---- |
| 1 | |

**Severity guide:** S1 = user-visible outage · S2 = degraded · S3 = internal only

## Recurring tasks

| Task | Cadence | Procedure |
| :---- | :---- | :---- |
| Backup verify | | |
| Dependency patches | | |
| Access review | | |
| Cost review | | |

## Retirement notes

If this service or a capability within it will be **retired** (Ch. 07 — not
whole-product sunset): deprecate date, migration path, credential revocation
checklist. See [ADR-003-removal-vocabulary](../02-design/decisions/ADR-003-removal-vocabulary.md).

## Contacts and escalation

| Role | Contact |
| :---- | :---- |
| Primary on-call | |
| Secondary | |
| Vendor support | |

## Change log

| Date | Change | Author |
| :---- | :---- | :---- |
| | Initial runbook | |
