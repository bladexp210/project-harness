---
title: Playground
status: reference
created: 2026-06-12
updated: 2026-06-12
tags: [playground, experiment]
---

# _playground/ — safe exploration space

> [!NOTE] Not canon
> Nothing here is project truth until **promoted** into a chapter folder.
> Agents do not load `_playground/` unless the human names a specific path.

Experiments, mockups, HTML visuals, and A/B variants live here so you can
explore without breaking the book spine or failing validators.

## Rules

| # | Rule |
| :-- | :-- |
| 1 | **Not canon** — promote working results into `tasks/`, chapters, or [[viz/README|viz/]]. |
| 2 | **One folder per experiment** — each carries a `manifest.yaml` (see below). |
| 3 | **Archive, don't delete** — stale work moves to `_playground/_archive/` (exploration memory). |
| 4 | **4-day retention** — if not promoted within 4 days of last edit, auto-archive (human runs script). |
| 5 | **Link direction** — canon may link here as *experimental*; do not wiki-link from canon *as if* playground were shipped. |

> [!LEARN] Learn It
> Use the playground when prose overwhelms you or you need to *see* a task
> before writing it in ICOM markdown. Promote only what you would defend in
> a review.

> [!TIP] Fast Track
> ```powershell
> # Check what will archive (dry run)
> python scripts/playground_archive.py --dry-run
> # Archive experiments idle > 4 days
> python scripts/playground_archive.py
> ```

## manifest.yaml (required per experiment)

```yaml
title: Short human label
created: 2026-06-12   # YYYY-MM-DD — set once
updated: 2026-06-12   # bump on every edit session
promote_to: ""        # target path when promoted, e.g. viz/icom/task-01.html
status: experiment    # experiment | promoted
```

**Archive trigger:** `updated` + 4 calendar days &lt; today and `status` is still
`experiment`. Promoted experiments are never auto-archived.

## Promotion

1. Copy or adapt artifacts into the `promote_to` path (or chapter/task file).
2. Set `status: promoted` in manifest (or move folder to `_archive/` manually with a note).
3. Remove duplicate canon links that still say "experimental" if the visual is now stable.

## Folder layout

```
_playground/
  README.md              ← this file
  diagram-taxonomy.md      ← promoted → [[context/system/diagram-taxonomy|canon v0.3]]
  icom-plus-convention.md  ← promoted → [[context/system/icom-plus-convention|canon v0.3]]
  l4-models/               ← ground-up L4 task boxes (one folder per L3 process)
  mockups/                 ← one learning example per diagram type
  _archive/                ← stale experiments (timestamped)
  icom/
    task-01/               ← pilot (orphan L4 — supersede per taxonomy)
  workflows/               ← (future) one HTML per L3 process
```

## Distinction from `_inbox/`

| Folder | Purpose |
| :----- | :-------- |
| `_inbox/` | External ingress — research dumps to distill into `research/*-seed.md` |
| `_playground/` | Internal egress-before-promotion — your mockups and explorations |
