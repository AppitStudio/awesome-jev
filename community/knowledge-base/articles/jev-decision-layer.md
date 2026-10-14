# Jev agent decision layer: from judgment to permission

A Jev agent decision layer evaluates bounded questions about an agent's current state. An LLM still plans and generates; application code owns permissions, execution and observable completion. The useful design question is how a judgment reaches an action without taking over those responsibilities.

This guide draws on [Sumanth](https://x.com/Sumanth_077) and his [“Jev Clearly Explained”](https://x.com/sumanth_077/article/2101639788961112279), published on 20 September 2026. It focuses on responsibility boundaries. For task selection, see [Jev versus LLMs](jev-vs-llms.md); for implementation, see [agent-loop patterns](jev-agent-loops.md) and [a first Python request](jev-python-first-request.md).

## Key takeaways

- **Separate the proposal, judgment and permission.** Each needs different evidence and has a different owner.
- **Define the event being judged.** Risk, approval requirement and task completion are separate questions.
- **Keep exact checks in code.** A model cannot establish filesystem scope, authorization or remaining spend by expressing confidence.
- **Expose unresolved work.** Missing context, service failures and an exhausted retry budget need an explicit status.
- **Read wrapper policy carefully.** An aggregate confidence gate or shadow flag can behave differently from its name.

## Map the handoff before adding a model

Sumanth describes a three-part architecture: generation, bounded decisions and runtime enforcement. He discusses routing, tool safety, progress and evaluation, but provides no reproducible agent or measured trace. The following responsibility map is our editorial application of that architecture:

| Handoff | Information to preserve | Owner and observable check |
| --- | --- | --- |
| Generate a proposed action | User goal, operation, arguments and expected result | LLM proposes; code parses the exact operation. |
| Prepare decision state | Relevant evidence, current target and defined criteria | Application selects authorized input; missing context stays visible. |
| Judge meaning | Named alternatives, ordered rubric or a specific true/false condition | Jev returns a typed answer; application checks answer coverage. |
| Decide whether to act | Required judgments plus exact permissions, scope, budget and approval | Deterministic runtime checks every required rule before a side effect. |
| Observe the result | Exit status, changed artifact, tests or external acknowledgment | Code and independent review check acceptance evidence. |
| Continue or hand off | Remaining work, progress history and retry budget | Runtime records completed, incomplete or review-required status. |

For the source's example of deleting a build directory, semantic risk depends on context. Code must still resolve the actual path and enforce the allowed operation. A low risk estimate cannot override an approval requirement. Repeated searching may indicate a stall, but a fixed turn limit merely bounds execution; it does not establish success.

## Give each judgment a clear meaning

TypeSafe's [primitive reference](https://docs.typesafe.ai/primitives) distinguishes **Choice** for named alternatives, **Score** for ordered levels, and **Noul** for a true-condition probability. A Score can fall between rubric levels. Noul exposes `noul`, without a separate `confidence` field; Choice and Score include one.

A question about whether an action is risky differs from whether policy requires approval. Define the condition and direction before comparing values. Sumanth's `0.70` and `0.95` risk bands are illustrative, not validated operating thresholds. Keep exact boundaries explicit and choose them from representative labeled cases with separate validation cases.

TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) describes distribution-based statistics. Do not substitute a selected option's probability, a wrapper's average, and a probability of correctness for one another. Evaluate the statistic against observed outcomes for the specific decision and policy.

Independent questions can share state in one request. A completion check that needs a new test result belongs after that result exists. Put the full judgment in each question's instructions; IDs identify answers for code, rather than supplying model context.

## Inspect a concrete policy boundary

[jev-harness](../../projects/tools/jev-harness.md) is an **independent JevList suggestion**, not a project named or endorsed by Sumanth. The MIT TypeScript library, version 0.1.0 at the catalog's pinned [commit](https://github.com/AntonioCoppe/jev-harness/tree/2934d12e18157881440362d747d31b688a1c6ed6), illustrates how typed answers become an intended action and a resolved action. It requires Node 20+; live inference requires TypeSafe access, sends state and questions to that provider, and may incur charges.

