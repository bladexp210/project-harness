"""Unit tests for temporal awareness and session log dual-write."""

import json
import pathlib
import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from langfuse_bridge import session_log, temporal


class CanonFreshnessTests(unittest.TestCase):
    def test_detects_stale_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            state = root / "STATE.md"
            old = (datetime.now(timezone.utc) - timedelta(hours=48)).strftime(
                "%Y-%m-%d %H:%M"
            )
            state.write_text(f"---\nupdated: {old}\n---\n", encoding="utf-8")
            with patch.object(temporal, "CANON_FILES", (state,)):
                report = temporal.check_canon_freshness()
            self.assertIn("STATE.md", report.stale_files[0])
            self.assertIsNotNone(report.banner)

    def test_fresh_file_not_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            state = root / "STATE.md"
            recent = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            state.write_text(f"---\nupdated: {recent}\n---\n", encoding="utf-8")
            with patch.object(temporal, "CANON_FILES", (state,)):
                report = temporal.check_canon_freshness()
            self.assertEqual(report.stale_files, [])
            self.assertIsNone(report.banner)


class HumanGateDetectionTests(unittest.TestCase):
    def test_proceed_in_prompt(self) -> None:
        gate = temporal.detect_human_gate(
            "beforeSubmitPrompt", {"prompt": "yes, proceed with the plan"}
        )
        self.assertEqual(gate, "proceed")

    def test_merge_in_shell(self) -> None:
        gate = temporal.detect_human_gate(
            "beforeShellExecution", {"command": "git merge session-45/temporal-awareness"}
        )
        self.assertEqual(gate, "merge")

    def test_no_gate_on_unrelated_prompt(self) -> None:
        gate = temporal.detect_human_gate(
            "beforeSubmitPrompt", {"prompt": "fix the typo in README"}
        )
        self.assertIsNone(gate)


class MetricsTests(unittest.TestCase):
    def test_compute_duration_and_latency(self) -> None:
        events = [
            {"event": "sessionStart", "at": "2026-07-02T10:00:00.000Z"},
            {"event": "stop", "at": "2026-07-02T10:05:00.000Z"},
            {"event": "beforeSubmitPrompt", "at": "2026-07-02T10:07:00.000Z"},
            {"event": "human_gate.proceed", "at": "2026-07-02T10:07:30.000Z"},
            {"event": "sessionEnd", "at": "2026-07-02T10:30:00.000Z"},
        ]
        metrics = temporal.compute_metrics(events)
        self.assertEqual(metrics["session_duration_ms"], 30 * 60 * 1000)
        self.assertEqual(metrics["mean_human_latency_ms"], 2 * 60 * 1000)
        self.assertEqual(metrics["decision_count"], 1)


class SessionLogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.mkdtemp()
        self.logs = pathlib.Path(self.tmp) / "logs" / "sessions"
        patcher = patch.object(session_log, "LOGS_DIR", self.logs)
        self.addCleanup(patcher.stop)
        patcher.start()

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_init_and_finalize_writes_markdown(self) -> None:
        sid = "test-session-001"
        freshness = temporal.FreshnessReport(
            checked_at="2026-07-02T10:00:00.000Z",
            stale_files=[],
            banner=None,
        )
        session_log.init_log(sid, "2026-07-02T10:00:00.000Z", freshness)
        session_log.append_human_gate(sid, "proceed", "manual", note="confirmed scope")
        metrics = session_log.finalize_log(sid, "2026-07-02T10:30:00.000Z")
        path = session_log.log_path(sid)
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        self.assertIn("session_id: test-session-001", text)
        self.assertIn("human_gate.proceed", text)
        self.assertIn("| proceed | manual |", text)
        self.assertIsNotNone(metrics["session_duration_ms"])


if __name__ == "__main__":
    unittest.main()
