# Jev agent triage desk: routes, audits and total cost

A Jev agent desk can screen incoming events with typed questions, then let code send each event to ignore, log, draft or human review. Begin with one feed and an offline replay, measure missed events in the quiet lane, and price the writer and reviewers separately. Cheap routing alone does not establish a cheap or reliable 24/7 operation.

**Based on:** [“Jev Desk: How to Build a 24/7 AI Agent That Decides for Free and Only Pays to Write (Full Guide)”](https://x.com/gippp69/article/2103394701063737504) by [Gipp 🦅](https://x.com/gippp69), published 25 September 2026. This is an independent Appit Studio guide drafted with AI assistance. Gipp did not write or endorse it, and no human reviewer is claimed. The article's 20,000-event day is explicitly **estimated from assumptions**, not a measured invoice or accuracy test.

## Key takeaways

- **Separate the jobs.** Jev answers closed-set questions about an event. Code owns the lane, permissions, queues, audit sampling and billing records. A writing model drafts text only for selected events; a person approves consequential work and any outbound message.
- **The model-only example is arithmetic.** At the article's assumed 20,000 events, 1,000 input tokens each, 4% drafts and $0.03 per draft, Jev costs $0.84 and writing costs $24. Human reviews, audits, hosting, retries and mistakes are extra.
- **Audit the silent lane.** A wrong draft may be noticed in review, while a wrong `ignore` can disappear. Save enough evidence to sample and label ignored events, then report the missed-action rate with the sample size and uncertainty.
- **A floor is a policy choice.** TypeSafe's Choice `confidence` describes the answer distribution, not measured correctness. A higher floor usually changes review volume; it cannot certify that the remaining ignores are safe.
- **The article's code is a sketch.** Its exception handler misses connection errors and timeouts, and it checks only the lane answer's confidence. Use its flow as a starting design, not as a tested unattended service.

## Route one event through four lanes

Normalize one feed into a small event record with a stable ID, source, time, short text and the facts the desk may use. Keep source text as **content to judge**, never as authority to change the desk's instructions. Do not send private email, credentials or other sensitive material to a provider without a reviewed data path and retention policy. Define one independent Choice question for the intended lane, one for urgency and one for whether the supplied evidence is sufficient. [TypeSafe's question guide](https://docs.typesafe.ai/primitives) explains the three primitives and why each question must carry its own instructions; the question ID is only for your code.

The article asks all three questions in one Jev request. That shares the state and one round trip, but each question still adds input tokens. Code then applies the decision table. A useful initial policy is:

| Lane | Default code action | Review or audit condition |
| --- | --- | --- |
| Ignore | Retain a minimal receipt instead of notifying anyone. | Send a reproducible random sample to a reviewer; preserve enough evidence to label a miss. |
| Log | Record the event and its reason without interrupting the owner. | Escalate urgent contradictions or missing context. |
| Draft | Ask a separate writing model for a proposed reply or summary and save it to a review queue. | A person approves any send or post; missing facts go to human before drafting. |
| Human | Put the event and model answers in a durable review queue. | Service failure, uncertain or inconsistent answers, policy-sensitive content and overdue items remain visible. |

The article describes Grok Bot as its writer and always-on host, **not an official TypeSafe integration**. Its sample feed readers are placeholders. A machine staying on does not supply deduplication, retries, backpressure, health checks, secure feed credentials or a recovery plan. Add those before promising 24/7 coverage. Keep an event ID out of filesystem paths unless it is validated and mapped to a safe local filename.

For a smaller Python example, [Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) is an **independent JevList suggestion**, not a Gipp project. It asks several Jev questions about each email thread in one request, caches selected answer fields, then applies queue policy in separate code. Its MIT source needs Python 3.10+, uv and a billed TypeSafe key for live classification; a real inbox also needs IMAP credentials. It covers email only, has no Grok Bot or cross-feed runner, and its live path was not tested for this guide. Start with its synthetic demo shape rather than connecting a real inbox immediately.

## Price the whole desk

TypeSafe lists [`jev-1.13.0` at $0.042 per million input tokens](https://docs.typesafe.ai/models), with output tokens free, as checked 27 September 2026. That price is for Jev calls; a writing model, human review and infrastructure have different rates. Let `N` be events per day, `T` measured Jev input tokens per event, `e` the fraction sent to a writer, and `C` the actual average cost of a draft. The article's model-only estimate is `N × T × $0.042 / 1,000,000 + N × e × C`.

| Assumed daily events | Assumed tokens each | Assumed draft share and price | Jev | Writing | Model-only total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 20,000 | 1,000 | 4% at $0.03 | $0.84 | $24.00 | $24.84 |
| 200,000 | 1,400 | 4% at $0.03 | $11.76 | $240.00 | $251.76 |

These are **scenarios**, not the author's invoices or our benchmark. The source's `bill.py` then adds sampled ignored events to the writing count at the same $0.03 rate, producing $29.04 for the first day. Yet the earlier description calls that audit a **human second look**. A human audit has its own cost and capacity; it is not automatically a model draft. With the source's assumed 70% ignore share and 1% sample, 140 events a day need audit. The correct full ledger adds `human reviews × review cost`, `ignore audits × audit cost`, hosting, retries and correction work. Leave unknown costs unknown until measured.

Log `response.usage.input_tokens` and the returned model ID from actual calls; do not bill from the article's `350 + characters // 4` estimate. [jevtok](../../projects/tools/jevtok.md) is an **independent JevList suggestion** for an offline whole-request estimate before launch. Its MIT Python package needs no key to count, but its reconstructed encoder is not a future billing guarantee. Compare estimates with reported usage after any model or request change. A 200,000-event average is about 139 requests a minute; peak arrival rate, worker concurrency and retries still need a load plan. TypeSafe's published limits can change.

## Measure misses before moving the floor

The article cites [the TypeSafeAI community jev-harness](../../projects/tools/typesafeai-jev-harness.md) as a **source-mentioned** threshold example. That MIT, source-only Node 22+/pnpm project is a coding-agent proposal gate, not this event desk or an official TypeSafe SDK. Its historical report says a combined pipeline caught 20 bad proposals in 20 synthetic pairs, **seven through deterministic validation before Jev**. The threshold sweep reused the same examples; it is not held-out calibration. Current repository offline totals use a labeled mock transport. Those results cannot establish a safe floor for a desk's ignored events.

Start with labeled examples for every source and lane. Keep model, question wording and policy version on each record. Review a random sample of `ignore` events, including all obvious high-risk categories under a separate deterministic rule. Count false ignores against the sampled denominator and show uncertainty; do not call an uninspected `ignore` correct. Also track drafts rejected by the owner, human queue age, service errors, duplicate events and total cost per useful outcome. If the floor changes, compare the same frozen labeled cases and then watch a fresh period. A threshold can change both the review count and the composition of what remains ignored.

The article's code sends a low-confidence **lane** to human, an urgent `ignore`/`log` contradiction to human, and a `draft` with missing evidence to human. It does not gate low-confidence urgency or evidence answers, and a high-confidence `ignore` with `evidence=missing` still stays ignored. In an offline replay with `typesafe-sdk` 0.7.2 fake responses, that case routed to `ignore`. The article catches `TypeSafeAPIError`, an HTTP-response error; [connection errors and timeouts](https://docs.typesafe.ai/sdk/python/api/exceptions) have a different branch under `TypeSafeError`. Make all unavailable and malformed responses visible in the human queue. The example's `0.85` is uncalibrated for this workload.

## Copyable build prompt

```text
Build an offline-first Jev event triage pilot for [ONE INPUT SOURCE] in [MY PYTHON VERSION AND HOST]. My event schema is [ID, SOURCE, TIME, ALLOWED TEXT/FIELDS]; sensitive fields to exclude are [FIELDS]. The four destinations are ignore, log, draft-for-review and human. The action owner is [ROLE]. Use only synthetic records until I explicitly enable a bounded live run. Do not send, post, delete, trade or approve anything automatically.

Read the current TypeSafe docs before coding: https://docs.typesafe.ai/primitives , https://docs.typesafe.ai/sdk/python , https://docs.typesafe.ai/sdk/python/api/types/responses , https://docs.typesafe.ai/sdk/python/api/exceptions and https://docs.typesafe.ai/models . Pin a current model ID and record the response model and usage.input_tokens. Check installed SDK fields; do not copy the article's handler untested. Jev supplies typed judgments; deterministic code owns permissions, queues, sampling, cost accounting and every action. A separate writing model may create review-only text for the draft lane.

Create a source adapter for [ONE SOURCE], an idempotent event store, three independently worded Choice questions for lane, urgency and evidence sufficiency in one request, and a pure policy function. Validate model answers and event IDs. Route HTTP errors, connection errors, timeouts, malformed or missing answers, low-evidence drafts and policy-sensitive events to a durable human queue with a reason. Store a minimal ignore receipt and sample ignored events with a reproducible seed for a reviewer; never erase evidence before its review window. Make queue failures visible and retry safely without duplicate drafts. Provide a stop switch, rate limit, concurrency cap and backlog/queue-age metrics.

Deliver synthetic fixtures and offline tests for every lane, low confidence in each question, urgent-ignore disagreement, missing evidence, all error classes, duplicate IDs, unsafe IDs, writer outage, queue-write failure and audit sampling. Verify the writer saves drafts to review and cannot send. Add a ledger with actual provider usage when present, estimated usage clearly marked when absent, writer cost, human-review time, audit time, hosting assumptions and later corrected outcomes. Show both false-ignore count and sampled denominator; do not claim an accuracy rate if labels are missing.

Compare candidate floors on one labeled set and check one chosen policy on untouched cases. Start a live shadow run only behind [EXPLICIT OPT-IN FLAG], [MAX REQUEST COUNT], [SPEND CAP], a provider key from the environment and an approved data path. Keep the existing workflow as the authority until the action owner signs off. Report exactly what ran and what remains unmeasured. Jev Inbox Queue (https://github.com/tusharck/jev-inbox-queue) is an optional email-only teaching example; jevtok (https://github.com/LabGuy94/jevtok) is an optional local token estimator. Neither is Gipp's desk or a verified 24/7 integration.
```

## Validation and limits

We read all 13 sections and code blocks in the logged-in X article and inspected its diagrams. We checked TypeSafe's current model, SDK, confidence and exception documentation, the catalog pages and pinned upstream code for the connected projects. We installed `typesafe-sdk` 0.7.2 in a scratch environment and replayed three synthetic answer combinations without an API call. The source arithmetic was checked; the source's triage accuracy, latency, Grok Bot wiring and 24/7 operation were **not** reproduced. Exact-title and opening-line searches found no verified author republication. The diagram on this guide is original Appit Studio work licensed CC0, not an article image.

The prompt is a reviewed specification, not a built service. We did not connect a feed, send data to TypeSafe or a writer, gather real reviewer labels, calibrate a floor or measure the full bill. The article's demo figures and jev-harness results describe other workloads. Recheck prices, SDK contracts, source permissions and data handling before a live deployment.

## Adoption questions

### How do I build a Jev agent triage desk?

Start with one input source and four code-owned lanes: ignore, log, draft and human. Ask Jev bounded routing questions, keep generation in a separate writer, record every outcome, and review a sample of ignored events before adding more feeds.

### What does a Jev desk cost per day?

At the article's assumed 20,000 events, 1,000 Jev input tokens per event, 4% drafts and $0.03 per draft, model charges are $0.84 for Jev plus $24 for writing. Human review, ignored-event audits, hosting, retries and mistakes are additional and were not measured.

### Does a higher Jev confidence floor make ignored events safe?

No threshold guarantees that. Raising the floor sends more low-confidence events to review, but confident wrong ignores can remain silent. Label a representative sample of ignored events and measure misses at each candidate floor before changing the policy.

### What happens if Jev is unavailable?

Send the event to a durable human-review queue and record the error. Handle HTTP failures, timeouts, connection failures and malformed responses; never turn an unavailable judgment into an automatic ignore or send a draft without review.

## Sources, credits and corrections

The primary source is [Gipp's complete X article](https://x.com/gippp69/article/2103394701063737504), published 25 September 2026. Its worked day and scale-up are assumptions, as the article says. [TypeSafe's model pricing and limits](https://docs.typesafe.ai/models), [Python SDK guide](https://docs.typesafe.ai/sdk/python), [confidence explanation](https://docs.typesafe.ai/confidence) and [exception reference](https://docs.typesafe.ai/sdk/python/api/exceptions) support the technical corrections. The source-mentioned [TypeSafeAI community jev-harness](https://github.com/TypeSafeAI/jev-harness) supplies a separate proposal-gate example; the [Inbox Queue](https://github.com/tusharck/jev-inbox-queue) and [jevtok](https://github.com/LabGuy94/jevtok) connections are our suggestions, without endorsement by Gipp. Appit Studio wrote this guide with AI assistance, no claimed human review, affiliation or paid placement. [Report a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) if a source, project or API detail has changed.
