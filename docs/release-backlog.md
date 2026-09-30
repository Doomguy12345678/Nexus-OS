# Nexus-OS Release Backlog

## Purpose

This backlog turns the Beta-ready architecture into a concrete delivery plan. It prioritizes the tasks that reduce support and release risk before the first public beta launch.

## Release priority legend

- P0: release-blocking and must be closed before beta
- P1: required before the first public beta but can be scheduled with explicit risk
- P2: post-beta or next-phase value-add

## Backlog

### P0 — Platform and support foundation

1. Confirm final base platform and freeze the product image source
   - Owner: Engineering
   - Status: planned
   - Deliverable: selected base platform and written rationale

2. Validate hardware support matrix across AMD, Intel, and NVIDIA
   - Owner: QA + Platform Engineering
   - Status: planned
   - Deliverable: supported and unsupported hardware lists with evidence

3. Prove update and rollback path on the selected base
   - Owner: Platform Engineering
   - Status: planned
   - Deliverable: tested updated image, recovery path, and rollback procedure

4. Publish known issues and support policy
   - Owner: Support + Product
   - Status: planned
   - Deliverable: public support tiers and issue reporting path

5. Define and prove installer and recovery flow
   - Owner: Platform + QA
   - Status: planned
   - Deliverable: tested install, data safety, and recovery flow

6. Freeze beta release criteria
   - Owner: Product + Engineering
   - Status: planned
   - Deliverable: approved Beta gate and sign-off package

### P1 — User-facing product experience

7. Build curated app catalog with metadata and policy
   - Owner: Product + Platform
   - Status: planned
   - Deliverable: app manifest schema and catalog entries for supported tools

8. Implement compatibility launcher policy resolver
   - Owner: Platform
   - Status: planned
   - Deliverable: runtime selection logic for native, Proton, Waydroid, and VM scenarios

9. Ship gaming and studio profiles
   - Owner: UX + Platform
   - Status: planned
   - Deliverable: game-mode, performance, studio, and creator profiles with rollback

10. Validate end-to-end app install and uninstallation flows
   - Owner: QA
   - Status: planned
   - Deliverable: user-visible workflow and rollback evidence

11. Publish Beta release notes and communication package
   - Owner: Product + Marketing
   - Status: planned
   - Deliverable: release notes, user agreement, and beta notice

### P2 — Expansion features

12. Expand AI assistant workflows
   - Owner: AI Platform
   - Status: planned
   - Deliverable: local offline assistant and workflow automation layer

13. Add mobile app container experience and controller tuning
   - Owner: Android + Platform
   - Status: planned
   - Deliverable: Waydroid and controller profiles for supported devices

14. Add broader macOS compatibility guidance
   - Owner: Compatibility + Legal review
   - Status: planned
   - Deliverable: supported alternatives and lawful VM guidance only

15. Add advanced creator automation and render workflows
   - Owner: Creator Platform
   - Status: planned
   - Deliverable: OBS, render presets, and workflow automation

## Definition of done for each backlog item

- requirement has an owner
- support impact is identified
- test evidence exists or is scheduled
- user-facing behavior is clearly described
- rollback or safe failure path is documented
- release or support gate is identified

## Beta release target

The Beta release should not happen until all P0 items are complete and all P1 items show a credible readiness path. A single unresolved P0 item is a release blocker.
