---
title: "ADR-010: VS Code hub — barbell execution pattern"
chapter: 2
status: accepted
date: 2026-07-01
tags:
  - decision
  - execution
  - track-b
  - vscode
---

# ADR-010 — VS Code hub: barbell execution pattern

**Status:** accepted — 2026-07-01, Session 43.

## Context

[ADR-007](ADR-007-dual-execution-tracks.md) named Track A (OpenHands) and Track B
(IDE/CLI agents) but left Track B as a **generic checklist** plus ad hoc
adapter lines in [constraints/project](../../03-plan/constraints/project.md). Vendor churn (Cursor rules,
Copilot instructions, MCP hosts) risks **book rewrites** every quarter.

[session-roadmap-s40-plus](../../context/system/sessions/session-roadmap-s40-plus.md) S43 scoped a **VS Code hub** refactor: solid
book-owned core vs reader-owned tooling seam. Path C observability (S44) and
temporal hooks (S45) assume a stable shell contract.

**Hierarchy unchanged:** Track A ideal; Track B fallback. This ADR names the
**Track B shell** and the **manifest seam** — not a new execution track.

## Decision

Adopt the **barbell execution pattern** for Track B:

### Solid core (book-owned — do not fork per vendor)

| Artifact | Role |
| :------- | :--- |
| [session-workflow](../../context/system/session-workflow.md) | Plan → Proceed → Execute → Close |
| [STATE](../../STATE.md) + `_index/dashboard/` | Handoff snapshot |
| `scripts/validate_md.py` | Markdown gate |
| ICOM+ task frames + `task_context.py` | Bounded agent inputs (ADR-006) |
| Hook contract + temporal schema | Path C / S45 — specified in core, wired later |

### Extensible seam (reader-owned)

| Artifact | Role |
| :------- | :--- |
| `_templates/tooling-manifest.md` | Stable concern rows; reader fills product names |
| [constraints/project](../../03-plan/constraints/project.md) § Tool adapters | One-line map from checklist §7 to local config |

Human approves filled manifest at **Proceed** when major tools change.

### Shell (reader-owned — default for POC)

**VS Code** (or VS Code–compatible IDE) + extensions + **CLI agents in integrated
terminal**. Documented in [vscode-hub](../../05-build/execution-tools/vscode-hub.md). Cursor, Claude Code, Codex, OpenCode
are **adapter rows** — not separate canon chapters.

### Design tools demotion

Ch. 00 `design-tools/` index lists Cowork, Cursor, Antigravity as **peer
alternatives** for design phase — no single "primary" vendor. Execution hub is
VS Code pattern per this ADR.

**Reversibility & blast radius:** Revert is doc + template delete; no runtime
wire. Wrong seam → stale extension names in reader manifest only; core harness
unaffected. Fallback: generic [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) without manifest.

## Why

- Matches [manifesto](../../00-start-here/manifesto.md) barbell — boring core, experimental edge isolated.
- Anti-pattern from roadmap: per-vendor book chapters violate barbell and churn.
- `reader-skeleton` fork gets same template — teachability for engineering handoff.
- Path C hooks (S44) target one shell contract instead of N IDE guides.

## Alternatives considered (red-teamed)

- **Per-IDE canon chapters (Cursor guide, Codex guide, …)** — Best argument:
  lowest friction for one product. Rejected: N× maintenance, contradicts ADR-007
  generic Track B checklist.
- **Cowork remains primary design + execution story** — Best argument: matches
  early S30 stubs. Rejected: harness authored on Cursor/Track B; POC default is
  VS Code hub per roadmap mission boundary.
- **Tooling manifest in `constraints/` only, no template** — Best argument: one
  file fewer. Rejected: template is fork artifact; constraints stay living values.

### AI-suggested approach considered and rejected

none — human approved barbell split at S43 Proceed.

## Pre-mortem

1. **Manifest rots (wrong extension IDs)** → mitigation: Proceed gate re-approval;
   change log row in manifest; validator cannot catch — accepted risk with human review.
2. **Readers skip manifest, edit book chapters** → mitigation: ADR-010 + hub doc
   state "update manifest not book"; track-b-checklist §7 points to template.
3. **VS Code fork incompatibility** → mitigation: concern rows are product-agnostic;
   "IDE shell" row names the fork explicitly.

## Left on the table

- Full install scaffolds per design tool (Cowork, Antigravity) — later canon pass.
- Workspace settings JSON checked into harness — reader product choice.
- Automated manifest freshness lint — post-handoff tooling.

## Reference

- Hub doc: [vscode-hub](../../05-build/execution-tools/vscode-hub.md)
- Template: [_templates/tooling-manifest.md](../../_templates/tooling-manifest.md)
- Roadmap: [session-roadmap-s40-plus](../../context/system/sessions/session-roadmap-s40-plus.md) § VS Code hub
- Prior execution ADR: [ADR-007-dual-execution-tracks](ADR-007-dual-execution-tracks.md)
