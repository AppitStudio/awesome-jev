# Build a Jev and Kimi K3 confidence cascade

Use a Jev and Kimi K3 cascade when an agent repeatedly makes a **bounded choice** but some cases still need a fuller read. Let code apply exact rules, send the remaining choices to Jev, escalate uncertain cases to Kimi K3, and keep consequential actions under code and human control. A threshold is a policy to test against your own labeled cases, not an accuracy guarantee.

This guide interprets [Mr. Buzzoni's September 29, 2026 article](https://x.com/polydao/article/2104783226833186920), *How to Cut Your Agent Bill by 90% With Jev Engineering and Kimi K3*. The author proposes replacing repeated generation calls with typed decisions and a larger-model fallback. The project links below have explicit provenance; an editorial connection does not imply the author's endorsement.

## Key takeaways

- **Sort the work before adding a model.** Text, code and plans need a generative model; exact limits and permissions need code; choices from a known menu can use Jev; irreversible actions need a person or a separate approved policy.
- **Ask independent questions together.** Jev can judge several questions over one shared state in one call. A question that depends on new evidence needs a later call after the state changes.
- **Keep an exit option.** A Choice about message type should include `other`; code can route no-match and uncertain answers to review. `confidence` exists for Choice and Score, while Noul returns a yes probability without that extra field.
- **Measure the complete loop.** The article's headline savings come from a price model. They do not establish a 90% reduction in an agent's observed bill.

## Choose one bounded decision

Start with a task such as routing an inbound support email to a known queue. Write down the allowed labels, a no-match label, and the exact evidence in the message that each label requires. Compute hard facts, such as account status, retry count and budget, in code. Send only the state needed for the questions. Do not ask Jev to extract arbitrary prose or to grant permissions.

The article's shared-state ticket example combines a Choice for department, a Score for frustration and a Noul for an explicit refund request. These judgments can be asked together because none needs another answer. Application code then decides whether the result is usable and which queue receives it. [TypeSafe's primitives](https://docs.typesafe.ai/primitives) and [fan-out pattern](https://docs.typesafe.ai/patterns/fan-out) describe the request shapes. Version each question and its criteria along with the pinned model and routing policy.

For an inspectable inbox prototype, [Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) is **suggested by JevList**. Its pinned Python implementation asks seven typed questions per thread and applies queue rules in code. It is MIT licensed and needs Python 3.10+, `uv` and a TypeSafe key for live use; IMAP is optional. Live email content goes to TypeSafe and usage may be billed. It does **not** implement Kimi fallback or reproduce the fraud result in the article.

## Escalate what the first decision cannot settle

Code should reject a no-match Choice and compare Choice confidence with a threshold selected for this particular action. [TypeSafe defines `confidence`](https://docs.typesafe.ai/confidence) as a summary of the answer distribution, not a measured probability that this individual answer is correct. Keep the full distribution in logs, along with model, question and policy versions. Inspect labeled outcomes by confidence band and validate the chosen threshold on untouched cases before automating a route.

An uncertain message can go to Kimi K3 with the original text and an explicit allowed output schema. Validate its category against the same menu; a free-form `sure` flag is not proof of correctness. If either provider times out, returns malformed data or disagrees on a consequential case, put the message in a visible review queue. Never let a model answer bypass account permissions, send an email, move money or delete data by itself. A shadow run still transmits the message to the provider even when no downstream action executes.

The article links [Hassan's Jev + Kimi K3 fraud demo](https://github.com/Nutlope/jev-fraud) as a concrete cascade. Its README says both models see the original email, Jev handles a confident subset and Kimi independently reviews the rest. The repo offers a recording replay without keys and a separate paid live run. Its [validation note](https://github.com/Nutlope/jev-fraud/blob/main/VALIDATION.md) reports 70 Jev-only decisions, 30 Kimi reviews, 92/100 combined correct and about $0.102 for the later Together AI recording. The article quotes an **earlier** 96/100 run at about $0.07. Those results refer to different runs on a small, balanced sample; neither is an accuracy guarantee for production mail. The recorded Jev charge was reported as zero by its gateway, while Kimi's amount was a token-price estimate.

The article also names [Browser Use Jev Ultrafast](../../projects/tools/jev-ultrafast.md), a **source-mentioned** but separate example. Its MIT Python agent builds fresh operation and DOM-target choices for each browser step; code executes the selected action and checks the page. It needs Python 3.12+, `uv`, Chrome, a TypeSafe key and a separate text-model key when typing. It is not an inbox or Kimi cascade, and its cited flight timing was not reproduced here.

## Price the actual workflow

For 10,000 messages with 1,000 Jev input tokens each, the article's stated $0.042 per million Jev input tokens gives **$0.42**. If 10% then require Kimi, and each Kimi call consumes 1,500 input and 300 output tokens at the article's $3/$15 per million rates, Kimi adds **$9.00**, for **$9.42**. Kimi on all 10,000 under the same token assumptions is **$90**. The resulting reduction is about **89.5%** against that Kimi-only scenario. [Kimi's model page](https://platform.kimi.ai/) listed those rates when checked; pricing and access can change.

This is a modeled inference line item. Real cost also includes extra agent planning calls, retries, gateway differences, storage, infrastructure, human review and correction of wrong routes. Escalation share and token lengths must be measured from your own trace. Track provider-reported usage and elapsed task time, not only one decision call. Do not compare the demo's recorded bill with the article's modeled 10,000-message table as though they were the same experiment.

## Validation and limits

The complete X article and its code were read in signed-in Chrome. The linked fraud repository and its later validation note, the two catalog projects' pinned source evidence, and current TypeSafe and Kimi documentation were reviewed. The cost arithmetic above was recomputed from the article's assumptions. No live Jev/Kimi request, email benchmark, browser task or billing audit was run for this guide. Source-reported latencies, accuracy and speedups remain attributed claims.

The source cover has no verified reuse permission, so this guide uses an original CC0 decision-flow diagram. Use synthetic messages first. For a real pilot, obtain suitable permission for message processing, label representative outcomes, hold out evaluation cases and record abstentions and service failures. Review mistakes and total operating cost before moving any band from shadow observation to action.

## Copyable build prompt

```text
Build a small Python 3.10+ email-routing prototype with a Jev Choice first pass and an optional Kimi K3 second opinion. Inputs I will edit: [message source or synthetic fixture], [allowed categories and clear criteria, including other], [action-specific confidence threshold], [review-queue location], [monthly provider budget], and [provider/model versions]. Start with five synthetic messages and no network requests.

Read https://docs.typesafe.ai/sdk/python, https://docs.typesafe.ai/primitives/choice, https://docs.typesafe.ai/confidence, https://docs.typesafe.ai/models and https://platform.kimi.ai/ before choosing API names and model IDs. Use https://github.com/Nutlope/jev-fraud as a source-mentioned cascade example; compare its README and VALIDATION.md, but do not copy its reported accuracy as our result. Jev Inbox Queue at https://github.com/tusharck/jev-inbox-queue is an independent JevList-suggested reference for batched inbox judgments and code-owned queues, not a Kimi implementation.

Deliver a runnable CLI, a synthetic fixture, offline tests and a short operator README. Code must apply exact allowlists/budgets first; construct one complete Choice instruction and criteria from current message state; include other; preserve the raw Jev answer and distribution; validate category, model response and confidence before routing. Only uncertain or no-match cases may request Kimi, which must receive the original message and return a schema-validated category and reason. Keep sending, deletion and permission changes behind human review. On timeout, bad JSON, unknown category, exceeded budget or provider failure, record the error and queue review instead of acting. Make live calls explicitly opt-in and bounded.

Show which synthetic messages are accepted, escalated and reviewed, including the reason for each. Test threshold boundaries, other, malformed answers and both provider failures offline. Then propose a shadow pilot and held-out labeled evaluation with per-provider tokens, billed usage, review time, wrong-route cost and end-to-end latency. Do not claim production accuracy, calibration or 90% savings from the synthetic fixture.
```

## Adoption questions

### How does a Jev and Kimi K3 confidence cascade work?

Code handles exact rules first. Jev answers a bounded Choice over current state; code accepts a tested confidence band or sends uncertain and no-match cases to Kimi K3. A human reviews unresolved or consequential cases, and permissions remain in code.

### Does a 0.95 Jev confidence mean 95% accuracy?

No. Choice confidence summarizes how concentrated Jev's answer distribution is; it is not the measured chance that this particular answer is correct. Set thresholds against labeled outcomes from your own workflow and check them on untouched cases.

### Did the Jev and Kimi fraud demo score 96 or 92 out of 100?

The article quotes an earlier 96/100 run. The linked repository's later recorded Together AI run reports 92/100 on a balanced 100-email sample. They are different builder-reported runs, and neither establishes production accuracy.

### Can the cascade cut an agent bill by 90%?

The article's roughly 90% figure is a token-price scenario: $9.42 for Jev plus 10% Kimi escalation versus $90 for Kimi on every email. It excludes retries, review, infrastructure, incorrect routes and other agent calls. Measure your own full workflow before claiming savings.

### What if Jev, Kimi K3 or the answer schema fails?

Record the error and place the item in a review queue or a previously approved safe fallback. Do not treat a timeout, malformed answer, unknown category or low confidence as permission to act.

## Sources, credits and corrections

- [Original article by Mr. Buzzoni](https://x.com/polydao/article/2104783226833186920), published September 29, 2026. The guide's prose and diagram are by Appit Studio with AI assistance; no human reviewer is recorded.
- [Hassan's fraud demo](https://github.com/Nutlope/jev-fraud), its [September 19 validation note](https://github.com/Nutlope/jev-fraud/blob/main/VALIDATION.md) and [earlier demonstration post](https://x.com/nutlope/status/2100614659690713543). The article's 96/100 figure and the repository's later 92/100 recording are different runs.
- [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python), [primitives](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence) and [fan-out](https://docs.typesafe.ai/patterns/fan-out); [Kimi model and pricing page](https://platform.kimi.ai/).
- [Jev Ultrafast](../../projects/tools/jev-ultrafast.md) is source-mentioned for browser choices. [Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) is a JevList suggestion for inbox questions. Neither project claims to be the article author's recommended fraud implementation.
