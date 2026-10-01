#!/usr/bin/env bash
set -Eeuo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
image_tag="${1:-localhost/nexus-os:kinoite-candidate}"
platform="${NEXUS_PLATFORM:-linux/amd64}"

docker build \
  --pull \
  --platform "$platform" \
  --file "$repo_root/os/Containerfile.kinoite" \
  --tag "$image_tag" \
  "$repo_root/os"

printf 'Built %s for %s\n' "$image_tag" "$platform"