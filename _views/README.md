---
title: HTML Views — Page Registry
status: reference
updated: 2026-07-03 00:35
---

# HTML views — page registry

Static single-file HTML suite for project status, arc roadmaps, session gates,
and frozen history. Markdown canon (`STATE.md`, `_index/dashboard/`,
`session-roadmap-*.md`) stays authoritative; HTML is the human control
surface. Agents patch embedded `DATA`; humans export decisions back via
**Copy as markdown**.

Design spec: [[html-views-dashboard-design|context/system/html-views-dashboard-design.md]].

## Page registry

| Page | Type | Status | DATA schema |
| :--- | :--- | :----- | :---------- |
| `project/index.html` | project | live | `project-v1` |
| `arc/s41-s47/roadmap.html` | arc-living | live | `arc-roadmap-v1` |
| `arc/s41-s47/close.html` | arc-frozen | live | `arc-close-v1` |
| `session/s41-close.html` | session-frozen | live | `session-close-v1` |
| `session/s47-close.html` | session-frozen | live | `session-close-v1` |
| `session/_template/close.html` | session-template | live | `session-close-v1` |
| `gates/inbox-triage.html` | gate | live | `inbox-triage-v1` |
| `gates/proceed.html` | gate | live | `session-gate-v1` |
| `gates/validate.html` | gate | live | `session-gate-v1` |
| `gates/merge.html` | gate | live | `session-gate-v1` |
| `arc/_template/roadmap.html` | arc-template | live | `arc-roadmap-v1` |

### A/B variant column

Canonical arc template uses **layout-b (kanban)** for the Sessions section after
human A/B (2026-07-03). Viz ID: `kanban`.

## DATA schemas

### `project-v1`

Embedded in `<script type="application/json" id="page-data">` on
`project/index.html`.

```json
{
  "mission": "string",
  "phase": "idle | active-arc | handoff",
  "spinePercent": 98,
  "validator": "validate_md.py --all — 0 failures",
  "activeArc": { "id": "s41-s47", "label": "S41–S47 post-arc42", "roadmapHref": "../arc/s41-s47/roadmap.html" },
  "arcHistory": [
    { "id": "s41-s47", "label": "S41–S47", "closed": "2026-07-02", "closeHref": "../arc/s41-s47/close.html" }
  ],
  "milestones": [{ "name": "string", "status": "done|partial|planned", "session": "S47" }]
}
```

`activeArc` is `null` when phase is idle and no arc is in progress.

### `arc-roadmap-v1`

Embedded on `arc/<id>/roadmap.html`.

```json
{
  "arcId": "s41-s47",
  "title": "Session roadmap S41–S47",
  "missionLine": "string",
  "frozen": false,
  "closeHref": "close.html",
  "sessions": [
    { "id": "S41", "primary": "Inbox triage", "status": "done", "branch": "session-41/inbox-triage" }
  ],
  "deferrals": [{ "item": "string", "rationale": "string" }],
  "targetSnapshot": { "oneLine": "string", "successCriteria": ["string"] },
  "currentSession": { "id": null, "focus": "Idle — arc complete" }
}
```

Set `frozen: true` when the arc is closed; the page shows a banner linking to
`closeHref`.

### `arc-close-v1`

Embedded on `arc/<id>/close.html`. Read-only frozen snapshot written once at arc
close. No export toolbar.

```json
{
  "arcId": "s41-s47",
  "title": "Session roadmap S41–S47 — arc close",
  "closed": "2026-07-02 19:30",
  "missionLine": "string",
  "sessions": [
    { "id": "S41", "primary": "Inbox triage", "status": "done", "branch": "session-41/inbox-triage", "closeHref": "../../session/s41-close.html" }
  ],
  "milestones": [{ "name": "string", "grade": "Achieved|Partial|Deferred", "session": "S41" }],
  "targetSnapshot": {
    "oneLine": "string",
    "successCriteria": [{ "criterion": "string", "grade": "Achieved|Partial|Deferred" }]
  },
  "deferrals": [{ "item": "string", "rationale": "string", "grade": "Deferred" }]
}
```

### `session-close-v1`

Embedded on `session/sNN-close.html`. Read-only frozen snapshot written once at
session close. No export toolbar.

```json
{
  "session": 47,
  "branch": "session-47/promotion-remote-ci",
  "boot": "Promotion wave 1 — RCA/EOL/Docker canon",
  "closed": "2026-07-02 19:30",
  "outcome": "Promotion wave 1; remote/CI; handoff checklist; arc complete",
  "decisions": ["string"],
  "nextBootstrap": null
}
```

