# Nexus-OS Release Risk Register

## Purpose

This register captures the highest-risk items for the Beta program and assigns mitigation owners. A Beta release is not safe to ship if these risks are unmanaged or undocumented.

## High-priority risks

| Risk ID | Risk | Likelihood | Impact | Owner | Mitigation |
|---|---|---:|---:|---|---|
| R-01 | Platform choice fails on critical hardware support | Medium | High | Engineering | Validate final base on AMD, Intel, and NVIDIA before Beta |
| R-02 | Update/rollback path fails on real users | Medium | High | Platform Engineering | Prove rollback on a clean install and interrupted update |
| R-03 | Installer causes data loss or recovery confusion | Low | High | QA + Security | Explicit confirmation, disk review, recovery guide |
| R-04 | NVIDIA or laptop suspend issues block support claims | Medium | High | QA | Publish as supported-with-notes or experimental where needed |
| R-05 | Windows anti-cheat or DRM compatibility is misrepresented | Medium | High | Compatibility Team | Explicit support policy and user warnings |
| R-06 | Creator workflow stability is worse than advertised | Medium | High | Creator Platform | Validate OBS, Blender, and DAW workflows before Beta |
| R-07 | A third-party dependency or app source creates security risk | Low | High | Security | SBOM, provenance, and signed package review |
| R-08 | User support burden exceeds the team’s capacity | Medium | Medium | Support | Define tiers and triage process before Beta |

## Mitigation review cadence

- review weekly during active Beta preparation
- escalate any P0 risk immediately to the release manager
- require mitigation owner sign-off before the Beta approval package is closed

## Decision rule

A risk is release-blocking if it cannot be mitigated, has a named owner, and still impacts the supported hardware or user workflow claims. Beta launch is not allowed if a release-blocking risk remains open without documented mitigation and approval.
