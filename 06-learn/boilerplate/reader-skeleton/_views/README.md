---
title: HTML Views — Page Registry
status: reference
---

# HTML views — page registry

Static single-file HTML suite for project status, arc roadmaps, session gates,
and frozen history. Markdown canon (`STATE.md`, dashboard, session roadmaps)
stays authoritative; HTML is the human control surface. Agents patch embedded
`DATA`; humans export decisions back via **Copy as markdown**.

## Page registry

| Page | Type | Status | DATA schema |
| :--- | :--- | :----- | :---------- |
| `project/index.html` | project | template | `project-v1` |
| `arc/_template/roadmap.html` | arc-template | template | `arc-roadmap-v1` |
| `session/_template/close.html` | session-template | template | `session-close-v1` |
| `gates/proceed.html` | gate | template | `session-gate-v1` |
| `gates/validate.html` | gate | template | `session-gate-v1` |

## Getting started

1. Open `_views/project/index.html` in a browser for project status.
2. When starting a multi-session arc, copy `arc/_template/roadmap.html` to
   `arc/<your-arc-id>/roadmap.html` and fill the `page-data` JSON block.
3. Copy `session/_template/close.html` to `session/sNN-close.html` at session
   close.
4. Use `gates/proceed.html` and `gates/validate.html` for session human gates;
   export markdown back into chat or session artifacts.

## DATA schemas

### `project-v1`

Embedded in `<script type="application/json" id="page-data">` on
`project/index.html`.

```json
{
  "mission": "string",
  "phase": "planning | idle | active-arc | handoff",
  "spinePercent": 0,
  "validator": "YOUR validator command — green",
  "activeArc": { "id": "your-arc", "label": "Your arc label", "roadmapHref": "../arc/your-arc/roadmap.html" },
  "arcHistory": [
    { "id": "your-arc", "label": "Your arc", "closed": "YYYY-MM-DD", "closeHref": "../arc/your-arc/close.html" }
  ],
  "milestones": [{ "name": "string", "status": "done|partial|planned", "session": "S1" }]
}
```

`activeArc` is `null` when phase is idle and no arc is in progress.

### `arc-roadmap-v1`

Embedded on `arc/<id>/roadmap.html`. Start from `arc/_template/roadmap.html`.

```json
{
  "arcId": "YOUR-ARC",
  "title": "Session roadmap YOUR-ARC",
  "missionLine": "string",
  "frozen": false,
  "closeHref": "close.html",
  "sessions": [
    { "id": "S1", "primary": "Your primary goal", "status": "planned", "branch": "session-1/your-topic" }
  ],
  "deferrals": [{ "item": "string", "rationale": "string" }],
  "targetSnapshot": { "oneLine": "string", "successCriteria": ["string"] },
  "currentSession": { "id": null, "focus": "Idle — arc not started" }
}
```

Set `frozen: true` when the arc is closed; the page shows a banner linking to
`closeHref`.

### `session-close-v1`

Embedded on `session/sNN-close.html`. Start from `session/_template/close.html`.

```json
{
  "session": 1,
  "branch": "session-1/your-topic",
  "boot": "YOUR boot line",
  "closed": "YYYY-MM-DD HH:mm",
  "outcome": "YOUR one-line outcome",
  "decisions": ["string"],
  "nextBootstrap": "YOUR next session bootstrap or null"
}
```

### `session-gate-v1`

Embedded on `_views/gates/proceed.html` and `validate.html`. Interactive gate
pages with export toolbar. Shared logic: `_shared/gate.js`.

```json
{
  "gate": "proceed | validate",
  "session": 1,
  "arc": "your-arc",
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

Pipe characters in table cells MUST be escaped as `\|`. Implementation:
`_shared/export.js`.

## Viz catalog

| ID | Use |
| :- | :-- |
| `table` | Session table, deferrals, evidence |
| `milestone-bar` | Spine / milestone progress |
| `breadcrumb-nav` | Cross-page orientation |

## Relative asset depth

| Page | Prefix to `_shared/` |
| :--- | :------------------- |
| `project/index.html` | `../_shared/` |
| `gates/*.html` | `../_shared/` |
| `arc/<id>/*.html` | `../../_shared/` |
| `session/*.html` | `../_shared/` |
