# Nexus-OS Beta Release Policy

## Scope

This policy defines the minimum standards for any beta-channel release of Nexus-OS. The objective is to deliver a useful, recoverable, and supportable preview to a limited audience without overstating compatibility or claiming the product is production-ready.

## Release boundaries

- Beta is a preview for a defined, limited audience.
- Beta is not equivalent to stable support commitments.
- Beta release notes must include supported hardware, known limitations, and a recovery path.

## Requirements for admission

- selected base platform validated against at least the minimum hardware matrix
- update and rollback path proven on a clean install
- no unresolved critical security issue without mitigation
- no unresolved installer or recovery issue without an alternative recovery plan
- user-facing support documentation published

## Support policy

| Category | Definition |
|---|---|
| Supported | tested and documented on the fixed matrix |
| Supported with notes | tested, but with a known limitation or workaround |
| Experimental | early access or limited validation |
| Unsupported | not tested and not approved for public use |

## Security baseline

- signed artifact policy required for all release images
- provenance and SBOM required before beta publication
- no unreviewed third-party script execution in the installer path
- privacy standards published, including diagnostics opt-in behavior

## Quality gates

- install succeeds on at least the target supported systems
- suspend and resume work on supported laptops
- GPU and audio detection pass on the supported matrix
- OBS or creator capture works on at least one supported creator profile
- Steam and Proton launch is validated at minimum on one representative system
- rollback path is tested and repeatable

## Human factors

- release notes must be understandable by non-experts
- GUI states must clearly explain unsupported or experimental features
- recovery and data backup instructions must be visible before install begins

## Release decision

A beta can be published only after the release owner, engineering owner, support owner, and security reviewer sign off that the gate checklist is complete. This is a governance checkpoint, not a symbolic approval.
