# Alpha 0 Image Spike

This builds a minimal Fedora bootc OCI image to verify that Nexus-OS can produce a bootc-derived artifact in CI. It is not a desktop, installer, live ISO, or supported operating system image.

## Requirements

- Docker Engine with access to the image registry
- x86-64 host for the default `linux/amd64` build

## Build and inspect

From the repository root:

```sh
bash os/build.sh
docker image inspect localhost/nexus-os:alpha0
docker run --rm --entrypoint bootc localhost/nexus-os:alpha0 --version
```

The base is pinned to Fedora bootc 44's multi-architecture manifest digest. Set `NEXUS_PLATFORM=linux/arm64` to build another OCI architecture from that same pinned manifest if the upstream image supports it. This does not establish Nexus-OS hardware support.

The Alpha 0 CI workflow builds the image and checks that its bootc entry point and metadata are present. This is a build smoke test, not a boot test, desktop image, installer, or update/rollback test. Before distribution, automate reviewed base-digest updates, record build provenance/SBOM, and sign outputs. Never install this Alpha 0 image on a physical machine.
${/^$/d;}
