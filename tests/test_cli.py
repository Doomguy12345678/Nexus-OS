from nexusos.cli import main, render_mode_plan


def test_render_mode_plan_returns_default_app_selection():
    plan = render_mode_plan("creator")

    assert plan["mode"] == "creator"
    assert plan["runtime"] == "native"
    assert plan["install_policy"] == "flatpak-first"
    assert "obs-studio" in plan["default_apps"]


def test_cli_main_prints_json_for_selected_mode(capsys):
    exit_code = main(["--mode", "gaming", "--catalog", "examples/app_catalog.yaml"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert '"mode": "gaming"' in captured.out
    assert '"install_policy": "proton-first"' in captured.out


def test_render_first_boot_plan_adds_onboarding_and_recovery_guidance():
    from nexusos.firstboot import render_first_boot_plan

    plan = render_first_boot_plan("studio")

    assert plan["mode"] == "studio"
    assert plan["install_policy"] == "native-first"
    assert "timezone" in plan["health_checks"][0].lower()
    assert "backup" in " ".join(plan["recovery_guidance"]).lower()


def test_first_boot_cli_accepts_explicit_mode_and_returns_zero():
    from nexusos.firstboot import main

    assert main(["--mode", "creator"]) == 0
