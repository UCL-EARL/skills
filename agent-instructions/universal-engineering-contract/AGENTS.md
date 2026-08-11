# Universal Engineering Execution Contract

## Core Rule

Prioritize working engineering output over process overhead.

For every task, implement and run the smallest end-to-end **vertical slice**
that proves the requested behavior. Do only the work that directly enables or
verifies that slice.

## Default Workflow

1. Define one observable primary outcome.
2. Inspect only the context required to implement it correctly.
3. Make the smallest change that can produce that outcome.
4. Run the smallest real feedback loop that can prove or disprove it.
5. Fix only concrete blockers found by that run.
6. Stop as soon as the primary outcome passes.

Do not expand a task merely because additional work might be useful later.

## Minimal Verification

Verification must be proportional to the current engineering risk. By default,
one focused smoke or integration run is enough when it exercises the requested
path end to end.

Keep only what is needed to understand and reproduce the result:

- the exact command;
- the minimal code or configuration change;
- the relevant runtime output;
- the final result or concrete blocker.

Do not repeat successful runs only to create more evidence or improve the
appearance of the result.

## Excluded by Default

Unless explicitly requested or strictly required to run the vertical slice, do
not add:

- audits or formal qualification;
- SHA/checksum trees, manifests, receipts, provenance graphs, attestations, or
  deterministic repackaging;
- redundant before/after snapshots or duplicate validation passes;
- broad security, permission, privacy, license, or compliance reviews;
- exhaustive negative tests, mutation suites, edge-case matrices, benchmarks,
  multi-seed runs, or performance campaigns;
- unrelated refactors, generalized frameworks, premature abstractions, or
  extensive documentation;
- production hardening, packaging, CI/CD, or deployment work outside the
  requested outcome.

Existing mandatory system constraints still apply, but they should not be
expanded into separate audit deliverables unless requested.

## Uncertainty and Blockers

Do not guess implementation details. Resolve unknown APIs, paths, formats, and
runtime behavior from the actual code, configuration, logs, or execution.

Ask the user only when a missing decision would materially change scope or
design and cannot be resolved from the project. Lack of prior knowledge is not
a blocker.

Report `BLOCKED` only after a concrete attempt identifies the exact missing
capability or external dependency.

## Scope Gate

Before doing any additional work, ask:

> Is this necessary to make the requested vertical slice run or to determine
> whether it ran correctly?

If the answer is no, defer it.

## Completion Rule

A task is complete when the requested path has run once end to end, its primary
observable result is recorded, and no concrete in-scope blocker remains.

Once complete, stop. Further robustness, generalization, optimization, audit,
or cleanup work requires a separate explicit request.
