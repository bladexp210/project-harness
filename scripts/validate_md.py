#!/usr/bin/env python3
"""Markdown validator for project-harness.

Catches the defect classes that broke the vault on 2026-06-10, plus the
declared budgets (T7 — closes D-006):
  1. Missing / empty / invalid YAML frontmatter (Google Docs export flattens it)
  2. Escaped wiki-links and backslash-escape artifacts outside code fences
  3. Indented headings outside code fences (1-3 spaces still parse as real
     headings per CommonMark - they pollute the Obsidian outline)
  4. Line budgets and Mermaid node budgets (constraints/global.md), with a
     grace band: over budget by <=5% = WARN, by >5% = FAIL.
  5. ADR-006 Phase 3: reader-fillable [placeholders] inside [!LEARN]/[!TIP]/
     [!TEACH] teaching callouts on dual-purpose markdown files.
  6. ADR-008 T7: industry fog words in artifact zones on dual-purpose files.

Path -> budget map (DECIDE-FIRST, T7). First matching rule wins; files that
match no rule get no line-budget check. Globs are matched against the
repo-relative POSIX path.

  | Budget kind            | Limit | Globs                                   |
  |------------------------|-------|-----------------------------------------|
  | agent definition (yaml)|    60 | **/agents/*.yaml, **/agents/*.yml       |
  | task file              |   100 | **/tasks/*.md, _templates/new-task.md   |
  | Layer-1 context file   |   200 | context/system/*.md, STATE.md           |
  | source module          |   300 | **/*.py                                 |

  Mermaid node budget (20, ADR-002) applies to every *.md, regardless of row.

Excluded by design: context/system/sessions/** is the append-only session
archive (history, not active context) - the non-recursive context/system/*.md
glob excludes it automatically. _inbox/**, _playground/**, **/.build-context/** are
non-canon material (ingress, experiments, prompt output) — no frontmatter requirement, no line budget,
and no md_checks (link/placeholder/ADR/lifecycle/structure). research/** has
frontmatter but skips md_checks.

Usage:
  python scripts/validate_md.py FILE [FILE ...]   # what pre-commit does
  python scripts/validate_md.py --all             # every file in the repo
  python scripts/validate_md.py --all --root DIR  # override repo root (CI/test)

Link-resolution (D-003) runs only with --all — it needs the full note index.
Pre-commit checks staged files without it; run --all periodically or in CI.

Exit code 1 if any file has errors. Warnings never block.
"""
import re
import sys
import pathlib

# Add scripts directory to sys.path to allow importing md_checks
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

try:
    import yaml
    HAVE_YAML = True
except ImportError:  # graceful degradation when run standalone without pyyaml
    HAVE_YAML = False

FENCE = re.compile(r"```.*?```", re.S)
ESCAPED_LINK = re.compile(r"\\\[\\\[|\\\]\\\]")
ESCAPE_ARTIFACT = re.compile(r"\\[\[\]#*+~=_]")
INDENTED_HEADING = re.compile(r"^ {1,3}#{1,6} ", re.M)
ARTIFACT_THRESHOLD = 5  # tolerate the odd legitimate backslash (Windows paths)

MD_SUFFIXES = {".md", ".markdown"}

# (kind, limit, [glob, ...]) in priority order — first match wins.
LINE_BUDGETS = [
    ("agent definition (yaml)", 60, ["**/agents/*.yaml", "**/agents/*.yml"]),
    ("task file", 100, ["**/tasks/*.md", "_templates/new-task.md"]),
    ("Layer-1 context file", 200, ["context/system/*.md", "STATE.md"]),
    ("source module", 300, ["**/*.py"]),
]
MERMAID_NODE_BUDGET = 20
WARN_BAND = 0.05  # over by <=5% warns; over by >5% fails

MERMAID_BLOCK = re.compile(r"```mermaid\s*\n(.*?)```", re.S)
# Node shape declarations: id followed by an opener ([ ( { [[ (( [( {{ > ).
SHAPE_DECL = re.compile(r"\b([A-Za-z_][\w-]*)\s*(?:\[\[|\(\(|\[\(|\{\{|\[|\(|\{|>)")
PARTICIPANT = re.compile(r"^\s*(?:participant|actor)\s+([A-Za-z0-9_]+)", re.M)
ER_ENTITY = re.compile(r"\b([A-Z][A-Z0-9_]*)\b")
# Words that are mermaid syntax, never node identifiers.
MERMAID_KEYWORDS = {
    "subgraph", "end", "direction", "flowchart", "graph", "sequencediagram",
    "classdiagram", "erdiagram", "statediagram", "gantt", "pie", "note",
    "loop", "alt", "opt", "par", "and", "rect", "activate", "deactivate",
    "lr", "rl", "tb", "td", "bt",
}


