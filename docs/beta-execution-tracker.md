# Nexus-OS Beta Execution Tracker

## Purpose

This tracker converts the release backlog into a week-by-week execution plan with ownership, explicit dependencies, and clear release gating.

## Core principles

- Every task has an owner.
- Every release-blocking item has a clear status and risk.
- Every item must be tied to evidence or a test plan.
- No beta launch without a signed release package.

## Trackers

### Sprint 1 — Base and support proof

| Task | Owner | Priority | Status | Evidence required |
|---|---|---:|---|---|
| Freeze chosen base platform | Engineering | P0 | Planned | signed decision record |
| Qualify AMD hardware path | QA | P0 | Planned | hardware test matrix |
| Qualify Intel hardware path | QA | P0 | Planned | hardware test matrix |
| Qualify NVIDIA hardware path | QA | P0 | Planned | driver validation |
| Validate suspend/resume and audio routing | Platform | P0 | Planned | pass/fail report |

### Sprint 2 — Update, installer, and recovery

| Task | Owner | Priority | Status | Evidence required |
|---|---|---:|---|---|
| Stage update mechanism and rollback | Platform | P0 | Planned | rollback drill |
| Validate clean install flow | QA | P0 | Planned | install log and check list |
| Validate encryption and recovery path | Security | P0 | Planned | recovery guide and test report |
| Publish first support matrix | Support | P0 | Planned | support document |
| Validate first-boot onboarding | UX | P1 | Planned | onboarding checklist |

### Sprint 3 — Product and compatibility

| Task | Owner | Priority | Status | Evidence required |
|---|---|---:|---|---|
| Define app catalog metadata schema | Product | P1 | Planned | app manifest spec |
| Prototype compatibility launcher resolver | Platform | P1 | Planned | runtime selection examples |
| Validate native, Proton, and Waydroid flows | QA | P1 | Planned | support statuses |
| Define gaming and studio profiles | UX | P1 | Planned | profile review |
| Publish known issues log | Support | P0 | Planned | issue tracker |

### Sprint 4 — Beta release gate

| Task | Owner | Priority | Status | Evidence required |
|---|---|---:|---|---|
| Complete Beta sign-off package | Release manager | P0 | Planned | signed approval |
| Final release notes and communications | Product | P0 | Planned | public notes |
| Smoke test release artifact | QA | P0 | Planned | release smoke check |
| Approve beta user cohort | Product | P0 | Planned | cohort list |
| Ship beta announcement | Release manager | P0 | Planned | public announcement |

## Release gate rule

No sprint may be marked complete if its evidence is missing or the issue is not tied to a realistic user impact. Beta launch is blocked if any P0 item remains incomplete.
