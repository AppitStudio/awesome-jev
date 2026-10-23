# Plan the hosted Jev boundary: state, transfers, latency and fallbacks

Jev answers bounded questions about messy text, but the official model runs only as TypeSafe's hosted API. Everything you put in the `state` leaves your network, every decision pays a round trip, and an outage at the provider becomes your outage unless code decides otherwise. This guide turns that boundary into four checks before production: minimise the state, review the transfer, budget the latency, and route failures to a safe lane.

**Based on:** [“Jev: Bounded semantic judgments for messy text”](https://developers.redhat.com/articles/2026/10/20/jev-bounded-semantic-judgments-messy-text) by Maarten Vandeperre on [Red Hat Developer](https://developers.redhat.com), published **20 October 2026** and read in full on **23 October 2026**. The article uses a coffee shop to separate exact facts, semantic judgments and generated text, and closes with the hosted deployment boundary. Guide by **Appit Studio**, with AI-assisted research, drafting and offline tests; no human reviewer or legal review is recorded.

## Key takeaways

- **Exact facts stay in code; messy meaning goes to Jev; new text goes to an LLM.** The source calls these design aids, not hard boundaries, and asks you to measure against simpler options.
- **A probability is not permission.** Thresholds and actions belong to application policy, and refunds can always require a person.
- **The official Jev is hosted only.** No published weights, no container, no vLLM; calling it from OpenShift does not make it local.
- **For European teams, that means a transfer review and a latency budget** before customer data goes into the state.
- **Failure needs a lane.** Errors, timeouts and missing answers should land in review, never in the automatic path.

For the general judgment-versus-permission pattern in agents, see [the decision-layer guide](jev-decision-layer.md); for choosing between code, Jev and an LLM, see [Jev vs LLMs](jev-vs-llms.md).

## The source's model of the boundary

The article's figure gives each component one job: a generative LLM composes, a decision model judges, and application code executes. Jev receives `state` plus Choice, Noul or Score questions and returns typed answers with probabilities. The source adds practical rules for each part:

- **State is data, not instructions.** Keep it relevant, since a year of unrelated orders can distract, and preserve conflicts such as "delivered" in the database against "not received" from the customer.
- **Bound every question.** A Choice allows up to 255 options and should include `OTHER` or a review path. A Noul should define both sides when the wording is open to interpretation. A Score has 2 to 10 described levels, numbered from 0.
- **Typed does not mean true.** A Choice cannot invent an option, but it can still pick the wrong one, confidently.
- **Code owns three lanes.** High probability acts automatically on low-risk steps, a middle band asks a follow-up question, and contradictory or sensitive cases go to a person.

Then comes the deployment point this guide builds on. Your till and coffee machine stay in the shop; for each judgment, the application sends relevant state to a remote order desk and receives a typed assessment. TypeSafe's [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) says the service is currently based on the US West Coast. The source concludes that if local processing, offline operation, EU-only processing or control of the weights is mandatory, the official Jev service does not currently meet that requirement. It suggests a hybrid as one option: Jev for bounded decisions, a self-hosted LLM for generation.

## Four checks before production

### 1. Send an allowlisted, minimal state

Build the state from named fields rather than serialising whole records. In the coffee example, the judgment needs the item, status, waiting time, earlier delays and the last few messages. It does not need the customer's name, email or card details, and the order ID can stay local and be joined back to the answer afterwards. Truncate free text to a known length. Write a test that fails if a new field appears in the outgoing request, so that the boundary does not widen with every new feature.

### 2. Review the transfer with whoever owns data protection

Before personal data goes into the state, collect the documents a reviewer will ask for:

- TypeSafe's [data processing addendum](https://typesafe.ai/legal/data-processing), which provides for international transfers under the EU Standard Contractual Clauses or the UK International Data Transfer Addendum;
- the current [subprocessor list](https://trust.typesafe.ai/subprocessors);
- the [legal documentation page](https://docs.typesafe.ai/legal), which links the privacy policy's commitment not to train models on user data and offers zero data retention to enterprise customers.

Record what data categories the state contains and which lawful basis and transfer mechanism apply. This guide lists the documents; it does not assess them. If the answer is that the data cannot leave the EU, the hosted Jev service is not an option for that flow today, whatever the accuracy results.

### 3. Measure the round trip from where you run

TypeSafe's launch post notes that its published speed evaluations are generally run from laptops on the West Coast. A European deployment adds network distance, TLS setup and your own gateway. Measure p50 and p95 for a realistic request from the region and network path you will run in, during your busy hours, and set the client timeout inside the step's latency budget. Several questions can share one request, which saves round trips when they judge the same state. The [openai-decisions-vs-jev-vs-laya benchmark](../../projects/tools/openai-decisions-vs-jev-vs-laya.md), an **independent JevList suggestion** that the source does not name, shows one way to record latency with and without network alongside accuracy. Its numbers come from one run on Portuguese-language tasks and do not transfer to your setup.

### 4. Give failures a lane in code

A timeout, a provider error or a response missing the expected answer must not look like a confident "no". In this offline-tested sketch with the official Python SDK, each of those lands in review:

```python
from typesafe_sdk import Noul, NoulCriteria, TypeSafeError

MODEL = "jev-1.13.0"            # pin a dated version; re-test before moving
ALERT_AT, CLEAR_BELOW = 0.80, 0.20   # placeholders: set from your labelled examples
SENT_FIELDS = ("item", "status", "waiting_minutes", "earlier_delays")

QUESTION = Noul(
    instructions="Does this complaint meet the shop's conditions for manager review?",
    criteria=NoulCriteria(
        true="A repeated or serious service failure, or a safety or allergy concern",
        false="A one-off delay or question the counter can resolve now",
    ),
)

def assess(order, messages, client, budget_s=2.0):
    state = {k: order[k] for k in SENT_FIELDS if k in order}
    state["customer_messages"] = [m[:500] for m in messages[-3:]]
    try:
        r = client.system_one(state=state, questions={"manager_review": QUESTION},
                              model=MODEL, timeout=budget_s)
        p = r.nouls["manager_review"].noul
    except (TypeSafeError, KeyError) as e:
        return {"lane": "review", "by": "fallback", "error": type(e).__name__}
    lane = "alert_manager" if p >= ALERT_AT else "counter" if p < CLEAR_BELOW else "review"
    return {"lane": lane, "by": "jev", "p": p, "model": r.model}
```

Count `by == "fallback"` results and alert on a rise: a silent switch to review is safer than a silent switch to "counter", but it still needs someone to notice. Refunds and other money movements stay outside this function, as the source recommends. If you add a local substitute for outages or data that cannot leave, put both behind one interface and evaluate the substitute on the same examples. The [quarkus-langchain4j-jev-laya](../../projects/tools/quarkus-langchain4j-jev-laya.md) proof of concept, another **independent JevList suggestion**, shows that shape in Java with hosted Jev, local models and a stub. It has no licence file, so read it rather than copying it.

## Copyable build prompt

```text
Add a hosted Jev judgment to an existing service with an explicit
deployment boundary.

Inputs:
- Judgment: [ONE BOUNDED QUESTION, WITH TRUE/FALSE OR OPTION DEFINITIONS]
- Source records: [ORDER/TICKET SCHEMA]; fields allowed to leave the
  network: [ALLOWLIST]
- Latency budget for this step: [MS]; region the service runs in: [REGION]
- Lanes: automatic (low-risk only), follow-up/review, human
- Labelled examples: [PATH]

Read first:
- https://developers.redhat.com/articles/2026/10/20/jev-bounded-semantic-judgments-messy-text
- https://docs.typesafe.ai/primitives/noul and https://docs.typesafe.ai/models
- https://typesafe.ai/legal/data-processing and https://trust.typesafe.ai/subprocessors

Steps:
1. Build state from the allowlist only; truncate free text; keep IDs local.
   Add a test that fails if any other field is sent.
2. Pin a dated model ID. Set the client timeout inside the budget; no
   retries that would exceed it.
3. Map probabilities to lanes in code with placeholder thresholds; any
   error, timeout or missing answer goes to the review lane.
4. Offline tests with the SDK's mock transport: each lane, 5xx, timeout,
   missing answer, and the outgoing field set.
5. Script to measure p50/p95 latency from the deployment region against
   the live API, run only with an explicit flag and key.
6. Write a one-page data-flow note for the data protection review: fields
   sent, purpose, provider documents, retention option.

Never let the model's answer authorise refunds, payments or account
changes. Do not claim the hosted model runs locally.
```

## Validation and limits

- **Source inspected:** the complete article and its example requests. The article's figures are labelled as created by the author with Claude by Anthropic and are not reused. It also promotes a Red Hat model distribution as a self-hosted alternative; that claim was not checked and is not repeated here. A second part is planned and may refine the deployment advice.
- **Offline tests:** the sketch above, with the official `typesafe-sdk` 0.7.5 and a mock transport, passed six cases: three lanes from high, middle and low probabilities; a 503, a connection timeout and a missing answer all routed to review; and a request containing only the allowlisted fields, with no name, email or card data.
- **Documents checked:** TypeSafe's launch post, data processing addendum, subprocessor list, legal documentation page and models page, on 23 October 2026.
- **Not tested:** any live Jev call, real latency from any region, the accuracy of the example question, or any legal assessment. The thresholds are placeholders.

## Adoption questions

### Can I run Jev on my own servers or in vLLM?

No. The source explains that the official Jev model is offered only as a closed, managed API: its weights are not published, so it cannot be downloaded, containerised or loaded into vLLM. Calling it from OpenShift or beside vLLM still sends state to TypeSafe.

### Where does hosted Jev process requests?

TypeSafe's launch post says its service is currently based on the US West Coast. Treat that as a dated statement and confirm the current location and subprocessors with TypeSafe before sending personal data.

### What should a European team check before sending customer data?

Map which personal data is in the state, check TypeSafe's data processing addendum and subprocessor list with whoever owns data protection, and decide whether zero data retention for enterprise is needed. This guide is not legal advice.

### How much latency does the remote call add?

Measure it from where your application runs. TypeSafe's launch post says its published speed evaluations are generally run from the West Coast, so their figures do not include a round trip from Europe.

### What should happen when Jev is slow or unavailable?

Application code should send the case to a safe lane, such as human review or a follow-up question, never to the automatic one. Set a timeout inside your latency budget and count fallbacks so an outage is visible.

### Can a local open model replace Jev here?

It can fill the same slot if your requirements demand local processing, but it is a different model. Run it on the same labelled examples and thresholds before swapping; results for hosted Jev do not carry over.

## Sources, credits and corrections

- **Main source:** [“Jev: Bounded semantic judgments for messy text”](https://developers.redhat.com/articles/2026/10/20/jev-bounded-semantic-judgments-messy-text), Maarten Vandeperre, Red Hat Developer, 20 October 2026. The three kinds of question, state and question guidance, three lanes, "typed does not mean true", and the hosted-only deployment analysis are the author's. The four production checks, the allowlist and fallback code, and the offline tests are Appit Studio's additions.
- **Provider documents:** TypeSafe's [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [data processing addendum](https://typesafe.ai/legal/data-processing), [subprocessors](https://trust.typesafe.ai/subprocessors), [legal docs](https://docs.typesafe.ai/legal) and [models](https://docs.typesafe.ai/models), checked 23 October 2026. Hosting location and terms can change.
- **Editorial connections:** [openai-decisions-vs-jev-vs-laya](https://github.com/mateusfonsek/openai-decisions-vs-jev-vs-laya/tree/b9d296e97b4ed382cbad65248800ec63096225f4) (MIT) and [quarkus-langchain4j-jev-laya](https://github.com/kdubois/quarkus-langchain4j-jev-laya/tree/f312884dbeffeb226a74aab2fe8ee0c9afc076e9) (no licence file), both suggested by JevList and not named by the source; no affiliation with their maintainers is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0.

Appit Studio wrote this guide with AI assistance; it is not legal advice, and no human reviewer, source-author or Red Hat endorsement, or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
