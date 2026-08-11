# Curation Policy

This repository accepts skills and agent instruction contracts that help Robotics & AI researchers do concrete work more reliably.

## Accept

- Reusable workflows for literature search, paper reading, evidence synthesis, ideation, writing, reviewing, figures, experiments, code, and reproducibility.
- Skills with narrow triggers and clear completion criteria.
- Skills that explicitly handle citation, provenance, or evidence when scientific claims are involved.
- Tool workflows that include validation, not just usage instructions.
- Persistent instruction contracts that address a distinct recurring agent behavior and document their scope and precedence.

## Reject

- Prompt dumps without workflow or completion criteria.
- Skills that encourage fabricated citations, unsupported claims, or unverifiable benchmark statements.
- Private paths, credentials, lab-only assumptions, or undocumented external services.
- Large third-party content copied without license/provenance review.
- Mega-skills that should be split into a router plus atomic skills.
- Instruction files that are only personality prompts, duplicate an existing profile, or depend on private machine permissions.

## Instruction Contracts

Instruction contracts are curated separately from skills. They do not use
skill frontmatter, maturity labels, forward-test fixtures, or `catalog.json`.
Each accepted profile must include:

- a distinct behavioral objective;
- an intended usage mode and client-placement assumption;
- explicit interaction with project-specific and higher-precedence rules;
- no credentials, private paths, or hidden environment access; and
- redistribution rights compatible with the repository license.

Profiles with conflicting defaults should be presented as alternatives unless
a deterministic precedence rule makes composition safe.

## Maturity

- `draft`: usable scaffold, not yet forward-tested.
- `beta`: used on at least one realistic task and revised.
- `stable`: used repeatedly across projects with no major scope changes.

## Examples and Forward Tests

Core skills should include either a realistic example in `examples/` or a forward-test fixture in `forward-tests/` before promotion beyond `draft`.

Examples show artifact shape. Forward tests check whether a fresh agent can use the skill without leaked context. Neither should include fabricated citations, unverifiable metrics, private paths, or credentials.

## Provenance

When a skill is inspired by another repo or method, record it in `catalog.json` under `source_inspiration`. This is not a license grant; it is a provenance note. Do not copy source text unless the license permits it and attribution is included.
