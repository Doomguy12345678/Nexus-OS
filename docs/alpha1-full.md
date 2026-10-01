# Nexus-OS Alpha 1: Full Execution Plan

## Objective

Alpha 1 makes the first real product decisions: which base to ship, how we qualify hardware, how we support users, how we verify updates, and how the system chooses the correct compatibility adapter for a given app or game.

This milestone is not a public release. It is a disciplined engineering gate that reduces product risk before the first beta image.

## 1. Recommended base

Use Fedora Atomic KDE (Kinoite) as the preferred base for the first production-grade evaluation. Keep Bazzite as a comparison and fallback target.

### Why this is the recommended baseline

- Better maintainability and long-term platform clarity.
- Strong Fedora security and image provenance story.
- Clear separation between base image and user-installed tools.
- Lower custom-support burden for a project that still needs to be polished and audited.

Use the weighted comparison in [platform-evaluation.md](platform-evaluation.md) as the source of truth. The current model prefers Fedora Atomic KDE by a small but meaningful margin.

## 2. Hardware qualification matrix

A supportable distro must be proven on hardware. The Alpha 1 stage requires a real matrix, not a speculative list.

### Minimum hardware classes and priority

Begin with one representative x86-64 laptop using Intel integrated graphics as the reference system. Record the exact laptop model, CPU and iGPU generation, firmware, driver, wireless devices, and connected peripherals; results apply only to that tested configuration.

Then qualify the broader pre-Beta matrix:

- additional Intel laptop generations and hybrid-graphics configurations
- AMD desktop GPU systems
- NVIDIA desktop GPU systems
- NVIDIA laptop systems if laptop support is in the Beta scope
- USB audio interface
- MIDI controller
- Bluetooth headset or controller
- multi-monitor desktop setup

Intel-first is a sequencing decision based on the initial target-user profile. It does not restrict product support or waive validation of AMD and NVIDIA systems before publishing claims for those classes.

### Required test categories

- boot time and first boot
- update and rollback
- suspend/resume
- Steam launch and Proton support
- OBS Studio capture
- Blender launch and simple render
- Ardour or equivalent DAW startup
- multi-monitor and display scaling
- GPU driver detection and Vulkan/OpenGL validation
- controller detection and mapping
- audio device routing and latency test

### Hardware qualification scoring

Each system receives a status:

- `supported`
- `supported-with-notes`
- `experimental`
- `unsupported`

A `supported` designation requires all critical checks to pass without manual workaround. A `supported-with-notes` designation allows a known limitation with clear documentation. `experimental` is reserved for pre-beta hardware and early support only.

## 3. Alpha 1 support policy

### Support tiers

| Tier | Scope | Examples |
|---|---|---|
| Tier 1 | Fully supported | Steam on supported GPU, OBS, Blender, PipeWire, KDE desktop |
| Tier 2 | Supported with notes | Waydroid, Proton titles with anti-cheat exceptions, external USB audio drivers |
| Tier 3 | Experimental | macOS VM workflows, edge-case gaming tools, specialized AI model tooling |

### Support policy requirements

- Each supported app, runtime, or game must be bound to a tested configuration.
- Every compatibility claim must include app version, GPU driver version, and test date.
- Unsupported workloads must be marked as such clearly and not silently hidden by the launcher.
- If a tool relies on Windows, Android, or VM support, the UI must show the status before execution.

## 4. Update and rollback architecture

See [update-rollback.md](update-rollback.md) for full details.

### Core rules

- Use the selected upstream atomic update model as the base OS update path.
- Stage a new image and verify it before a reboot or user-visible cutover.
- Do not permit a blocked update to overwrite a known-good user boot target.
- Keep one known-good deployment available at all times.
- Make rollback visible and simple to explain to the user.

### Required update checks

- signature verification
- volatile data retention policy
- health checks after reboot
- rollback entry in user-visible history
- clear user notice during an interrupted update

## 5. Compatibility launcher design

See [compatibility-launcher.md](compatibility-launcher.md) for the full design.

### Launcher responsibilities

- detect file type, app type, or launch target
- select a runtime adapter: native, Wine/Proton, Waydroid, or VM
- show a compatibility policy before launch
- record install, launch, and failure metadata
- maintain a reversible per-app environment

### Runtime adapters

| App type | Adapter |
|---|---|
| native Linux app | Flatpak or native package |
| Windows game or app | Proton or Wine prefix |
| Android app | Waydroid |
| macOS workflow | VM or native alternative only if legally supported |
| legacy installer | audited Wine prefix with strict permissions |

## 6. Alpha 1 deliverables checklist

At the end of Alpha 1, the project must have:

- a selected base platform with a documented rationale
- a completed hardware matrix with pass/fail records
- a support tier policy and public known-issues structure
- a staged update/rollback design written down and reviewed
- a compatibility-launcher pattern and manifest schema
- a release gate for Beta that is measurable and enforceable

## 7. Exit criteria for Beta

The Beta gate opens only when all of the following are true:

- the base platform is selected and justified
- support matrix is published with real pass/fail data
- key hardware classes are covered by the test matrix
- rollback and update health checks are proven on the chosen base
- launcher policy is documented for supported and unsupported workflows
- there are no unresolved critical security or licensing blockers

## 8. Alpha 1 conclusion

This milestone is the first real engineering lock-in. If completed properly, it gives Nexus-OS an evidence-driven product direction instead of a purely conceptual design. It is the difference between an OS proposal and an OS program with a measurable foundation.
