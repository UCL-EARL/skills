# Research Notes

These notes summarize the external repository scan used to organize ERL Research Skills. The goal is to borrow structure and workflow patterns, not third-party prose.

## Primary Sources Reviewed

### Skill Repository Sources

| Source | Organization pattern | What ERL adopts |
| --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | A skill is a directory with `SKILL.md`; optional `scripts/`, `references/`, and `assets/`; progressive disclosure keeps the main skill small. | Keep every skill self-contained and put detailed contracts in optional resource directories. |
| [Agent Skills best practices](https://agentskills.io/best-practices) | Skills should be grounded in real tasks, scoped as coherent units, include output templates, and validate their work. | Require concrete artifacts, completion criteria, and validation loops before maturity promotion. |
| [anthropics/skills](https://github.com/anthropics/skills) | Demonstrates official-style skill folders, a spec/template split, and self-contained examples across domains. | Keep `templates/`, `docs/`, and `skills/` separate; make the repo useful as both catalog and authoring reference. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Distinguishes user-invoked routers from model-invoked reusable discipline; emphasizes small composable engineering skills. | Keep `rai-*` flows thin and route to focused skills instead of creating mega-skills. |
| [obra/superpowers](https://github.com/obra/superpowers) | Treats skills as a methodology with phase gates, planning, verification, and review workflows. | Use phase gates for research work: do not ideate, write, or polish past missing evidence. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Maps skills to a lifecycle and command entry points, then lists all skills by phase and purpose. | Organize ERL skills around the research lifecycle: `DISCOVER -> MAP -> IDEATE -> DESIGN -> WRITE -> AUDIT -> PACKAGE`. |
| [DayuanJiang/next-ai-draw-io](https://github.com/DayuanJiang/next-ai-draw-io) | Shows that diagram generation needs layout planning, shape semantics, and visual validation. | Treat figure generation as a tool skill with a scientific figure contract, not as image prompting alone. |

### Paper Production Sources

| Source | Organization pattern | What ERL adopts |
| --- | --- | --- |
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) | Uses explicit questions for assumptions, limitations, experiments, reproducibility, and broader impacts. | Add gates for claim-evidence support, limitations, experiment reporting, and overclaim control. |
| [NeurIPS Code and Data Submission Policy](https://neurips.cc/public/guides/CodeSubmissionPolicy) | Treats code, data, environments, scripts, and instructions as part of reproducible paper artifacts. | Add `experiment-provenance-auditor` and provenance checks for configs, seeds, logs, code versions, and generated figures. |
| [Papers with Code releasing research code](https://github.com/paperswithcode/releasing-research-code) | Uses a code completeness checklist for dependencies, training, evaluation, pretrained models, and data processing. | Add source-backed checks for result traceability and runnable experiment packages. |
| [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) | Separates artifact availability, functionality, reusability, and result reproduction/replication. | Keep artifact claims separate from benchmark claims and avoid overpromising reproducibility. |
| [arXiv TeX submission help](https://info.arxiv.org/help/submit_tex.html) | Documents source-package expectations and common TeX upload failure modes. | Add `latex-submission-checker` checks for source packaging, missing files, build logs, and arXiv readiness. |
| [ACL Rolling Review author guidance](https://aclrollingreview.org/authors) | Separates review, author response, recommendation, and revision stages. | Add `reviewer-response-builder` with issue ledgers, response actions, and feasible revision promises. |
| [ACL Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/) | Encourages explicit attention to data, intended use, risks, and ethical considerations. | Add limitations and responsible research checks when deployment, humans, or safety are in scope. |
| [Model Cards](https://arxiv.org/abs/1810.03993) and [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Document intended use, evaluation context, data composition, performance characteristics, and limitations. | Add model/data documentation patterns to limitation and failure-case audits. |
| [FAIR Principles](https://www.go-fair.org/fair-principles/) and [The Turing Way](https://the-turing-way.netlify.app/) | Emphasize findable, reusable, documented research artifacts and reproducible project organization. | Add `knowledge-base-onboarding` with source inventories, trust labels, concept maps, and artifact maps. |
| [UNC Writing Center introductions](https://writingcenter.unc.edu/tips-and-tools/introductions/) and [literature reviews](https://writingcenter.unc.edu/tips-and-tools/literature-reviews/) | Emphasize focused openings, synthesis, patterns, debates, and gaps. | Add `abstract-introduction-builder` and `related-work-positioning` patterns that synthesize sources instead of listing them. |

## Findings

1. **Discovery needs entry points.** Users should not scan a flat list of skills first. They need routers, lifecycle phases, and examples of which skill starts a workflow.
2. **Routers should stay thin.** A router selects subskills, preserves context hygiene, and enforces phase gates. It should not contain every detailed rule.
3. **Skill value comes from artifacts.** Strong skills produce search logs, reading cards, matrices, audits, outlines, figure specs, or testable code outcomes.
4. **Progressive disclosure is the default.** Put only the essential procedure in `SKILL.md`; put long rubrics and contracts in `references/`; add `scripts/` only after repeated deterministic work appears.
5. **Public skills need provenance discipline.** Record inspiration and links, but avoid copying content from external repos.
6. **Research skills need stronger evidence gates than general coding skills.** The recurring Robotics & AI failure modes are hallucinated citations, weak baselines, invalid evaluation, unclear sim-to-real claims, and diagrams that imply false mechanisms.
7. **Paper production needs late-stage gates.** A strong paper workflow must cover benchmark fairness, result provenance, response-to-reviewers, limitations, and submission packaging, not only writing polish.

## ERL Design Decision

Use four skill types:

- `flow`: orchestration, routing, and gates;
- `atomic`: one concrete repeatable task;
- `reference`: rubric, venue/domain vocabulary, or reusable standard;
- `tool`: tool-specific workflow plus output validation.

The first release optimizes for reviewability. All initial skills remain `draft` until they are forward-tested on realistic research or coding tasks.
