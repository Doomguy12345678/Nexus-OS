# Hardware Qualification Procedure

## Purpose

Use one record per physical system and OS image. A hardware class is not qualified by a template, VM run, or result from a different machine. Keep the raw logs and link them from the record's `evidence` fields.

## What can be tested today

The repository does not yet contain an installable Nexus-OS image. Do not install the Alpha 0 OCI image on hardware. Tests run on Fedora Atomic KDE are baseline evaluations only; they do not qualify Nexus-OS until the product image exists and is tested separately.

### First reference profile: Intel laptop

Start with one representative x86-64 laptop using Intel integrated graphics. Record the laptop model, CPU/iGPU generation and PCI device IDs, firmware, graphics driver, Wi-Fi/Bluetooth devices, display panel, and any dock or external displays. Prioritize boot, graphics/Vulkan, suspend/resume, battery/AC behavior, Wi-Fi/Bluetooth, audio, and an everyday creator workflow. This qualifies only the exact tested configuration; it does not imply support for every Intel laptop. AMD and NVIDIA qualification remains required before making claims for those hardware classes.

### Chromebook-specific guardrails

The current PHASER360 inventory is from Linux Mint booted in UEFI mode with `/` on an `overlay` filesystem, consistent with a live-USB session. Limit this session to non-installing smoke checks: display, keyboard/touchpad, Wi-Fi/Bluetooth, audio, and suspend/resume (save no important work in the live session). Do not install an OS, repartition storage, run update/rollback drills, or flash firmware based on this inventory. The internal eMMC and USB disk are both present; device names alone are not approval to write to either. Any installed-OS trial needs a separate, model-specific plan and verified backup.

The tester reports that the current USB uses Ventoy with multiple operating-system images. The file `Fedora-Kinoite-ostree-x86_64-44-1.7.iso` presented `Install Fedora` and `Troubleshoot` at boot, with no live/try option identified. Treat this as installer media and do not proceed to disk selection. It is not currently suitable for the non-destructive live smoke test.

