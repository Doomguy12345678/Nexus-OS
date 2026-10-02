from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .catalog import AppCatalog
from .cli import render_mode_plan
from .product import DEFAULT_DESKTOP_PROFILE, DesktopProfile

DEFAULT_PROFILE_PATH = Path(__file__).resolve().parent.parent / "examples" / "nexus-desktop-profile.yaml"
DEFAULT_CATALOG_PATH = Path(__file__).resolve().parent.parent / "examples" / "app_catalog.yaml"

FIRST_BOOT_HEALTH_CHECKS = (
    "Confirm timezone and locale for the user session.",
    "Verify network connectivity and driver detection.",
    "Check GPU support status and display configuration.",
    "Confirm audio interface detection and session routing.",
    "Initialize the optional app catalog and update channel selection.",
    "Run a final health check before the user starts their first workflow.",
)

RECOVERY_GUIDANCE = (
    "Backup important files before enabling disk encryption or changing partitions.",
    "Keep a recovery USB or live image ready as part of the initial setup plan.",
    "Store recovery keys and admin guidance in a secure, offline location.",
)


def _load_profile(profile_path: str | Path | None = None) -> DesktopProfile:
    if profile_path is None:
        path = DEFAULT_PROFILE_PATH
    else:
        path = Path(profile_path)
    return DesktopProfile.load_yaml(path)


def _load_catalog(catalog_path: str | Path | None = None) -> AppCatalog:
    if catalog_path is None:
        path = DEFAULT_CATALOG_PATH
    else:
        path = Path(catalog_path)
    return AppCatalog.load_yaml(path)


def render_first_boot_plan(
    mode_name: str,
    profile: DesktopProfile | None = None,
    catalog: AppCatalog | None = None,
) -> dict:
    selected_profile = profile or DEFAULT_DESKTOP_PROFILE
    selected_catalog = catalog or _load_catalog(DEFAULT_CATALOG_PATH)
    base_plan = render_mode_plan(mode_name, profile=selected_profile, catalog=selected_catalog)

    return {
        "mode": base_plan["mode"],
        "install_policy": base_plan["install_policy"],
        "runtime": base_plan["runtime"],
        "tune_profile": base_plan["tune_profile"],
        "default_apps": base_plan["default_apps"],
        "apps": base_plan["apps"],
        "user_defaults": {
            "desktop": selected_profile.desktop,
            "default_mode": selected_profile.default_mode,
            "locale": "en_US.UTF-8",
            "timezone": "UTC",
            "shell": "plasma",
        },
        "recovery_guidance": list(RECOVERY_GUIDANCE),
        "health_checks": list(FIRST_BOOT_HEALTH_CHECKS),
    }


def _interactive_mode_selection(profile: DesktopProfile) -> str:
    modes = profile.supported_modes
    print("Available Nexus-OS modes:")
    for index, name in enumerate(modes, start=1):
        print(f"  {index}. {name}")

    while True:
        raw = input("Choose a mode [creator]: ").strip() or "creator"
        normalized = raw.lower()
        if normalized in {mode.lower() for mode in modes}:
            return normalized
        try:
            choice_index = int(raw) - 1
        except ValueError:
            choice_index = -1
        if 0 <= choice_index < len(modes):
            return str(modes[choice_index]).lower()
        print("Please choose a valid Nexus-OS mode number or name.")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Select a Nexus-OS first-boot mode and emit the initial onboarding plan.")
    parser.add_argument("--mode", help="Mode to select (gaming, creator, studio, productivity).")
    parser.add_argument("--profile", type=Path, help="Path to the desktop profile YAML file.")
    parser.add_argument("--catalog", type=Path, help="Path to the app catalog YAML file.")
    parser.add_argument("--interactive", action="store_true", help="Prompt for a mode interactively if no mode is supplied.")
    args = parser.parse_args(argv)

    try:
        profile = _load_profile(args.profile) if args.profile else DEFAULT_DESKTOP_PROFILE
        catalog = _load_catalog(args.catalog) if args.catalog else _load_catalog(DEFAULT_CATALOG_PATH)

        selected_mode = args.mode
        if not selected_mode and args.interactive:
            selected_mode = _interactive_mode_selection(profile)
        if not selected_mode:
            selected_mode = profile.default_mode

        plan = render_first_boot_plan(selected_mode, profile=profile, catalog=catalog)
    except (FileNotFoundError, OSError, ValueError, RuntimeError) as exc:
        print(f"First-boot selection failed: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(plan, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
