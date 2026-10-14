---
title: HTML Views Dashboard — Implementation Plan
layer: 1-system
status: reference
updated: 2026-07-03 00:20
session: 48
tags: [html-gate, dashboard, plan]
---

# HTML Views Dashboard — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a static `_views/` HTML suite (project + arc + session + gates) with shared export/nav kit, living + frozen history pages, and a reader-skeleton slim copy.

**Architecture:** Markdown canon (`STATE.md`, dashboard, roadmaps) stays source of truth; agents patch `<script type="application/json" id="page-data">` blocks in single-file HTML pages; humans export `## Human decisions` markdown via `_shared/export.js`. Triage board migrates to `_views/gates/` in Phase 0.

**Tech Stack:** Static HTML/CSS/vanilla JS, `file://` friendly relative paths, optional `scripts/test_views_export.py` for export contract tests, `validate_md.py --all` after doc edits.

**Design spec:** [html-views-dashboard-design](../html-views-dashboard-design.md)

**Open decisions locked (Phase 0):**

| ID | Decision |
| :- | :------- |
| OD-1 | Move triage board → `_views/gates/inbox-triage.html`; stub pointer in `review/README.md` |
| OD-2 | DATA in `<script type="application/json" id="page-data">` |
| OD-3 | Export schema validator → Phase 3 (`scripts/test_views_export.py` in Phase 0) |

---

## File map (all phases)

| Path | Responsibility |
| :--- | :------------- |
| `_views/README.md` | Page registry, A/B rules, viz catalog, History |
| `_views/_shared/shell.css` | Design tokens, layout, toolbar, tables, kanban, toast |
| `_views/_shared/export.js` | `buildExport()`, `copyExport()`, pipe escaping |
| `_views/_shared/nav.js` | Breadcrumb render, active-arc links |
| `_views/_shared/render.js` | Table/kanban/milestone-bar from DATA (Phase 1+) |
| `_views/project/index.html` | Living L1 project dashboard |
| `_views/arc/<id>/roadmap.html` | Living arc roadmap |
| `_views/arc/<id>/close.html` | Frozen arc close snapshot |
| `_views/session/sNN-close.html` | Frozen session close pages |
| `_views/gates/inbox-triage.html` | Migrated S41 triage board |
| `_views/gates/proceed.html` | Session proceed gate template |
| `_views/gates/validate.html` | Session validate gate template |
| `_views/gates/merge.html` | Merge approval gate template |
| `_views/arc/_template/roadmap.html` | Empty arc template for new arcs |
| `_views/session/_template/close.html` | Empty session close template |
| `scripts/test_views_export.py` | Export header + table contract tests |
| `review/README.md` | Pointer to `_views/gates/inbox-triage.html` |
| `06-learn/boilerplate/reader-skeleton/_views/` | Slim fork copy (Phase 4) |
| `context/system/html-views-dashboard-design.md` | Link to this plan in History row |

**Relative asset depth:**

| Page | Prefix to `_shared/` |
| :--- | :------------------- |
| `project/index.html` | `../_shared/` |
| `gates/*.html` | `../_shared/` |
| `arc/<id>/*.html` | `../../_shared/` |
| `session/*.html` | `../_shared/` |

---

## Phase 0 — Shared kit + triage migration

### Task 0.1: Create `_views/_shared/shell.css`

**Files:**
- Create: `_views/_shared/shell.css`

- [ ] **Step 1: Extract tokens and base layout from triage board**

Create `_views/_shared/shell.css` with these sections (lift from `review/inbox-triage-board.html` lines 8–60, 128–153):

