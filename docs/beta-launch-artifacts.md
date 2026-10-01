# Nexus-OS Beta Launch Artifacts

## Purpose

The Beta launch artifacts package gives the project the documentation required to communicate, support, and govern the first public beta release without overstating product maturity.

## Contents

- release notes
- support matrix
- known issues log
- compatibility statement
- escalation and support path
- beta user agreement
- release sign-off record

## Release notes template

### Overview

- Product: Nexus-OS Beta
- Baseline: Fedora Atomic KDE evaluation platform
- Mode: limited public beta
- Availability: invite-only or early-access cohort

### Included capabilities

- Linux desktop base with curated app catalog
- Steam and Proton integration
- Flatpak-first app installation
- Waydroid and virtualization support where approved and configured
- basic creator and gaming profiles

### Known limitations

- hardware support is limited to the published matrix
- some Windows DRM and anti-cheat titles remain unsupported
- macOS virtualization requires separate legal review and supported hardware
- AI and model features are opt-in and hardware-dependent

## Support matrix template

No physical qualification records are currently available. Treat this as an unpublished planning template, not a statement of Beta support. The first qualification target is an Intel integrated-graphics laptop; all other classes remain in the pre-Beta validation matrix.

| Hardware class | Status | Notes |
|---|---|---|
| Intel integrated-graphics laptop (reference target) | Not qualified | First physical test target; exact model and evidence pending |
| Additional Intel laptop generations and hybrid graphics | Not qualified | Validate per laptop/GPU/driver configuration |
| AMD desktop | Not qualified | Driver path and Steam workflow untested |
| NVIDIA desktop | Not qualified | Vendor driver and Vulkan validation untested |
| AMD laptop | Not qualified | Thermal and suspend checks untested |
| NVIDIA laptop | Not qualified | Vendor driver, suspend, and hybrid graphics checks untested |

## Known issues log

Each issue entry must contain:

- issue ID
- affected hardware class
- summary
- user impact
- workaround or mitigation
- status
- owner

## Compatibility statement

Nexus-OS Beta is a Linux-first distribution. Native Linux applications are the preferred path. Windows compatibility is delivered through tested Wine/Proton prefixes and approved game-launcher adapters. Android support is containerized and isolated. macOS support is limited to legal, supported workflows and documented alternatives.

## Beta user agreement

Users must acknowledge:

- the beta is not a stable release
- the project supports a limited hardware matrix
- data backup remains the user’s responsibility
- some titles and workflows may be unsupported
- issue reporting is required to improve the beta program

## Release package checklist

- [ ] public beta notes written
- [ ] support matrix published
- [ ] known issues log posted
- [ ] compatibility statement added to the install flow
- [ ] support contact documented
- [ ] rollback and recovery notes published
- [ ] release approval attached
