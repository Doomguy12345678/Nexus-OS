# Nexus-OS Beta Sprint Board

## Objective

This sprint board is the operational manifestation of the Beta execution tracker. It gives the release team a concrete schedule and a single source of truth for weekly progress.

## Sprint 1 — Platform and hardware proof

| ID | Task | Owner | Status | Due | Evidence |
|---|---|---|---|---|---|
| S1-1 | Finalize base platform decision | Engineering | Planned | Week 1 | signed decision record |
| S1-2 | Validate AMD support path | QA | Planned | Week 1 | pass/fail hardware report |
| S1-3 | Validate Intel support path | QA | Planned | Week 1 | pass/fail hardware report |
| S1-4 | Validate NVIDIA support path | QA | Planned | Week 1 | driver and Vulkan validation |
| S1-5 | Validate suspend/resume and audio routing | Platform | Planned | Week 2 | audio and power report |
| S1-6 | Publish initial support matrix | Support | Planned | Week 2 | support matrix |

## Sprint 2 — Installer, recovery, and release viability

| ID | Task | Owner | Status | Due | Evidence |
|---|---|---|---|---|---|
| S2-1 | Test clean install flow | QA | Planned | Week 3 | install log and result |
| S2-2 | Validate encryption and recovery path | Security | Planned | Week 3 | recovery test report |
| S2-3 | Validate update and rollback path | Platform | Planned | Week 3 | rollback runbook |
| S2-4 | Review known-issue triage and escalation policy | Support | Planned | Week 4 | issue workflow |
| S2-5 | Publish Beta release notes draft | Product | Planned | Week 4 | release notes |

## Sprint 3 — Compatibility and product polish

| ID | Task | Owner | Status | Due | Evidence |
|---|---|---|---|---|---|
| S3-1 | Validate native Linux app flow | QA | Planned | Week 5 | app install and run report |
| S3-2 | Validate Proton workflow | Compatibility | Planned | Week 5 | title matrix |
| S3-3 | Validate Waydroid flow | Compatibility | Planned | Week 5 | container test report |
| S3-4 | Validate gaming and studio profiles | UX | Planned | Week 5 | profile test report |
| S3-5 | Finalize known issues log | Support | Planned | Week 6 | issue tracker |

## Sprint 4 — Beta sign-off and launch

| ID | Task | Owner | Status | Due | Evidence |
|---|---|---|---|---|---|
| S4-1 | Complete release sign-off checklist | Release Manager | Planned | Week 7 | signed signoff |
| S4-2 | Complete Beta sign-off package | Release Manager | Planned | Week 7 | approval package |
| S4-3 | Final smoke test release artifact | QA | Planned | Week 7 | smoke test log |
| S4-4 | Approve beta user cohort | Product | Planned | Week 8 | cohort list |
| S4-5 | Publish beta announcement | Product | Planned | Week 8 | published announcement |

## Definition of done

A sprint item is complete only when:

- the owner has been assigned
- evidence is recorded and reviewed
- a clear status is visible to all stakeholders
- any unresolved issue is recorded in the risk register
- the item has a clear release impact note

## Release gate

No Beta launch is allowed unless:

- all S1 and S2 items are complete
- all P0 tasks are closed or explicitly accepted with written risk mitigation
- the Beta sign-off package is signed by all required owners
