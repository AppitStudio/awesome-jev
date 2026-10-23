# Replace hand-written routing rules with Jev: a migration test

Many backends have a function that turns a customer's sentence into one of dozens of actions, built from keyword and regex rules that grew one patch at a time. This guide shows how to test whether Jev can take over that selection: freeze the current rules as a baseline, compare exact-action accuracy on labelled messages, add a hybrid that refers disagreements, and keep a confirmation step for actions that change state, whichever selector picks them.

**Based on:** [“Can a Decision Model Replace Hand-Written Routing Rules? A 3,080-Message Experiment”](https://dev.to/md_almamunmamun_857ec/can-a-decision-model-replace-hand-written-routing-rules-a-3080-message-experiment-1mnd) by [Mo Al Mamun (Mamun)](https://dev.to/md_almamunmamun_857ec), published on dev.to on **17 October 2026** and read in full on **23 October 2026**. The author shared it on X as [@3dgrinder](https://x.com/3dgrinder). The article discloses no relationship with TypeSafe and notes that an AI assistant wrote most of the implementation, which the author directed and reviewed. Guide by **Appit Studio**, with AI-assisted research, drafting and offline checks; no human reviewer is recorded.

## Key takeaways

- **Jev beat this rules implementation.** Exact-action accuracy was 80.9% for zero-shot `jev-1.13.0` and 65.5% for 772 lines of AI-written, reviewed rules, on all 3,080 Banking77 test messages.
- **Jev was faster, not cheaper.** Median decision time was 111 ms against 975 ms for `gpt-6-luna`, whose cost was about a third of Jev's thanks to cached input pricing.
- **The hybrid trades coverage for accuracy.** Rules and Jev together answered 81.7% of messages at 90.7% accuracy and referred the rest.
- **Selection is not execution.** 32 of the hybrid's wrong picks chose a handler that can change account state.
- **Stability needs its own test.** Repeat runs changed 0.5 to 2.0% of selections on a subset; reversing option order changed 5.0%.

For routing tasks to agent workers rather than to backend handlers, see [the worker router guide](jev-agent-worker-router.md). For a general ship/return/escalate gate, see [the decision gate guide](jev-decision-gate.md).

## What the experiment showed

The author built *switchless*, a fictional bank with 11 service modules and 77 handlers behind one `POST /help` endpoint, and four interchangeable dispatchers: ordered keyword and regex rules developed in eight stages; Jev choosing among the 77 action IDs and their one-line descriptions; an LLM with the same catalogue and structured output; and a hybrid. Neither model saw example messages. The rules were frozen on separate data before the final test; the LLM was added afterwards without retuning the others.

| Measure | Rules | Jev | LLM | Hybrid |
| --- | --- | --- | --- | --- |
| Exact-action accuracy | 65.5% | 80.9% | 81.5% | 74.1% |
| Referred | 17.0% | 0% | 0% | 18.3% |
| Accuracy when answering | 78.9% | 80.9% | 81.5% | 90.7% |
| Median decision time | 0.29 ms | 111 ms | 975 ms | 112 ms |
| API cost per 1,000 messages | $0 | $0.083 | $0.028 | $0.083 |

*Figures from the article's recorded runs. API cost excludes infrastructure and human work.*

The Jev–LLM accuracy gap on the test split was not statistically detectable, with a paired 95% interval of −0.38 to +1.68 points. On a separate 1,000-message sample the LLM led by 2.2 points. Rules accuracy grew from 39.4% at 137 lines to 63.0% at 772 lines on the held-out sample, with later stages often repairing earlier ones. At an equal number of referrals, the hybrid made 233 wrong automatic selections against 282 for confidence-gated Jev and 310 for the gated LLM. The author calls that comparison exploratory, because the single-model cut-offs were chosen on the test split.

The repository's generated analysis adds a detail the article does not headline. For the five safety-critical intents, exact-intent recall was 79.5% for Jev alone and 66.5% for the hybrid; a referred message counts as a miss in that measure. Fewer wrong automatic actions can mean more protective requests waiting for a person. The author did not measure what happens after a referral.

## Run the migration test on your dispatcher

### 1. Freeze the current rules and label messages

Treat today's dispatcher as a router with a fixed version. Collect a few thousand real messages, label each with the action a person would choose, and split them: one sample for tuning the hybrid, one untouched test set. Keep near-duplicate messages in the same split. Score **exact action**, not service: in the source, Jev chose the right service for about 90% of messages but the exact action for 81%.

### 2. Describe each action, then ask one Choice

Give every handler an ID and a one-line description that separates it from its neighbours. In the source, the description is all the model sees about an action. A [Choice](https://docs.typesafe.ai/primitives/choice) accepts up to 255 options. Send the customer message as `state`, pin a versioned model, and record the returned `model`, `choice`, `confidence` and `probabilities`. The author's TypeScript router does exactly this and rejects any action ID outside the catalogue. Read it in the [switchless repository](https://github.com/grinder81/switchless/tree/f2afb84a5bcd0478f41af3956f3bd0b553bdfc71) before writing your own.

When two actions keep getting confused, the Choice documentation suggests describing each with an object that says what it covers and what belongs to a neighbouring option. Re-test after any description change. It is a new configuration, not a fix to the old one.

### 3. Combine rules and Jev, then gate execution separately

```python
FLOOR = 0.9   # the source's hybrid threshold, chosen on its tuning sample

def combine(rules_pick, jev):
    """rules_pick: action ID or None (no rule matched). jev: a Choice answer."""
    if rules_pick is not None and rules_pick == jev.choice:
        return jev.choice, "agree"
    if jev.confidence >= FLOOR:
        return jev.choice, "jev_confident"
    return None, "refer"

def dispatch(message, rules_pick, jev, state_changing, handlers):
    action, why = combine(rules_pick, jev)
    if action is None:
        return {"status": "referred", "why": why}
    if action in state_changing:
        return {"status": "needs_confirmation", "action": action, "why": why}
    return {"status": "done", "action": action, "why": why, "result": handlers[action](message)}
```

`combine` is the source's hybrid. `dispatch` is our editorial addition: any handler that can block a card, open a claim or cancel a transfer asks the customer or an agent to confirm, whatever the confidence. The source keeps a list of 20 such handlers and checks it with a test that runs every handler against seed customers. Build the same list for your backend from what handlers do, not from their names.

Choose `FLOOR` on the tuning sample, not the test set. [TypeSafe's confidence page](https://docs.typesafe.ai/confidence) describes `confidence` as a statistic of the probability spread, so its scale depends on the number of options. A floor tuned for 77 actions does not carry over to 20. The author found that higher confidence went with higher accuracy, but Jev was over-confident below 0.9. Any cut has to come from data.

### 4. Test order and repeat stability

Before freezing the floor, re-run a fixed subset twice and once with the options in reverse order. Count changed selections. The source's figures, 0.5 to 2.0% for repeats and 5.0% for order on 200 messages, give a sense of scale, not a bound for your catalogue. If many changes fall near the floor, widen the referral band.

### 5. Compare at equal referral volume, and price both

A hybrid that refers 18% of messages should be compared with Jev and the LLM referring the same number. Otherwise you are comparing coverage, not quality. Report wrong automatic selections, wrong selections of state-changing handlers, and recall on your safety-critical intents. Then price the options on your traffic. The source found the LLM cheaper because of input caching, which depends on your provider, catalogue size and call pattern.

[Support Ticket Router](../../projects/tools/support-ticket-router.md) is an **independent JevList suggestion** that takes a further step: it multiplies mistake probabilities by configured costs to choose auto, review or human routing, and can replay stored answers under a new policy without new calls. For a fast first look before a full study, [the Jev vs LLM Banking77 benchmark](../../projects/tools/jev-vs-llm-banking77.md), also a JevList suggestion, compares Jev with two Claude models on 100 messages. Neither is named by the source.

### 6. Decide what to keep

The source's result supports replacing hand-written *selection* logic in a similar task. It does not remove the need for a referral path, a confirmation step for state changes, or a trained baseline. The author notes that a logistic regression on the full labelled set scored higher than zero-shot Jev in another team's evaluation, and lists that baseline as missing. TypeSafe's [models page](https://docs.typesafe.ai/models) says Jev is not fine-tuned on customer data. Improvements come from better descriptions, state and question design, or a separate model trained on corrections and evaluated on new data.

## Copyable build prompt

```text
Run a routing-migration test for my intent dispatcher.

Inputs:
- Current dispatcher (frozen at commit): [REPO AND COMMIT]
- Action catalogue: [ACTION IDS WITH ONE-LINE DESCRIPTIONS]
- State-changing handlers: [LIST, OR DERIVE FROM HANDLER CODE WITH A TEST]
- Labelled messages: [CSV OF message, correct_action]
- Pinned model: jev-1.14.0

Read first:
- https://dev.to/md_almamunmamun_857ec/can-a-decision-model-replace-hand-written-routing-rules-a-3080-message-experiment-1mnd
- https://github.com/grinder81/switchless (MIT; reproduce its analysis offline
  with pnpm analyze before writing new code)
- https://docs.typesafe.ai/primitives/choice and https://docs.typesafe.ai/confidence

Steps:
1. Split messages into tuning and test sets; keep near-duplicates together.
2. Wrap the current dispatcher, Jev (one Choice over the catalogue, message
   as state) and a hybrid behind one interface. Reject off-catalogue IDs.
3. Hybrid: accept on agreement; else accept Jev at or above a floor chosen
   on the tuning set; else refer.
4. Execution gate: state-changing handlers return needs_confirmation.
5. Log every decision with model ID, choice, confidence, probabilities,
   latency and input tokens.
6. Test set, frozen configs: exact-action and service accuracy with
   intervals, referral rate, accuracy when answering, wrong selections of
   state-changing handlers, recall on safety-critical intents, latency, cost.
7. Stability: rerun 200 test messages twice and once with reversed options;
   report changed selections.
8. Compare at equal referral volume and state that this is exploratory if
   cut-offs are chosen on the test set.
9. Offline tests with recorded fixture answers for the combiner and gate.

Do not execute state-changing handlers during evaluation. Do not claim
safety from selection accuracy.
```

## Validation and limits

- **Source inspected:** the complete dev.to article, and the switchless repository at a pinned commit: README, the pinned `jev-1.13.0` router and generated analysis. The X share by @3dgrinder links to this article and is written in the first person.
- **Offline evidence reproduced:** on Node 22, `pnpm analyze` verified all 16 raw prediction files against their SHA-256 manifest and regenerated the committed analysis with no differences; `pnpm test` passed 61 tests with 2 skipped. The combiner and gate above passed five fixture cases. This reproduces the author's analysis from saved predictions, not the model calls.
- **Not tested:** any TypeSafe or OpenAI call, a new routing run, human handling of referrals, latency or cost. Every model figure here is from the author's recorded runs, on one public dataset and one rules implementation written by an AI assistant.
- **Design limits:** Banking77 messages are short and single-intent; real traffic has multi-intent and out-of-scope messages. A hybrid keeps the full cost of maintaining the rules. The 0.9 floor belongs to the source's catalogue and model version.

## Adoption questions

### Can Jev replace a keyword and regex intent dispatcher?

In the source's Banking77 experiment, zero-shot Jev chose the exact action for 80.9 percent of 3,080 messages against 65.5 percent for 772 lines of rules. That supports replacing intent selection in a similar task. It does not show the chosen actions are safe to run unchecked.

### Is Jev cheaper than an LLM for routing?

Not in the source's runs. The LLM cost about a third as much per 1,000 messages because its repeated action catalogue benefited from cached-input pricing. Jev was about nine times faster. Price both on your own catalogue and traffic.

### What does the rules plus Jev hybrid buy?

It accepts an action when both agree, accepts Jev alone at 0.9 confidence or more, and otherwise refers the message. In the source it answered 81.7 percent of messages at 90.7 percent accuracy, which still left about one wrong automatic choice in eleven.

### Why keep a confirmation step for state-changing actions?

Picking the right handler and executing it safely are different questions. In the source, 32 of the hybrid's 233 wrong selections chose a handler that can change bank state. Require confirmation for those handlers regardless of confidence.

### Does option order affect Jev's choice?

It can. Reversing the order of the 77 options changed 5 percent of selections on a 200-message subset in the source, and two repeat runs changed 2.0 and 0.5 percent. Test order and repeat stability before freezing a threshold.

### What baseline is missing from the source's comparison?

A trained classifier or embedding baseline. The author points to another evaluation where logistic regression on the full labelled set scored higher than zero-shot Jev. If you have labelled history, include such a baseline before choosing.

## Sources, credits and corrections

- **Main source:** [Mo Al Mamun's dev.to article](https://dev.to/md_almamunmamun_857ec/can-a-decision-model-replace-hand-written-routing-rules-a-3080-message-experiment-1mnd), 17 October 2026, also shared by the author as [@3dgrinder](https://x.com/3dgrinder/status/2111501581606871069). The experiment, figures, hybrid design and the selection-versus-execution distinction are the author's. The execution gate code, order and repeat checks as a pre-freeze step, and the safety-intent recall reading of the repository analysis are Appit Studio's editorial additions.
- **Source repository:** [switchless](https://github.com/grinder81/switchless/tree/f2afb84a5bcd0478f41af3956f3bd0b553bdfc71), MIT, by the article's author.
- **API references:** [Choice](https://docs.typesafe.ai/primitives/choice), [confidence](https://docs.typesafe.ai/confidence) and [models](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connections:** [jev-vs-llm](https://github.com/0xGondarxyz/jev-vs-llm/tree/8f80717e347eb5c041c1ff3e551905c836573312) and [support-ticket-router](https://github.com/khaledjamal/support-ticket-router/tree/e0831fc12abaf918bc7df8fab37165f7098dd3fd), both MIT, suggested by JevList; neither is named by the source, and no affiliation with their maintainers is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The article's images and charts are not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
