# Nexus-OS Beta Release Bundle

## Purpose

This document consolidates the user-facing and operational materials needed to run a Beta release responsibly. It is the package a support team and early users would receive before the public beta begins.

## Bundle contents

1. Release notes
2. installation and recovery guide
3. support matrix
4. supported and unsupported workflows
5. known issues and workaround list
6. beta agreement and consent note
7. support contact and escalation path

## 1. Release notes

### Beta overview

Nexus-OS Beta is an early-access Linux desktop focused on gaming, content creation, music production, streaming, AI-assisted workflows, and everyday productivity. The platform is Linux-first and intentionally conservative about compatibility claims.

### Included in Beta

- Fedora Atomic KDE-based platform
- Proton and Wine compatibility flow
- native Linux app catalog
- gaming, creator, and studio profiles
- update and rollback handling on the supported base
- opt-in diagnostic collection for early support feedback

### What is not included or is limited

- broad unsupported hardware coverage
- unconditional support for every Windows title or anti-cheat variant
- all macOS virtualization use cases
- AI model or Android features without tested hardware and policy review

## 2. Installation and recovery guide

### Before installing

- back up data and create a recovery plan
- verify your hardware is on the supported matrix
- confirm your GPU driver path is supported
- ensure you understand the supported interface paths for audio and controllers

### Recovery actions

- use the recovery media or live environment to restore the last known-good deployment
- verify all system-critical data before reinstalling
- keep a written record of the last known-good configuration

## 3. Supported workflows

| Workflow | Status |
|---|---|
| Native Linux desktop apps | Supported |
| Steam + Proton | Supported with notes |
| OBS and creator apps | Supported with notes |
| Blender and 3D workflows | Supported with notes |
| Waydroid | Experimental |
| VM-managed macOS workflows | Restricted to legal, approved scenarios |
| Unsupported or risky anti-cheat titles | Unsupported |

## 4. Known issues template

| Issue ID | Workload | Impact | Workaround | Status |
|---|---|---|---|---|
| BETA-001 | unsupported hardware | limited performance or failure | use supported matrix | active |
| BETA-002 | specific anti-cheat game | launch failure | do not install unsupported title | active |
| BETA-003 | certain audio interfaces | routing issues | validate device profile | triage |

## 5. Beta agreement

By participating in the Beta program, users agree that:

- beta software may be unstable
- support is limited to the published matrix
- data backup is the user’s responsibility
- some workloads remain unsupported or experimental
- feedback is required to improve the product

## 6. Support contact and escalation

- support email or issue tracker to be defined by the project owner
- escalation route: engineering -> support -> product owner -> release manager
- issue response policy should be provided before public launch

## 7. Release approval gate

The Beta release bundle is ready only when:

- release notes are finalized
- support matrix is approved
- recovery instructions are published
- support contact is live
- sign-off package is completed
