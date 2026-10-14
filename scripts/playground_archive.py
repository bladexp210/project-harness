#!/usr/bin/env python3
"""Archive stale _playground/ experiments (4-day rule).

Spec: _playground/README.md
Usage:
  python scripts/playground_archive.py --dry-run
  python scripts/playground_archive.py
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import shutil
import sys

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ARCHIVE_AFTER_DAYS = 4
SKIP_DIRS = {"_archive"}
MANIFEST_NAME = "manifest.yaml"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def _parse_date(value: str | None) -> dt.date | None:
    if not value or not isinstance(value, str):
        return None
    value = value.strip()
    if not DATE_RE.match(value):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def _folder_mtime_date(path: pathlib.Path) -> dt.date:
    ts = max((p.stat().st_mtime for p in path.rglob("*") if p.is_file()), default=path.stat().st_mtime)
    return dt.date.fromtimestamp(ts)


def load_manifest(exp_dir: pathlib.Path) -> dict:
    manifest_path = exp_dir / MANIFEST_NAME
    if not manifest_path.is_file():
        return {}
    if yaml is None:
        return {}
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def last_activity_date(exp_dir: pathlib.Path, manifest: dict) -> dt.date:
    created = _parse_date(manifest.get("created"))
    updated = _parse_date(manifest.get("updated"))
    if updated:
        return updated
    if created:
        return created
    return _folder_mtime_date(exp_dir)


def should_archive(manifest: dict, last_active: dt.date, today: dt.date) -> bool:
    status = str(manifest.get("status", "experiment")).strip().lower()
    if status == "promoted":
        return False
    return (today - last_active).days > ARCHIVE_AFTER_DAYS


def archive_name(exp_dir: pathlib.Path, last_active: dt.date) -> str:
    return "{}-{}".format(last_active.isoformat(), exp_dir.name)


def find_experiments(playground: pathlib.Path) -> list[pathlib.Path]:
    out: list[pathlib.Path] = []
    for child in sorted(playground.iterdir()):
        if not child.is_dir() or child.name in SKIP_DIRS:
            continue
        for exp in sorted(child.rglob("*")):
            if exp.is_dir() and (exp / MANIFEST_NAME).is_file():
                if exp.parent.name == "_archive" or "_archive" in exp.parts:
                    continue
                out.append(exp)
    return out


def run_archive(root: pathlib.Path, *, dry_run: bool) -> list[tuple[pathlib.Path, pathlib.Path]]:
    if yaml is None:
        raise SystemExit("playground_archive.py requires PyYAML (pip install pyyaml)")

    playground = root / "_playground"
    archive_root = playground / "_archive"
    today = dt.date.today()
    moved: list[tuple[pathlib.Path, pathlib.Path]] = []

    for exp_dir in find_experiments(playground):
        manifest = load_manifest(exp_dir)
        last_active = last_activity_date(exp_dir, manifest)
        if not should_archive(manifest, last_active, today):
            continue
        dest = archive_root / archive_name(exp_dir, last_active)
        if dest.exists():
            dest = archive_root / "{}-{}".format(
                last_active.isoformat(),
                exp_dir.relative_to(playground).as_posix().replace("/", "-"),
            )
        moved.append((exp_dir, dest))
        if not dry_run:
            archive_root.mkdir(parents=True, exist_ok=True)
            shutil.move(str(exp_dir), str(dest))

    return moved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Archive _playground experiments idle > 4 days.")
    parser.add_argument("--dry-run", action="store_true", help="List moves without executing")
    parser.add_argument("--root", type=pathlib.Path, default=None, help="Repo root override")
    args = parser.parse_args(argv)

    root = args.root or _repo_root()
    moved = run_archive(root, dry_run=args.dry_run)

    if not moved:
        print("playground_archive: nothing to archive")
        return 0

    for src, dest in moved:
        label = "would move" if args.dry_run else "moved"
        print("{} {} -> {}".format(label, src.relative_to(root), dest.relative_to(root)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
