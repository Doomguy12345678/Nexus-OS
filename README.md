# Nexus-OS

Nexus-OS is a Linux desktop distribution for gaming, creation, and everyday work. It aims to make native Linux software excellent and Windows compatibility approachable, while keeping the base system supportable, secure, and recoverable.

> **Project status:** architecture and discovery. This repository does not yet contain an installable operating system. Hardware support, licensing, update infrastructure, and a maintainable support team must be proven before a public release.

## Product principles

- Build on a supported Linux distribution and upstream desktop; do not fork the kernel or desktop to establish product identity.
- Keep the operating-system image small and mostly immutable. Install desktop applications separately and make system changes transactional and reversible.
- Treat compatibility as a per-application capability, not a promise that every Windows, macOS, or Android application works.
- Prefer upstream components, documented interfaces, signed artifacts, and reproducible builds.
- Offer creator reliability and predictable latency without making gaming tweaks the default for every workload.

## Architecture and plan

- [Architecture and feature designs](docs/architecture.md): platform choices, subsystem diagrams, compatibility boundaries, and risks.
- [Release roadmap](docs/roadmap.md): staged alpha-to-1.0 gates and measurable exit criteria.
- [Alpha 0 decision record](docs/alpha0.md): what the image spike proved and what remains open.
- [Alpha 1 platform evaluation](docs/alpha1.md): the next decision point for the operating-system base.
- [Full Alpha 1 implementation plan](docs/alpha1-full.md): hardware validation, support policy, update/rollback, and compatibility launcher design.
- [Beta gate checklist](docs/beta-gate.md): the criteria required before a public beta is declared.
- [Beta release policy](docs/beta-release-policy.md): support policy, security gating, and quality criteria for beta channel releases.
- [Beta sign-off package](docs/beta-signoff.md): the signed approval package used to decide whether the beta can ship.
- [Release sign-off checklist](docs/release-signoff-checklist.md): the review checklist used by engineering, product, and support signatories.
- [Beta launch artifacts](docs/beta-launch-artifacts.md): release notes, support matrix, known issues, and beta communication package.
- [Product implementation blueprint](docs/product-implementation-blueprint.md): the product architecture for the first public-facing beta.
- [Release backlog](docs/release-backlog.md): prioritized tasks for Beta readiness and the next delivery milestones.
- [Milestone plan](docs/milestone-plan.md): the phased project progression from Alpha 0 to 1.0.
- [Beta execution tracker](docs/beta-execution-tracker.md): sprint-based delivery plan with owners and release gates.
- [Release risk register](docs/release-risk-register.md): the active risk list and mitigation ownership for the Beta release.
- [Release owner matrix](docs/release-owner-matrix.md): the governance model and decision ownership for Beta readiness.
- [Beta sprint board](docs/beta-sprint-board.md): the weekly execution plan for the Beta program.
- [Beta release bundle](docs/beta-release-bundle.md): the user-facing release notes, support matrix, and beta agreement package.
- [Installer and first-boot design](docs/installer-design.md): disk layout, recovery, and first-boot validation plan.
- [Platform comparison matrix](docs/platform-evaluation.md): weighted decision analysis for Fedora Atomic KDE vs Bazzite.
- [Update and rollback design](docs/update-rollback.md): staged releases, rollback policy, and signed-asset handling.
- [Compatibility launcher design](docs/compatibility-launcher.md): policy and runtime selection for native, Proton, Android, and VM workflows.
- [Hardware qualification template](examples/hardware-qualification.yaml): checklists and telemetry for real-world validation.
- [Compatibility launcher manifest](examples/launcher-manifest.yaml): example launch policy for a Windows game or creator tool.
- [Example app catalog entry](examples/catalog-entry.yaml): illustrative metadata for a curated application.
- [Alpha 0 image spike](os/README.md): build and inspect the first bootc-derived OCI image.

## Initial platform proposal

Start with an upstream Fedora Atomic KDE desktop as the evaluation target, using its supported image and update model rather than maintaining a custom distribution stack. Keep the choice provisional until a hardware and workflow spike compares image build/update options, recovery, NVIDIA Secure Boot, creator software, and support burden. Use upstream kernels and drivers first; custom kernel work requires measured evidence and a separate tested, signed variant.

## Build status

The project has a verified Alpha 0 image spike and is now evaluating the real product base in Alpha 1. The next milestone is a measured comparison against candidate upstream Linux distributions, not a claim of full OS completion. See the [roadmap](docs/roadmap.md) and [Alpha 1 plan](docs/alpha1.md) for release gates.
