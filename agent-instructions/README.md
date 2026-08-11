# Agent Instruction Contracts

Agent instruction contracts are persistent behavioral rules for coding agents.
They are not skills and are not registered in `catalog.json`.

## Skills vs. Instruction Contracts

| | Skills | Instruction contracts |
| --- | --- | --- |
| Primary question | What workflow should the agent run? | How should the agent behave throughout the work? |
| Activation | Invoked or routed when a task matches. | Loaded as persistent project or user instructions. |
| Scope | A concrete task and checkable artifact. | Cross-task engineering discipline and constraints. |
| Location | `skills/<area>/<skill-name>/SKILL.md` | `agent-instructions/<profile>/<target>.md` |
| Registry | `catalog.json` | This index |

## Available Profiles

| Profile | Best for | Distinctive behavior | File |
| --- | --- | --- | --- |
| Universal Engineering Execution Contract | Fast, bounded implementation work. | Proves one vertical slice, keeps verification proportional, and stops when the requested outcome works. | [`AGENTS.md`](./universal-engineering-contract/AGENTS.md) |
| Codex Engineering Rules | Debugging, refactoring, and higher-risk code changes. | Reads before writing, surfaces assumptions, preserves local style, finds root causes, and verifies behavior. | [`CODEX.md`](./codex-engineering-rules/CODEX.md) |
| Universal Survey Writing and Audit Guide | Long-running academic survey drafting, revision, and final audit. | Protects the manuscript source of truth, narrative backbone, claim-evidence alignment, global consistency, and publication hygiene. | [`CODEX.md`](./survey-writing-audit/CODEX.md) |

The two engineering profiles express different verification defaults. Choose
one as a base instead of stacking both without resolving conflicts. The survey
guide is domain-specific and can be paired with one engineering base when the
client supports multiple instruction scopes.

## Install or Adapt

Instruction discovery and precedence depend on the agent client. Use the file
name and location documented by that client.

For a client that discovers repository-level `AGENTS.md` files:

```bash
cp agent-instructions/universal-engineering-contract/AGENTS.md /path/to/project/AGENTS.md
```

For a client or wrapper configured to load `CODEX.md`:

```bash
cp agent-instructions/codex-engineering-rules/CODEX.md /path/to/project/CODEX.md
```

For a survey-writing workspace, use the domain profile at the client-supported
project or directory scope:

```bash
cp agent-instructions/survey-writing-audit/CODEX.md /path/to/survey/CODEX.md
```

Do not overwrite an existing instruction file blindly. Compare the files,
retain project-specific build and test commands, and resolve contradictory
rules explicitly. System, platform, security, and user instructions take
precedence over these reusable templates.

## Selection Guide

Use the Universal Engineering Execution Contract when excessive process,
duplicate validation, or speculative scope is the main productivity problem.

Use the Codex Engineering Rules when the main risks are shallow codebase
reading, guessed fixes, style drift, broad refactors, or weak testing.

Add the Universal Survey Writing and Audit Guide when the work spans survey
drafting, revision, claim-evidence control, redundancy removal, and final
submission audit. It complements rather than replaces the executable
`survey-synthesis-builder` skill.

Project-specific instructions should remain short and concrete: name the real
commands, protected paths, architecture boundaries, and acceptance checks that
cannot be inferred from the repository.

## Contribution Contract

A new instruction profile must:

- solve a distinct and recurring agent-behavior problem;
- state its intended client, scope, and precedence assumptions;
- avoid credentials, private paths, and machine-specific permissions;
- avoid silently conflicting with existing profiles;
- use testable rules where possible rather than personality prose; and
- have redistribution rights compatible with this repository's license.