### `session-gate-v1`

Embedded on `_views/gates/proceed.html`, `validate.html`, `merge.html`.
Interactive gate pages with export toolbar.

```json
{
  "gate": "proceed | validate | merge",
  "session": 48,
  "arc": "s48-html-views",
  "willDecide": ["string"],
  "willNotDecide": ["string"],
  "questions": ["string"],
  "evidence": [
    { "question": "string", "where": "string", "passWhen": "string" }
  ],
  "decisionRule": "string"
}
```

Export appends a `## Scope confirmation` block (past tense) from form inputs.
Shared logic: `_shared/gate.js`.

## Export contract

Every gate export MUST start with a `## Human decisions` heading followed by
HTML comment metadata and a markdown table. Required comment fields:

| Field | Example |
| :---- | :------ |
| `exported-from` | `_views/gates/proceed.html` |
| `exported-at` | `YYYY-MM-DD HH:mm` (local time) |
| `gate` | gate id (when applicable) |
| `arc` | arc id (when applicable) |
| `session` | session number (when applicable) |

Pipe characters in table cells MUST be escaped as `\|`. Close gates add scope
confirmation (past tense) per human gate shape. Implementation:
`_shared/export.js`. Full contract:
[[html-views-dashboard-design|context/system/html-views-dashboard-design.md]] §
Export contract.

## Viz catalog

Allowed visualization types — no unbounded chart soup. A/B compares layouts
using the same viz ID, not new viz types ad hoc.

| ID | Use |
| :- | :-- |
| `table` | Session table, deferrals, evidence |
| `kanban` | Session disposition, task board |
| `timeline-svg` | Arc session sequence |
| `milestone-bar` | Spine / milestone progress |
| `breadcrumb-nav` | Cross-page orientation |

## A/B rules

| Step | Procedure |
| :--- | :-------- |
| Register variant | Add a registry row with `status: experiment`, `variant: layout-b` |
| Duplicate template | Same `DATA` schema, different layout or CSS |
| Human test | Complete identical gate on A and B; record preference + time |
| Promote | Rename winner to canonical filename; delete loser |
| Log | Add a History row in this file |

## A/B History — worked example (arc roadmap sessions)

First registered experiment: **session list as table (A) vs kanban columns (B)** on
the arc roadmap template.

| Field | Value |
| :---- | :---- |
| Canonical | `arc/_template/roadmap.html` — `ViewsRender.renderTable` on `#session-table` |
| Experiment | `arc/_template/roadmap.layout-b.html` — todo / doing / done columns on `#session-kanban` |
| DATA schema | `arc-roadmap-v1` (unchanged) |
| Status mapping | `done` → Done; `doing` / `active` / `in-progress` → Doing; else → Todo |
| Human task | Open both pages with the same session DATA (e.g. copy S41–S47 rows from `arc/s41-s47/roadmap.html` into each `#page-data` block). Complete: *review the S41–S47 session list* — note scan time, missed rows, and preference. |
| **Result (2026-07-03)** | **Winner: layout-b (kanban)** — human tested; promoted to `roadmap.html`; `roadmap.layout-b.html` deleted |

**Promote path (completed):**

1. ~~Record preference~~ — kanban preferred (pages tested, no issues).
2. Kanban merged into `arc/_template/roadmap.html`; experiment file removed.
3. Registry row `arc/_template/roadmap.html` → `live` / viz `kanban`.

## History

| When | Change | Snapshot |
| :--- | :----- | :------- |
| 2026-07-03 | A/B promote — kanban wins; `roadmap.layout-b.html` merged into `arc/_template/roadmap.html` | Human tested; no issues |
| 2026-07-03 | Phase 5 — A/B framework registered | [[html-views-dashboard-plan\|context/system/plans/html-views-dashboard-plan.md]] |
| 2026-07-03 | Phase 3 — proceed, validate, merge HTML gates + `gate.js` | [[html-views-dashboard-plan\|context/system/plans/html-views-dashboard-plan.md]] |
| 2026-07-02 | Phase 2 — arc close snapshot, S41/S47 session close pages, session close template | [[html-views-dashboard-plan\|context/system/plans/html-views-dashboard-plan.md]] |
| 2026-07-02 | Phase 1 — `render.js`, project dashboard, arc roadmap + template; schemas documented | [[html-views-dashboard-plan\|context/system/plans/html-views-dashboard-plan.md]] |
| 2026-07-02 | Phase 0 start — shared kit (`shell.css`, `export.js`, `nav.js`) + registry | [[html-views-dashboard-plan\|context/system/plans/html-views-dashboard-plan.md]] |
