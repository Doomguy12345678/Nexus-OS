# Nexus-OS Beta Gate Checklist

## Purpose

The Beta gate is the threshold that proves the platform is ready for a real user cohort. It is not a marketing milestone; it is a technical commitment to support and recovery, with hard criteria for launch readiness.

## Gate 1: Platform selection

- one supported base platform selected and documented
- decision record approved by engineering
- rationale includes support burden, update behavior, and hardware validation
- fallback candidate identified and evaluated

## Gate 2: Hardware coverage

- AMD, Intel, and NVIDIA support matrix completed or documented as unsupported
- at least one representative creator workstation profile validated
- at least one gaming-focused setup validated
- suspend/resume, audio interfaces, controllers, and display scaling pass in the supported matrix

## Gate 3: Update and rollback

- signed update process defined and reviewed
- rollback path proven on the chosen base
- recovery instructions published
- boot health checks pass after staged deployment

## Gate 4: Security and provenance

- all packaged inputs traced to reviewed, signed sources
- SBOM generated for release candidate
- vulnerability review performed for third-party bundles and runtimes
- Secure Boot and encryption guidance documented
- key custody and signatory process recorded

## Gate 5: Installer and first-boot

- first-boot path validated for clean install and user creation
- disk selection and encryption flow reviewed
- install does not silently wipe data
- recovery USB or live path exists and is documented

## Gate 6: Compatibility and support

- supported workflows are explicitly labeled
- unsupported workflows are explicitly marked as such
- app catalog entries contain clear support status and compatibility notes
- user-facing support model and known issues page exist

## Gate 7: Beta-operational readiness

- release notes are written and versioned
- deprecation and support policy communicated
- issue tracker and escalation path exist
- support team or owner is assigned

## Exit rule

A public beta is allowed only when all critical gates are closed and no unresolved release-blocking item remains without a mitigation owner. If a blocker exists, it must have a documented owner, a workaround or removal path, and a clearly stated risk to the beta cohort.