For a no-install desktop/hardware smoke test, use the [official Fedora KDE Plasma Desktop download page](https://fedoraproject.org/kde/download/) and select the x86_64 **Fedora KDE Desktop Live ISO** (the current page lists `Fedora-KDE-Desktop-Live-44-1.7.x86_64.iso`), not the Kinoite OSTree ISO. Copy it as a file onto the Ventoy data partition after checking free space and verify its checksum using Fedora's linked checksum file. This tests the Fedora KDE live environment only; it does not qualify Fedora Kinoite's Atomic update or rollback behavior. Do not use a USB imaging tool, reformat the Ventoy drive, write to the internal eMMC, or change Chromebook firmware. If a future Kinoite image does not provide a verified live/try path, test it only on a separate, recoverable target under a model-specific plan.

Use a spare machine with recoverable data for hardware testing. First copy the template and capture a baseline inventory from a terminal:

```sh
record_dir="qualification/$(hostname)-$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$record_dir"
cp examples/hardware-qualification.yaml "$record_dir/record.yaml"
{
    date -u --iso-8601=seconds
    cat /etc/os-release
    uname -a
    rpm-ostree status
    lscpu
    lspci -nnk
    lsusb
    kscreen-doctor -o
    wpctl status
} 2>&1 | tee "$record_dir/inventory.txt"
```

Fill in the record's hardware and image fields from this output. Also run `systemd-analyze time` for boot timing. If optional tools such as `vulkaninfo` or `glxinfo` are installed, capture `vulkaninfo --summary` and `glxinfo -B`; record a tool as unavailable rather than installing unreviewed packages just for a pass.

Do not publish raw logs without reviewing them for usernames, serial numbers, device names, and other personal information.

## Before testing

1. Copy [the qualification template](../examples/hardware-qualification.yaml) to a uniquely named record for the machine under test.
2. Record the owner, UTC test date, base release, deployed image digest or OSTree commit, kernel, system model, CPU, GPU models and driver versions, connected devices, and display configuration.
3. Record the image and configuration changes used for the run. Do not change the image midway through a record; create a new record for a different image.

## Run the checks

For each check, set `status` to `pass`, `fail`, `blocked`, or `not-run` and attach concise evidence. Evidence should include command output, logs, screenshots, or a reproducible workflow description. Record measurements with units rather than subjective summaries.

For application workflows, add one `applications` entry per exact app version and runtime version. Capture `id`, `version`, `runtime`, `runtime_version`, `status`, and `evidence`. A pass for one game or creator app does not qualify other apps using the same runtime.

Run each relevant workflow from a clean boot, hold the image and settings constant within a record, and capture the exact application/runtime versions. Use the following repeatable checks for the candidate matrix:

- **Gaming / Proton:** record the game build, Steam version, Proton version, GPU/driver, resolution, and graphics settings. Launch to gameplay, exercise graphics/audio/controller input, then repeat the same saved benchmark or fixed gameplay route. Record crashes, visual defects, and frame-time data; do not treat one game as evidence for all Proton titles.
- **Blender / 3D creation:** record Blender version and render device. Open a saved test scene, render it with the intended CPU/GPU backend, save the output, and inspect the render for errors. Keep the scene and settings identical between machines.
- **OBS / video:** record OBS version, source, encoder, resolution, and frame rate. Capture a 60-second display-plus-audio sample, play the recording back, and inspect OBS statistics for dropped frames and encoder overload. Attach the recording or a sanitized report.
- **REAPER / audio:** record REAPER version, interface model, sample rate, buffer size, and plugin versions. Open a saved test project, play and record a track, then inspect for dropouts and xruns. For creator qualification, perform and record a loopback latency measurement; startup alone is not a pass.
- **LibreOffice / productivity:** record application version and document formats tested. Open representative ODT/DOCX, spreadsheet, and presentation files, inspect layout, save a copy, reopen it, and verify the result. Note that this checks only the tested files and formats.
- **Hardware checks:** test suspend/resume, each display topology and scaling mode, controller pairing/input, and audio routing only for devices listed in the record. Attach command output or short evidence for each check.

For update/rollback, first save work and verify that the test machine has a known-good deployment. Record `rpm-ostree status`, apply an update using the supported desktop workflow or `rpm-ostree upgrade`, reboot, rerun the critical smoke checks, and record the new deployment. Then use `rpm-ostree rollback`, reboot, and verify the prior deployment and user data. Do this only on a spare, recoverable test installation; it changes the OS deployment.

Set each check's status only after reviewing its evidence. For example, a successful app launch with rendering glitches is not a pass; a command's exit code alone is not a workflow pass.

## Decision rules

- `not-run` is missing evidence, never a pass.
- `blocked` means the test could not be completed; document the external dependency and keep the hardware class unqualified for that check.
- Any critical check that is not `pass` blocks `supported` status.
- `supported` requires all applicable critical checks to pass without manual workarounds.
- `supported-with-notes` requires passing critical checks; document each non-critical failure or workaround as a known issue.
- `experimental` is a limited qualification result, not a substitute for missing release-critical coverage.
- Publish a support claim only after review of the completed record and linked evidence.

## Validate a record

Install the declared Python dependency once, then run the validator against the completed record:

```sh
python3 -m pip install -r requirements.txt
python3 scripts/validate_hardware_qualification.py qualification/<system-id>/record.yaml
```

Keep evidence files under that record directory and use relative paths in each `evidence` field; a field may contain one path or a list of paths. The validator checks required system and GPU/driver metadata, requires the boot, graphics, and update/rollback checks to pass, and verifies that evidence files exist. Application entries must include exact app/runtime versions; a passing application also needs evidence. Exit code `0` means the minimum gate passed, `1` means the record is incomplete or unqualified, and `2` means the record could not be read or parsed or the dependency is missing.

The validator checks record completeness, not the truth or quality of the test result. A reviewer must inspect the linked evidence before approving any support claim.

## Current state

The checked-in template is intentionally blank. No physical AMD, Intel, or NVIDIA hardware result is implied by this procedure or by the example app compatibility matrix.
