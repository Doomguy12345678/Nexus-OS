from nexusos.catalog import AppCatalog, AppRecord, RuntimePolicy


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
