#!/usr/bin/env python3
"""Golden-task fixtures — all core roles: context paths and strip markers."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from task_context import build_task_context, resolve_context_paths

ROOT = pathlib.Path(__file__).resolve().parents[1]

FIXTURES = (
    {
        "path": "04-your-agents/golden-tasks/01-design-option-tiebreak.md",
        "required_paths": (
            "04-your-agents/evaluator.md",
            "context/system/agent-team.md",
            "research/red-team-seed.md",
        ),
        "context_markers": (
            "score matrix",
            "family separation",
            "position swap",
            "multi-label",
            "never sole judge",
        ),
    },
    {
        "path": "04-your-agents/golden-tasks/02-dev-bounded-patch.md",
        "required_paths": (
            "03-plan/constraints/global.md",
            "_templates/new-task.md",
            "03-plan/constraints/project.md",
        ),
        "context_markers": (
            "atomic commits",
            "scope — modify",
            "task.md",
        ),
    },
    {
        "path": "04-your-agents/golden-tasks/03-tester-edge-case-repro.md",
        "required_paths": (
            "research/lifecycle-playbook-seed.md",
            "04-your-agents/tasks/02-track-a-golden-path.md",
        ),
        "context_markers": (
            "gate b",
            "break",
            "acceptance criteria",
        ),
    },
    {
        "path": "04-your-agents/golden-tasks/04-security-injection-probe.md",
        "required_paths": (
            "02-design/threat-model.md",
            "research/red-team-seed.md",
        ),
        "context_markers": (
            "prompt injection",
            "abuse",
            "detection",
        ),
    },
    {
        "path": "04-your-agents/golden-tasks/05-redteam-premortem-gate.md",
        "required_paths": (
            "02-design/threat-model.md",
            "02-design/decisions/ADR-005-failure-condition-convention.md",
            "research/lifecycle-playbook-seed.md",
        ),
        "context_markers": (
            "gate b",
            "pre-mortem",
            "detection",
        ),
    },
)

STRIP_ABSENT = ("[!learn]", "[!teach]", "[!tip]")


def assert_in(needle, haystack, label):
    if needle not in haystack:
        raise AssertionError("{}: {!r} not in output".format(label, needle))


def assert_not_in(needle, haystack, label):
    if needle in haystack:
        raise AssertionError("{}: {!r} should be absent".format(label, needle))


def test_fixture_paths(fixture):
    paths = resolve_context_paths(fixture["path"], ROOT)
    for req in fixture["required_paths"]:
        assert_in(req, paths, fixture["path"] + " paths")


def test_fixture_context(fixture):
    ctx = build_task_context(fixture["path"], ROOT).lower()
    for marker in fixture["context_markers"]:
        assert_in(marker, ctx, fixture["path"] + " context")
    for tag in STRIP_ABSENT:
        assert_not_in(tag, ctx, fixture["path"] + " strip")


def main():
    for fixture in FIXTURES:
        test_fixture_paths(fixture)
        test_fixture_context(fixture)
    print("test_golden_tasks: all passed ({} fixtures)".format(len(FIXTURES)))


if __name__ == "__main__":
    main()
