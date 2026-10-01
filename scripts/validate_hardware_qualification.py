#!/usr/bin/env python3
"""Validate that a hardware record meets the minimum qualification gate."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - depends on local environment.
    yaml = None

VALID_STATUSES = {"pass", "fail", "blocked", "not-run"}
EVIDENCE_STATUSES = {"pass", "fail", "blocked"}
REQUIRED_CRITICAL_CHECKS = {"boot_first_login", "graphics_api", "update_rollback"}


def _mapping(value: Any, path: str, errors: list[str]) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        errors.append(f"{path} must be a mapping")
        return {}
    return value


def _required_value(data: Mapping[str, Any], key: str, path: str, errors: list[str]) -> None:
    value = data.get(key)
    if value is None or not str(value).strip() or str(value).strip().upper() in {"TBD", "TODO"}:
        errors.append(f"{path}.{key} is required")


def _required_evidence(
    data: Mapping[str, Any],
    path: str,
    errors: list[str],
    evidence_root: Path | None,
) -> None:
    evidence = data.get("evidence")
    if isinstance(evidence, str):
        references = [evidence]
    elif isinstance(evidence, list) and all(isinstance(item, str) for item in evidence):
        references = evidence
    else:
        references = []

    if not references or any(not item.strip() for item in references):
        errors.append(f"{path}.evidence must reference at least one evidence file")
        return

    if evidence_root is None:
        return

    root = evidence_root.resolve()
    for reference in references:
        relative_path = Path(reference)
        if relative_path.is_absolute() or ".." in relative_path.parts:
            errors.append(f"{path}.evidence paths must stay inside the record directory")
            continue
        evidence_path = (root / relative_path).resolve()
        if not evidence_path.is_relative_to(root):
            errors.append(f"{path}.evidence paths must stay inside the record directory")
        elif not evidence_path.is_file():
            errors.append(f"{path}.evidence file does not exist: {reference}")


def validate_record(record: Any, evidence_root: Path | None = None) -> list[str]:
    """Return errors that prevent this record from passing the qualification gate."""
    errors: list[str] = []
    record = _mapping(record, "record", errors)

    if record.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    system = _mapping(record.get("system"), "system", errors)
    for key in ("id", "owner", "tested_at_utc"):
        _required_value(system, key, "system", errors)

    base = _mapping(system.get("base"), "system.base", errors)
    for key in ("distribution", "release", "image_digest", "kernel"):
        _required_value(base, key, "system.base", errors)

    hardware = _mapping(system.get("hardware"), "system.hardware", errors)
    for key in ("system_model", "cpu"):
        _required_value(hardware, key, "system.hardware", errors)

    gpus = hardware.get("gpus")
    if not isinstance(gpus, list) or not gpus:
        errors.append("system.hardware.gpus must list at least one tested GPU")
    else:
        for index, gpu_value in enumerate(gpus):
            gpu = _mapping(gpu_value, f"system.hardware.gpus[{index}]", errors)
            for key in ("vendor", "model", "driver"):
                _required_value(gpu, key, f"system.hardware.gpus[{index}]", errors)

    checks = _mapping(record.get("checks"), "checks", errors)
    for name in REQUIRED_CRITICAL_CHECKS:
        if name not in checks:
            errors.append(f"checks.{name} is required and critical")

    for name, check_value in checks.items():
        path = f"checks.{name}"
        check = _mapping(check_value, path, errors)
        status = check.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{path}.status must be one of {', '.join(sorted(VALID_STATUSES))}")
            continue
        if name in REQUIRED_CRITICAL_CHECKS and check.get("critical") is not True:
            errors.append(f"{path}.critical must be true")
        if status in EVIDENCE_STATUSES:
            _required_evidence(check, path, errors, evidence_root)
        if name in REQUIRED_CRITICAL_CHECKS and status != "pass":
            errors.append(f"{path} is critical and must pass (currently {status})")

    applications = record.get("applications", [])
    if not isinstance(applications, list):
        errors.append("applications must be a list")
    else:
        for index, application_value in enumerate(applications):
            path = f"applications[{index}]"
            application = _mapping(application_value, path, errors)
            for key in ("id", "version", "runtime", "runtime_version"):
                _required_value(application, key, path, errors)
            status = application.get("status")
            if status not in VALID_STATUSES:
                errors.append(f"{path}.status must be one of {', '.join(sorted(VALID_STATUSES))}")
            elif status in EVIDENCE_STATUSES:
                _required_evidence(application, path, errors, evidence_root)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check whether a hardware qualification record has the required evidence."
    )
    parser.add_argument("record", type=Path, help="Path to a qualification YAML record")
    args = parser.parse_args()

    if yaml is None:
        print("PyYAML is required; install dependencies with: python3 -m pip install -r requirements.txt", file=sys.stderr)
        return 2

    try:
        with args.record.open("r", encoding="utf-8") as stream:
            record = yaml.safe_load(stream)
    except OSError as exc:
        print(f"Cannot read qualification record: {exc}", file=sys.stderr)
        return 2
    except yaml.YAMLError as exc:
        print(f"Invalid YAML: {exc}", file=sys.stderr)
        return 2

    errors = validate_record(record, evidence_root=args.record.parent)
    if errors:
        print("NOT QUALIFIED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("QUALIFIED: required hardware checks passed with evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
