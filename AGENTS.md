# Agent Instructions

This repository stores reusable agent skills and agent instruction contracts.

- Read `README.md`, `CONTRIBUTING.md`, and `catalog.json` before changing repository structure.
- Keep skill changes focused. Do not rewrite unrelated skills in the same pull request.
- Add or update the matching `catalog.json` entry when adding a skill under `skills/`.
- Keep files under `agent-instructions/` out of `catalog.json`; update their local index instead.
- Run `python scripts/validate_catalog.py` before claiming the repository is valid.
- Run `python scripts/validate_repository.py` after changing branding, governance, documentation links, or repository metadata.
- Do not include private credentials, local-only absolute paths, or unverifiable claims.
- Prefer primary documentation links for tools, APIs, papers, and datasets.
