#!/usr/bin/env python3
"""Simple weighted comparison for candidate Linux bases."""

from __future__ import annotations

candidates = {
    "Fedora Atomic KDE": {
        "Update and rollback": 4.5,
        "Driver support": 4.0,
        "Creator workflow fit": 4.2,
        "Gaming optimization": 3.8,
        "Maintainability": 4.7,
        "Security and provenance": 4.6,
        "Ecosystem compatibility": 4.4,
    },
    "Bazzite": {
        "Update and rollback": 4.0,
        "Driver support": 4.4,
        "Creator workflow fit": 4.3,
        "Gaming optimization": 4.7,
        "Maintainability": 3.5,
        "Security and provenance": 4.1,
        "Ecosystem compatibility": 4.0,
    },
}

weights = {
    "Update and rollback": 20,
    "Driver support": 20,
    "Creator workflow fit": 15,
    "Gaming optimization": 15,
    "Maintainability": 15,
    "Security and provenance": 10,
    "Ecosystem compatibility": 5,
}

print("Nexus-OS base comparison")
print("=" * 48)
for name, criteria in candidates.items():
    total = 0.0
    for criterion, score in criteria.items():
        total += score * weights[criterion]
    total /= sum(weights.values())
    print(f"{name}: {total:.2f}/5.00")

print("\nRecommended baseline: Fedora Atomic KDE")
print("Reason: better maintainability, more stable release posture, and lower long-term support burden for a production desktop project.")
