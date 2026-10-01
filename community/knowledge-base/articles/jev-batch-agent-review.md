# Batch-review parallel agent results with Jev

To review many independent agent results with Jev, give each result a stable ID and evidence, ask one bounded question per result against shared review rules, then route the typed answers in code. A large swarm does not guarantee one Jev request: size the actual payload against the context budget, chunk when needed, and keep ambiguous or failed checks visible for human review.

**Based on:** [“Jev Engineering: Parallel Decisions for a 300-Agent Kimi Swarm”](https://x.com/0xRicker/article/2104935716492869999) by [Ricker](https://x.com/0xRicker), published 29 September 2026. Appit Studio wrote this independent guide with AI assistance. Ricker did not write or endorse it; no human reviewer is claimed.

The article proposes matching parallel Kimi execution with parallel Jev judgments, then rerunning only rejected results. Its 300 results, 29 misses and subsequent shrinking rounds illustrate a design; they are not a published run with logs or a measured speedup. For a broader agent-loop design, see our [Jev agent loops guide](jev-agent-loops.md). This guide focuses on the review boundary after results arrive.

## Key takeaways

- **Separate independent checks from comparisons.** Source support, topical fit and completeness can be judged for each result against fixed rules. Ranking, deduplication and selecting a final set require the other results and belong after those checks.
- **Use the actual System One contract.** TypeSafe accepts `state` plus a map of typed questions through `client.system_one(...)`. The article's `jev.batch(...)` and `kimi.run(...)` are pseudocode, not verified integration methods.
- **Budget both content and questions.** Current Jev 1.13 documentation allows 32k tokens for state plus the longest question and 64k for the full request. Three hundred detailed outputs may require chunks.
- **Read Noul as a yes probability.** It has no separate confidence field. A high probability of source support is not proof that the source is true or that the whole report is safe to publish.
- **Measure the full loop.** Compare elapsed review time, billed input, accepted-result errors, human review and rerun work against the existing process. The cost of Kimi, source retrieval and correction remains outside Jev's quoted token rate.

## Define a reviewable result

Ricker asks whether a result matches its source. Make that question answerable: each record needs an immutable result ID, its claim or short summary, a cited source excerpt or structured evidence, and the review rule. A URL alone is not the excerpt, and a model match check is not an independent fact check of the source. Fetch and preserve sources under your application's normal permissions before review. If a source is absent or unverifiable, send the item to review rather than asking Jev to guess.

[Kimi's Agent Swarm help page](https://www.kimi.com/en/help/agent/agent-swarm) describes up to 300 simultaneous subagents and notes that swarm tasks consume credits. It does not establish that a particular run emits 300 reviewable records or provide the export interface for this article's code. Start from a result feed or export you are authorized to use. Keep Kimi execution, evidence collection, Jev judgments and final publication as separately observable stages.

## Batch the independent judgments

[TypeSafe's state guide](https://docs.typesafe.ai/concepts/state) says every question in a request sees the same state and is evaluated independently. Put shared criteria and a bounded group of results in structured state. Give each Noul question complete instructions such as “Does result `R-041`'s claim follow from its supplied source excerpt under the review rule?” The response key `R-041` is for your code to match the answer; the key itself is not model instructions. Use separate questions if topical fit and source support have different consequences.

The current [Python Noul documentation](https://docs.typesafe.ai/primitives/noul) uses `Noul(instructions=...)`, `TypeSafeClient.system_one(state=..., questions=...)` and `response.answers[id].noul`. The article's `v >= 0.85` treats an answer as a bare number. In the real response, `.noul` is the yes probability and there is **no separate Noul confidence**. A 0.85 keep boundary is the author's example, not a validated threshold for your records. A strong no can go to a bounded, recoverable rerun; a middle value, missing answer, bad source or malformed response goes to a reviewer. Keep any irreversible action under host-owned authorization.

Measure the serialized payload before sending it. [TypeSafe's model reference](https://docs.typesafe.ai/models) currently gives a 32k budget for state plus the longest question, a 64k total input budget and $0.042 per million input tokens for `jev-1.13.0`; output is free. The 300-question request may fit when results are short, but the count alone says nothing about fit. Split at stable record boundaries, preserve ID-to-answer mapping, and record chunk size, token estimate, actual `usage.input_tokens`, model version and elapsed time. A failed chunk should leave its records pending, not silently count them as approved. The independent [jevtok](../../projects/tools/jevtok.md) project is a **JevList suggestion** for estimating structured request tokens locally before a live call; it cannot judge content, and its reviewed encoder needs rechecking when the provider changes.

Only after the individual checks should code compute counts, group duplicates or prepare a ranking. If the next judgment depends on the scores or on freshly retrieved evidence, submit a later request with that new state. Ricker's speculative low/moderate/high failure-rate branches are useful only when their answers truly depend on known state. A fixed policy like “over 20% rejected means pause” is simpler and more auditable in code.

## Compare the actual tradeoff

Ricker compares 300 serial review calls, ten chunks of 30, and one request. Those are request counts under three possible implementations, not end-to-end timings. If the current reviewer already fans calls out concurrently, a serial baseline exaggerates the latency saving. Source length, question length, provider limits, network retries and chunk failures can also change the result. TypeSafe's [parallel-questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions) measured its own 13-question document workload; transfer the batching mechanism, not its exact multiplier, to a swarm.

The independent [jev-fanout-bench](../../projects/tools/jev-fanout-bench.md) is another **JevList suggestion**, for evaluating billing and serial-call timing. Its published synthetic English-ticket run through OpenRouter found shared-state savings; it did not test Kimi output quality or this 300-result pipeline. Its reported serial timing is not a comparison with a concurrent baseline. Provider reruns need credentials and incur charges. For this guide's workflow, label a representative set of accepted, rejected and ambiguous results, reserve untouched cases, and compare mistakes and total cost as well as tokens.

## Copyable build prompt

The source includes a two-stage review and rerun sketch. This Appit Studio prompt turns that sketch into a bounded adapter to an existing result feed; it does not assume a Kimi export API exists.

```text
Build an offline-first Python review adapter for [AUTHORIZED AGENT RESULT FEED OR EXPORT]. I will provide [RESULT SCHEMA WITH STABLE IDs], [CLAIM AND SOURCE-EXCERPT FIELDS], [SHARED REVIEW RULES], [EXISTING REVIEW QUEUE], [RECOVERABLE RERUN HANDLER], [MAX RETRIES], [REQUEST BUDGET], [LABELLED CASES], and [PERMITTED ACTIONS]. If the feed, source excerpts or rerun handler are missing, leave a documented integration boundary rather than inventing a Kimi API.

Read Ricker's source at https://x.com/0xRicker/article/2104935716492869999 and the current TypeSafe state, Noul, models and Python SDK documentation at https://docs.typesafe.ai/concepts/state , https://docs.typesafe.ai/primitives/noul , https://docs.typesafe.ai/models and https://docs.typesafe.ai/introduction/quickstart . Check the installed typesafe-sdk version and exception classes. Ricker's jev.batch and kimi.run calls are pseudocode. Use the documented client.system_one API and the Noul answer's .noul field; a Noul has no separate confidence field.

Normalize each result into an ID, claim, source excerpt, citation and attempt count. Put fixed rules and a bounded set of normalized results in structured state. Ask one complete, atomic Noul question per result about support from its supplied excerpt. Keep the result ID in the question instructions as well as the response map key. Estimate the full request and split on record boundaries before either the state-plus-longest-question 32k limit or total 64k limit. Pin a supported model version and record the resolved version, token usage and latency.

Keep routing deterministic: strong supported results become candidates for a later comparative review; strong unsupported results may be rerun only if the failure is recoverable and the retry budget remains. Middle probabilities, absent evidence, unknown IDs, missing or malformed answers, timeouts and provider errors go to the existing human-review queue. Treat 0.85 as a placeholder; select keep, rerun and review bands from labelled cases, then check untouched cases. Never turn missing model output into approval or run an unbounded retry loop. Let code own publication, permissions, budgets and deduplication; use a writing model only for prose that this review step does not produce.

Deliver the adapter, an injected fake TypeSafe client, a bounded chunk planner, durable per-result status and attempt records, a reviewer view, and offline tests for keep, rerun, ambiguity, missing source, oversized request, duplicate ID, partial chunk failure and service timeout. Default tests must send no data to any provider and execute no reruns. Make live inference a separate opt-in capped at [SMALL REQUEST COUNT]; explain that selected evidence goes to TypeSafe and may be billed. Report raw answers separately from code decisions. Compare the current review path with the new one on untouched labelled outputs: accepted-result error rate, human workload, rerun count, end-to-end time and all provider charges. Do not claim the guide's synthetic checks establish model accuracy or a 300-agent speedup.
```

## Validation and limits

We read the full X article, including its two code blocks, in a logged-in Chrome session on 1 October 2026. It has no external project links. An exact-title and author search found an earlier Ricker Kimi/Jev article with a different title and scope, but no verified republication of this one. The article's cover reuse rights were not established, so the image here is an original Appit Studio diagram released as CC0.

We checked the current TypeSafe state, Noul, model and fan-out documentation and Kimi's Agent Swarm help page, plus the two catalog entries and their pinned upstream evidence. In a scratch Python 3.12 environment, we installed `typesafe-sdk` 0.7.2 and checked synthetic `SystemOneResponse` routing without making a provider call. We did not run a Kimi swarm, obtain a Kimi result export, send a live TypeSafe request, test review accuracy or reproduce Ricker's cost and speed claims. The source's proposed 29 failed results and shrinking later rounds are illustrative, not observations from this review.

## Adoption questions

### Can Jev review 300 agent results in one request?

Possibly, if the shared state plus the longest question fits 32k tokens and the entire request fits 64k. Estimate the real payload first; split larger sets into bounded chunks and keep one answer ID for each result.

### Does a Jev Noul answer have a confidence score?

No. Noul returns the probability of yes from 0 to 1, without a separate confidence field. Treat a value near 0.5 as ambiguous and validate any keep or requeue threshold on labeled results.

### Should every failed swarm result be rerun automatically?

No. Rerun only a result with a recoverable failure after checking its source evidence and retry budget. Send ambiguous, missing or malformed answers to review, and stop after a fixed number of attempts.

### Is this a working Kimi Agent Swarm integration?

No. The article sketches a review loop but does not document a Kimi result-export API. Supply an authorized result feed or export, then test the adapter separately before connecting a live swarm.

## Sources, credits and corrections

The primary source is [Ricker's X article](https://x.com/0xRicker/article/2104935716492869999), published 29 September 2026. We checked [Kimi's Agent Swarm help](https://www.kimi.com/en/help/agent/agent-swarm) and TypeSafe's [state](https://docs.typesafe.ai/concepts/state), [Noul](https://docs.typesafe.ai/primitives/noul), [models and pricing](https://docs.typesafe.ai/models), [fan-out](https://docs.typesafe.ai/patterns/fan-out) and [parallel-questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions). [jevtok](../../projects/tools/jevtok.md) and [jev-fanout-bench](../../projects/tools/jev-fanout-bench.md) are independent JevList suggestions, not Ricker's recommendations. Appit Studio drafted this guide with AI assistance; no human review, paid placement or source-author endorsement is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) with the claim and supporting primary evidence.
