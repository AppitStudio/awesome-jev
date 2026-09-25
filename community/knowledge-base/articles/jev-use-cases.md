# Jev use cases: nine patterns developers are building

Jev is TypeSafe's System One model. It never writes prose. It answers typed questions about state you send: pick one option, place something on a scale, or say yes or no, each with probabilities. Developers use it for the many small judgments inside a program. It picks a browser agent's next click, drops stale tool output from an agent's context, screens shell commands and routes requests between models. It also filters retrieved passages, triages email and labels rows. Below are nine patterns from Matt Van Horn's community roundup, what stands behind each one, an open project to start from, and an offline-tested recipe for the RAG filter.

**Based on:** [“WTF Is Jev? 9 Things People Are Already Building With It”](https://x.com/mvanhorn/article/2100784142850097482) by [Matt Van Horn](https://x.com/mvanhorn), published 18 September 2026. This is an original Appit Studio guide, drafted with AI assistance. Matt Van Horn did not write or endorse this guide. No human reviewer is claimed.

Van Horn's article is a research roundup rather than a build log. He compiled it with /last30days, an open-source research tool he makes, across X, YouTube, Hacker News, Reddit and other sites. He then checked the popular posts by hand and ranked the workflows people were shipping. He says plainly that he did not run them. The speed, cost and engagement figures below come from the posts he cites, as displayed when he pulled them. Treat them as their authors' claims unless we say otherwise.

## Key takeaways

- **Jev decides; it does not generate.** A request carries your state and named questions of three types. [Choice](https://docs.typesafe.ai/primitives/choice) picks one of up to 255 options. Score places the state on a scale you describe. Noul answers yes or no as a probability between 0 and 1.
- **Not every answer has a confidence value.** The article says every answer carries probabilities and a confidence score. TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) and `typesafe-sdk` 0.7.1 both say Choice and Score answers do, and a Noul answer carries only its probability. For a Noul, the distance from 0.5 is your uncertainty signal.
- **Give it candidates; compute facts in code.** The strongest examples never ask Jev to invent an option. Code builds the list from the page, the retriever, the tool log or the inbox, and Jev picks or filters. Arithmetic, parsing and permissions stay in code.
- **Ask many questions in one request.** Questions about the same state are answered together, so five checks cost about five questions' worth of input tokens and one round trip. Output tokens are free.
- **The price is measured; the multiples are claims.** TypeSafe lists `jev-1.13.0` at $0.042 per million input tokens with free output ([checked 25 September 2026](https://docs.typesafe.ai/models)). The 193.6x-faster and 444.6x-cheaper headline comes from TypeSafe's own workflow benchmarks. Independent comparisons in the article came out smaller: about 25 times faster in one test and about 7 times end to end in another.
- **A valid answer can still be wrong.** Jev cannot return an option you didn't define, but it can confidently pick the wrong one. In the article's most careful comparison, Jev caught six of seven planted defects where a frontier model caught all seven. Decide in code what happens on low confidence, disagreement and service errors.

## How a Jev call works

You send `state` (a string, a JSON object or an array) and a `questions` object to `POST https://api.typesafe.ai/v1/systemone`, or call `system_one` in an SDK. Question names are keys for your code and [are not shown to the model](https://docs.typesafe.ai/primitives), so each question's `instructions` must stand on its own.

| Question type | Use it to | What comes back |
| --- | --- | --- |
| Choice | Pick one of a known set: a route, a department, the next action | The chosen option, a probability for every option and a confidence value |
| Score | Place the state on an ordered scale you describe | A score, probabilities for each level and a confidence value |
| Noul | Answer one yes-or-no question | A single probability of yes |

A request can hold 64,000 tokens, of which 32,000 can be state plus the longest question. The `jev-latest` alias [moves to new releases](https://docs.typesafe.ai/models), so pin a version such as `jev-1.13.0` once you tune thresholds against it. The article reports Jev arriving on the Vercel AI Gateway, Cloudflare AI Gateway and, in beta, OpenRouter within the launch week; we did not test those routes.

## Nine patterns and where to start

Each pattern below says who reported it, and links the catalog project that shows it best. Projects are marked **source-mentioned** when the article names them and **suggested by JevList** when we chose them. Our suggestions are not the article author's endorsements.

### 1. A browser agent that picks the next action

Code lists the controls it can see on the page, and Jev picks the operation and target for the next step. A small text model runs only when a field needs typing. Browser Use founder Gregor Zunic reported a flight search in 7 seconds for $0.0039.

Start with [Jev Ultrafast](../../projects/tools/jev-ultrafast.md) (**source-mentioned**). It is Browser Use's MIT-licensed experimental Python agent. Each step asks several Choice questions in one request, and code uses only the target that matches the chosen operation. It applies no confidence threshold. Live runs need a TypeSafe key, a separate text-model key and Chrome through Browser Harness, and can incur charges. It finds flights without booking them and doesn't handle frames, shadow DOM, canvas or uploads.

### 2. Instant compaction of an agent's context

Instead of summarizing a long coding-agent session, score each tool call for whether it still matters and drop the rest. Tamara Tran proposed it and published the code the same day. Alex Volkov reported cutting a Claude session from nearly 1 million tokens to 86,000 in about a second.

Start with [fast-jev-compaction](../../projects/tools/fast-jev-compaction.md) (**source-mentioned**), an MIT TypeScript library with an optional Claude Code hook. It asks two Noul questions per tool call and result pair, then keeps the pair, shortens the result or drops both at a 0.5 threshold. Jev sees each result's status and length, not its body. Library errors throw, so keep the original transcript. The Claude Code adapter falls back to the host's own summary on errors. The article gives a one-line install prompt for Claude Code; neither we nor the catalog review tested that install.

### 3. A safety reviewer for agent commands

Before an agent in auto mode runs a shell command, a classifier asks whether it should. Vercel CEO Guillermo Rauch wrote that in Vercel's `fx` tool Jev was up to 18 times faster at p95 and more accurate than the model doing the job. LangChain then released `AutoModeMiddleware` in `langchain-typesafe`. Our guide [Guard LangChain agent tool calls with Jev and human approval](building-a-jev-agent-harness.md) covers it. LangChain marks that middleware experimental, and its auto mode refuses risky calls without asking a person.

For an open command gate, see [typesafe-agent-gates](../../projects/tools/typesafe-agent-gates.md) (**suggested by JevList**). This Apache-2.0 LangChain and Deep Agents middleware asks four Noul questions about each `execute` command. By default it holds commands when TypeSafe is unreachable instead of running them. It depends on the alpha `langchain-typesafe` package, and its tests use fake classifiers. Whatever the classifier says, keep deterministic permission checks in front of anything destructive.

### 4. Model routing as middleware

Jev picks which model handles each request, and the probabilities stay in agent state for auditing. The article calls this the most-cited job for Jev in its research and quotes LangChain's `ModelRouterMiddleware` example. Note that it chooses one model for the whole run from the latest user message, not one per step. [The same LangChain guide](building-a-jev-agent-harness.md) discusses this router and links a coding-agent alternative.

### 5. RAG precision: filter retrieved passages

Keep your retriever as it is. Ask one Noul per retrieved passage, "does this contain what the answer needs?", and drop the ones that fail. Kush Bhuwalka proposed it in a post; the article's code for it is the author's own untested draft. This is the pattern we build and test in the next section.

### 6. Real-time decision loops

Some loops decide several times a second, which rules out a frontier model. Wuyang Zhou paired Jev for quick reactions with a larger model planning ahead in Minecraft. Nader Dabit built a launcher that re-ranks results on every keystroke in about 100 milliseconds. TypeSafe's own launch demo played Doom. Two video explainers estimated its roughly ten decisions a second at about $7 an hour. The shared design has a fast model that reacts and a slow model that plans. Code generates the legal actions and supplies a fallback when an answer arrives late.

### 7. Email triage in batches

Send each message as state and ask several questions at once: which team, how frustrated, how urgent. TypeSafe's Python quickstart is already this pipeline. The article cites a YouTube creator who ran 1,500 exported emails in batches of 100 across 8 workers.

For a working inbox tool, see [Jev Inbox Queue](../../projects/apps/jev-inbox-queue.md) (**suggested by JevList**). This MIT Python app asks seven typed questions per email thread. A local policy file then sorts threads into “To do”, “Check these” and “Filtered out”, so you can change thresholds without another API call. It needs a TypeSafe key and, optionally, a Gmail IMAP app password. The catalog review inspected its source but did not run it live.

### 8. Map-reduce over documents and rows

Apply one set of questions to every document or row. Mike Taylor, head of evals at Every, [reported](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) 777 judgments (27 articles plus 10 AI-styled rewrites, 21 questions each) in under 0.7 seconds for about a quarter of a cent. TypeSafe lists this as “AI map-reduce over big data” on its [use-case map](https://docs.typesafe.ai/concepts/use-case-map).

For spreadsheets, see [jev-table](../../projects/tools/jev-table.md) (**suggested by JevList**). This Apache-2.0 CLI adds Jev answer columns to CSV or JSONL rows from a YAML spec. Low-confidence and `unknown` answers go to a review column instead of being accepted, and a dry run estimates cost without calling the API. The catalog review ran its offline tests but no live labelling.

### 9. Local look-alikes

Within days, people rebuilt the interface on other models: Reflex runs a Qwen model with typed answers in the browser on WebGPU, and jevlike and mini-jev imitate it with trainable and local models. The article reads this as a sign that the interface is the real invention. The look-alikes also offer an escape hatch for data you can't send over the network, because the official model runs only as a hosted API.

[Jevlike](../../projects/tools/jevlike.md) (**source-mentioned**) is the one in our catalog. It is an MIT training starter for a small model that scores a changing list of options. It is **not Jev** and doesn't use TypeSafe. Its scores are not calibrated, and it truncates context to 192 bytes. It loads checkpoints with `torch.load(weights_only=False)`, which can execute code from an untrusted file. Use it to learn how option scoring works, not as a drop-in replacement.

## Build a RAG relevance filter

This recipe implements pattern 5 with the official [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python) (`typesafe-sdk` 0.7.1 when we checked). The input is the user's question and the passages your retriever returned. The output is the subset that the answer model should see, plus every probability for later calibration.

1. **Set up access.** You need a TypeSafe account and an API key from the [console](https://console.typesafe.ai/), set as `TYPESAFE_API_KEY` in the environment. Create a Python 3.12 virtual environment and install `typesafe-sdk`.
2. **Write one complete question.** Use `NoulCriteria` to describe what counts as yes and no. A passage that only shares keywords with the question should be a no.
3. **Judge each passage in its own request, concurrently.** Each request's state is the question and one passage, so a long passage can't crowd out another. A semaphore bounds the number of requests in flight; TypeSafe lists 1,200 requests per minute, and rate limits were changing with demand.
4. **Keep the policy in code.** Passages at or above `KEEP_AT` survive. If none do, return an empty list and let your application search again or say it found no support.

```python
import asyncio

from typesafe_sdk import AsyncTypeSafeClient, Noul, NoulCriteria, TypeSafeError

KEEP_AT = 0.5  # placeholder: set it from your own labelled cases
MAX_IN_FLIGHT = 8

RELEVANT = Noul(
    instructions="Does this chunk contain information needed to answer the user's question?",
    criteria=NoulCriteria(
        true="The chunk states a fact, figure or step that the answer needs.",
        false="The chunk is off-topic or only shares keywords with the question.",
    ),
)


async def judge(client, limit, question, chunk):
    async with limit:
        response = await client.system_one(
            {"question": question, "chunk": chunk},
            {"relevant": RELEVANT},
        )
    return response.nouls["relevant"].noul


async def filter_chunks(client, question, chunks):
    """Return (kept chunks, probabilities); on a service error keep every chunk."""
    limit = asyncio.Semaphore(MAX_IN_FLIGHT)
    try:
        probabilities = await asyncio.gather(
            *(judge(client, limit, question, chunk) for chunk in chunks)
        )
    except TypeSafeError:
        return list(chunks), None
    kept = [chunk for chunk, p in zip(chunks, probabilities) if p >= KEEP_AT]
    return kept, probabilities


async def main(question, chunks):
    async with AsyncTypeSafeClient(model="jev-1.13.0") as client:
        return await filter_chunks(client, question, chunks)
```

**Why a failure keeps every passage.** This filter improves precision; it is not a safety gate. If TypeSafe is unavailable, the answer model gets the retriever's original list and behaves as it did before you added Jev. A command gate like pattern 3 should do the opposite and hold the action. Log the `None` probabilities so failures are visible.

**Calibrate before you trust the threshold.** Collect a few hundred question and passage pairs, label whether each passage was actually needed, and store the raw probabilities. Choose `KEEP_AT` from the precision and recall you need, and consider sending passages near 0.5 to a stricter check. Pin the model version once the threshold depends on it. TypeSafe's [RAG passage cookbook](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) adds further Noul questions per passage when you need more than relevance: whether it holds answer evidence, contradicts the query's premise or tries to instruct the answering system.

**Expected result:** passages the question needs survive, keyword-only matches are dropped, and an outage changes nothing for the reader. That is a design target checked with fake responses, not a measured accuracy.

**What we changed from the article's draft.** Its code runs unchanged against SDK 0.7.1. It sends one request at a time and has no error handling, so we added concurrency, a bounded request count, a failure path and outcome criteria.

**Cost.** A 400-token passage plus the question is roughly 500 input tokens. At the listed price, 20 passages per query cost about $0.00042, or about $4.20 per 10,000 queries. That is arithmetic, not a benchmark, and repeated state in each request is billed each time.

If you would rather install a library than write this, [jev-reranker by hotchpotch](../../projects/tools/hotchpotch-jev-reranker.md) is an **alternative suggested by JevList**. The MIT Python package's `relevance_rerank()` scores passages with Noul questions and drops those below its threshold, which defaults to 0.2. It returns an empty list when nothing passes. It can judge many passages per request (listwise) or one per request (pointwise), retries rate limits and server errors with backoff, and raises errors instead of scoring failures as zero. Its offline tests passed in the catalog review; live calls were not run.

## Copyable build prompt

Copy the following into your coding agent and fill in the bracketed inputs. Review the threshold and failure behavior before any live call.

```text
Add a Jev relevance filter to the retrieval step of [YOUR RAG APPLICATION] in [LANGUAGE/FRAMEWORK, default Python 3.12]. Use the official TypeSafe SDK and read the current docs before writing calls: https://docs.typesafe.ai/sdk/python, https://docs.typesafe.ai/primitives/noul, https://docs.typesafe.ai/confidence, https://docs.typesafe.ai/models and https://docs.typesafe.ai/cookbooks/classifying_rag_passages. Check the installed SDK version and use its real names (in typesafe-sdk 0.7.1 a Noul answer exposes .noul and has no confidence field).

Inputs I will supply: where the retriever returns passages [FILE/FUNCTION], the passage fields to send [TEXT FIELD, optional TITLE/SOURCE], and the maximum passages per query [N].

Steps:
1. Define one Noul question with complete instructions and NoulCriteria describing yes (the passage states something the answer needs) and no (off-topic or only shares keywords). Question names are not shown to the model.
2. For each retrieved passage, send state {"question": ..., "chunk": ...} in its own request. Run requests concurrently with a bounded semaphore [MAX IN FLIGHT, default 8] and a timeout. Pin the model version.
3. Keep passages whose probability is at or above a named KEEP_AT constant (placeholder 0.5). If none pass, return an empty list and make the answer step say it found no support, or retry the search once.
4. On any SDK error or timeout, return the retriever's original passages unchanged and log the failure. Never drop passages because the service failed.
5. Log the question, passage IDs, raw probabilities, model ID, kept IDs and any failure as separate fields.

Deliver: the filter module wired into the retrieval step, a pinned dependency list, and tests that use fake SystemOneResponse objects for mixed relevance, nothing passing, an empty input and a service error. Default commands must make no network call. Add an opt-in script that runs the filter over [NUMBER] labelled question and passage pairs I provide, stores every raw probability, and prints precision and recall at several thresholds; explain that it sends those passages to TypeSafe and costs money. State that the tests prove wiring, not model accuracy.
```

## Validation and limits

On 25 September 2026 we read the full article in a logged-in Chrome session, including its code blocks and embedded posts. We followed the repositories and pages it links to and searched for republished versions. We checked its technical claims against TypeSafe's current documentation and the installed SDK. Two corrections resulted. Noul answers carry no confidence value. And TypeSafe's guidance is to treat a confidence below 0.5 as a reason not to act automatically, with thresholds set from your own data; the article's summary said “under 0.3 to 0.5”. The article also has two internal inconsistencies, nine and eleven research runs and 31 and 39 candidate workflows, which don't affect the patterns.

We installed `typesafe-sdk` 0.7.1 in a scratch environment and ran the filter above with **fake responses built from the SDK's own models**, making no API call. Mixed relevance kept exactly the passages at or above the threshold. Nothing passing returned an empty list, an empty input returned nothing, and a simulated service error returned every passage. The article's own draft also ran against the same SDK. This checks the code paths only.

We did **not** call TypeSafe or measure latency, cost or accuracy. We ran none of the seven linked projects; their descriptions come from pinned catalog reviews. We also did not reproduce any figure the article reports, including the speed, cost and benchmark numbers, the builders' results or the engagement counts. The guide image is an original Appit Studio diagram (CC0), not the article's cover. Recheck SDK names, prices and limits before implementing.

## Adoption questions

### What is Jev?

Jev is TypeSafe's System One model. Instead of writing text, it answers typed questions about data you send: it picks one of your options, scores on a scale you define, or gives a yes-or-no probability. Software uses those answers to decide what to do next.

### What can you build with Jev?

Developers use it for the small decisions inside larger systems: choosing a browser agent's next action, pruning an agent's context, screening commands, routing requests between models, filtering retrieved passages, triaging email and labelling rows in bulk. It works best when code supplies the candidates.

### Is Jev an LLM?

No. Jev does not generate prose, plan or explain. It returns structured answers with probabilities that code can threshold. Keep a language model for writing and reasoning, and use Jev for the judgments in between.

### How much does Jev cost?

TypeSafe lists Jev 1.13 at $0.042 per million input tokens, and output is free. Several questions about the same state share one request, so extra questions add only their own input tokens. Retries, human review and wrong decisions add real cost, so measure per completed task.

### Can I run Jev locally?

No. The official model is available only through TypeSafe's hosted API and the gateways that resell it. Local projects such as Reflex, jevlike and mini-jev copy the interface on other models; they are not Jev and don't match its calibration.

### How do I filter RAG results with Jev?

Ask one yes-or-no Noul question per retrieved passage, such as whether it contains information the answer needs, and keep passages above a threshold you calibrate on labelled examples. If the service fails, fall back to the retriever's original list.

## Sources, credits and corrections

Original article: [Matt Van Horn, “WTF Is Jev? 9 Things People Are Already Building With It”](https://x.com/mvanhorn/article/2100784142850097482). Van Horn built the research with [/last30days](https://x.com/slashlast30days), his own open-source project; the article promotes no paid product. We found no republication by the author; an aggregator site mirrors the X article. Primary material the article links to includes [Browser Use's Jev Ultrafast](https://github.com/browser-use/jev-ultrafast), [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction), [Reflex](https://kshetrajna12.github.io/reflex/), [jevlike](https://github.com/vinnylarouge/jevlike), [mini-jev](https://github.com/r-ms/mini-jev), Mike Taylor's [Every review](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds), and the [Hacker News launch thread](https://news.ycombinator.com/item?id=49717558). The posts it quotes by Gregor Zunic, Tamara Tran, Alex Volkov, Guillermo Rauch, Kush Bhuwalka, Wuyang Zhou and others make claims that belong to their authors. Technical references: [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python), [question types](https://docs.typesafe.ai/primitives), [Choice](https://docs.typesafe.ai/primitives/choice), [confidence](https://docs.typesafe.ai/confidence), [models and pricing](https://docs.typesafe.ai/models) and the [use-case map](https://docs.typesafe.ai/concepts/use-case-map). The guide was written by Appit Studio with AI assistance; no paid placement, affiliate link or human review is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) for a stale API, mismatched project or attribution error.
