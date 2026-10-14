#!/usr/bin/env python3
"""Manually annotate a human gate on the active session log."""

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from langfuse_bridge.session import read_state
from langfuse_bridge.session_log import append_human_gate


def main() -> int:
    parser = argparse.ArgumentParser(description="Annotate human gate on session log")
    parser.add_argument("gate", choices=["proceed", "merge"], help="Gate type")
    parser.add_argument("--note", default="", help="Optional annotation note")
    args = parser.parse_args()

    state = read_state()
    session_id = state.get("session_id")
    if not session_id:
        sys.stderr.write("No active session — run during an agent session.\n")
        return 1

    append_human_gate(session_id, args.gate, source="manual", note=args.note)
    print(f"Annotated gate '{args.gate}' on session {session_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
