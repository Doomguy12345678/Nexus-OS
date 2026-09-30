# Platform Comparison Matrix

This matrix is the engineering basis for the Alpha 1 decision. It compares the strongest candidates for the base image and helps maintain the product-level discipline of making a distribution choice from evidence rather than marketing.

## Candidate summary

| Candidate | Strengths | Risks | Strategic fit |
|---|---|---|---|
| Fedora Atomic KDE (Kinoite) | Upstream-first, stable, maintainable, strong Fedora ecosystem, transparent update model | Requires more customization for gaming-first defaults, fewer “out-of-the-box” tuning choices | Best default choice for a professional and maintainable platform |
| Bazzite | Strong gaming/device defaults, tuned for a creator/gaming workflow, aggressive convenience | More opinionated, higher support complexity, platform-specific assumptions, more maintenance/upgrade friction | Best candidate if the project wants a gaming-heavy base with less initial tuning work |

## Weighted scorecard

Scores are out of 5 and weighted by the Alpha 1 model.

| Criterion | Weight | Fedora Atomic KDE | Bazzite |
|---|---:|---:|---:|
| Update and rollback | 20 | 4.5 | 4.0 |
| Driver support | 20 | 4.0 | 4.4 |
| Creator workflow fit | 15 | 4.2 | 4.3 |
| Gaming optimization | 15 | 3.8 | 4.7 |
| Maintainability | 15 | 4.7 | 3.5 |
| Security and provenance | 10 | 4.6 | 4.1 |
| Ecosystem compatibility | 5 | 4.4 | 4.0 |

### Weighted totals

- Fedora Atomic KDE: 4.3 / 5
- Bazzite: 4.1 / 5

## Interpretation

The weighted total favors Fedora Atomic KDE because the base must be maintainable, auditable, and compatible with a long-term product roadmap. Bazzite is very strong in gaming-first defaults and may be the correct choice if the product settles on a gaming-heavy distribution identity, but its maintenance burden is higher and its defaults are more opinionated.

## Recommendation

This repository should proceed with Fedora Atomic KDE as the default evaluation base for the next milestone, while preserving Bazzite as a fallback experiment and a product comparison target. The project should not commit to Bazzite for a public release until its support burden, update safety, and creator workflow evidence are fully captured.

## Required test checklist

Collect the following on both candidates before finalizing the decision:

- boot time and first-boot behavior
- system update and rollback recovery
- suspend and resume success
- NVIDIA/AMD/Intel GPU enumeration and driver selection
- audio interface detection and sample-rate routing
- Bluetooth and controller detection
- Steam and Proton launch verification
- OBS capture and screen-sharing verification
- Blender/creator app startup
- DAW or audio workstation startup
- Flatpak installation and permission review
- application uninstall and recovery behavior

## Decision rule

The final base choice should prefer the candidate with the best measured supportability and the fewest unresolved release-blocking risks. A more “exciting” default is not a win if it cannot be supported, documented, and recovered under real world conditions.
