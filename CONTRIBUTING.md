# Contributing

Thanks for helping improve ERL Research Skills.

This repository is meant to stay practical, easy to review, and safe to reuse across research and engineering projects. Please keep contributions focused and executable.

Open-ended usage questions and workflow ideas belong in [GitHub Discussions](https://github.com/UCL-ERL/skills/discussions). Use issues for concrete bugs, proposals, and documentation problems. By participating, you agree to the [Code of Conduct](./CODE_OF_CONDUCT.md) and project [Governance](./GOVERNANCE.md).

## What Makes a Good Skill

A strong skill has:

- A clear trigger: when should an agent use it?
- A concrete workflow: what steps should it follow?
- Explicit constraints: what should it avoid?
- Validation guidance: how can a user know the work is correct?
- Minimal assumptions: no hidden credentials, local-only paths, or undocumented dependencies.

## Add a Skill

1. Create a directory under `skills/<area>/<skill-name>/`.
2. Copy `templates/SKILL.md` into that directory.
3. Fill in the frontmatter and instructions.
4. Add an entry to `catalog.json`.
5. Run:

```bash
python scripts/validate_catalog.py
python scripts/validate_forward_tests.py
```

6. Open a pull request and explain:

- What problem the skill solves.
- Who should use it.
- Any external tools, papers, APIs, or datasets it relies on.
- How you tested or sanity-checked the workflow.

Accepted contributions are attributed according to the work performed. A contribution does not imply ERL Lab membership or maintainer status.

## Choose the Right Layer

Before adding a skill, decide which layer it belongs to:

| Layer | Add one when | Avoid when |
| --- | --- | --- |
| `flow` | The user needs routing across several skills and phase gates. | The detailed workflow fits inside one atomic skill. |
| `atomic` | One repeatable task produces one checkable artifact. | The skill is mostly a shared rubric or vocabulary. |
| `reference` | Multiple skills need the same rubric, venue framing, or terminology. | It secretly performs a multi-step workflow. |
| `tool` | A tool or output medium needs a protocol and validation contract. | It only describes a tool without checking the output. |

Prefer adding detail to an existing skill when the boundary already fits. Add a new skill only when it has a distinct trigger, artifact, and completion condition.

## Catalog Entry Format

Each skill entry in `catalog.json` should look like this:

```json
{
  "id": "example-skill",
  "name": "Example Skill",
  "description": "A short description of the concrete task this skill handles.",
  "path": "skills/research/example-skill",
  "type": "atomic",
  "domain": "research",
  "maturity": "draft",
  "depends_on": [],
  "tags": ["research", "workflow"]
}
```

Allowed `type` values are `flow`, `atomic`, `reference`, and `tool`.

Allowed `maturity` values are `draft`, `beta`, and `stable`.

## Review Checklist

Before requesting review, check that:

- `python scripts/validate_catalog.py` passes.
- `python scripts/validate_forward_tests.py` passes when forward tests are present.
- The skill has a narrow, understandable scope.
- The `catalog.json` entry matches the `SKILL.md` frontmatter.
- The instructions do not require private credentials.
- Claims about tools, libraries, APIs, or research papers are accurate.
- Examples are small enough to inspect.
- The contribution does not include copyrighted text that cannot be redistributed.
- The contribution does not include credentials, restricted data, confidential research material, or personal information.
- New external sources are recorded as provenance and are compatible with the repository license.

## Style

- Use plain technical English in repository files.
- Prefer exact commands over vague guidance.
- Keep examples short and runnable.
- Use links to primary documentation where possible.
- Avoid adding dependencies unless they are necessary.

## Review and Decisions

ERL Lab maintainers review contributions for scope, correctness, evidence discipline, compatibility, and maintainability. Repository-wide architecture, governance, license, and compatibility changes should be discussed before implementation. See [GOVERNANCE.md](./GOVERNANCE.md) for decision responsibilities.
