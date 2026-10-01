from nexusos.catalog import AppCatalog, AppRecord, RuntimePolicy
from nexusos.product import DesktopProfile


def test_default_nexus_desktop_profile_matches_product_scope():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")

    assert profile.name == "Nexus-OS"
    assert profile.desktop == "kde-plasma"
    assert profile.base_image == "fedora-kinoite"
    assert profile.default_mode == "creator"
    assert profile.supported_modes == ("gaming", "creator", "studio", "productivity")
    assert profile.supported_runtimes == ("native", "proton")


def test_gaming_mode_exposes_default_runtime_and_tuning():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")
    gaming = profile.mode_profile("gaming")

    assert gaming.name == "gaming"
    assert gaming.default_runtime == "proton"
    assert gaming.tune_profile == "low-latency"
    assert gaming.default_apps == ("steam", "heroic")


def test_creator_mode_exposes_default_runtime_and_tuning():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")
    creator = profile.mode_profile("creator")

    assert creator.name == "creator"
    assert creator.default_runtime == "native"
    assert creator.tune_profile == "creator-balanced"
    assert creator.default_apps == ("obs-studio", "blender")


def test_studio_mode_exposes_low_latency_default_runtime_and_apps():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")
    studio = profile.mode_profile("studio")

    assert studio.name == "studio"
    assert studio.default_runtime == "native"
    assert studio.tune_profile == "audio-stable"
    assert studio.default_apps == ("reaper", "ardour")


def test_productivity_mode_exposes_default_runtime_and_apps():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")
    productivity = profile.mode_profile("productivity")

    assert productivity.name == "productivity"
    assert productivity.default_runtime == "native"
    assert productivity.tune_profile == "balanced"
    assert productivity.default_apps == ("libreoffice", "firefox")


def test_app_catalog_can_resolve_mode_defaults():
    catalog = AppCatalog.load_yaml("examples/app_catalog.yaml")
    gaming_apps = catalog.apps_for_mode("gaming")

    assert [app.id for app in gaming_apps] == ["game.cyberpunk2077", "video.obs-studio"]


def test_desktop_profile_resolves_mode_plan_with_default_apps():
    profile = DesktopProfile.load_yaml("examples/nexus-desktop-profile.yaml")
    catalog = AppCatalog.load_yaml("examples/app_catalog.yaml")

    plan = profile.resolve_mode("gaming", catalog)

    assert plan["mode"] == "gaming"
    assert plan["install_policy"] == "proton-first"
    assert plan["runtime"] == "proton"
    assert [app["id"] for app in plan["apps"]] == ["game.cyberpunk2077", "video.obs-studio"]


def test_app_catalog_selects_supported_runtime_for_windows_game():
    catalog = AppCatalog(
        apps=[
            AppRecord(
                id="game.cyberpunk2077",
                name="Cyberpunk 2077",
                kind="windows-game",
                runtimes=[
                    RuntimePolicy(name="proton", status="supported-with-notes"),
                    RuntimePolicy(name="wine", status="unsupported"),
                ],
                default_runtime="proton",
            )
        ]
    )

    selected = catalog.select_runtime("game.cyberpunk2077")
    assert selected.name == "proton"
    assert selected.status == "supported-with-notes"


def test_app_catalog_rejects_unknown_app():
    catalog = AppCatalog(apps=[])
    assert catalog.select_runtime("missing.app") is None


def test_preferred_runtime_skips_explicitly_unsupported_runtime():
    app = AppRecord(
        id="creator.example",
        name="Example Creator App",
        runtimes=[
            RuntimePolicy(name="wine", status="unsupported"),
            RuntimePolicy(name="native", status="supported-with-notes"),
        ],
        default_runtime="wine",
    )

    assert app.preferred_runtime().name == "native"


def test_app_catalog_filters_by_category():
    catalog = AppCatalog(
        apps=[
            AppRecord(id="video.obs", name="OBS Studio", kind="video"),
            AppRecord(id="audio.reaper", name="REAPER", kind="audio"),
        ]
    )

    assert [app.id for app in catalog.apps_by_kind("VIDEO")] == ["video.obs"]


def test_preferred_runtime_returns_none_when_all_runtimes_are_blocked():
    app = AppRecord(
        id="app.blocked",
        name="Blocked App",
        runtimes=[RuntimePolicy(name="wine", status="unsupported")],
    )

    assert app.preferred_runtime() is None
