#!/usr/bin/env python3
"""Path C — Cursor/VS Code hook bridge to Langfuse (stdlib-only, fail-open)."""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from langfuse_bridge.ingest import (
    build_batch_item,
    flush_queue,
    load_track_a_env,
    new_id,
    send_batch,
    utc_now_iso,
)
from langfuse_bridge.redact import MAX_FIELD_LEN, redact_value
from langfuse_bridge.session import clear_state, read_state, write_state
from langfuse_bridge.session_log import (
    append_human_gate,
    append_timeline,
    finalize_log,
    init_log,
)
from langfuse_bridge.temporal import (
    TEMPORAL_EVENTS,
    check_canon_freshness,
    detect_human_gate,
)

GATE_EVENTS = frozenset(
    {
        "beforeSubmitPrompt",
        "preToolUse",
        "beforeShellExecution",
        "beforeMCPExecution",
        "beforeReadFile",
        "subagentStart",
    }
)


def span_name(hook_event: str) -> str:
    return f"cursor.{hook_event}"


def _timeline_detail(hook_event: str) -> str:
    if hook_event == "beforeSubmitPrompt":
        return "human prompt submitted"
    if hook_event in {"afterAgentResponse", "stop"}:
        return "agent turn complete"
    return ""


def _record_temporal(
    hook_event: str,
    hook_input: dict[str, Any],
    session_id: str,
    trace_id: str | None,
    at: str,
) -> None:
    if hook_event not in TEMPORAL_EVENTS:
        return
    if hook_event == "sessionEnd":
        finalize_log(session_id, at)
        return
    append_timeline(session_id, hook_event, detail=_timeline_detail(hook_event), at=at)
    gate = detect_human_gate(hook_event, hook_input)
    if not gate:
        return
    append_human_gate(session_id, gate, source="hook-detected")
    if trace_id:
        send_batch(
            [
                build_batch_item(
                    "span-create",
                    {
                        "id": new_id(),
                        "traceId": trace_id,
                        "name": f"cursor.human_gate.{gate}",
                        "startTime": at,
                        "metadata": {
                            "hook_event": hook_event,
                            "gate": gate,
                            "source": "hook-detected",
                        },
                    },
                )
            ]
        )


def emit_for_event(hook_event: str, hook_input: dict[str, Any]) -> None:
    safe_input = redact_value(hook_input)
    state = read_state()
    trace_id = state.get("trace_id")
    session_id = state.get("session_id")
    now = utc_now_iso()

    if hook_event == "sessionStart":
        flush_queue()
        trace_id = new_id()
        session_id = hook_input.get("session_id") or new_id()
        freshness = check_canon_freshness()
        write_state(
            {
                "trace_id": trace_id,
                "session_id": session_id,
                "started_at": now,
            }
        )
        init_log(session_id, now, freshness)
        if freshness.banner:
            sys.stderr.write(freshness.banner + "\n")
        send_batch(
            [
                build_batch_item(
                    "trace-create",
                    {
                        "id": trace_id,
                        "timestamp": now,
                        "name": "cursor-agent-session",
                        "sessionId": session_id,
                        "tags": ["path-c", "cursor-hook", "temporal"],
                        "metadata": {
                            "hook_event": hook_event,
                            "canon_freshness": freshness.to_dict(),
                        },
                        "input": safe_input,
                    },
                )
            ]
        )
        return

    if hook_event in {"sessionEnd", "stop"}:
        if session_id:
            _record_temporal(hook_event, hook_input, session_id, trace_id, now)
        if not trace_id:
            return
        send_batch(
            [
                build_batch_item(
                    "event-create",
                    {
                        "id": new_id(),
                        "traceId": trace_id,
                        "name": span_name(hook_event),
                        "startTime": now,
                        "input": safe_input,
                        "metadata": {"hook_event": hook_event},
                    },
                )
            ]
        )
        if hook_event == "sessionEnd":
            clear_state()
        return

    if not trace_id:
        trace_id = new_id()
        session_id = session_id or new_id()
        write_state(
            {
                "trace_id": trace_id,
                "session_id": session_id,
                "started_at": now,
            }
        )
        send_batch(
            [
                build_batch_item(
                    "trace-create",
                    {
                        "id": trace_id,
                        "timestamp": now,
                        "name": "cursor-agent-session",
                        "sessionId": session_id,
                        "tags": ["path-c", "cursor-hook", "implicit-start"],
                        "metadata": {"reason": "event-before-sessionStart"},
                    },
                )
            ]
        )

    if session_id and hook_event in TEMPORAL_EVENTS:
        _record_temporal(hook_event, hook_input, session_id, trace_id, now)

    span_id = new_id()
    body: dict[str, Any] = {
        "id": span_id,
        "traceId": trace_id,
        "name": span_name(hook_event),
        "startTime": now,
        "input": safe_input,
        "metadata": {"hook_event": hook_event},
    }
    if hook_event.startswith("post") or hook_event in {
        "afterShellExecution",
        "afterMCPExecution",
        "afterFileEdit",
        "afterAgentResponse",
    }:
        body["endTime"] = now

    send_batch([build_batch_item("span-create", body)])


def main() -> int:
    load_track_a_env()
    hook_event = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    raw = sys.stdin.read()
    hook_input: dict[str, Any] = {}
    if raw.strip():
        try:
            hook_input = json.loads(raw)
        except json.JSONDecodeError:
            hook_input = {"raw": raw[:MAX_FIELD_LEN]}

    try:
        emit_for_event(hook_event, hook_input)
    except Exception:
        pass

    if hook_event in GATE_EVENTS:
        sys.stdout.write(json.dumps({"permission": "allow"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
