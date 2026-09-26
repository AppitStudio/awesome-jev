# Jev setup guide: batch questions to cut API costs

Jev's API bill depends less on its price than on how you shape each request. Ask every question you might need about one state in a single call, send only the fields those questions read, and pin the model version. Then route on the answer and its confidence in your own code. This guide sets up a support-ticket triage that way in Python and shows how to check a request's size and cost before you send it.

**Based on:** [“The Jev Setup Guide: How to Get Maximum Quality for Minimum Cost (Exact Config Inside)”](https://x.com/zodchiii/article/2101243146596384854) by [darkzodchi](https://x.com/zodchiii), published 19 September 2026. This is an original Appit Studio guide, drafted with AI assistance. darkzodchi did not write or endorse this guide. No human reviewer is claimed.

The article is a setup checklist for developers who have just gained access to Jev. It argues that at $0.042 per million input tokens, you lose money through architecture rather than the price sheet. It covers five practices: batching questions, confidence tiers, trimming state, pinning versions and logging what answered. It then summarizes the failure modes TypeSafe publishes for Jev 1.13. Most of its examples adapt TypeSafe's own documentation, which it credits. The article's figures come from TypeSafe's docs and cookbook, and its model comparison uses one other provider's list price. It also promotes the author's newsletter. We checked each technical claim against the current documentation and the Python SDK, and note below where we changed the code.

## Key takeaways

- **Input is the whole bill.** TypeSafe [lists `jev-1.13.0`](https://docs.typesafe.ai/models) at $0.042 per million input tokens, with output tokens free (checked 26 September 2026). So the cost of a decision is the size of the request you send.
- **One call per state, not one call per question.** Every question in a request is [evaluated in parallel against the same state](https://docs.typesafe.ai/concepts/state), and the state is sent once. TypeSafe's [parallel-questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions) measured one batched call as 12.2x cheaper and 10.0x faster than 13 single-question calls. That was over a 54,000-character article on `jev-1.12`. The saving grows with state size and question count, so a short ticket with three questions saves far less (see "What it costs" below).
- **Trim the state in code.** TypeSafe's [Jev 1.13 jaggedness page](https://docs.typesafe.ai/model-jaggedness/jev-1.13) says irrelevant detail lowers accuracy. It also costs tokens on every call. Send the fields your questions read and nothing else.
- **Confidence decides whether to act, not whether you are right.** [Choice and Score answers](https://docs.typesafe.ai/confidence) carry a confidence from 0 to 1; a Noul answer carries only its probability. Gate low-stakes actions lower and destructive ones higher. A confident answer still says nothing about whether a side effect happened.
- **Pin the version and log what answered.** The `jev-latest` alias [moves when a new release ships](https://docs.typesafe.ai/models). Thresholds tuned on one version need re-checking on the next, so request `jev-1.13.0` and log `response.model` and `response.usage` on every call.
- **Keep arithmetic, counting, dates and text generation out of Jev.** The jaggedness page lists them as weak spots. Do them in code, or with a generative model for text.

## Set up a cost-efficient ticket triage

The primary path uses the official [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python) (`typesafe-sdk`, version 0.7.1 when we checked). The input is a support ticket; the output is a queue name. The questions follow the article's example, which adapts TypeSafe's [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) page.

1. **Get access.** Create an API key in the [TypeSafe console](https://console.typesafe.ai/) and set `TYPESAFE_API_KEY` in your environment, not in source. Create a Python 3.10+ virtual environment (the SDK's minimum) and install `typesafe-sdk`.
2. **Decide the queues first.** Write down what each outcome means and which actions follow it (assigning, paging, replying), and keep those actions in ordinary code.
3. **Build a small state.** Keep the subject and the customer's latest message. Drop quoted history, signatures, headers, IDs and anything no question reads.
4. **Ask every question in one request.** Include the speculative ones. If a ticket turns out to be a feature request, the severity answer costs a few tokens and your code ignores it. Question IDs are keys for your code and are [not sent to the model](https://docs.typesafe.ai/primitives), so write the complete question in `instructions`.
5. **Route in code.** Check the category and its confidence first, then read only the answers that matter for that category.

```python
import json
import logging

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient, TypeSafeError

MODEL = "jev-1.13.0"
log = logging.getLogger("triage")

QUESTIONS = {
    "category": Choice(
        instructions="Based on the subject and latest_message, which team should handle this support ticket?",
        criteria={
            "bug_report": "Something is broken or producing errors.",
            "billing": "Charges, invoices, refunds or subscriptions.",
            "feature_request": "The customer asks for functionality that does not exist yet.",
            "account": "Login, permissions, profile or security.",
            "other": "Anything that fits none of the teams above.",
        },
    ),
    "bug_severity": Score(
        instructions="If latest_message reports a problem, how badly does it block the customer?",
        criteria=[
            "Cosmetic; nothing stops working.",
            "A feature is broken or degraded, but a workaround exists.",
            "Blocking; no workaround.",
        ],
    ),
    "refund_requested": Noul(
        instructions="Does latest_message explicitly ask for a refund or a credit?"
    ),
}


def build_state(ticket: dict) -> dict:
    return {
        "subject": ticket["subject"],
        "latest_message": ticket["latest_message"],
    }


def triage(ticket_id: str, ticket: dict, client: TypeSafeClient) -> str:
    try:
        response = client.system_one(build_state(ticket), QUESTIONS)
    except TypeSafeError:
        return "human_review"
    log.info(json.dumps({
        "ticket": ticket_id,
        "model": response.model,
        "input_tokens": response.usage.input_tokens,
        "answers": {key: answer.model_dump() for key, answer in response.answers.items()},
    }))
    category = response.choices["category"]
    if category.choice == "other" or category.confidence < 0.5:
        return "human_review"
    if category.choice == "bug_report":
        severity = response.scores["bug_severity"]
        if severity.score >= 1.5 and severity.confidence >= 0.8:
            return "engineering_now"
        return "bug_backlog"
    if category.choice == "billing":
        if response.nouls["refund_requested"].noul >= 0.7:
            return "billing_refund"
        return "billing"
    if category.choice == "feature_request":
        return "product_backlog"
    return "account_support"
```

Create the client once with `TypeSafeClient(model=MODEL)` and pass it in. The SDK retries rate-limited requests with backoff by default. When a call still fails, the ticket goes to a person instead of an automatic queue.

**What we changed from the article's code.** The article's field names match SDK 0.7.1, so its calls work as written. We made four changes:

- **Added an `other` option.** Without one, Jev must pick one of the four teams even when none fits, and confidence alone may not catch that. TypeSafe's [Choice documentation](https://docs.typesafe.ai/primitives/choice) recommends an escape option when the list might not cover every input.
- **Lowered the severity check to 1.5.** A Score is a probability-weighted position between levels, so on a three-level scale the article's `sev.score >= 2` fires only when nearly all the probability sits on "blocking". A ticket scored 1.9 at confidence 0.85 went to the backlog under the article's rule. Treat 1.5 as a placeholder too.
- **Gave every category an outcome.** In the article's snippet, a billing ticket without a refund request fell through with no route.
- **Named the state fields.** Each question now names the field it reads, and the `frustration` question the article included is dropped because no route used it.

**Expected result:** clear tickets land in a team queue, blocking bugs reach engineering, and unclear tickets, `other` and failed calls reach a person. This design target was checked with fake responses (see "Validation and limits"), not measured on real tickets.

### Check size and cost before calling

Jev has a [64,000-token budget per request](https://docs.typesafe.ai/models), and the state plus the longest single question must fit in 32,000. [jevtok](../../projects/tools/jevtok.md) is **independently suggested by JevList**; darkzodchi doesn't mention it. It is an MIT Python package that reproduces Jev's input tokenizer offline. Its `estimate_request_tokens(state, questions)` predicts the `input_tokens` the API will bill and raises an error before a request would exceed the limit. Run it in tests or a pre-flight check, and compare its estimates with `response.usage` from real calls. Its author verified it against recorded usage for `jev-1.13`. Re-check it if TypeSafe changes the tokenizer. Counting runs locally and sends nothing to TypeSafe.

### Lint the request before paying for it

[wellposed](../../projects/tools/wellposed.md) is also **independently suggested by JevList**. The MIT npm package lints a Jev request JSON offline for known structural problems. It checks for a missing model, a Choice with no escape option, state fields no question mentions, and a request with only one question. We ran it at the pinned commit on the article's category question: it flagged the missing escape option and the single-question request. The triage request above passes with no findings. Its rules are heuristics aligned with TypeSafe's docs, not proof that a question is well written. Its optional semantic checks call TypeSafe and can incur charges.

### Study a complete router

This repository's [Support router](../../../projects/support-router/README.md) is a runnable example of the same practices: one request per ticket, a Choice with an `other` option, a model pinned to `jev-1.13.0` and a state that holds only the message. It also has a review queue for low confidence and a summary of token usage and returned models. It is a **teaching example suggested by JevList**, not something the article names. Its offline demo uses authored fixtures, and live runs are capped at 50 requests unless you raise the limit.

### Tune thresholds and keep the jagged edges in code

The article's 0.5 floor and its note that destructive actions wait for 0.9 echo TypeSafe's [confidence guide](https://docs.typesafe.ai/confidence). They are starting points. Collect real tickets with the queue a person chose, then set each threshold from how accuracy changes with confidence. Our guide to [replacing LLM decision calls with a Jev gate](jev-decision-gate.md) walks through that shadow-mode rollout.

The article's summary of the jaggedness page is accurate as of the page's 17 September 2026 review. In short:

- Write the exact condition, because Jev reads literally.
- Count, calculate and compare dates in code.
- Filter the state.
- Test injected instructions in the state before you ship.
- Don't expect a Noul and a yes/no Choice to agree.
- Use a generative model when you need text.

A Noul of 0.5 means yes and no are equally likely, not "medium". Questions in one request can't read each other's answers, so a decision that needs a new search result belongs in a second request.

### What it costs

The article's comparison puts 1,000 decisions over a 10,000-token state at $0.42 on Jev, against $100 on a frontier model priced at $10 per million input tokens. The Jev half is simple arithmetic from TypeSafe's list price. The other half is the author's pricing claim, which we did not check.

For a short ticket the numbers are smaller, and so is the batching saving. jevtok estimated the triage request above at 547 input tokens as one call and 1,199 as three single-question calls, because each request carries a fixed overhead plus the state. That is about $0.023 against $0.050 per 1,000 tickets. With 25 quoted replies and a signature left in the state, the same estimates rose to 1,726 and 4,736 tokens. These are offline estimates from jevtok's model of the API, not billed usage. Retries, human reviews and wrong routes cost far more than the tokens, so measure cost per resolved ticket.

## Copyable build prompt

Copy the following into your coding agent and fill the bracketed inputs. Review the questions, queues and thresholds before any live call.

```text
Build a cost-efficient Jev triage step for [WHAT YOU ARE TRIAGING, e.g. support tickets] in [YOUR PROJECT]. Use the official TypeSafe Python SDK (typesafe-sdk) and read the current docs before writing calls: https://docs.typesafe.ai/sdk/python, https://docs.typesafe.ai/primitives, https://docs.typesafe.ai/patterns/fan-out, https://docs.typesafe.ai/confidence, https://docs.typesafe.ai/models and https://docs.typesafe.ai/model-jaggedness/jev-1.13. Check the installed SDK version and use its actual field names. If the TypeSafe agent skill is installed, use it.

Inputs I will supply: a sample of [N] records as JSONL, the fields that exist on each record [FIELD NAMES], the outcomes and what each means [QUEUE NAMES AND DEFINITIONS], and which outcomes trigger irreversible or customer-visible actions [LIST].

Steps:
1. Write a pure build_state function that keeps only the fields the questions read. Drop history, signatures, IDs and anything else no question needs. No model call.
2. Define every independent question in one QUESTIONS dict in its own module, including speculative ones. Write complete instructions that name the state field each question reads; question IDs are not seen by the model. Give every Choice an "other" option.
3. Send all questions in one system_one request with the model pinned to jev-1.13.0 (or the version I name). Never call once per question.
4. Route in code with named threshold constants: "other" or low category confidence goes to a person, and irreversible outcomes need a higher confidence than reversible ones. Remember a Score is a weighted position between levels, and a Noul has no confidence field. Treat all thresholds as placeholders.
5. Keep counting, arithmetic and date comparison in code. Do not ask Jev to generate text.
6. On any SDK error, timeout or missing answer, route to a person. Never default to an automatic action.
7. Log the record ID, response.model, response.usage, every raw answer and the final route as separate fields.

Deliver: the module, a pinned dependency list, and tests that use fake SystemOneResponse objects for every route, low confidence, "other", a Score between levels and a service failure. Default commands must make no network calls. Add a pre-flight check that estimates each request's input tokens offline (for example with jevtok) and fails before a request would exceed the context limit. Add an opt-in script that runs the triage over my [N] labelled records, stores every raw answer and prints accuracy by confidence band plus total input tokens, and warn me that it sends those records to TypeSafe and costs money. State clearly that the tests prove routing and cost wiring, not model accuracy.
```

## Validation and limits

On 26 September 2026 we read the full article in a logged-in browser session, including its code blocks and six images, and its identical Substack republication. We checked each claim against TypeSafe's models, confidence, fan-out, Choice, Score, API, agent-skill and jaggedness pages, and the parallel-questions cookbook. The price, rate limits, context budget, 255-option and ten-level limits, the 12.2x and 10.0x cookbook figures and the jaggedness list all matched. We installed `typesafe-sdk` 0.7.1 in a scratch environment and ran the triage above with **fake responses**, making no API call. A blocking bug, a bug split between levels, low category confidence, `other`, a refund, a billing question without a refund, a feature request, an account issue and a rate-limit error all produced the intended routes. The same check showed the article's `score >= 2` rule sending a 1.9 severity to the backlog. We ran jevtok (commit `698c53b`) and wellposed (commit `86e6f8c`) offline on the request, and the Support router's offline demo (three automatic suggestions, three reviews, zero errors).

We did **not** call TypeSafe or measure latency, billed cost or accuracy. The token figures are jevtok's estimates. The frontier-model price is the article's claim. The guide image is an original Appit Studio diagram (CC0), not one of the article's images. Recheck pricing, rate limits, SDK field names and the jaggedness page before implementing, because TypeSafe says its rate limits can change without notice.

## Adoption questions

### Is it cheaper to ask Jev several questions in one call?

Yes. Jev bills input tokens, and a batched request sends the state and the fixed request overhead once instead of once per question. TypeSafe measured 12.2x cheaper for 13 questions over a long article; a short state with a few questions saves less.

### Should I use jev-latest or pin a version?

Pin a versioned ID such as jev-1.13.0 once you have tuned thresholds, and log the model each response reports. The jev-latest alias moves when TypeSafe ships a new release, which can change answers without a change on your side.

### How large can the Jev state be?

TypeSafe lists 64,000 tokens per request for Jev 1.13, with 32,000 for the state plus the longest single question. Stay well below that: irrelevant detail costs accuracy as well as tokens, so filter the state in code first.

### What confidence threshold should I use with Jev?

Start with 0.5 as a floor below which a person decides, and require more for destructive actions. Then set each threshold from your own labelled cases. Confidence exists only on Choice and Score answers and says nothing about whether an action succeeded.

### What should I not ask Jev to do?

Don't ask it to count, calculate, compare dates or write text. TypeSafe's jaggedness page lists those as weak spots for Jev 1.13, along with very literal reading, large irrelevant state and instructions injected into the state.

## Sources, credits and corrections

Original article: [darkzodchi, “The Jev Setup Guide: How to Get Maximum Quality for Minimum Cost (Exact Config Inside)”](https://x.com/zodchiii/article/2101243146596384854), published on X on 19 September 2026 and republished unchanged on the author's [Substack](https://zodchiii.substack.com/p/the-jev-setup-guide-how-to-get-maximum) on 21 September 2026. The article promotes that newsletter; this guide does not depend on it. Technical references: [models and pricing](https://docs.typesafe.ai/models), [state](https://docs.typesafe.ai/concepts/state), [question types](https://docs.typesafe.ai/primitives), [confidence](https://docs.typesafe.ai/confidence), [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out), [parallel-questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions), [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13), the [TypeSafe agent skill](https://docs.typesafe.ai/agent-skill), the [Python SDK changelog](https://docs.typesafe.ai/sdk/python/changelog) and the linked project pages. The guide was written by Appit Studio with AI assistance; no paid placement, affiliate link or human review is claimed. [Propose a correction](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml) for a stale API, mismatched project or attribution error.