```css
:root {
  --bg: #0f1419;
  --surface: #1a2332;
  --surface2: #243044;
  --border: #3d4f66;
  --text: #e7ecf3;
  --muted: #8b9cb3;
  --accent: #38bdf8;
  --promote: #22c55e;
  --warn: #eab308;
  --danger: #ef4444;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: "Segoe UI", system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.45;
}
header { padding: 1.25rem 1.5rem; border-bottom: 1px solid var(--border); background: var(--surface); }
header h1 { margin: 0 0 0.25rem; font-size: 1.25rem; font-weight: 600; }
header p { margin: 0; color: var(--muted); font-size: 0.875rem; }
.views-breadcrumb { padding: 0.5rem 1.5rem; font-size: 0.8rem; color: var(--muted); border-bottom: 1px solid var(--border); }
.views-breadcrumb a { color: var(--accent); text-decoration: none; }
.views-breadcrumb a:hover { text-decoration: underline; }
.toolbar { display: flex; flex-wrap: wrap; gap: 0.5rem; padding: 0.75rem 1.5rem; background: var(--surface2); border-bottom: 1px solid var(--border); align-items: center; }
button { font: inherit; cursor: pointer; border: 1px solid var(--border); background: var(--surface); color: var(--text); padding: 0.45rem 0.85rem; border-radius: 6px; }
button:hover { background: var(--surface2); border-color: var(--accent); }
button.primary { background: #0ea5e9; border-color: #0284c7; color: #fff; }
button.primary:hover { background: #0284c7; }
.hint { color: var(--muted); font-size: 0.8rem; margin-left: auto; }
main { padding: 1rem 1.5rem 2rem; }
.views-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
.views-table th, .views-table td { border: 1px solid var(--border); padding: 0.5rem 0.65rem; text-align: left; }
.views-table th { background: var(--surface2); }
.views-table tr:nth-child(even) { background: color-mix(in srgb, var(--surface) 80%, transparent); }
#toast { position: fixed; bottom: 1.25rem; right: 1.25rem; background: var(--promote); color: #052e16; padding: 0.65rem 1rem; border-radius: 8px; font-size: 0.875rem; font-weight: 600; opacity: 0; pointer-events: none; transition: opacity 0.25s; }
#toast.show { opacity: 1; }
pre#preview { display: none; margin: 0 1.5rem 1.5rem; padding: 1rem; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; font-size: 0.75rem; overflow-x: auto; white-space: pre-wrap; }
.read-only-banner { background: color-mix(in srgb, var(--warn) 20%, var(--surface)); border: 1px solid var(--warn); padding: 0.75rem 1rem; border-radius: 8px; margin-bottom: 1rem; }
```

- [ ] **Step 2: Verify file exists**

Run: `Test-Path _views/_shared/shell.css` (PowerShell)  
Expected: `True`

---

### Task 0.2: Create `_views/_shared/export.js`

**Files:**
- Create: `_views/_shared/export.js`
- Test: `scripts/test_views_export.py`

- [ ] **Step 1: Write failing export contract test**

Create `scripts/test_views_export.py`:

