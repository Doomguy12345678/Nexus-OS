from scripts.validate_hardware_qualification import validate_record


REQUIRED_CRITICAL_CHECKS = ("boot_first_login", "graphics_api", "update_rollback")


def qualified_record():
    return {
        "schema_version": 1,
        "system": {
            "id": "test-host-01",
            "owner": "qa",
            "tested_at_utc": "2026-09-30T12:00:00Z",
            "base": {
                "distribution": "Fedora Atomic KDE",
                "release": "43",
                "image_digest": "sha256:example",
                "kernel": "6.16.0",
            },
            "hardware": {
                "system_model": "Test workstation",
                "cpu": "Test CPU",
                "gpus": [
                    {"vendor": "AMD", "model": "Test GPU", "driver": "test-driver"}
                ],
            },
        },
        "checks": {
            name: {"critical": True, "status": "pass", "evidence": "logs/check.txt"}
            for name in REQUIRED_CRITICAL_CHECKS
        },
        "applications": [],
    }


def test_complete_record_passes_qualification_gate():
    assert validate_record(qualified_record()) == []


def test_non_pass_critical_check_blocks_qualification():
    record = qualified_record()
    record["checks"]["graphics_api"]["status"] = "not-run"
    record["checks"]["graphics_api"]["evidence"] = None

    errors = validate_record(record)
    assert any("checks.graphics_api" in error for error in errors)


def test_pass_without_evidence_is_rejected():
    record = qualified_record()
    record["checks"]["boot_first_login"]["evidence"] = None

    errors = validate_record(record)
    assert any("checks.boot_first_login.evidence" in error for error in errors)


def test_application_pass_requires_exact_versions_and_evidence():
    record = qualified_record()
    record["applications"] = [
        {"id": "video.obs-studio", "status": "pass"},
    ]

    errors = validate_record(record)
    assert any("applications[0].version" in error for error in errors)
    assert any("applications[0].evidence" in error for error in errors)


def test_evidence_references_must_exist_inside_record_directory(tmp_path):
    errors = validate_record(qualified_record(), evidence_root=tmp_path)

    assert any("evidence file does not exist" in error for error in errors)
