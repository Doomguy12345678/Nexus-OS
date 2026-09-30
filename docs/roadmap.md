# Nexus-OS Release Roadmap

The dates are intentionally omitted: each phase advances on evidence and staffing, not a calendar promise. A phase is not complete because a demo boots; its exit gates below must pass.

## Alpha 0: Feasibility

- Compare candidate upstream atomic desktops on two AMD/Intel systems and one NVIDIA system.
- Demonstrate image build, signed update, failed-update rollback, Secure Boot, and recovery.
- Validate Wayland desktop, Steam/Proton, PipeWire/JACK workflow, OBS, Blender, and one supported editor on real hardware.
- Review licensing/distribution terms for all proposed bundled software, codecs, runtimes, and app sources.
- **Exit:** architecture decisions recorded; repeatable CI image build; hardware matrix and risk register published; no unresolved critical security or licensing blocker.

## Alpha 1: Internal prototype

- Build a reproducible branded image from upstream components; keep the desktop usable without Nexus services.
- Implement catalog metadata verification and a read-only UI prototype; no arbitrary installer execution.
- Add update channels, signature verification, rollback, installer evaluation, and opt-in diagnostics design.
- Exercise clean install, upgrade, rollback, GPU driver, audio interface, controller, and multi-monitor test cases.
- **Exit:** internal testers can install/update/recover without developer intervention; all changes are traceable and signed; blocker bugs have owners.

## Alpha 2: Developer and creator alpha

- Add curated native apps and opt-in game compatibility adapters; per-app status and logs.
- Add bounded Game/Studio profiles with visible changes and rollback; validate audio latency and game frame-time baselines.
- Publish known-good hardware list, privacy notice, data backup/recovery guide, and vulnerability reporting channel.
- Run an external security review of privileged services, update trust, and installer flows.
- **Exit:** zero open critical/high findings without an accepted mitigation; update and recovery success meet declared thresholds on the supported matrix.

## Beta: Public hardware qualification

- Freeze the 1.0 feature set; provide accessible installer, signed channels, stable release notes, and support lifecycle.
- Expand test coverage across AMD/Intel/NVIDIA, Secure Boot, laptops, suspend, VRR, controllers, audio/MIDI, and creator workflows.
- Validate app upgrade/uninstall, disk-full behavior, offline use, encryption recovery, and update interruption.
- Pilot macOS VM guidance only where lawful; keep Waydroid, AI, and proprietary tools opt-in and separately licensed.
- **Exit:** no unresolved release-blocking defects; rollback and recovery drills pass; support and security response staffing is operational; license inventory approved.

## Release Candidate

- Feature freeze; only release, security, and data-loss fixes accepted.
- Rebuild artifacts from pinned inputs; verify signatures, SBOM, provenance, install media, upgrade, and rollback.
- Publish compatibility matrix, supported hardware, known issues, support window, privacy documentation, and recovery instructions.
- **Exit:** release checklist signed by engineering, security, support, and release owners; candidate passes a defined soak period with no critical regression.

## 1.0

- Ship a supported, signed Linux desktop image with one clearly documented base/update path, curated app installation, security updates, recovery, and support policy.
- Declare compatibility accurately; optional runtimes and vendor software are not 1.0 blockers unless advertised as supported.
- Monitor update health and security advisories; publish a post-release review and prioritize fixes from real support data.

## Definition of Done for a release feature

- Named owner, user value, and supported scope.
- Threat model and licensing review where the feature handles privileges, third-party software, models, codecs, or external services.
- Unit/integration tests plus hardware tests where hardware behavior is part of the claim.
- Accessible UI, clear failure state, logs with privacy controls, uninstall/disable path, and documentation.
- Update/rollback behavior tested; signed and traceable release artifact.