# Nexus-OS Alpha 0 Decision Record

## Objective

Validate that the project can produce a real image artifact before committing to a broader distribution strategy. This milestone does not claim that the final operating system is complete or installable. It proves only that the repo can produce a reproducible OCI image and that the project has a practical engineering path.

## Decision

Use an upstream Fedora-based base image for the first build prototype and keep a second candidate in the evaluation set. The prototype intentionally avoids a custom kernel and avoids an end-user desktop claim until the hardware and update matrix is proven on real machines.

## What we validated

- Docker is available and is able to build an OCI image in this workspace.
- A repository-defined build path can create a versioned Nexus-OS image artifact.
- The build process is inspectable and can be extended with signing and update metadata later.
- The architecture is now grounded in a real asset, not just prose.

## What remains open

- Which base distribution is the eventual product default.
- NVIDIA and AMD/Intel driver strategy.
- Secure Boot, rollback, and update verification policy.
- Supported hardware matrix and creator workloads.
- Installation, recovery, and package catalog for end-user use.

## Prototype command

```bash
./scripts/build-alpha0.sh
```

## Evidence requirement for future phases

Each later milestone must include:

- a reproducible build artifact;
- a documented test matrix;
- rollback or recovery evidence;
- a supported hardware list; and
- a signed or verifiable update path.

This is the minimum evidence required before any installer or end-user support promise is made.
