from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised only when PyYAML is absent.
    yaml = None


@dataclass(frozen=True)
class RuntimePolicy:
    name: str
    status: str = "unknown"
    notes: Optional[str] = None

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "RuntimePolicy":
        return cls(
            name=str(data.get("name", "unknown")),
            status=str(data.get("status", "unknown")),
            notes=data.get("notes"),
        )

    def is_supported(self) -> bool:
        return self.status.lower() in {"supported", "supported-with-notes"}

    def is_blocked(self) -> bool:
        return self.status.lower() in {"unsupported", "not-applicable"}


@dataclass
class AppRecord:
    id: str
    name: str
    kind: str = "generic"
    runtimes: list[RuntimePolicy] = field(default_factory=list)
    default_runtime: Optional[str] = None
    description: str = ""

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "AppRecord":
        runtime_entries = data.get("runtimes", [])
        return cls(
            id=str(data["id"]),
            name=str(data.get("name", data["id"])),
            kind=str(data.get("kind", "generic")),
            runtimes=[RuntimePolicy.from_mapping(item) for item in runtime_entries],
            default_runtime=data.get("default_runtime"),
            description=str(data.get("description", "")),
        )

    def runtime_by_name(self, runtime_name: str) -> Optional[RuntimePolicy]:
        for runtime in self.runtimes:
            if runtime.name.lower() == runtime_name.lower():
                return runtime
        return None

    def preferred_runtime(self) -> Optional[RuntimePolicy]:
        if self.default_runtime:
            runtime = self.runtime_by_name(self.default_runtime)
            if runtime is not None and not runtime.is_blocked():
                return runtime

        for runtime in self.runtimes:
            if runtime.is_supported():
                return runtime

        return next((runtime for runtime in self.runtimes if not runtime.is_blocked()), None)


_MODE_DEFAULT_APP_IDS: dict[str, tuple[str, ...]] = {
    "gaming": ("game.cyberpunk2077", "video.obs-studio"),
    "creator": ("creator.blender", "video.obs-studio"),
    "studio": ("audio.reaper", "video.obs-studio"),
    "productivity": ("productivity.libreoffice",),
}


class AppCatalog:
    def __init__(self, apps: Iterable[AppRecord] | None = None):
        self.apps = list(apps or [])

    @staticmethod
    def mode_default_app_ids(mode_name: str) -> tuple[str, ...]:
        return _MODE_DEFAULT_APP_IDS.get(str(mode_name).lower(), ())

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "AppCatalog":
        app_entries = data.get("apps", [])
        return cls([AppRecord.from_mapping(item) for item in app_entries])

    @classmethod
    def load_yaml(cls, path: str | Path) -> "AppCatalog":
        if yaml is None:
            raise RuntimeError("PyYAML is required to load catalog files.")

        document = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        if not isinstance(document, dict):
            raise ValueError("Catalog YAML must contain a mapping at the top level.")
        return cls.from_mapping(document)

    def add_app(self, app: AppRecord) -> None:
        self.apps.append(app)

    def get_app(self, app_id: str) -> Optional[AppRecord]:
        for app in self.apps:
            if app.id.lower() == app_id.lower():
                return app
        return None

    def apps_by_kind(self, kind: str) -> list[AppRecord]:
        normalized_kind = kind.lower()
        return [app for app in self.apps if app.kind.lower() == normalized_kind]

    def apps_for_mode(self, mode_name: str) -> list[AppRecord]:
        app_ids = {app_id.lower() for app_id in self.mode_default_app_ids(mode_name)}
        if not app_ids:
            return []

        return [app for app in self.apps if app.id.lower() in app_ids]

    def install_policy_for_mode(self, mode_name: str) -> dict[str, object]:
        normalized_name = str(mode_name).lower()
        if normalized_name == "gaming":
            return {
                "mode": "gaming",
                "install_policy": "proton-first",
                "default_app_ids": list(self.mode_default_app_ids(normalized_name)),
            }
        if normalized_name == "studio":
            return {
                "mode": "studio",
                "install_policy": "native-first",
                "default_app_ids": list(self.mode_default_app_ids(normalized_name)),
            }
        if normalized_name in {"creator", "productivity"}:
            return {
                "mode": normalized_name,
                "install_policy": "flatpak-first",
                "default_app_ids": list(self.mode_default_app_ids(normalized_name)),
            }
        return {
            "mode": normalized_name,
            "install_policy": "native-first",
            "default_app_ids": [],
        }

    def select_runtime(self, app_id: str, runtime_name: Optional[str] = None) -> Optional[RuntimePolicy]:
        app = self.get_app(app_id)
        if app is None:
            return None

        if runtime_name:
            return app.runtime_by_name(runtime_name)

        return app.preferred_runtime()
