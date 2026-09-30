#!/usr/bin/env python3
"""Prototype launcher policy selector for Nexus-OS Alpha 1.

This script reads a launcher manifest and resolves the runtime adapter for a given app.
It is intentionally conservative: unresolved or unsupported states are reported as such.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover
    print("PyYAML is required to run this prototype.")
    sys.exit(2)


def resolve_runtime(manifest: dict) -> dict:
    kind = manifest.get("kind", "unknown")
    runtime = manifest.get("runtime", "native")
    policy = manifest.get("policy", {})
    status = policy.get("status", "unknown")

    if kind == "windows-game":
        if runtime == "proton":
            adapter = "Proton"
        elif runtime == "wine":
            adapter = "Wine"
        else:
            adapter = "Unknown compatibility adapter"
    elif kind == "android-app":
        adapter = "Waydroid"
    elif kind == "macos-workflow":
        adapter = "Virtualized macOS or native alternative"
    else:
        adapter = "Native Linux package"

    return {
        "kind": kind,
        "runtime": runtime,
        "adapter": adapter,
        "status": status,
        "notes": policy.get("notes", []),
        "name": manifest.get("name", "Unknown app"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve launcher runtime policy for a Nexus-OS app manifest.")
    parser.add_argument("manifest", type=Path, help="Path to the app or game manifest YAML file")
    args = parser.parse_args()

    try:
        with args.manifest.open("r", encoding="utf-8") as fh:
            manifest = yaml.safe_load(fh)
    except FileNotFoundError:
        print(f"Manifest not found: {args.manifest}", file=sys.stderr)
        return 2
    except yaml.YAMLError as exc:
        print(f"Invalid YAML: {exc}", file=sys.stderr)
        return 2

    result = resolve_runtime(manifest)
    print(f"App: {result['name']}")
    print(f"Kind: {result['kind']}")
    print(f"Selected adapter: {result['adapter']}")
    print(f"Compatibility status: {result['status']}")
    if result["notes"]:
        print("Notes:")
        for note in result["notes"]:
            print(f"  - {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