Three details matter when studying its [harness](https://github.com/AntonioCoppe/jev-harness/blob/2934d12e18157881440362d747d31b688a1c6ed6/src/harness.ts), [policy](https://github.com/AntonioCoppe/jev-harness/blob/2934d12e18157881440362d747d31b688a1c6ed6/src/policy.ts) and [confidence calculation](https://github.com/AntonioCoppe/jev-harness/blob/2934d12e18157881440362d747d31b688a1c6ed6/src/confidence.ts):

- The library averages answer confidence and derives a Noul stand-in as `2 × abs(noul − 0.5)`. A strong answer can mask a weak required answer in that average. Check each required judgment separately when your policy needs it.
- `policy.decide` runs **before** the low-confidence fallback. Keep that callback pure: return an intended action, then execute only after the resolved action and deterministic permissions have been checked. A side effect inside the callback would already have happened before fallback or shadow mode.
- Shadow mode calls the client first and then replaces the resolved action with `shadow_noop`. It suppresses that returned action, not provider transmission or billing. An injected fake client is the offline path. Provider exceptions propagate; the host must handle them visibly.

This is source inspection of a pinned teaching example, not a tested integration or a recommendation to use its defaults. Newer upstream revisions exist; recheck the version you actually install. The library does not supply your OS sandbox, approval system or independent completion verifier.

## Measure the workflow you change

The source argues that recurring decisions make latency and cost consequential. It does not measure how much reasoning an agent spends on them, establish a speedup, or prove calibration on your workload. Record which existing calls a new gate replaces and which it adds. Include planning, tool latency, retries, review, mistakes and downstream generation in cost and time per correctly completed task.

For adoption steps, use [the first-pilot guide](jev-system-one-first-pilot.md). Keep the existing workflow as a baseline and preserve uncertain and failed cases in coverage totals. A valid typed response establishes neither correctness nor authorization.

## Validation and limits

Read the complete X article, including all visible diagrams and code blocks, in logged-in Chrome on 14 October 2026. Its body contained no outbound project or post links. We also read Sumanth P's [23 September newsletter version](https://aiengineering.beehiiv.com/p/jev-clearly-explained). It shares the architectural explanation but changes sections and adds claims; it is not an identical copy. Its separate voice GitHub agent uses AssemblyAI and an LLM Gateway. We followed its repository link and did not connect that adjacent tutorial as a Jev project.

Inspected current official primitive and confidence references and the pinned project's README, MIT license, package metadata, harness, policy and confidence code. No provider request, project execution, independent accuracy/calibration study, latency benchmark or billing measurement was performed. Publication checks validate content structure and rendering. This conceptual source supports no concrete application to reproduce, so the guide has no build prompt.

No source artwork is reused. The image is an original Appit Studio diagram dedicated to CC0. Reading or crediting an article does not establish permission to copy its cover.

## Adoption questions

### What is a Jev agent decision layer?

It is a set of bounded semantic judgments around an agent, such as route selection, risk assessment or completion checks. The LLM generates and plans; Jev supplies typed answers; application code enforces permissions and chooses the resulting action.

### Can Jev authorize an agent tool call?

No. A model judgment can inform review, but code must check the exact operation, allowed target, budget and required human approval. Missing evidence, uncertain answers and provider failures must not silently grant permission.

### Is a Noul probability the same as confidence?

No. Noul is the probability that its stated condition is true and has no separate confidence field. Choice and Score include distribution-based confidence. A library may derive another statistic; inspect its formula before using it as a gate.

### Can several Jev checks run in one request?

Yes, when they use the same supplied state and are independent. If one answer determines which evidence to fetch, update the state and make a later request. Put each complete question in its instructions rather than its lookup ID.

### Does shadow mode make a Jev harness offline?

No. The inspected jev-harness version calls TypeSafe before replacing the resolved action with shadow_noop. Use an injected fake client for offline checks, and keep policy callbacks free of side effects.

### Does a completion judgment prove the task is finished?

No. Compare the judgment with observable acceptance evidence, such as test results or a verified artifact. A retry cap can stop a run with work still incomplete; record that state and hand it to review.

## Sources, credits and corrections

- [Original X article](https://x.com/sumanth_077/article/2101639788961112279), Sumanth (@Sumanth_077), 20 September 2026; complete visible source read 14 October.
- [Newsletter version](https://aiengineering.beehiiv.com/p/jev-clearly-explained), Sumanth P, 23 September 2026; read separately, with its distinct adjacent tutorial and repository link.
- Official TypeSafe references and pinned project evidence are linked beside their claims. The wrapper's Noul stand-in is its own derived statistic, not an extra provider answer field.

Appit Studio wrote this original guide with AI assistance. No human reviewer, source-author endorsement, affiliation with the suggested project's maintainer or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md). API or wrapper changes require a fresh review before adapting the boundary.
