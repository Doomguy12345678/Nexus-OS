# First Hardware Qualification: Lenovo Chromebook PHASER360

## Qualification decision

**Status: NOT QUALIFIED — candidate reference system only.**

This document is the single qualification checklist and Alpha 1 decision record
for the Lenovo Chromebook PHASER360, Phaser board revision 4, with an Intel
Celeron N4000 and Gemini Lake UHD Graphics 600. A result applies only to this
physical system, its recorded firmware and peripherals, and the exact Nexus-OS
image tested. It does not establish support for Chromebooks generally or for
Intel laptops as a class.

No Nexus-OS image has been installed or qualified on this laptop. Existing
observations below came from Fedora KDE and Linux Mint live sessions; they are
useful hardware-smoke evidence only, not Nexus-OS passes. The current Fedora
Kinoite ISO trial did not expose a live/try option. Do not install to the
internal eMMC, repartition storage, or change firmware as part of this record.
An installed-image test requires a separately reviewed, model-specific recovery
plan and verified backup.

## System and test record

| Field | Value |
|---|---|
| System | Lenovo Chromebook PHASER360, Phaser revision 4 |
| Reported model number | KSB-B3K-F47-B3S-N8A-I8Q-C2A-A2A-Q87 |
| CPU / architecture | Intel Celeron N4000, x86_64 |
| Integrated GPU | Intel Gemini Lake UHD Graphics 600; Linux driver reported as `i915` |
| Memory | 3.7 GiB reported |
| Internal storage | 29.1 GB eMMC reported; **not approved for OS writes** |
| Network | Wi-Fi interface reported as `wlp0s12f0`; adapter identity not yet recorded |
| Audio | Celeron/Pentium Silver HDA; speaker output reported working |
| Firmware | UEFI boot observed; firmware version and configuration not recorded |
| Nexus-OS image / release / digest | Not available |
| Nexus-OS kernel / driver versions | Not available |
| Test owner / Nexus-OS test date | Unassigned / not run |
| Overall decision | Not qualified; no product support claim |

Inventory details are provisional where explicitly reported as such in
[`record.yaml`](record.yaml). Confirm them from raw, sanitized output before
making a support decision.

## Evidence ledger

The following are prior reports, not independent lab results. Keep source OS and
evidence level attached to each result.

| Area | Existing observation | Source and evidence | Nexus-OS result |
|---|---|---|---|
| Boot | UEFI boot into live sessions reported; Fedora KDE Desktop Live reached a desktop from Ventoy. Fedora Kinoite media presented installer/troubleshooting entries and no identified live option. | Fedora live-session user report, [evidence/fedora-kde-live-smoke.md](evidence/fedora-kde-live-smoke.md); media and UEFI notes in [`record.yaml`](record.yaml) | **Not run** — no installable/approved Nexus-OS test image |
| Network | Wi-Fi connectivity reported working. | Fedora live-session user report, [evidence/fedora-kde-live-smoke.md](evidence/fedora-kde-live-smoke.md); LMDE note in [evidence/live-session-smoke.md](evidence/live-session-smoke.md) | **Not run** — record adapter identity, reconnect behavior, and Nexus-OS logs |
| GPU | Mesa Intel UHD Graphics 600 with direct rendering reported. Vulkan was not checked in the LMDE session; the Fedora report did not establish Vulkan support. | [evidence/live-session-smoke.md](evidence/live-session-smoke.md) and [evidence/fedora-kde-live-smoke.md](evidence/fedora-kde-live-smoke.md) | **Not run** — capture PCI ID, kernel module, OpenGL and Vulkan capability on Nexus-OS |
| Audio | Speaker playback reported working in Fedora KDE and LMDE live sessions. Routing, microphone, Bluetooth, and latency were not measured. | [evidence/fedora-kde-live-smoke.md](evidence/fedora-kde-live-smoke.md) and [evidence/live-session-smoke.md](evidence/live-session-smoke.md) | **Not run** — check output/input routing and record an audio workload |
| Suspend/resume | Suspend/resume reported working in both live sessions. No cycle count, wake-source, or post-resume device checks recorded. | [evidence/fedora-kde-live-smoke.md](evidence/fedora-kde-live-smoke.md) and [evidence/live-session-smoke.md](evidence/live-session-smoke.md) | **Not run** — complete repeatability test on the exact image |

Reported 720p/1080p video playback and keyboard/touchpad operation are useful
ancillary smoke observations, but are not substitutes for the checks above or
for application qualification.

## Required Nexus-OS hardware checks

Run these on one immutable, identified Nexus-OS image after a safe, approved
deployment path exists. Record UTC time, image digest, kernel, firmware,
connected devices, commands, unedited logs, and any workaround. Sanitize
usernames, serial numbers, and other personal data before adding evidence.

