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

Set `NEXUS_PLATFORM=linux/arm64` to test another OCI architecture if the upstream base supports it. This does not establish Nexus-OS hardware support.

The Fedora 43 tag is a discovery-stage input, not a release pin. Before CI or distribution, pin the upstream image by digest, automate reviewed updates to that pin, record build provenance/SBOM, and sign outputs. Do not install this image on a physical machine.