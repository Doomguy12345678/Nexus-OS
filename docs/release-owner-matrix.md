# Nexus-OS Release Owner Matrix

## Purpose

This file maps the major Beta and release responsibilities to named owners so the program has a clear command structure and accountability model.

## Owner assignments

| Area | Owner | Responsibilities |
|---|---|---|
| Product | Product Lead | release scope, communication, user expectations |
| Engineering | Platform Lead | architecture decisions, final platform selection, build health |
| QA | QA Lead | hardware validation, install testing, regression review |
| Security | Security Lead | provenance, signing, SBOM, trust, recovery review |
| Support | Support Lead | support tiers, known issues, user escalation process |
| Release Manager | Release Lead | sign-off gate, launch timing, announcement, risk review |
| Compatibility | Compatibility Lead | Proton/Wine, Waydroid, VM policy, unsupported-workflow labeling |
| Creator Platform | Creator Lead | OBS, Blender, DAW, creator workflow validation |

## Governance requirements

- Every release-blocking item must be associated with an owner.
- Every owner must sign off on the final Beta package before launch.
- The release manager owns the final “go/no-go” decision.

## Sign-off policy

The release manager may approve a Beta only when all owners confirm their areas meet the Beta gate requirements and all open risks are categorized and accepted by the responsible owner.
