from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .catalog import AppCatalog
from .product import DEFAULT_DESKTOP_PROFILE, DesktopProfile

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROFILE_PATH = REPO_ROOT / "examples" / "nexus-desktop-profile.yaml"
DEFAULT_CATALOG_PATH = REPO_ROOT / "examples" / "app_catalog.yaml"


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


def render_mode_plan(
    mode_name: str,
    profile: DesktopProfile | None = None,
    catalog: AppCatalog | None = None,
) -> dict:
    selected_profile = profile or DEFAULT_DESKTOP_PROFILE
    selected_catalog = catalog

    if selected_catalog is None:
        selected_catalog = _load_catalog(DEFAULT_CATALOG_PATH)

    return selected_profile.resolve_mode(mode_name, selected_catalog)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve the Nexus-OS desktop mode and install plan.")
    parser.add_argument("--mode", default="creator", help="Product mode to resolve (for example: gaming, creator, studio, productivity).")
    parser.add_argument("--profile", type=Path, help="Path to the desktop profile YAML file.")
    parser.add_argument("--catalog", type=Path, help="Path to the app catalog YAML file.")
    args = parser.parse_args(argv)

    try:
        profile = _load_profile(args.profile) if args.profile else DEFAULT_DESKTOP_PROFILE
        catalog = _load_catalog(args.catalog) if args.catalog else _load_catalog(DEFAULT_CATALOG_PATH)
        plan = render_mode_plan(args.mode, profile=profile, catalog=catalog)
    except (FileNotFoundError, OSError, ValueError, RuntimeError) as exc:
        print(f"Failed to resolve Nexus mode: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(plan, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
