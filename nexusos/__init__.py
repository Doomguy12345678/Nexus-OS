from .catalog import AppCatalog, AppRecord, RuntimePolicy
from .product import DEFAULT_DESKTOP_PROFILE, DesktopProfile, ModeProfile

__all__ = [
    "AppCatalog",
    "AppRecord",
    "RuntimePolicy",
    "DesktopProfile",
    "ModeProfile",
    "DEFAULT_DESKTOP_PROFILE",
    "main",
    "render_mode_plan",
    "render_first_boot_plan",
]


def __getattr__(name: str):
    if name in {"main", "render_mode_plan"}:
        from .cli import main, render_mode_plan

        return {"main": main, "render_mode_plan": render_mode_plan}[name]
    if name == "render_first_boot_plan":
        from .firstboot import render_first_boot_plan

        return render_first_boot_plan
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
