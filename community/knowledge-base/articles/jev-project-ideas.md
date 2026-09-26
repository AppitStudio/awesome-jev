# 10 Jev project ideas with practical starting points

If you want to build with Jev, begin with a queue of short judgments whose possible answers you can name in advance. An inbox triage prototype is a useful first project: Jev classifies each message, while your code decides whether to route it or ask for review. The ten ideas below adapt a community roundup into starting points with evidence and limits; they are not ten tested applications or a promise that each can be shipped in an afternoon.

**Based on:** [“Top 10 Jev Builds You Can Ship in an Afternoon”](https://x.com/0x_rody/article/2103165281149354256) by [rody](https://x.com/0x_rody), published 24 September 2026. This original Appit Studio guide was drafted with AI assistance. Rody did not write or endorse it, and no human reviewer is claimed.

The article collects numbers builders posted on X or GitHub via [Made with Jev](https://madewithjev.com/). Rody says explicitly that none is an independent benchmark and that prices and limits change. We read the full article and checked the linked directory, selected builder posts, official TypeSafe documentation and the catalog evidence cited below. We did not reproduce the reported runs.

## Key takeaways

- **Jev answers bounded questions.** Code supplies state and a known menu; Jev returns a Choice, Score or Noul answer. It does not write an email reply, generate SQL or approve a merge. [TypeSafe's question guide](https://docs.typesafe.ai/primitives) explains the three shapes.
- **Batch questions about the same state.** Ask several independent questions about one email or PR in one request. Extra questions add input tokens even when latency changes little; measure the full workflow rather than assuming they are free.
- **Leave an escape route.** Add `other` to a Choice when the menu may miss the right answer. Low confidence is a review signal, not proof that a high-confidence answer is correct. [Choice and Score have `confidence`; Noul does not](https://docs.typesafe.ai/confidence).
- **Keep actions in code.** Thresholds, permissions, exact arithmetic and retries belong to the application. A tool-call classifier must not replace deterministic authorization. Start in shadow mode and compare decisions with labeled examples before automating a consequential action.
- **Treat the numbers as reported examples.** Rody quotes Hassan's 100-email fraud cascade at 96/100 correct for about $0.07, and Zachi's 129 SQL rows in roughly one second for $0.0009. These are the builders' results on their inputs, not accuracy, speed or cost guarantees for yours.

## Ten builds and where to start

These are ten different jobs. The project links marked **suggested by JevList** are our editorial connections, not the article author's recommendations. A **source-mentioned** label means Rody named the project.

### 1. Triage an inbox with a review queue

Give each email a Choice for its owning team, a Noul for whether it needs a reply today, and a Score for tone. Rody cites Riley Brown's 500-email cost and Hassan's separate fraud experiment, in which uncertain cases went to a larger model. The author-reported 95% confidence cutoff belongs to that experiment, not to every inbox.

[Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) is **suggested by JevList** as a source-build example: it asks seven typed questions per thread and applies queue rules in Python. It is MIT licensed, needs Python 3.10+, `uv` and a TypeSafe key, and can optionally read Gmail through IMAP. Email text goes to TypeSafe during live calls; inference is billed separately. Its policy does not reproduce Hassan's fraud fallback or establish his 96/100 result. Use synthetic mail first.

### 2. Score posts against your own archive

Ask about the hook, specificity and whether a claim has visible proof, then compare those features with engagement in your own published posts. Rody cites Ian Nuttall's and Rob Hallam's reported runs. A score on a draft is not a prediction of future reach; split historical posts by time before evaluating whether the features help.

### 3. Filter retrieved passages for RAG

Retrieve candidates normally, then ask whether each passage actually supports the current question. Drop weak candidates before the answer model sees them, and define what happens when none survives. [The earlier JevList RAG guide](jev-use-cases.md) contains an offline-tested example. [jev-reranker](../../projects/tools/hotchpotch-jev-reranker.md) is **suggested by JevList** if your Python application already has passages: its `relevance_rerank()` filters by a configurable threshold. It is MIT licensed, requires Python 3.11+ and a TypeSafe key for live calls, sends query and passage text to TypeSafe, and raises errors that your application must handle. It cannot recover evidence your retriever never found.

### 4. Screen agent tool calls

Ask narrow questions about a proposed command before execution: does it touch secrets, write externally or conflict with the stated task? Keep file permissions, allowlists and human approval in code. The article names Vercel's `fx`, LangChain's middleware, Bouncer and Interlock, but their reported latency and spending do not validate a new gate. [The JevList LangChain guide](building-a-jev-agent-harness.md) covers a reviewable implementation and the experimental middleware's limits.

### 5. Prune stale tool output

Judge whether an older tool call and its result still matter to the current goal; protect recent and unresolved calls. [fast-jev-compaction](../../projects/tools/fast-jev-compaction.md) is **suggested by JevList** as the catalog implementation of the Tamara Tran idea Rody describes. The MIT TypeScript library keeps, truncates or drops paired call/results, with an optional Claude Code hook. It does not summarize reasoning, and its Jev state omits result bodies; live transcript material goes to TypeSafe. Rody also cites Theo's objection that edits high in history can invalidate a prompt cache and cause agents to repeat work. Start with bulky tool output, preserve the original transcript and measure total token cost.

### 6. Route coding-agent requests to models

Pick a model tier from the task and eligible model list, then record the raw answer so a bad route can be audited. Rody names [jev-router](../../projects/tools/jev-router.md) (**source-mentioned**). Its MIT Node.js proxy routes Claude Code and Codex turns, with a three-second Jev deadline and a fallback to the current tier on error. It needs an authenticated coding CLI and a TypeSafe key; both services may have separate costs. Prompt text and routing metadata go to TypeSafe, while the coding request passes through a local proxy. Its thresholds and CLI compatibility are project choices, not validated savings for your workload.

### 7. Classify rows in SQL

Use SQL to select allowed rows and columns, then ask Jev only for a semantic judgment that an exact predicate cannot express. Rody mentions both DuckDB and PostgreSQL examples. [pg-jev](../../projects/tools/pg-jev.md) is **suggested by JevList** for a PostgreSQL database you administer: it exposes `jev()` and `jev_prob()` and can cache answers. Its PostgreSQL-licensed code needs server installation privileges, PL/Python, outbound HTTPS and a TypeSafe key. A live query sends selected row data to TypeSafe and can evaluate more rows than a final `LIMIT` suggests; filter deterministically and set budgets first. It is not the same as an ordinary free local SQL function.

### 8. Tag a competitor ad library

After collecting ads lawfully, classify each creative's hook, offer and call to action, then compare the ad promise with the landing page. Rody quotes Matthew Berman's 724-ad and maxfusion's 1,891-ad figures. The article does not give a public, inspectable pipeline for these runs. Treat the numbers as leads for a small labeled pilot, and preserve the source ad and landing-page text with each verdict.

### 9. Check citations in a draft

Pass one claim with the exact passage it cites. Ask whether that passage supports, contradicts or fails to establish the claim; have a person read the pair before publishing. A whole page can contain support somewhere other than the cited lines. [TypeSafe's citation-check cookbook](https://docs.typesafe.ai/cookbooks/citation_check) is a primary reference. Rody's editorial speed figure is a reported run, not a substitute for human fact-checking.

### 10. Label pull requests for review

Ask about scope mismatch, sensitive files and risk, then add a label or select a reviewer. Rody names DiffJury and a GitHub Action; the catalog's [jev-pr-judge](../../projects/tools/jev-pr-judge.md) is a **JevList suggestion**, a distinct MIT TypeScript app and Action with code-owned policy. PR text and selected diff evidence go to TypeSafe on live runs. It can post a sticky comment and can be configured to fail a job, so begin with labels only and compare judgments with human reviews before making it a merge gate.

## Build an inbox triage prototype

Use the [official Python SDK](https://docs.typesafe.ai/sdk/python) and a small synthetic JSONL file before connecting an inbox. The state for each message should contain a stable local ID, subject and only the body excerpt needed for the decision. Ask the same three complete questions about each message in one `system_one` request: a Choice among `billing`, `technical`, `sales` and `other`; a Noul for a real reply deadline today; and a Score with `neutral`, `impatient`, `angry` levels. The article's sample questions are a starting point; rewrite criteria for your team's actual responsibilities.

Read `response.choices["owner"].choice` and `.confidence`, `response.nouls["reply_today"].noul`, and `response.scores["tone"].score`. [The SDK reference](https://docs.typesafe.ai/sdk/python/usage) shows these fields. First save raw answers and route every message to a review queue. Label at least 50 representative messages by hand, inspect errors and probability distributions, then choose your own threshold and run shadow mode before automatic routing. `other`, a missing answer, an uncertain Choice, an SDK error or an unavailable provider all leave the message for review. A Noul probability is not the Choice's confidence, and no fixed 0.5 or 0.95 cutoff is universally safe.

Expected artifacts are a local JSONL decision log with message ID, versioned model ID, raw answers and final route; an offline test using fake SDK responses for confident, uncertain, `other` and error cases; and a short comparison with the hand labels. Do not log full private email bodies. A live run requires a TypeSafe account and key, sends message text to TypeSafe and incurs input-token charges. [The model page](https://docs.typesafe.ai/models) listed `jev-1.13.0` at $0.042 per million input tokens on 26 September 2026; check it again before estimating your own bill.

## Copyable build prompt

```text
Build a local Python 3.11+ inbox-triage prototype using the official TypeSafe SDK.
Inputs I will supply: [synthetic JSONL path], [billing/technical/sales definitions], [what counts as a real deadline], [review queue output path]. Do not connect to Gmail or send live requests by default.

Read https://docs.typesafe.ai/sdk/python, https://docs.typesafe.ai/primitives/choice, https://docs.typesafe.ai/primitives/noul, https://docs.typesafe.ai/primitives/score, https://docs.typesafe.ai/confidence and https://docs.typesafe.ai/models before naming SDK fields. Use Jev Inbox Queue only as an optional, independent example: https://github.com/tusharck/jev-inbox-queue . It does not implement the article's fraud cascade.

For each message, send a minimal subject/body excerpt as state and ask three complete questions in one call: Choice owner (billing, technical, sales, other), Noul real reply deadline today, Score tone (neutral, impatient, angry). Keep the original message ID locally. Code owns routing and permission checks. Start with every result in review; do not invent a universal confidence threshold.

Produce a small CLI, a synthetic fixture, fake-response tests for confident, uncertain, other, missing answer and provider error, and a JSONL log of message ID, versioned model, raw probabilities, chosen route and reason. Never log full private email bodies. Support an explicit --live switch with a bounded maximum request count and a TypeSafe key from the environment. On any service failure or unexpected response, preserve the message in review and report the error without losing it. Do not send, delete or archive mail.

Show how to label 50 representative messages, compare decisions against those labels, choose a threshold from observed errors, and run shadow mode before routing live traffic. Report exactly which checks ran; do not claim accuracy or cost from synthetic tests.
```

## Validation and limits

This guide was checked against the full X article, the linked Made with Jev directory, selected builder posts, current TypeSafe docs and pinned catalog source files. Its recommendations are editorial matches. The repository validator checks metadata and links, and the local site check tests presentation and sync. We did not run any of the ten projects with live Jev, reproduce the article's metrics or evaluate classification accuracy on real data. The inbox prototype is a plan to build and test, not a completed integration.

## Adoption questions

### What is the easiest Jev project to build first?

Start with a synthetic inbox triage queue. A fixed team menu, a deadline question and a review fallback let you inspect every answer before connecting private mail or taking an action.

### Can every Jev project here be shipped in an afternoon?

No. The article's time claim is a prompt to prototype, not a verified delivery estimate. Database extensions, agent hooks, inbox permissions and review workflows may require substantially more setup and evaluation.

### Does a high confidence score make an automatic action safe?

No. Confidence measures how concentrated a Choice or Score answer is, not whether the answer is correct. Test the decision against labeled cases, keep deterministic rules in code and route uncertain or consequential cases to review.

### How much will these projects cost to run?

Cost depends on input tokens, request volume, retries and any fallback model or human review. TypeSafe listed Jev 1.13 at $0.042 per million input tokens on 26 September 2026, with free output tokens; the article's project figures are their builders' reports, not your forecast.

## Sources, credits and corrections

Rody's [full X article](https://x.com/0x_rody/article/2103165281149354256) and its linked [Made with Jev directory](https://madewithjev.com/) are the source trail. The directory links to the builders' original posts; it is not an independent benchmark. We found no author republication of this article during this review. Official [TypeSafe SDK](https://docs.typesafe.ai/sdk/python), [confidence](https://docs.typesafe.ai/confidence) and [model](https://docs.typesafe.ai/models) pages support the API and pricing details. Appit Studio wrote this guide with AI assistance; linked projects were independently curated where marked. Report corrections through an [Awesome Jev issue](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml).
