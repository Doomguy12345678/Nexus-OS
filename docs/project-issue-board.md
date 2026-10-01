# Nexus-OS Project Issue Board

## Purpose

This issue board converts the release plan into discrete work items that can be tracked, assigned, and closed. It is the operational layer behind the architecture and Beta documentation.

## Epic 1 — Platform foundation

### Issue 1.1 — Finalize base platform decision
- Status: Planned
- Priority: P0
- Owner: Engineering Lead
- Acceptance criteria:
  - final platform selected
  - reasons documented
  - fallback option recorded
  - engineering sign-off complete

### Issue 1.2 — Validate supported hardware classes
- Status: Planned
- Priority: P0
- Owner: QA Lead
- Acceptance criteria:
  - AMD, Intel, and NVIDIA paths reviewed
  - support matrix published
  - unsupported classes labeled and documented

### Issue 1.3 — Prove update and rollback
- Status: Planned
- Priority: P0
- Owner: Platform Engineering
- Acceptance criteria:
  - clean install update path validated
  - rollback path documented and tested
  - recovery instructions published

## Epic 2 — Installer and recovery

### Issue 2.1 — Install flow validation
- Status: Planned
- Priority: P0
- Owner: QA Lead
- Acceptance criteria:
  - clean install succeeds on supported matrix
  - disk review and confirmation path confirmed
  - data-loss protections validated

### Issue 2.2 — Recovery flow validation
- Status: Planned
- Priority: P0
- Owner: Security + Support
- Acceptance criteria:
  - recovery media or path documented
  - last-known-good restore tested
  - user guidance published

## Epic 3 — Compatibility and app catalog

### Issue 3.1 — Catalog metadata model
- Status: Planned
- Priority: P1
- Owner: Product + Platform
- Acceptance criteria:
  - app manifest schema defined
  - support state documented
  - runtime and permissions defined

### Issue 3.2 — Compatibility launcher policy
- Status: Planned
- Priority: P1
- Owner: Compatibility Team
- Acceptance criteria:
  - native, Proton, Waydroid, and VM selection model defined
  - unsupported launch flows are blocked with explicit warnings

### Issue 3.3 — Creator and gaming profiles
- Status: Planned
- Priority: P1
- Owner: UX + Creator Platform
- Acceptance criteria:
  - gaming profile published
  - studio profile published
  - profile rollback tested

## Epic 4 — Release readiness

### Issue 4.1 — Beta sign-off package
- Status: Planned
- Priority: P0
- Owner: Release Manager
- Acceptance criteria:
  - all required sign-offs complete
  - release packet published
  - no unresolved critical blocker remains open

### Issue 4.2 — Beta launch artifacts
- Status: Planned
- Priority: P0
- Owner: Product + Support
- Acceptance criteria:
  - release notes published
  - support matrix published
  - known issues page published
  - beta agreement issued

### Issue 4.3 — Public beta announcement
- Status: Planned
- Priority: P0
- Owner: Product + Release Manager
- Acceptance criteria:
  - announcement prepared
  - support contact live
  - user cohort defined

## Definition of done

An issue can be closed only when:

- the owner has completed the task
- the acceptance criteria are met
- the evidence is recorded or linked
- support impact is understood
- the release-impact note is included