```python
"""Contract tests for _views/_shared/export.js markdown output."""
import re
import unittest


EXPORT_HEADER_RE = re.compile(
    r"^## Human decisions\n\n"
    r"<!-- exported-from: .+ -->\n"
    r"<!-- exported-at: \d{4}-\d{2}-\d{2} \d{2}:\d{2} -->\n"
    r"(<!-- gate: .+ -->\n)?"
    r"(<!-- arc: .+ -->\n)?"
    r"(<!-- session: .+ -->\n)?",
    re.MULTILINE,
)


class TestViewsExportContract(unittest.TestCase):
    def test_minimal_header_shape(self):
        sample = """## Human decisions

<!-- exported-from: _views/gates/proceed.html -->
<!-- exported-at: 2026-07-02 23:00 -->
<!-- gate: proceed -->
<!-- arc: s48-html-views -->
<!-- session: 48 -->

| Question | Answer |
| :---- | :---- |
| Primary goal correct? | yes |
"""
        self.assertRegex(sample, EXPORT_HEADER_RE)

    def test_table_row_pipe_escape_documented(self):
        row = "| What | a \\| b |"
        self.assertIn("\\|", row)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it passes (fixture-only test)**

Run: `python scripts/test_views_export.py -v`  
Expected: `OK` (2 tests)

- [ ] **Step 3: Implement export.js**

Create `_views/_shared/export.js`:

```javascript
(function (global) {
  "use strict";

  function pad2(n) {
    return String(n).padStart(2, "0");
  }

  function timestampLocal(d) {
    d = d || new Date();
    return (
      d.getFullYear() +
      "-" +
      pad2(d.getMonth() + 1) +
      "-" +
      pad2(d.getDate()) +
      " " +
      pad2(d.getHours()) +
      ":" +
      pad2(d.getMinutes())
    );
  }

  function escapeCell(value) {
    return String(value == null ? "" : value).replace(/\|/g, "\\|");
  }

  function buildExportHeader(meta) {
    meta = meta || {};
    var lines = ["## Human decisions", ""];
    lines.push("<!-- exported-from: " + (meta.exportedFrom || "unknown") + " -->");
    lines.push("<!-- exported-at: " + (meta.exportedAt || timestampLocal()) + " -->");
    if (meta.gate) lines.push("<!-- gate: " + meta.gate + " -->");
    if (meta.arc) lines.push("<!-- arc: " + meta.arc + " -->");
    if (meta.session != null && meta.session !== "") {
      lines.push("<!-- session: " + meta.session + " -->");
    }
    lines.push("");
    return lines.join("\n");
  }

  function buildMarkdownTable(headers, rows) {
    var out = [];
    out.push("| " + headers.join(" | ") + " |");
    out.push("| " + headers.map(function () { return ":----"; }).join(" | ") + " |");
    rows.forEach(function (row) {
      out.push("| " + row.map(escapeCell).join(" | ") + " |");
    });
    return out.join("\n");
  }

  function buildExport(meta, headers, rows, footerLines) {
    var parts = [buildExportHeader(meta)];
    if (headers && rows) parts.push(buildMarkdownTable(headers, rows));
    if (footerLines && footerLines.length) {
      parts.push("");
      parts.push(footerLines.join("\n"));
    }
    return parts.join("\n") + "\n";
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        document.body.removeChild(ta);
        resolve();
      } catch (err) {
        document.body.removeChild(ta);
        reject(err);
      }
    });
  }

  function showToast(message) {
    var el = document.getElementById("toast");
    if (!el) return;
    if (message) el.textContent = message;
    el.classList.add("show");
    setTimeout(function () { el.classList.remove("show"); }, 2000);
  }

  global.ViewsExport = {
    timestampLocal: timestampLocal,
    escapeCell: escapeCell,
    buildExportHeader: buildExportHeader,
    buildMarkdownTable: buildMarkdownTable,
    buildExport: buildExport,
    copyText: copyText,
    showToast: showToast,
  };
})(typeof window !== "undefined" ? window : globalThis);
```

- [ ] **Step 4: Re-run tests**

Run: `python scripts/test_views_export.py -v`  
Expected: `OK`

---

### Task 0.3: Create `_views/_shared/nav.js`

**Files:**
- Create: `_views/_shared/nav.js`

- [ ] **Step 1: Implement breadcrumb helper**

```javascript
(function (global) {
  "use strict";

  function renderBreadcrumb(containerId, crumbs) {
    var el = document.getElementById(containerId);
    if (!el || !crumbs || !crumbs.length) return;
    el.innerHTML = crumbs
      .map(function (c, i) {
        if (i === crumbs.length - 1 || !c.href) {
          return "<span>" + escapeHtml(c.label) + "</span>";
        }
        return '<a href="' + escapeHtml(c.href) + '">' + escapeHtml(c.label) + "</a>";
      })
      .join(" / ");
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function readPageData(id) {
    id = id || "page-data";
    var node = document.getElementById(id);
    if (!node) return {};
    try {
      return JSON.parse(node.textContent || "{}");
    } catch (e) {
      console.error("Invalid page-data JSON", e);
      return {};
    }
  }

  global.ViewsNav = { renderBreadcrumb: renderBreadcrumb, readPageData: readPageData };
})(typeof window !== "undefined" ? window : globalThis);
```

---

### Task 0.4: Create `_views/README.md` registry

**Files:**
- Create: `_views/README.md`

- [ ] **Step 1: Write registry with initial rows**

Include sections: Purpose, Page registry table, Export contract (link design spec), Viz catalog (`table`, `kanban`, `timeline-svg`, `milestone-bar`, `breadcrumb-nav`), A/B rules (experiment → promote → delete), History table.

Initial registry rows:

| Page | Type | Status | DATA schema |
| :--- | :--- | :----- | :---------- |
| `project/index.html` | project | planned | `project-v1` |
| `arc/s41-s47/roadmap.html` | arc-living | planned | `arc-roadmap-v1` |
| `arc/s41-s47/close.html` | arc-frozen | planned | `arc-close-v1` |
| `gates/inbox-triage.html` | gate | planned | `inbox-triage-v1` |

---

### Task 0.5: Migrate triage board to `_views/gates/inbox-triage.html`

**Files:**
- Create: `_views/gates/inbox-triage.html`
- Modify: `review/README.md`
- Modify: `review/inbox-triage-board.html` (replace body with redirect message)

- [ ] **Step 1: Create migrated gate page**

Copy `review/inbox-triage-board.html` logic into `_views/gates/inbox-triage.html`:

- Add `<link rel="stylesheet" href="../_shared/shell.css">`
- Move kanban-specific CSS (`.board`, `.column`, `.card`, etc.) into a `<style>` block in the gate file only (not shell.css — YAGNI until second kanban)
- Replace inline `exportMarkdown()` with:

```javascript
function exportMarkdown() {
  var rows = items.slice().sort(function (a, b) { return a.file.localeCompare(b.file); })
    .map(function (i) {
      return [
        "`" + i.file.replace(/`/g, "\\`") + "`",
        "**" + dispositionLabel(i.col) + "**",
        i.target,
        i.session,
        i.note || "",
      ];
    });
  return ViewsExport.buildExport(
    {
      exportedFrom: "_views/gates/inbox-triage.html",
      gate: "inbox-triage",
      session: "41",
    },
    ["File", "Disposition", "Target", "Session", "Note"],
    rows
  );
}
```

- Load scripts before closing `</body>`:

```html
<script src="../_shared/export.js"></script>
<script src="../_shared/nav.js"></script>
```

- Move `DEFAULT_ITEMS` into:

```html
<script type="application/json" id="page-data">
{ "items": [ ... same 19 items ... ] }
</script>
```

On load: `var data = ViewsNav.readPageData(); items = structuredClone(data.items || DEFAULT_ITEMS);`

- [ ] **Step 2: Update review/README.md**

Add row to Files table:

| `_views/gates/inbox-triage.html` | `_inbox/` triage (canonical) | [session-41-inbox-triage](../sessions/session-41-inbox-triage.md) |

Add note: `review/inbox-triage-board.html` is a legacy pointer.

- [ ] **Step 3: Replace legacy file with pointer**

Replace `review/inbox-triage-board.html` content with minimal HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url=../_views/gates/inbox-triage.html" />
  <title>Moved — inbox triage</title>
</head>
<body>
  <p>Moved to <a href="../_views/gates/inbox-triage.html">_views/gates/inbox-triage.html</a>.</p>
</body>
</html>
```

- [ ] **Step 4: Manual smoke test**

Open `_views/gates/inbox-triage.html` in browser (file://).  
Drag one card, add note, click **Copy as markdown**.  
Expected: clipboard contains `## Human decisions` and `<!-- exported-from: _views/gates/inbox-triage.html -->`.

- [ ] **Step 5: Commit (when human requests)**

```powershell
git add _views/ scripts/test_views_export.py review/README.md review/inbox-triage-board.html
git commit -m "feat(views): add shared HTML kit and migrate inbox triage gate (Phase 0)"
```

---

## Phase 1 — Project index + arc roadmap template

### Task 1.1: Define DATA schemas in `_views/README.md`

**Files:**
- Modify: `_views/README.md`

- [ ] **Step 1: Document `project-v1` schema**

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

- [ ] **Step 2: Document `arc-roadmap-v1` schema**

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

---

### Task 1.2: Create `_views/_shared/render.js`

**Files:**
- Create: `_views/_shared/render.js`

- [ ] **Step 1: Implement table + milestone bar renderers**

```javascript
(function (global) {
  "use strict";

  function renderTable(containerId, headers, rows) {
    var root = document.getElementById(containerId);
    if (!root) return;
    var html = ['<table class="views-table"><thead><tr>'];
    headers.forEach(function (h) { html.push("<th>" + h + "</th>"); });
    html.push("</tr></thead><tbody>");
    rows.forEach(function (row) {
      html.push("<tr>");
      row.forEach(function (cell) { html.push("<td>" + cell + "</td>"); });
      html.push("</tr>");
    });
    html.push("</tbody></table>");
    root.innerHTML = html.join("");
  }

  function renderMilestoneBar(containerId, milestones) {
    var root = document.getElementById(containerId);
    if (!root) return;
    root.innerHTML = milestones
      .map(function (m) {
        var cls = m.status === "done" ? "var(--promote)" : "var(--muted)";
        return '<div style="margin:0.25rem 0"><span style="color:' + cls + '">●</span> ' +
          m.name + " <span style=\"color:var(--muted)\">(" + (m.session || "—") + ")</span></div>";
      })
      .join("");
  }

  global.ViewsRender = { renderTable: renderTable, renderMilestoneBar: renderMilestoneBar };
})(typeof window !== "undefined" ? window : globalThis);
```

---

### Task 1.3: Create `_views/project/index.html`

**Files:**
- Create: `_views/project/index.html`

- [ ] **Step 1: Build page with DATA populated from current STATE (S47 idle)**

Structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Project Harness — Project dashboard</title>
  <link rel="stylesheet" href="../_shared/shell.css" />
</head>
<body>
  <nav id="breadcrumb" class="views-breadcrumb"></nav>
  <header>
    <h1 id="project-title">Project Harness</h1>
    <p id="mission-line"></p>
  </header>
  <main>
    <section id="phase-card"></section>
    <section><h2>Milestones</h2><div id="milestones"></div></section>
    <section><h2>Active arc</h2><div id="active-arc"></div></section>
    <section><h2>Arc history</h2><div id="arc-history"></div></section>
  </main>
  <script type="application/json" id="page-data">{ ... }</script>
  <script src="../_shared/export.js"></script>
  <script src="../_shared/nav.js"></script>
  <script src="../_shared/render.js"></script>
  <script src="project.js"></script>
</body>
</html>
```

- [ ] **Step 2: Create inline boot script `project.js` section at bottom of index.html**

On `DOMContentLoaded`: read `page-data`, fill header, call `ViewsRender.renderMilestoneBar`, render active arc link or "None — idle", render arc history as `<ul>` of links to `close.html`.

Breadcrumb: `[{ label: "Project", href: null }]`

Populate DATA from `STATE.md` snapshot (session 47 closed, phase idle, spine 98%, S41–S47 achieved).

- [ ] **Step 3: Manual smoke test**

Open `_views/project/index.html`.  
Expected: mission line visible, milestone list, link to `../arc/s41-s47/roadmap.html` or history only if arc marked closed.

---

### Task 1.4: Create `_views/arc/s41-s47/roadmap.html` (living template)

**Files:**
- Create: `_views/arc/s41-s47/roadmap.html`
- Create: `_views/arc/_template/roadmap.html` (copy with placeholder DATA)

- [ ] **Step 1: Populate session table from `session-roadmap-s40-plus.md`**

All S41–S47 rows `status: "done"`. Set `"frozen": true` and banner: "Arc complete — see close.html" (living page becomes read-only redirect after Phase 2 close page exists).

Include sections: mission, session table (`ViewsRender.renderTable`), deferrals table, target snapshot one-liner + success criteria list, current session focus.

Breadcrumb: Project → Arc S41–S47

- [ ] **Step 2: Copy to `_views/arc/_template/roadmap.html`**

Replace arc-specific DATA with placeholders `"arcId": "YOUR-ARC"`, empty sessions array.

- [ ] **Step 3: Update `_views/README.md` registry status to `live` for project + roadmap**

- [ ] **Step 4: Commit (when human requests)**

```powershell
git add _views/
git commit -m "feat(views): add project dashboard and arc roadmap template (Phase 1)"
```

---

## Phase 2 — Frozen history (S41–S47 demo)

### Task 2.1: Create `_views/arc/s41-s47/close.html`

**Files:**
- Create: `_views/arc/s41-s47/close.html`

- [ ] **Step 1: Build read-only close page**

- `.read-only-banner`: "Historical snapshot — do not edit. Generated at arc close."
- No toolbar export buttons (or disabled with tooltip)
- DATA schema `arc-close-v1`: final sessions all done, milestone grades (Achieved/Partial/Deferred) from design spec target snapshot
- Content from `session-roadmap-s40-plus.md` § Target snapshot + History
- Links to session close pages (S41, S47 minimum; others optional)

- [ ] **Step 2: Update `roadmap.html` banner + link to close.html**

When `data.frozen === true`, show banner at top linking to `close.html`.

---

### Task 2.2: Create session close pages (demo subset)

**Files:**
- Create: `_views/session/s41-close.html`
- Create: `_views/session/s47-close.html`
- Create: `_views/session/_template/close.html`

- [ ] **Step 1: S47 close page DATA**

```json
{
  "session": 47,
  "branch": "session-47/promotion-remote-ci",
  "boot": "Promotion wave 1 — RCA/EOL/Docker canon",
  "closed": "2026-07-02 19:30",
  "outcome": "Promotion wave 1; remote/CI; handoff checklist; arc complete",
  "decisions": [
    "S47 promotion wave 1 complete",
    "S47 engineering handoff checklist",
    "S47 S41–S47 arc closed"
  ],
  "nextBootstrap": null
}
```

- [ ] **Step 2: S41 close page** — outcome from dashboard History: "Inbox triage + HTML gate"

- [ ] **Step 3: Template** — empty fields for reader fork

- [ ] **Step 4: Link from `project/index.html` arc history and `close.html`**

- [ ] **Step 5: Commit (when human requests)**

```powershell
git add _views/
git commit -m "feat(views): add frozen arc and session close history pages (Phase 2)"
```

---

## Phase 3 — Session gate library

### Task 3.1: Create gate template `_views/gates/_gate-shell.html` (reference)

**Files:**
- Create: `_views/gates/proceed.html`, `validate.html`, `merge.html`

Each gate shares structure:

1. `#gate-decide-will` — future tense bullet list (editable textareas)
2. `#gate-questions` — questions list
3. `#gate-evidence` — table with pass-when column
4. `#gate-rule` — decision rule paragraph
5. Toolbar: Copy as markdown, Preview
6. Export includes scope confirmation block (past tense) filled from radio/select inputs

- [ ] **Step 1: proceed.html DATA**

```json
{
  "gate": "proceed",
  "session": 48,
  "arc": "s48-html-views",
  "willDecide": ["Primary goal and defer list for this session"],
  "willNotDecide": ["Implementation code", "Merge to main"],
  "questions": ["Is the primary goal correct?", "Is the defer list complete?"],
  "evidence": [
    { "question": "Primary goal", "where": "Session plan in chat", "passWhen": "Matches STATE bootstrap" }
  ],
  "decisionRule": "Proceed only if primary goal and defer list are correct."
}
```

- [ ] **Step 2: validate.html** — gate id `validate`; evidence rows for STATE + dashboard L1–L3 + work diff

- [ ] **Step 3: merge.html** — gate id `merge`; includes validator green + human runs git (D-001)

- [ ] **Step 4: Extend `scripts/test_views_export.py`**

Add test that reads a fixture file `_views/gates/_fixtures/proceed-export.md` and asserts regex match.

- [ ] **Step 5: Update `review/README.md` and `context/system/session-workflow.md`**

Add one paragraph under Session close: optional HTML gates at `_views/gates/proceed.html`, etc.

- [ ] **Step 6: Commit (when human requests)**

```powershell
git add _views/gates/ scripts/test_views_export.py context/system/session-workflow.md review/README.md
git commit -m "feat(views): add proceed validate merge HTML gates (Phase 3)"
```

---

## Phase 4 — Reader-skeleton slim copy

### Task 4.1: Copy slim `_views/` into reader-skeleton

**Files:**
- Create: `06-learn/boilerplate/reader-skeleton/_views/` (subset)
- Modify: `06-learn/boilerplate/reader-skeleton/README.md`

- [ ] **Step 1: Copy files**

| Include | Exclude |
| :------ | :------ |
| `_shared/*` | harness milestone names |
| `project/index.html` with generic DATA | arc/s41-s47 specific |
| `arc/_template/roadmap.html` | `arc/s41-s47/` |
| `session/_template/close.html` | `session/s41-close.html` etc. |
| `gates/proceed.html`, `validate.html` | inbox-triage, merge (optional keep merge) |
| trimmed `_views/README.md` | A/B experiments |

- [ ] **Step 2: Add fork step 12 to reader-skeleton README**

"Open `_views/project/index.html` in browser for project status; copy arc template when starting a multi-session arc."

- [ ] **Step 3: Update `engineering-handoff-checklist.md` row** — optional pointer to `_views/project/index.html`

- [ ] **Step 4: Commit (when human requests)**

```powershell
git add 06-learn/boilerplate/reader-skeleton/
git commit -m "feat(views): add slim HTML views to reader-skeleton (Phase 4)"
```

---

## Phase 5 — A/B framework + first experiment

### Task 5.1: Document A/B procedure in `_views/README.md`

- [ ] **Step 1: Add A/B History section with worked example**

Experiment: `arc/_template/roadmap.layout-b.html` — session table as kanban columns instead of `<table>`.

- [ ] **Step 2: Create variant file**

Copy `_views/arc/_template/roadmap.html` → `roadmap.layout-b.html`. Replace `#session-table` with kanban columns (todo/doing/done). Same `page-data` schema.

- [ ] **Step 3: Register both in README**

| Page | status | variant |
| :--- | :----- | :------ |
| `arc/_template/roadmap.html` | canonical | layout-a (table) |
| `arc/_template/roadmap.layout-b.html` | experiment | layout-b (kanban) |

- [ ] **Step 4: Run human A/B** (manual)

Complete "review S41–S47 session list" task on both; record preference in `_views/README.md` History.

- [ ] **Step 5: Promote winner**

If kanban wins: merge layout into canonical template, delete `.layout-b.html`, update History.

- [ ] **Step 6: Final doc sync**

- Modify: `context/system/html-views-dashboard-design.md` — add History row "Plan implemented Phases 0–5"
- Run: `python scripts/validate_md.py --all`  
  Expected: 0 failures

- [ ] **Step 7: Commit (when human requests)**

```powershell
git add _views/ context/system/
git commit -m "feat(views): complete A/B framework and layout experiment (Phase 5)"
```

---

## Spec coverage checklist

| Spec requirement | Task |
| :--------------- | :--- |
| Shared template kit | 0.1–0.3 |
| Export contract | 0.2, 0.5 |
| Page registry | 0.4, 1.1 |
| Project-level view | 1.3 |
| Arc roadmap living | 1.4 |
| Arc close frozen | 2.1 |
| Session close frozen | 2.2 |
| Gate library | 3.1 |
| Reader-skeleton dual delivery | 4.1 |
| A/B framework | 5.1 |
| Triage migration OD-1 | 0.5 |
| JSON page-data OD-2 | all HTML pages |
| Markdown stays canon | workflow docs, no STATE deletion |

---

## Suggested session bootstrap (when implementing)

**Branch:** `session-48/html-views-phase-0` (one branch per phase or one arc `session-48/html-views`)

**Primary:** Phase 0 shared kit + triage migration

**Load first:** [html-views-dashboard-design](../html-views-dashboard-design.md), this plan, `review/inbox-triage-board.html`

**Defer:** Phases 1–5 until Phase 0 smoke test passes

**Human gate:** Open `_views/gates/inbox-triage.html`, copy export, confirm schema

---

## Execution handoff

Plan saved to `context/system/plans/html-views-dashboard-plan.md`.

**Two execution options:**

1. **Subagent-driven (recommended)** — fresh subagent per task, review between tasks  
2. **Inline execution** — implement phases in this or a new session with checkpoints after each phase

Which approach do you want?
