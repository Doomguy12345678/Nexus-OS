from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised only when PyYAML is absent.
    yaml = None


@dataclass(frozen=True)
class ModeProfile:
    """Small, explicit profile for a Nexus desktop mode."""

    name: str
    default_runtime: str = "native"
    tune_profile: str = "balanced"
    default_apps: tuple[str, ...] = ()
    notes: str = ""

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "ModeProfile":
        return cls(
            name=str(data.get("name", "mode")),
            default_runtime=str(data.get("default_runtime", "native")),
            tune_profile=str(data.get("tune_profile", "balanced")),
            default_apps=tuple(str(app) for app in data.get("default_apps", ())),
            notes=str(data.get("notes", "")),
        )


def _default_mode_profiles() -> dict[str, ModeProfile]:
    return {
        "gaming": ModeProfile(
            name="gaming",
            default_runtime="proton",
            tune_profile="low-latency",
            default_apps=("steam", "heroic"),
            notes="Low-latency gaming defaults with Proton-first compatibility policy.",
        ),
        "creator": ModeProfile(
            name="creator",
            default_runtime="native",
            tune_profile="creator-balanced",
            default_apps=("obs-studio", "blender"),
            notes="Creator defaults focus on capture, editing, and multi-monitor work.",
        ),
        "studio": ModeProfile(
            name="studio",
            default_runtime="native",
            tune_profile="audio-stable",
            default_apps=("reaper", "ardour"),
            notes="Studio defaults prioritize device routing, low latency, and predictable audio.",
        ),
        "productivity": ModeProfile(
            name="productivity",
            default_runtime="native",
            tune_profile="balanced",
            default_apps=("libreoffice", "firefox"),
            notes="Productivity defaults favor a clean, familiar desktop workflow.",
        ),
    }


@dataclass(frozen=True)
class DesktopProfile:
    """Minimal product definition for the Nexus-OS desktop layer.

    This intentionally stays small: it declares the Linux desktop base, the
    default user workflow, and the compatibility runtimes the project is
    presently willing to support by policy rather than assumption.
    """

    name: str = "Nexus-OS"
    desktop: str = "kde-plasma"
    base_image: str = "fedora-kinoite"
    default_mode: str = "creator"
    supported_modes: tuple[str, ...] = ("gaming", "creator", "studio", "productivity")
    supported_runtimes: tuple[str, ...] = ("native", "proton")
    install_policy: str = "flatpak-first"
    update_model: str = "fedora-atomic"
    notes: str = (
        "Nexus-OS starts from an upstream Fedora Atomic KDE base and keeps the "
        "product layer explicit, minimal, and evidence-driven."
    )
    mode_profiles: dict[str, ModeProfile] = field(default_factory=_default_mode_profiles)

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "DesktopProfile":
        mode_entries = data.get("mode_profiles", {})
        mode_profiles = {
            str(key).lower(): ModeProfile.from_mapping(value)
            for key, value in mode_entries.items()
        }
        if not mode_profiles:
            mode_profiles = _default_mode_profiles()

        return cls(
            name=str(data.get("name", "Nexus-OS")),
            desktop=str(data.get("desktop", "kde-plasma")),
            base_image=str(data.get("base_image", "fedora-kinoite")),
            default_mode=str(data.get("default_mode", "creator")),
            supported_modes=tuple(
                str(mode) for mode in data.get("supported_modes", cls().supported_modes)
            ),
            supported_runtimes=tuple(
                str(runtime) for runtime in data.get("supported_runtimes", cls().supported_runtimes)
            ),
            install_policy=str(data.get("install_policy", "flatpak-first")),
            update_model=str(data.get("update_model", "fedora-atomic")),
            notes=str(data.get("notes", cls().notes)),
            mode_profiles=mode_profiles,
        )

    @classmethod
    def load_yaml(cls, path: str | Path) -> "DesktopProfile":
        if yaml is None:
            raise RuntimeError("PyYAML is required to load desktop profile files.")

        document = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        if not isinstance(document, dict):
            raise ValueError("Desktop profile YAML must contain a mapping at the top level.")
        return cls.from_mapping(document)

    def mode_profile(self, mode_name: str) -> ModeProfile | None:
        return self.mode_profiles.get(str(mode_name).lower())

    def resolve_mode(self, mode_name: str, catalog: Any | None = None) -> dict[str, Any]:
        mode = self.mode_profile(mode_name)
        if mode is None:
            raise ValueError(f"Unknown Nexus desktop mode: {mode_name}")

        if catalog is None:
            catalog_entries = []
        else:
            from .catalog import AppCatalog

            if isinstance(catalog, AppCatalog):
                catalog_entries = catalog.apps_for_mode(mode.name)
            else:
                catalog_entries = []

        install_policy = {
            "gaming": "proton-first",
            "creator": "flatpak-first",
            "studio": "native-first",
            "productivity": "flatpak-first",
        }.get(mode.name, "native-first")

        return {
            "mode": mode.name,
            "install_policy": install_policy,
            "runtime": mode.default_runtime,
            "tune_profile": mode.tune_profile,
            "default_apps": list(mode.default_apps),
            "apps": [
                {
                    "id": app.id,
                    "name": app.name,
                    "kind": app.kind,
                    "preferred_runtime": app.preferred_runtime().name if app.preferred_runtime() else None,
                }
                for app in catalog_entries
            ],
        }


DEFAULT_DESKTOP_PROFILE = DesktopProfile()