def _glob_to_re(glob):
    """Translate a restricted glob (**/, *, ?) into an anchored regex."""
    out, i = [], 0
    while i < len(glob):
        if glob.startswith("**/", i):
            out.append(r"(?:.*/)?")
            i += 3
        elif glob[i] == "*":
            out.append(r"[^/]*")
            i += 1
        elif glob[i] == "?":
            out.append(r"[^/]")
            i += 1
        else:
            out.append(re.escape(glob[i]))
            i += 1
    return re.compile("^" + "".join(out) + "$")


_BUDGET_RULES = [
    (kind, limit, [_glob_to_re(g) for g in globs])
    for kind, limit, globs in LINE_BUDGETS
]


def _relpath(path, root):
    try:
        return path.resolve().relative_to(root).as_posix()
    except (ValueError, OSError):
        return path.as_posix()


def budget_for(relpath):
    """Return (kind, limit) for the first matching rule, else None."""
    for kind, limit, patterns in _BUDGET_RULES:
        if any(p.match(relpath) for p in patterns):
            return kind, limit
    return None


def band(n, limit):
    """None if within budget, 'warn' if over by <=5%, 'fail' if over by >5%."""
    if n <= limit:
        return None
    return "warn" if n <= limit * (1 + WARN_BAND) else "fail"


def _pct_over(n, limit):
    return round((n - limit) * 100.0 / limit)


def count_mermaid_nodes(block):
    """Count distinct node identifiers in one mermaid block.

    False-positive-safe by design: counts only declared nodes — flowchart
    shape declarations, sequence participant/actor declarations, and ER
    entities. It does NOT parse arrow endpoints, so it never mistakes
    edge-label text for a node. Trade-off: a node that is only referenced
    (never given a shape) is not counted; this under-counts rather than
    over-counts, so it cannot falsely flag a compliant diagram.
    """
    lines = [ln for ln in block.splitlines() if not ln.strip().startswith("%%")]
    header = lines[0].strip().lower() if lines else ""
    body = "\n".join(lines[1:]) if lines else ""
    body = re.sub(r"<[^>]*>", " ", body)  # drop HTML tags (<br>) in labels
    if header.startswith(("sequencediagram", "sequence")):
        return len(set(PARTICIPANT.findall(block)))
    if header.startswith("erdiagram"):
        ids = {t for t in ER_ENTITY.findall(body) if t.lower() not in MERMAID_KEYWORDS}
        return len(ids)
    # flowchart / graph / state / class — count shape declarations
    ids = {m for m in SHAPE_DECL.findall(body) if m.lower() not in MERMAID_KEYWORDS}
    return len(ids)


