"""Unit tests for langfuse_trace_bridge redaction and batch shape."""

import json
import pathlib
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from langfuse_bridge import ingest, redact, session
import langfuse_trace_bridge as bridge


class RedactValueTests(unittest.TestCase):
    def test_redacts_api_key_pattern(self) -> None:
        text = "OPENAI_API_KEY=sk-example_not_real"
        result = redact.redact_value(text)
        self.assertIn("[REDACTED]", result)
        self.assertNotIn("sk-example_not_real", result)

    def test_truncates_long_strings(self) -> None:
        long_text = "x" * 800
        result = redact.redact_value(long_text)
        self.assertIn("[truncated sha256:", result)
        self.assertLess(len(result), 600)

    def test_nested_dict_redaction(self) -> None:
        payload = {"command": "export DATABASE_PASSWORD=not-a-real-secret"}
        result = redact.redact_value(payload)
        dumped = json.dumps(result)
        self.assertIn("[REDACTED]", dumped)


class BatchItemTests(unittest.TestCase):
    def test_build_batch_item_has_required_keys(self) -> None:
        item = ingest.build_batch_item(
            "trace-create",
            {"id": "t1", "name": "test", "timestamp": ingest.utc_now_iso()},
        )
        self.assertEqual(item["type"], "trace-create")
        self.assertIn("id", item)
        self.assertIn("timestamp", item)
        self.assertIn("body", item)


class EmitEventTests(unittest.TestCase):
    def setUp(self) -> None:
        session.clear_state()
        if ingest.QUEUE_DIR.is_dir():
            for path in ingest.QUEUE_DIR.iterdir():
                path.unlink()

    def tearDown(self) -> None:
        session.clear_state()

    @patch("langfuse_trace_bridge.send_batch")
    def test_session_start_creates_state(self, mock_send) -> None:
        bridge.emit_for_event("sessionStart", {"workspace": "/tmp/repo"})
        state = session.read_state()
        self.assertIn("trace_id", state)
        self.assertIn("session_id", state)
        mock_send.assert_called_once()
        batch = mock_send.call_args[0][0]
        self.assertEqual(batch[0]["type"], "trace-create")

    @patch("langfuse_trace_bridge.send_batch")
    def test_session_end_clears_state(self, mock_send) -> None:
        session.write_state({"trace_id": "t1", "session_id": "s1"})
        bridge.emit_for_event("sessionEnd", {})
        self.assertFalse(session.STATE_PATH.is_file())
        mock_send.assert_called_once()


if __name__ == "__main__":
    unittest.main()
