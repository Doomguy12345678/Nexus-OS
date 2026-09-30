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
- [Example app catalog entry](examples/catalog-entry.yaml): illustrative metadata for a curated application.
- [Alpha 0 image spike](os/README.md): build and inspect the first bootc-derived OCI image.

## Initial platform proposal

Start with an upstream Fedora Atomic KDE desktop as the evaluation target, using its supported image and update model rather than maintaining a custom distribution stack. Keep the choice provisional until a hardware and workflow spike compares image build/update options, recovery, NVIDIA Secure Boot, creator software, and support burden. Use upstream kernels and drivers first; custom kernel work requires measured evidence and a separate tested, signed variant.

## Build status

There is no installer, image, package repository, launcher, or product service in this repository yet. The next engineering milestone is a hardware-backed technical prototype and written architecture decisions, not a claim of feature completeness. See the [roadmap](docs/roadmap.md) for release gates.
