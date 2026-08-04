# Governance

ERL Research Skills is an open-source project developed and maintained by ERL Lab.

## Stewardship

ERL Lab is responsible for the repository roadmap, scope, quality standards, releases, and maintainer appointments. Public use and contribution are open, but contribution does not by itself grant ERL Lab membership, maintainer status, or decision authority.

## Roles

### Maintainers

Maintainers are appointed by ERL Lab. They:

- review and merge contributions;
- enforce repository scope, evidence standards, and release criteria;
- maintain the catalog, validation tooling, and public documentation;
- moderate project spaces; and
- make routine project decisions.

Repository paths and current review responsibility are recorded in [`.github/CODEOWNERS`](./.github/CODEOWNERS).

### Contributors

Anyone may open an issue, join a discussion, or submit a pull request. Accepted work is attributed according to the actual contribution. Contributors do not need to be members of ERL Lab.

## Decisions

Routine fixes and focused skill changes are decided through pull-request review. Changes that materially affect architecture, governance, licensing, compatibility, or repository-wide policy should begin as a GitHub Discussion or design issue before implementation.

Maintainers should state the reason when rejecting or requesting major changes to a contribution. ERL Lab retains final responsibility for scope and releases.

## Releases and Maturity

Skill maturity is evidence-based:

- `draft`: usable scaffold that has not yet demonstrated broad reliability;
- `beta`: exercised on at least one realistic task and revised from evidence;
- `stable`: repeatedly used across projects or user contexts without major scope changes.

Validation passing is necessary but not sufficient for maturity promotion. See [`docs/quality-rubric.md`](./docs/quality-rubric.md).

## Public Development

Skills and reusable research workflows are developed publicly by default. Credentials, restricted data, confidential collaboration materials, personal data, and research artifacts that are not authorized for release must not be committed.

## Changes to Governance

Governance changes require maintainer review and explicit approval from ERL Lab. Proposed changes should explain the problem, affected roles, compatibility impact, and transition plan.
