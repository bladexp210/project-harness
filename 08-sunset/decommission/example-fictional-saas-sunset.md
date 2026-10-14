---
title: "Fictional decommission: NoteShelf SaaS"
chapter: 08
status: reference
tags: [decommission, example, fictional]
product: noteshelf
decision_date: 2025-11-15
final_shutdown: 2026-02-28
owner: product lead
---

# Decommission record — NoteShelf (fictional SaaS)

> **Training artifact only** — fictional B2C note-taking SaaS. Shows Gate F
> and kill-criteria discipline for a reader product.

## Decision summary

| Field | Value |
| :---- | :---- |
| **Decision date** | 2025-11-15 |
| **Kill criteria triggered** | MAU and MRR below thresholds at 24-month mark |
| **Approving authority** | founder + finance |
| **Final shutdown date** | 2026-02-28 |

**Rationale:** 380 MAU and $4.2K MRR at month 24 — below pre-registered
$10K MRR floor with flat growth. Support cost ($18/ticket × 210 tickets/quarter)
exceeded gross margin. Strategic pivot to B2B product line.

## Pre-registered kill criteria (reference)

| Signal | Threshold | Actual at decision | Met? |
| :---- | :---- | :---- | :--: |
| MAU | < 500 at 18 months, no growth | 410 MAU, flat 6 months | ✓ |
| MRR | < $10K at 24 months | $4.2K | ✓ |
| Gross margin | < 40% for 2 quarters | 22% | ✓ |
| Strategic alignment | Serves B2C ICP per annual review | pivoted to B2B | ✓ |

## User notification

| Milestone | Date | Channel | Owner |
| :---- | :---- | :---- | :---- |
| Internal decision | 2025-11-15 | leadership doc | product lead |
| Customer notice | 2025-11-20 | email + in-app banner | support |
| Export window opens | 2025-11-20 | Settings → Export | engineering |
| Export window closes | 2026-01-31 | — | support |
| Service offline | 2026-02-28 | DNS removed | ops |

**Commitments honored:** 60-day notice (TOS minimum 30); pro-rated refunds
for annual plans; export in Markdown + JSON.

## Export and migration

| Data class | Export format | Location / tool | Verified |
| :---- | :---- | :---- | :--: |
| User notes | Markdown zip + JSON API | `/export` job | sample audit ✓ |
| Attachments | S3 presigned bulk download | export job | ✓ |
| Billing | Stripe customer portal history | stripe.com | ✓ |

**Migration path:** blog post linking to three competitor import guides; no
official migration partner.

## Gate F — decommission checklist

| # | Gate | Evidence | Date | Owner |
| :-: | :---- | :---- | :---- | :---- |
| F1 | User access disabled | auth service read-only 2026-02-01; accounts deleted 2026-03-07 | 2026-02-28 | ops |
| F2 | Credentials revoked | Stripe, SendGrid, OAuth apps revoked | 2026-03-01 | security |
| F3 | Data retention executed | user blobs deleted per 30-day policy; invoices 7yr legal hold | 2026-03-07 | ops |
| F4 | Vendors terminated | AWS, Stripe subscriptions closed | 2026-03-05 | finance |
| F5 | Infrastructure torn down | ECS cluster deleted; RDS snapshot retained 90d | 2026-03-06 | ops |
| F6 | Dependencies cleared | domain DNS removed; no cron jobs | 2026-02-28 | ops |
| F7 | Archive searchable | code mirror + anonymized metrics in internal wiki | 2026-03-10 | product |
| F8 | No unowned obligations | zero open tickets at +14d | 2026-03-14 | support |

## Archive locations

| Artifact | Path or URI | Retention |
| :---- | :---- | :---- |
| Code mirror | `git.internal/archive/noteshelf` | 7 years |
| Anonymized learnings | wiki/noteshelf-sunset-2026 | indefinite |
| This record | `08-sunset/decommission/example-fictional-saas-sunset.md` | teaching |

## Final post-mortem

| Field | Value |
| :---- | :---- |
| **File** | `06-learn/post-mortems/POSTMORTEM-2026-03-noteshelf-sunset.md` |
| **Completed** | 2026-03-20 |
| **Reusable capabilities** | export job pattern → promoted to boilerplate; kill-criteria template reused in B2B product brief |

## Change log

| Date | Update | Author |
| :---- | :---- | :---- |
| 2025-11-15 | Record opened at decision | product lead |
| 2026-03-14 | Gate F complete | ops |
| 2026-06-23 | Copied as fictional teaching example (S25) | harness session |
