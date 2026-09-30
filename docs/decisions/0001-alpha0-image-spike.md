# ADR 0001: Alpha 0 Image-Build Spike

- **Status:** Local spike proven; production platform decision open
- **Date:** 2026-09-30
- **Decision owner:** Nexus-OS maintainers

## Context

Nexus-OS needs an image build and recovery strategy before investing in a custom desktop or compatibility UI. Fedora Kinoite and Bazzite are both viable candidates to evaluate, but their desktop integration and update models differ. Fedora bootc is available as a minimal OCI base and can test the container-image build path independently of that product decision.

## Decision

Use `quay.io/fedora/fedora-bootc:43` only for a disposable Alpha 0 OCI build spike. The image contains no Nexus packages or desktop customization. Keep the choice of production base, desktop, and update technology open until a hardware-backed comparison is complete.

## Consequences

- We can validate a repeatable container build with the current Docker-enabled development environment.
- The Fedora 43 image built locally on x86-64, retained the Nexus OCI label, and ran `bootc --version` successfully on 2026-09-30.
- A successful build does not prove bootability, installation, atomic rollback, GPU support, audio latency, or suitability as a desktop base.
- Fedora Kinoite's rpm-ostree model and bootc's OCI image model are alternatives to compare, not layers to combine in one design.
- The mutable Fedora tag is acceptable only for this short-lived experiment. Any shared or released artifact requires a reviewed digest pin, provenance, SBOM, and signature.

## Alpha 0 exit checks

- [x] Build the image locally with Docker.
- [x] Confirm the resulting image contains the expected bootc tooling and identifying OCI labels.
- [ ] Build the image from a clean checkout in CI.
- Compare Fedora Kinoite and Bazzite on real target hardware for install/update/rollback, Secure Boot, GPU, creator applications, and support burden.
- Record a separate decision before selecting the production base or creating install media.