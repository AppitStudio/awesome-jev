# Build a budget-aware Jev bot

A budget-aware Jev bot uses a cheap, bounded judgment to decide which events deserve further analysis, while code reserves money, checks permissions and records every bill. Start with an offline event replay: a low inference price can extend a *model-only* runway, but it cannot demonstrate that a bot earned revenue, made good decisions or paid its full operating costs.

**Based on:** [“Jev Bot: The AI That Has to Pay for Its Own Brain”](https://x.com/paonx_eth/article/2103881060878533066) by [Paone](https://x.com/paonx_eth), published 26 September 2026. This independent Appit Studio guide was drafted with AI assistance. Paone did not write or endorse it; no human reviewer is claimed.

Paone describes a bot that deducts hosting and decision costs from a finite balance. The article's central comparison then holds the input rate and starting balance fixed while changing model list prices. Its charts explicitly say they calculate **inference only**, without hosting, downstream analysis, fees or observed earnings. That distinction is the useful starting point for a builder.

## Key takeaways

- **Use Jev for bounded choices.** The article's `skip`, `watch` and `deep_dive` routes fit a Choice question. A separate text model may analyze a selected case; deterministic code owns money, permissions and actions. Jev does not write the analysis or calculate a balance.
- **The runway is arithmetic, not a run.** At the article's assumed one 1,000-input-token call each second, the listed Jev rate gives about $3.63 a day and about 17.9 days from $65 **if inference is the only bill**. A real server, retries and deeper calls shorten it.
- **An uncertain answer is a review path.** TypeSafe's Choice `confidence` measures the shape of returned option probabilities; it is not a measured chance of success. Paone's example `0.5` floor and rising balance-based thresholds are illustrative policy, not validated trading gates.
- **Calibrate the quantity you will use.** The independent study Paone cites measured several probability forms on one sentiment dataset. Its `0.117 → 0.008` result concerns a Noul positive-label probability on held-out data, not the article's Choice `confidence` on markets.
- **Log the entire loop.** A bot that spends less per call can still lose through unnecessary calls, large-model escalations, stale data, fees or bad actions. Without a verifiable balance and outcome ledger, “pays for itself” remains a hypothesis.

## Separate the price example from the operating budget

[TypeSafe's model page](https://docs.typesafe.ai/models) lists `jev-1.13.0` at **$0.042 per million input tokens**, with no output-token charge, as checked 27 September 2026. It also says the full request includes the state and questions, and that the model's alias can change. The article uses 10,000 decisions with roughly 1,000 input tokens apiece. On those assumptions, `10,000 × 1,000 × $0.042 / 1,000,000 = $0.42` for Jev input. At one call each second, the same rate is `$3.6288` per 24 hours, and `$65 / $0.000042` is about **17.9 days**. These are our reproductions of its price arithmetic, not provider receipts or measured runtime.

| Budget item | Record or estimate separately |
| --- | --- |
| Jev screening | Actual `usage.input_tokens`, request count, model ID, retries and provider charge. |
| Deep analysis | The separate writer or reasoning model's input, output, cache and retry bill. |
| Infrastructure | Server, storage, data feeds, monitoring and any minimum charges while idle. |
| Actions | Transaction or API fees, slippage, failed actions and correction work if an action is enabled. |
| Human work | Review, labeling, incident response and policy changes. |
| Revenue | Settled receipts only, with refunds and fees; none are demonstrated by the article's runway chart. |

Keep a reserve **before** each optional request: `available = settled balance − incurred costs − reserved pending costs`. Code must reject a request whose maximum allowed cost exceeds `available` or a separate daily cap. Set a timeout and a maximum number of calls; reconcile reservations with the provider's usage after a response or failure. A model estimate is useful for planning, but it is not the final bill. [jevtok](../../projects/tools/jevtok.md) is an **independent JevList suggestion**, not a Paone project: its MIT Python code estimates the whole Jev request locally, including structured state and questions. Python 3.10+ and its package dependencies are needed; no TypeSafe key or data transfer is needed for local counting. Its reconstructed encoder can drift, so compare it with provider usage after a model change.

The article cites a third-party [routing-price test](https://www.ayautomate.com/blog/jev-pricing-cost-per-decision) that reported roughly 40 times lower per-decision cost than one larger model on its own task, while the list-price chart shows a much larger multiple against a frontier model. The test is a different workload and tokenization; neither ratio predicts this bot's full cost. Price and access can change, so use the provider's current rate and your own recorded request sizes.

## Route a candidate without delegating the rules

Use one synthetic event record with an ID, event time, source, bounded facts and allowed actions. Keep any untrusted article, page or market text in the state as data, never as policy. A Jev Choice can ask whether this event warrants `skip`, `watch`, `deep_dive` or `other`; include `other` so a forced choice does not become an action. [TypeSafe's primitives guide](https://docs.typesafe.ai/primitives) says the question's instructions must stand alone; IDs only identify answers in code. Independent questions over the same state can share one request.

After the answer, code checks freshness, allowed action, calibrated evidence and the budget reserve. `skip` retains a minimal audit receipt; `watch` schedules a bounded later check; `deep_dive` may call a separate text model **only** within an approved cap and then saves a reviewable result. `other`, a missing answer, timeout, stale event, inconsistent evidence or exhausted budget goes to a visible review/stop route. None of these paths needs a wallet or live order. If a later product proposes financial action, an owner must separately define and approve permission, sizing, rate, loss and confirmation rules. A semantic classifier cannot grant those permissions.

The article points to [Conway Automaton](https://github.com/Conway-Research/automaton) for the finite-compute idea. Its README describes balance-based service tiers and a shutdown state; it is **not** the Jev Bot implementation. Paone's earlier [survival-mode post](https://x.com/paonx_eth/status/2102801840819556417) reported a 24-hour run and 180 paid bills. The later article promises a future live run and offers no public audited balance, request log or trading outcome for that claim. The earlier report may describe a separate run, but the two accounts cannot be reconciled from the published evidence. This guide does not count that post as verification of the 18-day scenario.

## Validate a gate against outcomes

[TypeSafe's confidence guide](https://docs.typesafe.ai/confidence) says Choice and Score answers include a `confidence` statistic derived from their probability distribution; Noul instead exposes its yes probability. The article's sample checks a Choice `confidence` and later suggests fitting a calibrator to that number. An [Anthus study](https://github.com/AnthusAI/Jev-Calibration) found that its highest Choice *top-label probability* bucket averaged 99.4% while its observed accuracy was 90.2% on 8,801 constructed sentiment examples. The study's reported expected calibration error improvement from 0.117 to 0.008 used a **Noul `P(positive)`** with a separate calibration and holdout split. Those are distinct quantities, and sentiment labels do not set a safe threshold for a different bot.

For your own workload, save the raw answer probabilities, chosen route, question and model versions, budget policy version, later verified outcome, and the cost of an error or review. Define the event you want a probability for, fit any calibrator on one labeled split, and check the chosen policy on untouched cases. Report sample sizes, missing outcomes, wrong automatic routes, review volume and complete cost. [jeval](../../projects/tools/jeval.md) is a second **independent JevList suggestion**: its Apache-2.0 Python 3.10+ CLI makes offline reliability and cost-threshold reports from labeled decisions, with no provider key for the report. You must supply credible labels and costs. It neither fits the article's calibrator nor enforces a live budget or action policy.

The [Jev decision audit guide](jev-decision-audit.md) covers outcome labels and held-out policy selection in more detail. The [agent triage desk guide](jev-agent-triage-desk.md) covers queues and reviewing silent `ignore` decisions. Here the extra question is whether the whole agent stays within a finite, reconciled budget while preserving useful outcomes.

## Copyable build prompt

```text
Build an offline-first, budget-aware Jev routing simulator in [MY STACK] for [ONE NON-TRADING EVENT FEED]. I will supply [SYNTHETIC EVENT JSONL], a starting balance of [AMOUNT], a daily cap of [AMOUNT], a reserved minimum balance of [AMOUNT], a candidate event rate, [HOSTING COST PER HOUR], [OPTIONAL WRITER COST ESTIMATE], [REVIEW COST ESTIMATE], and [DATA RETENTION RULES]. The action owner is [ROLE]. Do not connect to an exchange, wallet, private feed, live trading API or paid model by default.

Read the current TypeSafe model, primitives, confidence, Python SDK and error-handling docs before coding: https://docs.typesafe.ai/models , https://docs.typesafe.ai/primitives , https://docs.typesafe.ai/confidence , https://docs.typesafe.ai/sdk/python and https://docs.typesafe.ai/sdk/python/api/exceptions . Pin the versioned Jev model and record the returned model ID. Check the installed SDK's answer and usage fields. Jev judges one bounded event; deterministic code owns the ledger, reservation, freshness check, permissions, routing and all actions. A separate text model may draft analysis only for approved deep dives; its output remains review-only.

Deliver a pure budget ledger, a deterministic route function, a synthetic event replay CLI, test fixtures and a report. The Choice options are skip, watch, deep_dive and other; write complete option criteria and keep untrusted source text out of policy. For every event store ID, model/question/policy versions, raw answer distribution, choice, estimated and actual input tokens when present, costs, reservation, route reason and later outcome if known. Keep unresolved outcomes unresolved. Before any optional call, reserve its maximum configured cost; release or reconcile the reservation after the result. Stop on an exhausted balance or cap. Never allow an absent, malformed, late, other or service-failure answer to execute an action.

Show the article's one-call-per-second, 1,000-input-token, $65 scenario as inference-only arithmetic, then a second scenario that separately prices hosting, retries, approved deep dives, review and mistakes. Label every estimate and unknown. Optionally use jevtok (https://github.com/LabGuy94/jevtok) to estimate a whole Jev request and jeval (https://github.com/rlaope/jeval) to evaluate labeled decisions offline; both are independent JevList suggestions, not parts of Paone's bot. Compare a candidate gate on training labels with untouched cases. Do not borrow Anthus's sentiment threshold or treat Choice confidence as a probability of trading profit.

Test skip, watch, deep_dive, other, low evidence, stale data, duplicate ID, cap exhaustion, overlapping reservations, provider timeout, invalid response, missing usage and writer failure. Assert that no case sends an order, pays a bill or posts externally. Put live calls behind explicit opt-in, a maximum request count, a maximum spend, an approved data path and credentials from the environment. Report exactly what ran, what was simulated and what remains unmeasured. Do not claim the bot earns its keep, survives for 18 days or improves financial returns without a complete independently checked ledger and outcomes.
```

## Validation and limits

We read the full X article, its code blocks and image footnotes in the user's logged-in Chrome, and the author's earlier survival-mode post. We checked the cited Automaton repository, Anthus calibration study and pricing test, current TypeSafe docs, and the two catalog projects' pinned source and licenses. We reproduced the article's Jev-only arithmetic. Exact-title searches found no verified author republication. This guide's diagram is original Appit Studio work licensed CC0; the article's images have no stated reuse permission.

We did **not** run a Jev bot, call TypeSafe, verify Paone's earlier 24-hour claim, inspect a wallet or prove earnings. The article's `while balance > 0` loop and confidence snippets are design sketches, not a working, audited service. Its price comparisons exclude costs that can dominate a live system. Anthus's sentiment calibration cannot be transferred to a market gate without new labels, validation and an approved action policy. The copyable prompt is a specification for a safe offline pilot, not evidence that one has been built.

## Adoption questions

### How much does a Jev bot cost per day?

At one 1,000-input-token Jev call per second and TypeSafe's listed $0.042 per million input tokens, the Jev inference estimate is $3.63 per day. Add hosting, larger-model calls, retries, data, reviews, transaction fees and mistakes separately; measure actual usage before budgeting.

### Does a $65 budget let a Jev bot run for 18 days?

Only in the article's model-only scenario: one 1,000-input-token Jev call each second at the listed rate. The calculation omits hosting and every other cost, and it does not show revenue or a live 18-day run.

### Can Jev confidence decide when a bot should trade?

No raw confidence value proves that a trade is correct or profitable. Choice confidence summarizes the option distribution; a threshold needs task-specific labeled outcomes, a held-out check and code-owned risk limits. Keep trading disabled in the pilot.

### What happens when a Jev budget or service fails?

Stop paid calls before the reserved budget is exhausted, record the reason and leave the item for review. An unavailable, malformed or late model answer must not become an automatic action; reconcile estimated charges with provider usage when service returns.

## Sources, credits and corrections

The principal source is [Paone's complete article](https://x.com/paonx_eth/article/2103881060878533066), published 26 September 2026; the [earlier post](https://x.com/paonx_eth/status/2102801840819556417) is a separately reported claim. [Conway Automaton](https://github.com/Conway-Research/automaton), [Anthus's calibration repository](https://github.com/AnthusAI/Jev-Calibration) and [AY Automate's pricing test](https://www.ayautomate.com/blog/jev-pricing-cost-per-decision) are the identifiable primary material behind the examples used here. [TypeSafe's model](https://docs.typesafe.ai/models), [primitives](https://docs.typesafe.ai/primitives) and [confidence](https://docs.typesafe.ai/confidence) pages set the API and pricing boundaries checked on 27 September 2026. The jevtok and jeval links are Appit Studio editorial suggestions, with no source-author endorsement or paid placement. Appit Studio drafted this guide with AI assistance and no claimed human review. [Report a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) if a source, price or project behavior has changed.
