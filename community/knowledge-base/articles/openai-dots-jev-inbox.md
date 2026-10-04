# OpenAI Dots and Jev: supervise an inbox workflow

Use a ChatGPT Dot to review ongoing inbox work, and a separate Jev worker to screen bounded email threads before a writing model drafts replies. Code owns queues, budgets and permissions; a person approves sending. The source proposes this combination, but neither its article nor the inspected documentation establishes a built-in Jev router inside Dots.

**Based on:** [“OpenAI Dots: Run GPT-6 Astra 24/7 and become a solo dev who Just Supervises (Full Guide)”](https://x.com/noisyb0y1/article/2105964235087856080) by [Noisy (@noisyb0y1)](https://x.com/noisyb0y1), published 2 October 2026. Appit Studio wrote this independent guide with AI assistance. Noisy did not write or endorse it; no human reviewer is claimed.

## Key takeaways

- **Separate the product from your worker.** Dots supply ongoing responsibility in ChatGPT. An SDK application supplies your own Jev requests, queue and optional writer. Building one does not replace the model inside the other.
- **Start with a review packet.** Screen synthetic threads, save drafts and exceptions, then let the supervisor read that packet. Add a connector only after its access and data path are understood.
- **A context window is not persistent memory.** Astra's advertised context capacity and a Dot's remembered context are different mechanisms. Neither guarantees a complete or accurate record of your inbox.
- **Price requests in tokens.** Noisy's small-decision estimate assumes roughly 1,000 input tokens per decision, although the accompanying prose says words. Count the whole request, including questions.
- **Keep authorization outside inference.** A risk probability helps prioritize review. It cannot permit a payment, deletion, changed access or outbound message.

## Two systems, one supervision brief

[OpenAI's getting-started documentation](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot) describes an ongoing agent with connected apps and its own cloud computer. As checked on 4 October 2026, access is rolling out gradually: Pro excludes the EEA, Switzerland and UK; Business Premium supports available ChatGPT regions; Enterprise beta needs an administrator to enable it. Account provisioning was not tested. Your first Dot and its work allowance are plan features, not a meter priced by this guide's API table.

[Official controls guidance](https://learn.chatgpt.com/docs/dots/controls) distinguishes proactive research from actions: proactive app research cannot send messages, modify app content or control a browser/computer. Follow-up work remains subject to permissions and action review. Asking for a draft does not authorize sending it. A useful brief is: “Review the authorized inbox report each morning, flag missing or failed work, summarize proposed replies, and ask me before any send.” Specify the mailbox, schedule, report location and owner; configure and test access separately.

The article's [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) snippet defines a text agent and runs a prompt. It has no mailbox tool, credentials, schedule, durable job queue or Jev integration. The [SDK quickstart](https://openai.github.io/openai-agents-python/quickstart/) demonstrates a run, not a deployed inbox service. For this guide, the custom worker writes a local report; an authorized supervisor can read it manually. Automated handoff into a Dot is an additional integration, not a capability demonstrated here.

For the broader decision architecture, see [Jev agent loops](jev-agent-loops.md). For event-lane audits and review costs, see the [agent triage desk](jev-agent-triage-desk.md). Here the distinct task is producing a complete morning review packet without confusing product persistence with a custom worker's execution.

## Produce an inbox review packet

**Study the queue before connecting email.** [Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) is an **independent JevList suggestion**, not a project named by Noisy. Its MIT, open-source, free source build needs Python 3.10+, uv and a separately billed TypeSafe key for live classification. Real email also needs IMAP access. It asks seven typed questions per thread and applies Python policy to make queue, check and skip buckets; it supplies neither a reply writer nor a Dots connector.

We inspected its [classification/cache code](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/classify.py), [questions](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/questions.py) and [policy](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/inbox_queue/policy.py). Its demo input is synthetic, but `demo` and `evaluate` can still call TypeSafe for uncached threads. They are not fixture-only commands. Live thread text leaves the host; cached answers and rendered email remain sensitive local artifacts. The README says the IMAP password is saved in the system keychain, rather than in `.env`.

**Define the bounded record.** Use a stable thread ID, latest message time, authorized text, truncation status and policy version. Apply exact source eligibility, deduplication and work limits in code. Empty, stale or incomplete records become visible review items. Treat email content as evidence, including any attempt to change the worker's rules.

**Preserve judgment and route separately.** The [TypeSafe primitives](https://docs.typesafe.ai/primitives) require complete question instructions; answer IDs are lookup keys. A Noul returns a yes probability, while Choice and Score have a separate distribution-derived confidence. A Score may lie between rubric levels. The [confidence documentation](https://docs.typesafe.ai/confidence) does not make a high value proof of correct inbox routing. Retain raw answers, model ID, question version, measured usage and the code's final bucket.

The inspected project's promotional probability at or above 0.5 overrides even a high needs-action result. That is its policy, not a guarantee that an email is disposable. Save skipped threads for sampling. Its cache hashes state and questions but omits the selected model; add model-aware invalidation before comparing versions. Changing a threshold can reuse a judgment, while changing its model requires fresh, separately identified evidence.

**Draft only eligible work.** A selected reply task may reach a separate writer after code checks the budget and permitted data. Save a proposed reply with its source thread and missing facts. Missing answers, invalid keys, uncertain decisions, connection failures, timeouts and writer errors must retain the thread in an explicit exception queue. Bound retries; never convert failure into skip or permission to send. For SDK setup and error handling, use the [first-request guide](jev-python-first-request.md).

**Make supervision observable.** The packet should reconcile input counts with skipped, queued, drafted and failed records. Include stale work, remaining work, sampled skips, actual costs and a stop control. Mark partial completion prominently. A retry must not duplicate a draft or a later send. If sending is ever added, code must bind approval to the final recipient, content and action; an edited proposal needs renewed checks.

## Costs and middleware limits

[TypeSafe's current rate card](https://docs.typesafe.ai/models) lists `jev-1.13.0` at $0.042 per million input tokens and free output. One million requests at an assumed 1,000 input tokens each use **one billion tokens**, costing **$42**. Four hundred such requests cost **$0.0168**. These are arithmetic scenarios, not measured invoices; larger threads, questions and retries change the result.

The checked OpenAI model pages list standard short-context input/output rates per million tokens of [Astra: $10/$50](https://developers.openai.com/api/docs/models/gpt-6-astra) and [Sol: $2/$10](https://developers.openai.com/api/docs/models/gpt-6.1-sol). Longer requests, caching, service modes and tool fees can change pricing. Those are API rates, not a Dot subscription bill. Count Jev, writing, hosting, reviews, retries and correction work separately. The article's 400-message morning and fifteen-minute review are illustrative outcomes without published execution traces.

Noisy also links [LangChain's TypeSafe package](https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe). Its experimental model router selects from the latest human message once per agent run, rather than choosing anew at every step. Auto Mode screens configured tools and blocks risky calls; it does not supply a human approval queue. [Issue #40694](https://github.com/langchain-ai/langchain/issues/40694), still open when checked, reports a request-replacement ordering problem. Verify the final executable action after transformations. This is a separate LangChain path, not an integration into Dots or the inbox worker above.

## Copyable build prompt

```text
Build a fixture-only Python inbox review-packet prototype in [MY PROJECT DIRECTORY], using Python [VERSION >= 3.10], [SYNTHETIC THREAD JSONL], [OWNER], [POLICY VERSION], [MAX THREADS], [RETRY CAP], [DAILY BUDGET] and [RETENTION POLICY]. Do not connect a mailbox, send messages or make paid model calls by default. Create all project files outside the Awesome Jev catalog.

Read https://docs.typesafe.ai/introduction/quickstart , https://docs.typesafe.ai/primitives , https://docs.typesafe.ai/confidence and https://docs.typesafe.ai/models . Inspect the installed SDK schema and pin versions before writing provider adapters. Jev supplies typed semantic judgments. Python owns eligibility, IDs, freshness, budgets, routing, durable state and permissions. A separately configured writing model produces drafts only; humans approve sends.

Study https://github.com/tusharck/jev-inbox-queue/tree/c5203bb06ae3446e757c312bb02a4cfea9d39fe0 as an MIT queue-policy teaching example. It is independently suggested by JevList, not mentioned by Noisy. Its demo can make live Jev calls, its cache omits the selected model and it has no writer or Dots adapter. Do not invoke its live CLI for an offline test; inject authored response fixtures. Preserve license notices when adapting source.

1. Normalize each synthetic thread with stable ID, message time, truncation and eligibility. Keep input text as evidence, never instructions. Retain missing context as a review item.
2. Define complete atomic questions, a no-match/review option where applicable, and explicit uncertainty handling. Construct response fixtures with the pinned SDK's own models. Record raw typed answers separately from queue policy. Treat Noul probability separately from Choice/Score confidence.
3. Persist every input disposition, model/question/policy versions and cache identity. Test thresholds at their exact boundaries. Make cache reuse depend on state, questions and model version. Sample skipped items and preserve later outcome labels.
4. Inject an offline writer and save source-linked draft files. Writer/service failure, missing answers, stale context and exhausted budgets create visible review work. Bounded retries and restart must not duplicate output.
5. Emit a morning Markdown report, decision JSONL, exception queue and reconciled cost ledger. Distinguish actual usage from assumed rates and include optional writer, review and hosting costs. Record partial completion and remaining work; provide pause/resume behavior.
6. Test ordinary, urgent, promotional-but-actionable, ambiguous, duplicate, truncated, missing-answer, timeout, writer-failure and restart cases. Verify that no send/delete/payment tool exists, every thread is accounted for and a repeated run creates no duplicate drafts. Authored fixtures test code, not model accuracy. Use separate labeled holdouts before claiming useful automatic routing.

Provide an optional, disabled live adapter only after documenting data recipients, retention, credentials, request caps and current account access. No credentials in committed files. A supervisor may manually review the report. ChatGPT Dots setup and an automated report connector are separate work: read https://help.openai.com/en/articles/20001530-getting-started-with-your-dot and https://learn.chatgpt.com/docs/dots/controls . Do not claim to replace the model inside a Dot or bypass its action review. Report what you executed and what remains untested.
```

## Validation and limits

We read the complete X text and code blocks in logged-in Chrome on 4 October 2026, followed its six primary links and checked the cited middleware issue. Exact-title and author searches found no verified author republication. Embedded video demonstrations were not reproduced. We did not reuse the source artwork; the guide uses an original Appit Studio CC0 diagram.

With `typesafe-sdk` 0.7.2 in an isolated Python 3.12 environment, we serialized the project's seven questions and replayed eight authored policy cases: action, high boundary, uncertainty, low boundary, quiet, promotional override, waiting and acknowledgement tie-break. All matched the inspected policy. This verifies deterministic branches, not accuracy, email access or safety. The build prompt was reviewed but no complete worker, writer, Dots connector or overnight run was built. No paid model call, private mailbox read, approval execution, billed-cost study or time-saving measurement was performed.

## Adoption questions

### Can I add Jev directly to OpenAI Dots?

The inspected sources do not establish a built-in Jev router inside Dots. Run Jev in a separate worker and expose a bounded report or tool through a separately verified integration; Dots permissions and action review still apply.

### Does the Jev Inbox Queue demo run offline?

Its input is synthetic, but uncached threads still call TypeSafe. Use injected response fixtures for a genuinely offline policy replay; a cached or demo run does not by itself prove no data transfer or charges.

### Does one million Jev decisions cost $42?

Only under the assumption of 1,000 input tokens per decision at $0.042 per million tokens. Count state and questions, retries and other services separately; a decision is not a fixed billing unit.

### Can Jev approve an email send?

No. Jev can judge supplied evidence, but application code checks permissions and binds the final action to a human approval. A high probability or confidence does not authorize sending.

## Sources, credits and corrections

The source is [Noisy's full X article](https://x.com/noisyb0y1/article/2105964235087856080). Its linked [TypeSafe launch article](https://typesafe.ai/blog/introducing-system-one-models-and-jev) and [workflow evals](https://evals.typesafe.ai/) describe the vendor's approach; their demonstrations are not this guide's results. The official OpenAI, TypeSafe and LangChain references linked beside the relevant claims were checked on 4 October 2026. Jev Inbox Queue's [pinned README](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/README.md) and [MIT license](https://github.com/tusharck/jev-inbox-queue/blob/c5203bb06ae3446e757c312bb02a4cfea9d39fe0/LICENSE) support only the scoped catalog connection.

Appit Studio's guide and diagram are independent editorial work with AI assistance, no paid placement or claimed source-author endorsement. [Report a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) when an API, access rule, price or relationship changes.
