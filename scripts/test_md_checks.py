#!/usr/bin/env python3
"""Crafted fixtures for md_checks rules. Run: python scripts/test_md_checks.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from md_checks.link_resolution import check_links
from md_checks.fog_words import check_fog_words
from md_checks.placeholders import (
    check_placeholders,
    check_teaching_callout_placeholders,
)
from md_checks.adr_patterns import check_adr_patterns
from md_checks.lifecycle_rules import check_lifecycle_rules
from md_checks.markdown_structure import check_markdown_structure

INDEX = {"agents", "overview", "threat-model", "global"}


def assert_has(errors, substring, label):
    if not any(substring in e for e in errors):
        raise AssertionError("{}: expected error containing {!r}, got {}".format(
            label, substring, errors))


def assert_clean(errors, label):
    if errors:
        raise AssertionError("{}: expected no errors, got {}".format(label, errors))


def test_link_resolution():
    bad = "See [[missing-note]] for details."
    assert_has(check_links(bad, INDEX), "broken wiki-link", "dangling link")

    alias = "Read [[overview|the overview]]."
    assert_clean(check_links(alias, INDEX), "alias resolves on target")

    fence = "```\n[[ghost]]\n```\nLive [[missing-note]]."
    assert_has(check_links(fence, INDEX), "broken wiki-link", "fence skipped")
    assert len(check_links(fence, INDEX)) == 1

    heading = "Jump to [[overview#section]]."
    assert_clean(check_links(heading, INDEX), "heading form stem-only")


def test_placeholders():
    task = "---\nstatus: todo\n---\nFill [your API name] here.\n"
    assert_has(check_placeholders(task, "tasks/01-api.md"), "unfilled placeholder",
               "bracket placeholder")

    clean = "---\nstatus: todo\n---\nSee [docs](https://example.com).\n- [ ] todo\n"
    assert_clean(check_placeholders(clean, "tasks/01-api.md"), "link and checkbox ok")

    tmpl = "---\nstatus: template\n---\n[short imperative title]\n"
    assert_clean(check_placeholders(tmpl, "_templates/new-task.md"), "template skipped")


def test_teaching_callout_placeholders():
    bad = """---
status: living
---
> [!TEACH] Teach
> Put your [Shopper] role here before you lock the table.

| Role | Use Case |
| --- | --- |
| [Shopper] | [Buy item] |
"""
    assert_has(
        check_teaching_callout_placeholders(bad, "01-understand/use-cases.md"),
        "artifact placeholder inside teaching callout",
        "placeholder in TEACH block",
    )

    clean = """---
status: living
---
> [!TEACH] Teach
> For each role in [[user-roles]], list what they need to do.

| Role | Use Case |
| --- | --- |
| [Shopper] | [Buy item] |
"""
    assert_clean(
        check_teaching_callout_placeholders(clean, "01-understand/use-cases.md"),
        "artifact table outside callout ok",
    )

    note = """---
status: living
---
> [!NOTE] Ask your AI agent
> Paste [your roles here] and challenge the ratings.

| Role | Use Case |
| --- | --- |
| [Shopper] | [Buy item] |
"""
    assert_clean(
        check_teaching_callout_placeholders(note, "01-understand/use-cases.md"),
        "NOTE callout not scanned",
    )

    non_dual = """---
status: living
---
> [!TEACH] Teach
> Example `[!LEARN]` marker and [Shopper] inside teaching prose.
"""
    assert_clean(
        check_teaching_callout_placeholders(non_dual, "05-build/README.md"),
        "non dual-purpose path skipped",
    )


def test_fog_words():
    bad = """---
status: living
---
> [!TEACH] Teach
> Teaching prose only.

We will leverage the cache layer for reads.
"""
    assert_has(
        check_fog_words(bad, "02-design/layers/data.md"),
        "fog word 'leverage'",
        "leverage in artifact zone",
    )

    clean = """---
status: living
---
> [!TEACH] Teach
> We leverage teaching examples here only.

Use the cache layer for reads.
"""
    assert_clean(
        check_fog_words(clean, "02-design/layers/data.md"),
        "fog in teaching block only",
    )

    adr = "Industry fog: delete leverage and synergy from reader text."
    assert_clean(check_fog_words(adr, "02-design/decisions/ADR-008.md"), "ADR not dual-purpose")


def test_adr_patterns():
    bad = """---
status: accepted
---
| Pattern | When NOT to apply |
| --- | --- |
| CQRS | |
"""
    assert_has(check_adr_patterns(bad, False), "missing", "empty failure cell")

    good = """---
status: accepted
---
| Pattern | When NOT to apply |
| --- | --- |
| CQRS | Read-heavy CRUD with no write contention |
"""
    assert_clean(check_adr_patterns(good, False), "complete pattern row")


def test_lifecycle():
    bad = "Plain text mentions lifecycle without qualifier."
    assert_has(check_lifecycle_rules(bad, pathlib.Path("02-design/layers/data.md")),
               "bare 'lifecycle'", "bare lifecycle")

    good = "The product lifecycle ends at sunset."
    assert_clean(check_lifecycle_rules(good, pathlib.Path("02-design/layers/data.md")),
                 "qualified lifecycle")

    link = "See [[ADR-004-lifecycle-vocabulary|lifecycle]] rules."
    assert_clean(check_lifecycle_rules(link, pathlib.Path("02-design/layers/data.md")),
                 "wiki-link stripped")


def test_markdown_structure():
    broken_table = """---
status: living
---
| A | B |

| --- | --- |

| 1 | 2 |
"""
    assert_has(check_markdown_structure(broken_table), "blank line inside markdown table",
               "split table rows")

    good_table = """---
status: living
---
| A | B |
| --- | --- |
| 1 | 2 |
"""
    assert_clean(check_markdown_structure(good_table), "contiguous table")

    two_tables = """---
status: living
---
| open | one |

**Closed:**

| closed | two |
| --- | --- |
| C1 | done |
"""
    assert_clean(check_markdown_structure(two_tables), "two tables with prose gap")

    broken_mermaid = """---
status: living
---
```mermaid
flowchart LR

    A --> B

    B --> C

    C --> D
```
"""
    assert_has(check_markdown_structure(broken_mermaid), "mermaid block",
               "spaced mermaid lines")

    bad_wikilink_table = """---
status: living
---
| Path | Purpose |
| --- | --- |
| [[decommission/README|decommission/]] | Folder index |
"""
    assert_has(check_markdown_structure(bad_wikilink_table),
               "aliased wiki-link in table row", "unescaped alias pipe")

    good_wikilink_table = """---
status: living
---
| Path | Purpose |
| --- | --- |
| [[decommission/README\\|decommission/]] | Folder index |
| [[overview]] | No alias |
"""
    assert_clean(check_markdown_structure(good_wikilink_table), "escaped alias ok")


def main():
    test_link_resolution()
    test_placeholders()
    test_teaching_callout_placeholders()
    test_fog_words()
    test_adr_patterns()
    test_lifecycle()
    test_markdown_structure()
    print("test_md_checks: all fixtures passed")


if __name__ == "__main__":
    main()
