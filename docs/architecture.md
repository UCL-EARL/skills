# Agent Capability Architecture

This repository is an agent capability system for Robotics & AI research work, not a loose collection of prompts.

## Repository Surface Model

The repository separates two surfaces with different activation semantics:

| Surface | Activation | Contract |
| --- | --- | --- |
| `skills/` | Selected or invoked when a task matches a trigger. | Defines a workflow, artifact, and completion criteria. |
| `agent-instructions/` | Loaded persistently at user, workspace, or repository scope. | Defines cross-task behavior, constraints, and execution defaults. |

A persistent instruction file is not a `reference` skill. Reference skills are
loaded to support a matching task; instruction contracts govern every task in
their effective scope. For that reason, instruction profiles are indexed in
`agent-instructions/README.md` and never registered in `catalog.json`.

File names such as `AGENTS.md` and `CODEX.md` are deployment targets, not a
portable discovery standard. Each profile must state its client and placement
assumptions. Users must follow the precedence rules of their agent client and
merge project-specific instructions instead of overwriting them blindly.

## Skill System

The design is based on several observed patterns from mature skills projects:

- The official [Anthropic skills repository](https://github.com/anthropics/skills) keeps each skill self-contained with `SKILL.md` plus optional `references/`, `scripts/`, and `assets/`.
- [mattpocock/skills](https://github.com/mattpocock/skills) uses thin router skills and small composable workflow skills rather than one large "do everything" skill.
- [obra/superpowers](https://github.com/obra/superpowers) organizes skills as a methodology with gates, explicit phase transitions, subagent prompts, and verification-before-completion.
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) maps skills to a lifecycle, making the repo easy to navigate by intent rather than file name.
- [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) is useful as a diagram tool-integration reference: diagram generation needs layout planning, shape-library lookup, and visual validation, not just pretty prompts.

## Adopted Organization Patterns

The repository follows these patterns from established skill libraries and agent workflow repos:

| Pattern | Source model | ERL decision |
| --- | --- | --- |
| Standards-shaped skill packages | Agent Skills specification and Anthropic skills | Every skill is a folder with `SKILL.md`; optional `references/`, `scripts/`, and `assets/` are loaded only when needed. |
| Thin routers | mattpocock/skills and Superpowers | `skills/flows/` skills route and gate work; they should not duplicate the detailed workflow of atomic skills. |
| Lifecycle map | addyosmani/agent-skills and Superpowers | Skills are organized around the research lifecycle, not around a flat prompt collection. |
| Validation gates | Agent Skills best practices and Superpowers | Each skill needs a concrete output artifact and completion criteria. |
| Public provenance | Anthropic skills and open-source curation practice | Inspired-by repos are recorded as provenance, but third-party prose is not copied. |

The catalog is the machine-readable registry. Skill bodies remain the agent-facing execution instructions.

## Layer Model

ERL Research Skills use four layers:

| Layer | Role | Examples |
| --- | --- | --- |
| `flow` | User-invoked orchestration across several skills. | `rai-research-flow`, `rai-paper-flow`, `rai-coding-flow` |
| `atomic` | One concrete repeatable task with a checkable output. | `paper-reading-card`, `citation-integrity-auditor` |
| `reference` | Shared rubric or vocabulary used by other skills. | `research-idea-rubric`, `venue-paper-outline` |
| `tool` | Tool-specific workflow or validation protocol. | `scientific-figure-director` |

Flow skills should stay thin. They should decide route, sequence, gates, and artifacts. They should not contain the full detailed rules of every step.

Atomic skills should be useful alone. If a user asks only for a claim-by-claim citation audit, the agent should not need to load the full paper-writing flow.

Reference skills provide shared vocabulary, rubrics, and venue/domain framing. They should not become hidden workflows that produce many artifacts.

Tool skills wrap a specific tool or output medium with validation. A tool skill is not done when the tool has produced an output; it is done when the output has passed the relevant scientific or engineering contract.

## Research Lifecycle

The research lifecycle is:

```text
DISCOVER -> MAP -> IDEATE -> DESIGN -> WRITE -> AUDIT -> PACKAGE
```

| Phase | Skill family | Required artifact |
| --- | --- | --- |
| `DISCOVER` | Search papers, projects, datasets, code, and benchmarks. | Search log with query strings and source tiers. |
| `MAP` | Read papers and build evidence matrices. | Reading cards and comparison matrices. |
| `IDEATE` | Propose and refine project ideas. | Idea cards with novelty, feasibility, baselines, and evaluation plan. |
| `DESIGN` | Turn an idea into experiments and figures. | Experiment plan and figure plan. |
| `WRITE` | Draft venue-aware paper sections. | Section outline or manuscript draft. |
| `AUDIT` | Verify citations, claims, figures, and coherence. | Audit report with blocking and non-blocking issues. |
| `PACKAGE` | Prepare final repo, paper, slides, or review response. | Submission checklist and provenance summary. |

## Naming

- Use lowercase kebab-case.
- Start atomic skill names with the artifact or action: `paper-search-protocol`, `evidence-matrix-builder`.
- Prefix broad routers with `rai-`.
- Avoid venue names in skill names unless a skill is genuinely venue-specific.

## Folder Rules

Use this default shape:

```text
skills/<area>/<skill-name>/
|-- SKILL.md
|-- references/   # optional focused reference docs
|-- scripts/      # optional deterministic helpers
`-- assets/       # optional templates or static resources
```

Keep `SKILL.md` concise and procedural. Put long rubrics, detailed checklists, and tool-specific contracts in `references/`, then link to them from `SKILL.md` with clear load conditions.

Do not add per-skill README files by default. The skill itself is the entry point.

Agent instruction profiles use a separate shape:

```text
agent-instructions/<profile>/
`-- AGENTS.md or CODEX.md
```

The file should be usable as a deployment artifact. Cross-profile selection,
installation, compatibility, and precedence guidance belongs in
`agent-instructions/README.md`, not inside every contract.

## Completion Criteria

Every skill should define what "done" means. Good completion criteria are concrete:

- `paper-reading-card` is done when every required card field is filled or explicitly marked unavailable.
- `citation-integrity-auditor` is done when each claim has a support grade and source status.
- `scientific-figure-director` is done when the prompt or returned figure passes the figure contract.

Avoid criteria like "write a useful summary." They are too easy to satisfy prematurely.

## Public Curation

Do not copy third-party skill prose into this repository unless the license and provenance are explicitly compatible. Prefer original ERL skills that borrow structural ideas, not text.

Each accepted skill should have:

- a narrow trigger in frontmatter;
- a checkable artifact;
- no private paths or credentials;
- citation or provenance rules when external knowledge is involved;
- enough examples or references to prevent vague execution;
- a catalog entry with `type`, `domain`, `maturity`, and `depends_on`.
