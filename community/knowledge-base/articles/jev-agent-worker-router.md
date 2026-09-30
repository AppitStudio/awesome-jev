# Build a Jev agent worker router

To route an agent task with Jev, build a fresh set of eligible workers, ask one bounded Choice question about the goal and completed evidence, then validate the selected worker before saving a handoff. Send ambiguity and service failures to a durable review path. Start with one fork and measure whether complete tasks improve before extending the loop.

**Based on:** [“Jev in the Agent Loop: A Complete Guide to Decision-Layer Automation”](https://x.com/N01ennn/article/2103542021071978601) by [NO1ennn](https://x.com/N01ennn), published 25 September 2026. Appit Studio wrote this separate guide with AI assistance; NO1ennn did not write or endorse it. No human reviewer is claimed.

The source surveys eleven decision points in an agent. This guide follows its most concrete starter: a standalone router that hands a research briefing to research, writing or review. For the broader loop architecture, see our [agent-loop guide](jev-agent-loops.md); for LangChain's separate tool gate, see the [harness guide](building-a-jev-agent-harness.md).

## Key takeaways

- **Choose from live eligibility.** Code determines which workers exist, are free and are permitted. A route from yesterday's menu is invalid even when Jev sounds certain.
- **Send evidence, not a verdict.** Keep the original goal, completed work, gaps and constraints in separate fields. The Choice question must describe each worker's job; its ID is only a lookup key.
- **Save a handoff, then let a worker consume it.** The article's JSON queue example writes a pending job. It does not run a worker, prove that a briefing exists, or publish anything.
- **Treat uncertainty and errors as work to handle.** The article's `0.85` confidence floor is illustrative. A missing, stale or low-confidence choice and every provider failure need a review or established fallback path.
- **Measure full tasks.** The source and vendor report decision-level costs and timings; they do not establish savings for a worker system with planning, tool calls, retries, review and rework.

## Start with a bounded handoff

NO1ennn suggests testing one decision in the [TypeSafe Playground](https://console.typesafe.ai/playground), then running a standalone dispatcher before connecting it to an agent. Use a sanitized goal and realistic progress notes. Build a closed menu such as `research` for missing evidence, `write` for a draft supported by evidence, and `review` for an unclear goal, completed task or blocked route. If research is unavailable, omit it from the current candidate set; never map an unrecognized answer to an executable worker.

The [official quickstart](https://docs.typesafe.ai/introduction/quickstart) confirms a request with state and named questions, and a Choice answer with `choice`, `probabilities` and `confidence`. The current quickstart lists **Python 3.10+** for its SDK; the source article's **3.12+** is a more restrictive setup choice, not the documented SDK minimum. The [state guidance](https://docs.typesafe.ai/concepts/state) and [fan-out guidance](https://docs.typesafe.ai/patterns/fan-out) support batching independent questions over the same state. A question that depends on a new search result or a worker's output needs a later call.

Use this order for one research briefing:

1. **Collect bounded state.** Record the goal, verified sources, remaining gaps, available workers and “save drafts for review” constraint. Remove credentials and private content before any live provider call.
2. **Filter in code.** Exclude unavailable workers and apply budget, permissions and action limits before forming the Choice criteria. Keep `review` available. A worker description must say when it should be selected, not merely repeat its name.
3. **Inspect the answer.** Log the raw Choice distribution, selected key, confidence, resolved model version and state version. Validate that the key still names an eligible worker. A concentration score is not a probability that the chosen route is correct; [TypeSafe's confidence guide](https://docs.typesafe.ai/confidence) calls for calibration on your data.
4. **Save one pending job.** Write a durable, uniquely identified handoff to the selected queue. Include the goal and evidence references. A consumer claims the job once, records progress and hands an exception back to review. An empty file, duplicate claim or unacknowledged job is not completion.
5. **Verify the outcome.** Confirm the expected draft or research artifact exists and meets the original goal before marking the task done. Publishing and other consequential actions stay behind the application's own approval rules.

The source routes `research` or `write` only when Choice confidence is at least `0.85`; otherwise it saves a `review` job. We exercised that branch with synthetic SDK response objects: `0.86` selected `write`, while `0.84` selected `review`. Those fakes test code behavior, not model accuracy. Label representative goals and reserve untouched cases before choosing a production threshold. A route is useful only if its downstream worker finishes the right work without excessive review or rework.

## Learn from connected projects

[Jev Ultrafast](../../projects/tools/jev-ultrafast.md) is **source-mentioned**: NO1ennn links the [Browser Use repository](https://github.com/browser-use/jev-ultrafast). It reconstructs a menu of currently observed browser controls, asks Jev for an operation and compatible target, and independently checks the result. That is a useful illustration of *fresh options*, not a ready-made research/writing dispatcher. It is an experimental MIT Python agent; actual browser use needs Chrome, a TypeSafe key and a separate text-model key for typing. Page state can be sent to those providers and calls can cost money. We did not run it live.

[jev-layer](../../projects/tools/jev-layer.md) is a **JevList suggestion**, not a project NO1ennn named. Its Node/MCP interface routes among a host's bounded capabilities and records execution receipts. Use it only when an existing harness already owns capability discovery, permissions, execution and fallback. It does not supply the article's Python queues. The independent MIT package has an offline demo provider; live TypeSafe or OpenRouter modes transmit state and can be billed. Its documented fail-open result returns control to the host's normal policy, not permission to perform an action.

## Copyable build prompt

```text
Build a bounded Python worker dispatcher for [PROJECT] and [TASK TYPE]. First read NO1ennn's source at https://x.com/N01ennn/article/2103542021071978601 and current TypeSafe docs at https://docs.typesafe.ai/introduction/quickstart, https://docs.typesafe.ai/primitives/choice, https://docs.typesafe.ai/concepts/state, and https://docs.typesafe.ai/confidence. Check the installed typesafe-sdk version and its response and exception classes before writing code.

Inputs I will supply: [GOAL AND EVIDENCE SCHEMA], [CURRENT WORKER REGISTRY], [RESEARCH/WRITING/REVIEW HANDLERS], [QUEUE OR STORAGE LOCATION], [PERMISSION AND SPENDING RULES], [LABELED ROUTING CASES], and [ARTIFACT SUCCESS CHECK]. Do not invent workers or authority. If a handler is missing, produce a clearly pending handoff rather than pretending it ran.

Use Choice for one next-worker decision over the currently eligible workers and an explicit review route. Put each route's complete selection criteria in the question; treat its key as a code lookup only. Keep exact eligibility, limits, authorization, idempotency and final execution in deterministic application code. The LLM may draft text after a writing handoff; Jev selects a bounded route and does not generate the briefing.

Deliver a standalone CLI, pure eligibility and answer-validation functions, a durable idempotent queue record, an injected fake TypeSafe client, and offline tests for research, write, review, low confidence, unknown or stale route, duplicate job, unavailable worker, malformed response, HTTP error, connection error and timeout. Default test and demo commands must make zero provider calls and zero external actions. Log the raw answer, resolved model, intended route, actual consumed route, error, latency and verified artifact separately. Do not log secrets or full private input.

Make any live run a separate explicit opt-in with a fixed small request limit. Explain that it sends sanitized state to TypeSafe and may incur charges. On uncertainty or service failure, save a review job or use an existing reviewed fallback; never silently execute a worker. Keep publication and other consequential actions behind the host's approval policy. After offline tests, compare routing on untouched labeled cases and measure full-task completion, elapsed time, provider charges, human review and rework against the current dispatcher. Do not claim savings from synthetic answers.
```

## Validation and limits

We read NO1ennn's complete X article and code blocks in the user's logged-in Chrome on 30 September 2026. It links the Browser Use repository, LangChain's [harness article](https://www.langchain.com/blog/building-a-harness-with-jev), and TypeSafe documentation. An exact-title and author search found an independent JevMade summary, not a verified author republication. The source cover's reuse rights were not established; this guide uses an original Appit Studio diagram released as CC0.

We checked the official quickstart and installed `typesafe-sdk` 0.7.2 in an isolated Python 3.12 environment. Synthetic `SystemOneResponse` data confirmed the source's confidence branch. We also inspected the SDK's exception hierarchy: `TypeSafeAPIConnectionError`, including timeouts, does **not** inherit `TypeSafeAPIError`, so the article's catch of only `TypeSafeAPIError` leaves those failures untreated. We inspected the catalog pages and pinned upstream evidence for both connected projects. No live Jev call, queue consumer or full worker system was run, and none of the article's timing or cost claims was reproduced.

## Adoption questions

### How do I route an agent task to the next worker with Jev?

Build a current list of eligible workers, send the goal and completed evidence with a Choice question, and validate the returned key in code. Save one durable handoff; send unclear, invalid or failed decisions to review.

### Does a high Jev confidence mean the chosen worker is correct?

No. Choice confidence describes the concentration of its answer distribution, not a guarantee that the route is correct. Treat 0.85 as a starting example, then tune a review threshold on labeled cases and check untouched cases separately.

### What happens if the TypeSafe request times out?

Record the error and keep the task in a durable review or existing fallback queue. Catch connection and timeout failures as well as API errors; do not treat a missing model answer as approval to run a worker.

### Is Jev Ultrafast a worker router?

No. The source-mentioned Browser Use project routes among freshly observed browser operations and targets. It teaches the changing-menu pattern, while your application must still define workers, queues, permissions and completion checks.

## Sources, credits and corrections

The primary source is [NO1ennn's X article](https://x.com/N01ennn/article/2103542021071978601), published 25 September 2026. Its named examples lead to [Browser Use's source](https://github.com/browser-use/jev-ultrafast), [LangChain's harness guide](https://www.langchain.com/blog/building-a-harness-with-jev), and [TypeSafe's quickstart](https://docs.typesafe.ai/introduction/quickstart), [Choice](https://docs.typesafe.ai/primitives/choice), [state](https://docs.typesafe.ai/concepts/state), [confidence](https://docs.typesafe.ai/confidence) and [fan-out](https://docs.typesafe.ai/patterns/fan-out) documentation. [jev-layer](../../projects/tools/jev-layer.md) is an independent JevList suggestion. Appit Studio wrote this guide with AI assistance; no human review, source-author endorsement or paid placement is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) if an API, claim or project relationship has changed.
