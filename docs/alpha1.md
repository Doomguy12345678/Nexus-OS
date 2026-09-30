# Nexus-OS Alpha 1: Base Platform Selection

## Objective

Choose the upstream Linux base that best matches Nexus-OS goals before building the full desktop, compatibility stack, and release pipeline. Alpha 1 is about evidence and reduction of risk, not a public desktop release.

## Candidate bases

- Fedora Atomic KDE (Kinoite) as a standard Fedora-based atomic desktop with strong upstream support and predictable package/rebase behavior.
- Bazzite as a gaming-first Fedora derivative with many device and game optimizations already implemented, but with more opinionated defaults and a stronger maintenance burden.

## Decision criteria

1. Update and rollback model
2. Driver and hardware support, especially NVIDIA and hybrid graphics
3. Creator workload fit, including audio and video tools
4. Ease of support and maintainability
5. Gaming compatibility and low-latency defaults
6. Security posture, package provenance, and image immutability
7. Compatibility with a future Nexus shell and application catalog

## Weighted scoring model

The project uses a weighted comparison model to reduce subjective bias. A practical example is included in [platform-evaluation.md](platform-evaluation.md) and in the companion script [scripts/compare_platforms.py](../scripts/compare_platforms.py).

| Criterion | Weight | Why it matters |
|---|---:|---|
| Update and rollback | 20 | A stable base is required for production use |
| Driver support | 20 | Gamers and creators depend on GPU and audio reliability |
| Creator workflow fit | 15 | Multimedia needs are a central product promise |
| Gaming optimization | 15 | Steam, Proton, overlays, and controller support matter |
| Maintainability | 15 | Too much custom patching slows the roadmap |
| Security and provenance | 10 | Trust and auditability are essential |
| Ecosystem compatibility | 5 | Launchers, Flatpak, and app catalogs must work cleanly |

## Assessment approach

- Run both candidates in a controlled hardware-backed comparison.
- Meet on a common benchmark set: boot time, suspend/resume, GPU detection, audio interface detection, controller identity, Steam launch success, OBS capture, Blender startup, and DAW session open.
- Record results in a fixed matrix and include known issues, not just the best-case outcome.
- Rank the platforms by objective, reproducible measurements and one human-readability score.

## Deliverables for Alpha 1

- Platform comparison document with weighted scores and reasoning.
- Hardware qualification template with exact benchmarks to run on each system.
- Known-issue log for both candidates.
- Recommended base decision and final stance for the product team.

## Exit criteria

Alpha 1 is complete only after the following are true:

- both candidates have been evaluated on real hardware, not just spec sheets;
- the platform matrix is committed to the repository;
- all critical blockers are documented with mitigation paths;
- the team has a recommended base for Beta with a fallback if the primary candidate fails on support or security grounds.

## Recommendation at this stage

Use the data-first path: treat Fedora Atomic KDE as the safer default and Bazzite as the higher-opinion gaming-oriented candidate. Do not choose a platform on branding alone. The final decision must be backed by test data and support burden, not by preference.