def check(path, root, note_index=None):
    errors, warnings = [], []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return ["not valid UTF-8 ({} at byte {})".format(exc.reason, exc.start)], []
    if "\x00" in text:
        return ["contains NUL bytes - file corrupt or partially synced"], []

    is_md = path.suffix.lower() in MD_SUFFIXES
    relpath = _relpath(path, root)
    parts = pathlib.Path(relpath).parts
    is_non_canon_md = any(p in parts for p in ("_inbox", "_playground", ".build-context"))

    # --- markdown-only structural checks ---
    if is_md and not is_non_canon_md:
        is_template = False
        if not text.startswith("---\n"):
            errors.append("missing frontmatter block")
        else:
            end = text.find("\n---", 4)
            if end == -1:
                errors.append("frontmatter block never closed")
            else:
                block = text[4:end]
                is_template = bool(re.search(r"^status:\s*template\b", block, re.M))
                if HAVE_YAML:
                    try:
                        data = yaml.safe_load(block)
                        if not isinstance(data, dict) or not data:
                            errors.append("frontmatter empty or not a mapping "
                                          "(Google-Docs-export flattening?)")
                        elif "status" not in data:
                            warnings.append("no 'status' field - Dataview dashboard "
                                            "queries rely on it")
                    except yaml.YAMLError as exc:
                        errors.append("frontmatter is invalid YAML: {}".format(exc))
                elif not re.search(r"^\w[\w-]*\s*:", block, re.M):
                    errors.append("frontmatter has no 'key: value' lines")

        body = FENCE.sub("", text)
        if ESCAPED_LINK.search(body):
            errors.append(r"escaped wiki-links (\[\[) - export artifact, links won't resolve")
        artifacts = ESCAPE_ARTIFACT.findall(body)
        if len(artifacts) > ARTIFACT_THRESHOLD:
            errors.append("{} backslash-escape artifacts - unclean import suspected"
                          .format(len(artifacts)))
        indented = INDENTED_HEADING.findall(body)
        if indented:
            errors.append("{} indented heading(s) outside code fences - fence "
                          "examples or unindent real headings".format(len(indented)))

        # --- Mermaid node budget ---
        for i, block in enumerate(MERMAID_BLOCK.findall(text), 1):
            n = count_mermaid_nodes(block)
            verdict = band(n, MERMAID_NODE_BUDGET)
            if verdict:
                msg = ("mermaid block {} has {} nodes > {} budget (over by {}%) "
                       "- split C4-style (ADR-002)".format(
                           i, n, MERMAID_NODE_BUDGET, _pct_over(n, MERMAID_NODE_BUDGET)))
                (warnings if verdict == "warn" else errors).append(msg)

        # --- md_checks helper checks (active authored files only) ---
        is_active = not any(
            p in parts for p in ("_inbox", "_playground", "research", "_templates", "sessions")
        )
        if is_active:
            if note_index is not None:
                from md_checks.link_resolution import check_links
                errors.extend(check_links(text, note_index))

            from md_checks.placeholders import (
                check_placeholders,
                check_teaching_callout_placeholders,
            )
            errors.extend(check_placeholders(text, relpath))
            errors.extend(check_teaching_callout_placeholders(text, relpath))

            from md_checks.fog_words import check_fog_words
            errors.extend(check_fog_words(text, relpath))

            from md_checks.adr_patterns import check_adr_patterns
            errors.extend(check_adr_patterns(text, is_template))

            from md_checks.lifecycle_rules import check_lifecycle_rules
            errors.extend(check_lifecycle_rules(text, path))

            from md_checks.markdown_structure import check_markdown_structure
            errors.extend(check_markdown_structure(text))

    # --- line budget (all eligible file types) ---
    rule = budget_for(relpath)
    if rule:
        kind, limit = rule
        n = len(text.splitlines())
        verdict = band(n, limit)
        if verdict:
            msg = "{} {} lines > {} budget (over by {}%) - split or renegotiate".format(
                kind, n, limit, _pct_over(n, limit))
            (warnings if verdict == "warn" else errors).append(msg)

    return errors, warnings


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        
    root = pathlib.Path(__file__).resolve().parent.parent
    if "--root" in argv:
        idx = argv.index("--root")
        root = pathlib.Path(argv[idx + 1]).resolve()
        del argv[idx:idx + 2]

    exts = (".md", ".markdown", ".yaml", ".yml", ".py")
    if "--all" in argv:
        files = sorted(p for p in root.rglob("*")
                       if p.suffix.lower() in exts and ".git" not in p.parts)
    else:
        files = [pathlib.Path(a) for a in argv if a.lower().endswith(exts)]
    if not files:
        print("validate_md: no eligible files to check")
        return 0

    note_index = None
    if "--all" in argv:
        note_index = set()
        for p in root.rglob("*"):
            if ".git" not in p.parts:
                if p.is_file() and p.suffix.lower() in (MD_SUFFIXES | {".yaml", ".yml"}):
                    note_index.add(p.stem.lower())
                elif p.is_dir():
                    note_index.add(p.name.lower())
        # Add known planned directories/stems that don't exist yet in the harness
        note_index.update({"04-your-agents", "05-build", "project"})

    failed = 0
    for f in files:
        errors, warnings = check(f, root, note_index=note_index)
        for w in warnings:
            print("WARN  {}: {}".format(f, w))
        for e in errors:
            print("FAIL  {}: {}".format(f, e))
        failed += bool(errors)
    print("validate_md: {} file(s) checked, {} failed".format(len(files), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