| Check | Procedure and pass condition | Current status |
|---|---|---|
| Boot and first login | From the approved boot medium/deployment, complete three cold boots to a usable desktop; record time-to-login-ready for each. No boot repair, emergency shell, or manual kernel parameter is allowed. Record the installed image identity. | Not run |
| Network | Identify the Wi-Fi device and driver; connect to a known network, resolve DNS, transfer data, disconnect/reconnect, and confirm recovery after reboot. No unexplained disconnect or manual driver installation. | Not run |
| GPU / graphics | Record PCI ID, bound kernel driver, `glxinfo -B`, and `vulkaninfo --summary` where the tools are available. Verify direct rendering and the API required by the selected game. Missing diagnostic tools are “not measured,” not a pass or proof of unsupported hardware. | Not run |
| Audio | Verify speaker output, volume control, and an available microphone/input if present; save and play back a short test recording. Record PipeWire/PulseAudio devices and errors. Audio latency is not claimed unless measured separately. | Not run |
| Suspend/resume | Complete ten suspend/resume cycles on AC and five on battery. After each wake, verify display, Wi-Fi, audio, keyboard/touchpad, and that the session remains usable. No hang, forced reboot, lost device, or unrecovered network/audio failure. | Not run |
| Update and rollback | On an installed, recoverable Nexus-OS test deployment only, capture the known-good deployment, apply a signed update, verify boot and the smoke checks, roll back, and verify prior deployment and user data. Do not attempt this from a live session or on the internal eMMC without explicit recovery approval. | Not run; Alpha 1 blocker |

Attach evidence under this system's `evidence/` directory and link it here.
Every result must identify its OS/image; evidence from Fedora or LMDE must not be
relabelled as a Nexus-OS result.

## Narrow workload qualification

These are the only proposed gaming and creator profiles for the first
qualification. A pass qualifies only the exact tested application build,
runtime, image, settings, and hardware. It does not qualify all games, all
Proton titles, all creative applications, GPU rendering, or low-latency
production audio.

### Gaming mode: Steam / Proton, capped 720p

Test one named, legally obtained, non-anti-cheat game that is listed as
playable with the selected Proton version. Before execution, record the game
title/build, Steam and Proton versions, image digest, graphics driver, display
resolution, and settings. Use 1280x720, low graphics settings, plugged-in AC,
and a 30 FPS cap where the game supports it. Run the same built-in benchmark or
repeatable 10-minute gameplay route three times.

**Pass:** all runs reach playable gameplay without crash, blocking visual
defect, or audio/input failure; each run sustains at least 30 FPS average and
has 1% low of at least 20 FPS; no severe thermal or system-stability failure.
Attach the frame-time/FPS report and note whether the cap was achieved.
If no suitable title runs on the hardware, record `fail` or `blocked` with
reason; do not broaden the profile or lower the bar after seeing results.

**Selected title / build:** Not selected

**Steam / Proton versions:** Not available

**Result / evidence:** Not run

### Creator/studio mode: Blender CPU render

Use Blender's CPU renderer only; GPU rendering is outside this initial profile.
Record Blender version, scene source/revision, render engine, resolution,
sample count, and output checksum. Use a small, deterministic scene that fits
within the laptop's available memory. Render from a clean boot three times,
save each output, and inspect the image for missing assets, corruption, or
visible render errors. Record render time and peak memory for every run.

**Pass:** all three renders complete without crash, out-of-memory termination,
or visible corruption; outputs match the reference within the documented
deterministic comparison tolerance; the desktop remains recoverable after each
run. This is a bounded CPU-render workflow only, not a promise of interactive
3D performance, GPU rendering, OBS capture, DAW functionality, or real-time
audio latency.

**Blender version / scene revision:** Not available

**Result / evidence:** Not run

The gaming and creator profiles are independent release checks. Both must pass
for this candidate to be described as qualified for these two modes. A failed
profile must be listed as unsupported for this hardware/image combination
until retested; it must not be described as “supported with notes.”

## Alpha 1 qualification gate

Do not add a broader hardware target until this reference record has been
reviewed and the gate below is met.

**Required to pass Alpha 1 for this reference laptop:**

- [ ] Identify the exact Nexus-OS image, release, digest, kernel, firmware,
      hardware IDs, and test owner/date.
- [ ] Pass the boot/first-login and graphics checks with reproducible evidence.
- [ ] Pass network, audio, and suspend/resume checks with evidence.
- [ ] Complete update and rollback on a safely recoverable installed test
      deployment; never infer it from a live session.
- [ ] Pass the exact Steam/Proton gaming profile and Blender CPU-render
      creator/studio profile above, with versions, measurements, and artifacts.
- [ ] Review every failure, blocked test, workaround, and evidence artifact;
      publish the resulting supported/unsupported scope.

Until every required item passes, the decision remains **NOT QUALIFIED** and no
public support claim may name this laptop. If all checks pass, grant support
only for the exact recorded hardware and image configuration; rerun critical
checks when the image, kernel, or graphics stack changes materially.

## Explicitly unsupported at this stage

These exclusions prevent the first result from being stretched into unsupported
product claims. They may change only through separate, recorded qualification:

- Any laptop other than this PHASER360 Phaser revision 4 configuration,
  including other Chromebook models, board revisions, and firmware variants.
- AMD or NVIDIA graphics; discrete GPUs, hybrid graphics, and eGPUs.
- Docks, external or multi-monitor topologies, and peripherals not individually
  recorded and tested.
- Any game other than the exact qualified title/build; games requiring
  unsupported anti-cheat, kernel drivers, or unqualified DRM are unsupported.
- GPU-accelerated Blender, professional color-critical video, OBS streaming or
  encoding, and creator applications not explicitly tested.
- DAW/studio use that requires guaranteed low-latency audio, external interface
  support, MIDI, or Bluetooth audio; these have not been measured.
- Installation to or modification of this laptop's internal eMMC, firmware
  flashing, repartitioning, or dual-boot setup under this qualification.
- General battery-life, performance, security-certification, or long-term
  reliability claims; no such measurements are recorded here.

“Unsupported at this stage” means no product support is offered for that
configuration or workload; it is not a claim that upstream Linux cannot run
there.
