#!/usr/bin/env python3
"""Tests for task_context.py — task yaml → loader → prompt path."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from task_context import build_task_context, resolve_context_paths

ROOT = pathlib.Path(__file__).resolve().parents[1]
TASK = "04-your-agents/tasks/01-threat-model-premortem.md"


def assert_in(needle, haystack, label):
    if needle not in haystack:
        raise AssertionError("{}: {!r} not in output".format(label, needle))


def assert_not_in(needle, haystack, label):
    if needle in haystack:
        raise AssertionError("{}: {!r} should be absent".format(label, needle))


def test_resolve_paths_merges_agent_and_task():
    paths = resolve_context_paths(TASK, ROOT)
    assert_in("02-design/threat-model.md", paths, "threat model")
    assert_in("context/system/agent-team.md", paths, "agent default")
    assert_in("research/red-team-seed.md", paths, "task seed")
    # agent default before task-only path
    assert paths.index("context/system/agent-team.md") < paths.index(
        "research/lifecycle-playbook-seed.md"
    ), "agent defaults precede task paths"


def test_task_01_stripped_context():
    ctx = build_task_context(TASK, ROOT)
    assert_in("---", ctx, "file delimiter")
    assert_in("Crown jewels", ctx, "threat-model artifact")
    assert_not_in("[!TEACH]", ctx, "TEACH stripped from constraints")
    assert_not_in("[!LEARN]", ctx, "LEARN stripped from dual-purpose inputs")
    # ADR-005 exempt — teaching markers in ADR body would remain if present
    assert_in("failure condition", ctx.lower(), "ADR-005 content")


def main():
    test_resolve_paths_merges_agent_and_task()
    test_task_01_stripped_context()
    print("test_task_context: all passed")


if __name__ == "__main__":
    main()
