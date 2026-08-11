## Summary

Describe what this pull request adds or changes.

## Applicable Checklist

For a skill change:

- [ ] The skill has a narrow, concrete trigger.
- [ ] The workflow is executable and avoids hidden assumptions.
- [ ] The catalog entry is present and valid.
- [ ] `python scripts/validate_catalog.py` passes.

For an agent instruction contract:

- [ ] The contract addresses a distinct recurring behavior.
- [ ] Its client, scope, placement, and precedence assumptions are documented.
- [ ] It is indexed in `agent-instructions/README.md` and excluded from `catalog.json`.
- [ ] Conflicts with existing profiles are resolved or documented.

For every change:

- [ ] External facts, APIs, papers, or tools are linked to primary sources where relevant.
- [ ] No credentials, restricted data, confidential material, personal information, or local-only absolute paths are included.
- [ ] Compatibility and migration impact are documented when IDs, paths, dependencies, or output contracts change.
- [ ] `python scripts/validate_repository.py` passes.

## Validation

Paste the command output or describe the manual check.

## Evidence

Link or describe the forward test, realistic use case, or review evidence relevant to this change. Write `not applicable` for documentation-only changes.
