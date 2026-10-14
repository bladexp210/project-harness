#!/usr/bin/env python3
"""Tests for playground_archive.py."""
import datetime as dt
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from playground_archive import (
    ARCHIVE_AFTER_DAYS,
    last_activity_date,
    should_archive,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_should_archive_after_four_days():
    today = dt.date(2026, 6, 12)
    last = today - dt.timedelta(days=ARCHIVE_AFTER_DAYS + 1)
    assert should_archive({"status": "experiment"}, last, today)


def test_should_not_archive_promoted():
    today = dt.date(2026, 6, 12)
    last = today - dt.timedelta(days=30)
    assert not should_archive({"status": "promoted"}, last, today)


def test_should_not_archive_within_window():
    today = dt.date(2026, 6, 12)
    last = today - dt.timedelta(days=2)
    assert not should_archive({"status": "experiment"}, last, today)


def test_manifest_updated_wins():
    exp = ROOT / "_playground/icom/task-01"
    manifest = {"created": "2026-06-01", "updated": "2026-06-12"}
    assert last_activity_date(exp, manifest) == dt.date(2026, 6, 12)


def main():
    test_should_archive_after_four_days()
    test_should_not_archive_promoted()
    test_should_not_archive_within_window()
    test_manifest_updated_wins()
    print("test_playground_archive: all passed")


if __name__ == "__main__":
    main()
