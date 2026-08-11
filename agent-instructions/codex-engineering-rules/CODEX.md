# Codex Engineering Rules

LLMs make predictable mistakes when writing code. These rules target the
recurring failures that produce plausible changes which do not fit the
codebase, solve the root cause, or survive real execution.

These are execution rules, not suggestions.

## 1. Read Before You Write

The single biggest source of bad agent-generated code is not reading the
existing codebase before writing new code.

Before writing anything:

- Read the files you are about to modify.
- Look at how similar work is done elsewhere in the project and follow the
  established pattern.
- Check imports and dependencies before introducing another library.
- Read relevant tests to learn the expected behavior.

Code can be locally correct and still be wrong for the codebase. If no local
pattern exists, state that uncertainty and ask about materially different
options instead of guessing.

---

## 2. Think Before You Code

Do not start writing code until the task and success criteria are clear.

- **State assumptions.** Do not silently choose among materially different
  designs such as sessions, JWTs, or OAuth.
- **Name trade-offs.** Explain meaningful cost, complexity, performance, and
  maintenance consequences before committing to a design.
- **Offer limited options.** Present two or three realistic choices with a
  recommendation when the decision belongs to the user.
- **Stop on material ambiguity.** Do not fill missing requirements with
  plausible-looking implementation details.

---

## 3. Simplicity

Write the minimum amount of code that solves the specific problem now.

Avoid:

1. **Premature abstraction.** Do not build a generic service, strategy layer,
   or framework for one concrete use case.
2. **Speculative error handling.** Handle failures that can occur and that the
   code can meaningfully respond to. Check nullable values only when they can
   actually be null.
3. **Unnecessary configurability.** Every option creates another decision and
   validation surface. Hard-code stable values until variation is required.
4. **Dead flexibility.** An interface with one implementation or a generic
   parameter with one real type adds indirection without current value.

For example, if the task only requires one welcome email, prefer the concrete
function:

```python
async def send_welcome_email(user):
    body = f"Welcome {user.name}! Your account is ready."
    await send_email(user.email, subject="Welcome", body=body)
```

Do not introduce an `EmailService`, provider strategy, and template engine
until the project has requirements that need them.

The test for simplicity is whether an unfamiliar maintainer can explain every
abstraction from a current requirement rather than "in case we need it."

---

## 4. Surgical Changes

When editing existing code, keep the diff directly connected to the request.

- **Do not touch unrelated code.** Leave nearby naming, formatting, and cleanup
  alone unless the requested change makes them necessary.
- **Match existing style.** Follow the file's naming, formatting, and design
  patterns even when another style is also reasonable.
- **Clean up after your change.** Remove imports, variables, or functions made
  unused by your edit, but do not turn the task into general cleanup.
- **Do not reformat unrelated lines.** Large formatting diffs hide behavior
  changes and make review harder.

Review the final diff and justify every changed line against the request.

---

## 5. Verification

Distinguish code that works from code that merely looks correct.

- **Reproduce bugs first.** Before fixing a bug, create or identify a check that
  demonstrates the reported failure. Confirm it fails, then confirm the fix.
- **Run relevant existing tests.** If tests were already failing, record that
  baseline instead of attributing every failure to the new change.
- **Test behavior, not ceremony.** Prioritize failure modes, boundaries, and
  externally observable outcomes over trivial implementation assertions.
- **Explain test gaps.** If architecture or environment prevents a meaningful
  test, say exactly why and identify the residual risk.

Verification depth should match the blast radius. A focused change needs a
focused test; shared behavior or cross-module contracts need broader coverage.

---

## 6. Goal-Driven Execution

Define a verifiable success criterion before implementation.

Transform vague requests into observable outcomes:

- "Add validation" becomes "reject missing or invalid email values with a 400
  response and test both cases."
- "Fix the bug" becomes "reproduce the reported behavior, make that check pass,
  and confirm relevant existing tests still pass."
- "Improve performance" becomes "profile, identify the bottleneck, change that
  path, and measure it again."

For multi-step work, state a short plan before editing. The plan should name the
implementation sequence and verification, not narrate obvious mechanics.

---

## 7. Debugging

When something fails, investigate rather than guess.

- **Read the complete error.** Use the message, stack trace, command, and runtime
  context before proposing a cause.
- **Reproduce first.** A fix cannot be verified if the failure cannot be
  observed or otherwise characterized.
- **Change one causal variable at a time.** Multiple simultaneous changes hide
  which one fixed the problem and which introduced new behavior.
- **Find the root cause.** Do not add a guard or retry merely to suppress a
  symptom without understanding why the invalid state occurred.
- **Use available diagnostics.** Inspect relevant logs, process state, resource
  usage, and read-only runtime sessions when the environment permits it.
- **Report uncertainty precisely.** State what was tried, what happened, and
  which hypothesis remains unverified.

---

## 8. Dependencies

Every dependency adds maintenance, security, compatibility, and cognitive cost.

Before adding one, check:

- whether the project already has a library for the job;
- whether the standard library is sufficient;
- whether the dependency is maintained and compatible with the project; and
- whether its size and transitive dependency surface are proportionate.

When a dependency is necessary, name it explicitly and explain why the existing
stack is insufficient. Do not silently add packages to a manifest.

---

## 9. Communication

- **Say what changed and why.** Summarize the engineering decision, not every
  edited line.
- **Flag concrete concerns.** Identify performance, correctness, migration, or
  maintenance risks introduced or left unresolved.
- **Be precise about uncertainty.** Name the exact API, behavior, or environment
  fact that was not verified.
- **Match the user's level.** Do not explain basic concepts the user already
  demonstrates they understand.
- **Write specific commit messages.** Describe the behavior or defect, not only
  that something was changed.

---

## 10. Common Failure Modes

1. **The Kitchen Sink.** One requested feature turns into a broad rewrite.
2. **The Wrong Abstraction.** A generic architecture is built before a second
   real use case exists.
3. **The Invisible Decision.** A consequential architecture or API choice is
   made without surfacing it.
4. **The Optimistic Path.** The implementation handles only successful inputs
   and dependencies.
5. **The Knowledge Hallucination.** A nonexistent or outdated API is used
   without checking local code or primary documentation.
6. **The Style Drift.** New code follows the agent's preferred style rather than
   the project's conventions.
7. **The Runaway Refactor.** A focused fix cascades across unrelated files
   without renewed scope agreement.

If one of these patterns appears during implementation, stop, reduce scope, and
return to the observable outcome.
