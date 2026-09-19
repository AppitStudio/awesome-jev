# Adapt or build a starter

Use this after the user asks to implement a solution. Preserve their stack and place work in their application or an agreed new directory. The public Awesome Jev checkout is a source of patterns; it is not the destination for their private workflow or data.

## Define the smallest complete slice

Write a brief in plain language: trigger, sample input, desired output, the judgment Jev supplies, the deterministic steps code owns, and the uncertain/error outcome. Identify which parts come from a verified resource and which are new work. Keep existing user requirements; ask only about choices that change the implementation.

For example, a workflow might accept a message, select a support department, evaluate a separately defined urgency condition, and write a suggestion or review record. Connecting to a ticketing service is another integration with its own permissions; do not silently treat a classification as authorization to change a ticket.

Read the current [building guide](https://docs.typesafe.ai/concepts/how-to-build-with-system-one), the relevant [primitive](https://docs.typesafe.ai/primitives), [state guide](https://docs.typesafe.ai/concepts/state), and selected SDK/API reference. Use the official TypeSafe skill when available. Inspect the closest cookbook before inventing a broad prompt.

## Keep the design inspectable

- Put versioned questions, candidate definitions, rubrics, and policy settings where a developer can review them. Question IDs identify answers for code; they are not instructions to the model.
- Supply enough relevant state, with named fields for multiple facts or documents. Current facts must be supplied or retrieved by the application; Jev does not browse for them.
- Ask narrow, complete questions. Batch independent judgments over shared state; use another request when a later question truly needs an earlier answer. Do not build hidden dependencies between sibling questions.
- Include a no-match outcome where necessary. Multi-label judgments need separate conditions. For extraction, compute candidate spans in code, check coverage, and copy/normalize the selected source value exactly.
- Keep exact math, parsing, validation, permissions, and execution in code. Use concrete standalone Score levels and normalize compatible scales before combining them.
- Validate response IDs, types, and legal values before policy. Keep probabilities and confidence available for inspection; confidence is not accuracy. Noul has no extra confidence field and its midpoint is uncertainty.
- Define appropriate review, fallback, and service-error behavior. Thresholds are tunable policy, not universal recommendations. Do not force review onto a harmless preference where alternatives are equally acceptable.
- Bound timeouts, retries, and batch size. Avoid retrying ambiguous downstream actions. Keep keys server-side and redact credentials from failures and logs. User text is untrusted data; model screening is not an authorization or prompt-injection boundary.

## Deliver a usable starter, not just a snippet

Adapt these components to the existing project rather than imposing fixed filenames or a new framework:

| Component | Minimum useful behavior |
| --- | --- |
| Instructions | Problem, prerequisites, one runnable command, expected result, and what to customize. |
| Configuration | Deliberate model version, readable questions/policy, and blank/example secret configuration with a real loading path. |
| Offline path | Small synthetic input and clearly authored responses; default execution performs no paid calls or external actions. |
| Live path | Explicit opt-in, private key setup, inspected data scope, and documented attempt/request bounds. |
| Application logic | Input preparation, typed response validation, deterministic policy, and inspectable output or review record. |
| Checks | Meaningful ordinary, ambiguous, no-match/missing-data, malformed-response, and service-failure cases. |
| Handoff | Exact commands, actual verification, known limitations, and primary links relevant to the task. |

Prefer the official SDK for a new application in a supported language. Borrow the examples' policy structure without presenting the repository's small teaching HTTP client as a full SDK. When extracting a repo example, include its shared dependencies and relevant license; copying its tiny input directory alone is insufficient.

## Evaluate the user's task

Mock tests establish code behavior. Once live evaluation is authorized, use suitable representative data with labels written before inspecting model answers. Include realistic language variation, ambiguity, missing evidence, and costly failure cases. Keep development and holdout separate; choose thresholds on development data and evaluate the fixed policy on holdout.

Measure wrong automatic decisions together with automatic coverage and review rate. Count service/validation failures separately and do not drop them from workload denominators. Preserve requested/returned model IDs, questions/configuration versions, actual usage, and the limits of the evidence. Keep raw datasets and captures out of the public repo and out of public logs.

The repository's [evaluation runner](https://github.com/AppitStudio/awesome-jev/blob/main/evaluations/README.md) evaluates its Support Router. Reuse its protocol for another task, but implement the appropriate schema, request builder, labels, and metrics instead of claiming it already supports arbitrary workflows. Re-evaluate after meaningful changes to questions, candidates, policy, model, or workload.

Finish with a working offline slice even if account setup blocks live testing. State whether a live request was actually run and whether any representative task evaluation exists; do not label the new starter production-ready from a smoke check.
