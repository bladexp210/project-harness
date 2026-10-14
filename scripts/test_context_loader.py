#!/usr/bin/env python3
"""Fixtures for context_loader strip spec. Run: python scripts/test_context_loader.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from context_loader import load_task_context, strip_teaching_blocks

ROOT = pathlib.Path(__file__).resolve().parents[1]


def assert_eq(actual, expected, label):
    if actual != expected:
        raise AssertionError("{}: expected\n{!r}\ngot\n{!r}".format(label, expected, actual))


def assert_in(needle, haystack, label):
    if needle not in haystack:
        raise AssertionError("{}: {!r} not in output".format(label, needle))


def assert_not_in(needle, haystack, label):
    if needle in haystack:
        raise AssertionError("{}: {!r} should be stripped".format(label, needle))


def test_exempt_adr():
    adr = ROOT / "02-design/decisions/ADR-006-teaching-block-convention.md"
    text = adr.read_text(encoding="utf-8")
    assert_eq(strip_teaching_blocks(adr, text), text, "ADR unchanged")


def test_strip_learn_callout():
    raw = (
        "# Title\n\n"
        "> [!LEARN] Learn It\n"
        "> Instructional prose.\n"
        "\n"
        "| Col | Val |\n"
        "| --- | --- |\n"
        "| a   | 1   |\n"
    )
    expected = (
        "# Title\n\n\n"
        "| Col | Val |\n"
        "| --- | --- |\n"
        "| a   | 1   |\n"
    )
    assert_eq(strip_teaching_blocks("04-your-agents/README.md", raw), expected, "LEARN stripped")


def test_note_callout_kept():
    raw = "> [!NOTE] Operational prompt\n> Keep this.\n\nBody.\n"
    assert_eq(strip_teaching_blocks("foo.md", raw), raw, "NOTE callout kept")


def test_fence_callout_not_stripped():
    raw = (
        "```\n"
        "> [!LEARN] inside fence\n"
        "```\n\n"
        "> [!TIP] Fast Track\n"
        "> Remove me.\n\n"
        "After.\n"
    )
    expected = (
        "```\n"
        "> [!LEARN] inside fence\n"
        "```\n\n\n"
        "After.\n"
    )
    assert_eq(strip_teaching_blocks("foo.md", raw), expected, "fence + TIP")


def test_sessions_exempt():
    raw = "> [!LEARN] history note\n> stays\n"
    assert_eq(
        strip_teaching_blocks("context/system/sessions/foo.md", raw),
        raw,
        "sessions path exempt",
    )


def test_golden_data_layer():
    """ADR-006 retrofit: data.md keeps artifact tables and template rows."""
    path = "02-design/layers/data.md"
    stripped = strip_teaching_blocks(path, (ROOT / path).read_text(encoding="utf-8"))
    assert_not_in("[!TEACH]", stripped, "data.md TEACH stripped")
    assert_not_in("[!LEARN]", stripped, "data.md LEARN stripped")
    assert_not_in("[!TIP]", stripped, "data.md TIP stripped")
    assert_in("| Signal in your use cases |", stripped, "data.md decision table")
    assert_in("erDiagram", stripped, "data.md template mermaid")
    assert_in("[e.g., PostgreSQL]", stripped, "data.md fill-in row")
    assert_in("[!NOTE]", stripped, "data.md NOTE kept")


def test_golden_use_cases():
    """use-cases.md: template table and MUST row survive strip."""
    path = "01-understand/use-cases.md"
    stripped = strip_teaching_blocks(path, (ROOT / path).read_text(encoding="utf-8"))
    assert_not_in("[!LEARN]", stripped, "use-cases LEARN stripped")
    assert_in("| Role | Use Case |", stripped, "use-cases template table")
    assert_in("[Complete a purchase]", stripped, "use-cases example row")


def test_golden_project_plan():
    """PROJECT-PLAN.md: living plan table and mermaid survive strip."""
    path = "03-plan/PROJECT-PLAN.md"
    stripped = strip_teaching_blocks(path, (ROOT / path).read_text(encoding="utf-8"))
    assert_not_in("[!TIP]", stripped, "PROJECT-PLAN TIP stripped")
    assert_in("flowchart TD", stripped, "PROJECT-PLAN mermaid")
    assert_in("| 01 |", stripped, "PROJECT-PLAN task table")
    assert_in("- [ ] Every task", stripped, "PROJECT-PLAN exit checklist")


def test_load_task_context_batch():
    paths = ["02-design/layers/data.md", "03-plan/constraints/global.md"]
    batch = load_task_context(paths, ROOT)
    assert_in("---", batch, "batch separator")
    assert_in("| Artifact | Budget |", batch, "global constraints table")
    assert_in("| Signal in your use cases |", batch, "data layer table")
    assert_not_in("[!TEACH]", batch, "batch TEACH stripped")


def test_harness_context_tree_batch():
    """S22: architecture domain files load and strip cleanly."""
    paths = [
        "context/architecture/data/harness-artifacts.md",
        "context/architecture/application/validation-and-loader.md",
        "context/architecture/communication/handoff-and-git.md",
        "context/architecture/ux/book-structure.md",
    ]
    batch = load_task_context(paths, ROOT)
    assert_in("---", batch, "harness arch batch separator")
    assert_in("| Store | Role |", batch, "data harness-artifacts table")
    assert_in("validate_md.py", batch, "application loader component")
    assert_in("D-001", batch, "communication git rules")
    assert_in("flowchart LR", batch, "ux chapter spine mermaid")


def main():
    test_exempt_adr()
    test_strip_learn_callout()
    test_note_callout_kept()
    test_fence_callout_not_stripped()
    test_sessions_exempt()
    test_golden_data_layer()
    test_golden_use_cases()
    test_golden_project_plan()
    test_load_task_context_batch()
    test_harness_context_tree_batch()
    print("test_context_loader: all passed")


if __name__ == "__main__":
    main()
