# Jev in-context casebooks: test examples before you trust them

Jev's weights are the same for every account, so customization happens in the request. One way to customize is to include labelled precedents, a *casebook*, beside the input to classify. This guide sets up that experiment in the order the source's results support: make every answer category mean something, set no-example and retrieved-example baselines without leaking test labels, test a full casebook only if it fits, and treat the casebook as a versioned part of the application with its own test set.

**Based on:** [“How to Make In-Context Learning Work with Jev”](https://x.com/davidwbressler/article/2113374694405509628) by [David Bressler (@davidwbressler)](https://x.com/davidwbressler), published **22 October 2026** with a companion article, [“One Model, a Different Rulebook for Every Customer”](https://x.com/davidwbressler/article/2113374717516058674); both read in full on **23 October 2026**. The experiments are by Eventum. Both articles disclose that Eventum is an official TypeSafe technology partner and that TypeSafe's CTO advises Eventum. Guide by **Appit Studio**, with AI-assisted research, drafting and offline checks; no human reviewer is recorded.

## Key takeaways

- **Fix definitions before examples.** On CLINC150, replacing a bare `oos` label with an explicit description raised accuracy from 83.73% to 94.93%, more than any prompt search did.
- **Retrieved examples helped on all four tasks.** Adding up to 32 TF-IDF-retrieved training examples improved every task Eventum tested.
- **More is not automatically better.** A full 84K-token casebook beat 32 retrieved examples on banking intents. A random casebook of about 6,400 examples did worse than 32 retrieved on an emotion task.
- **Training can still win.** A fine-tuned small classifier was far stronger on one task.
- **Accuracy is not automation.** No highlighted configuration found a set of answers that met a 1% error target.

## What Eventum tested

Eventum used pinned `jev-1.14.0` through Choice questions on the complete official test sets of four public tasks: 3,080 BANKING77 banking queries, 2,000 Emotion texts, 5,500 CLINC150 requests including out-of-scope cases, and 2,091 ContractNLI judgments, 12,671 in total. Costs are recorded input tokens at $0.042 per million, excluding development, labelling and local retrieval. Production latency and throughput were not established.

| Task | No examples | 32 retrieved examples |
| --- | --- | --- |
| BANKING77 | 80.75% | 88.73% |
| Emotion | 60.15% | 71.05% |
| CLINC150 | 75.18% | 83.58% |
| ContractNLI | 74.75% | 78.72% |

*Eventum's results, as reported in the source.*

In a matched BANKING77 run with a fixed 2,446-example training pool, the full casebook, about 84,000 tokens in extended mode, reached 91.36% against 88.70% for 32 retrieved examples: 82 more correct decisions out of 3,080. Recorded input cost was $10.92 for the full casebook and $0.37 for retrieval, or about a third of a cent per decision for the full book. A two-stage pipeline where Jev scored 32 retrieved candidates, kept eight and then classified added 1.01 points on BANKING77 and 2.90 on Emotion over a first-eight control. The author notes the controls were retrospective. Against fine-tuned MiniLM, results were mixed: Jev ahead with 616 banking examples, no clear winner at 2,446, and MiniLM far ahead on Emotion at 92.35% against 76.00%.

The author describes the study as exploratory and not preregistered, with some follow-ups retrospective, and notes that the intervals do not cover variation across repeated calls. Treat the numbers as evidence that casebooks can work on public classification tasks, not as a forecast for yours.

## Build a casebook experiment

### 1. Define every answer before choosing examples

Write each Choice option as a testable statement. The source's illustration is a document-status decision: *complete* is ambiguous, *both parties have signed* is testable, and a record that does not establish signature status needs its own answer, separate from one that says a signature is pending. A semantic answer such as `unclear` describes missing evidence in the input. It does not replace checking the model's confidence.

Keep exact rules in code. The companion article notes that an explicit numeric threshold, such as an approval limit on a structured amount, should stay a numeric check. In the source's constructed purchase-policy tests, trained tree models substantially outperformed Jev at larger sample sizes.

### 2. Split first, then build a training-only index

Divide labelled records into training, development and test pools before anything else. Group related documents and near-duplicates so they stay in one pool, and build the retrieval index from the training pool only. A test case must not be able to retrieve its own label, a copy of itself, or another fragment of the same source. The source's warning is direct: a small test you can trust beats a large prompt search whose evaluation data leaked into its examples.

### 3. Compare no examples with retrieved examples

Hold the request fixed and vary only the examples. Put them in `state` beside the target, and tell the question to classify the target only:

```python
from typesafe_sdk import Choice

QUESTION = Choice(
    instructions="Classify target only. Use examples as precedents, not as evidence about target.",
    criteria={
        "complete": "The target explicitly establishes both parties signed.",
        "pending": "The target establishes at least one signature is pending.",
        "unclear": "The target does not establish whether signing is complete or pending.",
    },
)

def build_state(target, ranked_examples, k=32, budget=24_000, count=lambda s: len(s) // 4 + 8):
    """ranked_examples: training-pool records, best match first."""
    examples, used = [], count(target)
    for ex in ranked_examples[:k]:
        cost = count(ex["text"])
        if used + cost > budget:
            break                      # report the shortfall rather than hide it
        examples.append({"text": ex["text"], "label": ex["label"]})
        used += cost
    return {"examples": examples, "target": target}, {"requested": k, "sent": len(examples)}
```

The question is adapted from the source's request example. The token counter is a rough placeholder; use the `usage` the API returns to calibrate it. Pin the model version, log example IDs, exact requests, responses, usage, failures and retries, and report cases that received fewer examples because of the budget, as the source recommends. Report accuracy per category as well as overall, with intervals grouped by source document.

### 4. Test a full casebook only when it fits, and log the mode

If the whole training library fits, compare it against retrieval from the **same** library. Do not give one condition thousands of extra labelled records and credit the selection method. By default, the [models page](https://docs.typesafe.ai/models) allows 64k tokens per request and 32k per question. The `TypeSafe-Danger-Zone-Long-Context: true` header raises both to 262k, at the same price per token. TypeSafe describes such requests as slower and less accurate. Keep the header off unless you are testing it, and record it with every result.

### 5. Add a selection stage only if it beats fixed retrieval

The source's selector asks Jev to score the usefulness of each of 32 retrieved candidates, keeps eight, and classifies in a second call. Compare it against the first eight lexical matches and a category-diverse eight, with the same candidate pool, final prompt and ordering rule. Tune on development data and freeze before testing. Report the combined cost of both stages. The source found that extra rounds and example histories did not add a demonstrated benefit, and that a second round roughly doubled fresh-call token cost.

### 6. Compare with a trained model and with code

If you have a stable, high-volume task and enough labels, train a small classifier on the same training pool and test both on the same split. [Jev IDS](../../projects/tools/jev-ids.md) is an **independent JevList suggestion**, not named by the source, that shows this comparison in another domain. It places a record and labelled pool examples in one request's state, sweeps the number of examples per category across seeds, and scores Random Forest and Isolation Forest baselines on the same splits.

### 7. Fit acceptance separately, and version the casebook

Average accuracy does not say which answers can skip review. Fit any acceptance threshold on a separate calibration split, freeze it, and report both error and coverage on the test split. If no useful operating point exists, say so. In the source, neither highlighted selector met a 1% error target on 200 calibration cases per task, so that rule would have accepted nothing. The source's analysis used the chosen category's probability, not the separate `confidence` field. Check whichever you use against labels.

Version each casebook with its definitions and examples. The companion article suggests replaying historical inputs against the old and new casebook before release, and checking that the answers that change are the ones the policy owner intended. A reviewer's correction is a candidate example, not an automatic update. Historical labels can be inconsistent or out of date, and the test set must never be absorbed into the teaching material.

## Copyable build prompt

```text
Build an in-context casebook evaluation for one Jev Choice decision.

Inputs:
- Decision and answer definitions: [OPTION: TESTABLE DESCRIPTION, ...]
- Labelled records: [CSV OF id, source_group, text, label]
- Pinned model: jev-1.14.0; long-context header OFF unless I say so
- Token budget per request: [e.g. 24,000]

Read first:
- https://x.com/davidwbressler/article/2113374694405509628 (method)
- https://docs.typesafe.ai/primitives/choice and https://docs.typesafe.ai/models
- https://hamel.dev/blog/posts/decision-model-evals/ (threshold evaluation)

Steps:
1. Split into train, dev and test by source_group, removing exact and near
   duplicates across splits. Save the split and a checksum.
2. Build a TF-IDF index from train only.
3. Conditions on dev: no examples; up to 32 retrieved examples. Same
   question and instructions ("classify target only; examples are
   precedents"). Record cases that got fewer examples due to the budget.
4. Optional: full casebook from the same train pool if it fits; record the
   mode and per-request input tokens.
5. Log example IDs, exact request, response, usage, errors and retries.
6. Choose one configuration on dev, freeze it, score test once: accuracy,
   per-category results, grouped bootstrap intervals, input-token cost.
7. Fit an acceptance threshold on a separate calibration split for a target
   error rate; report error and coverage on test, or that none exists.
8. Offline tests: no test record or duplicate is retrievable, budget
   shortfall is reported, missing answers and API errors are counted.

Never put test labels in a request or choose prompts from test results.
Report results as limited to this dataset, split and model version.
```

## Validation and limits

- **Source inspected:** the complete article and companion through the X API on 23 October 2026, including the request example, with the partner disclosure. The linked Eventum write-up and reference pages resolve; Eventum's figures were not checked against raw data.
- **Offline example tested:** the casebook builder with a small TF-IDF retriever on fixture records. Groups were disjoint across train and test, the target never appeared among its own examples, and a tight budget reduced the examples sent and reported the shortfall. Long-context limits and the header were checked against current docs. Jev IDS was inspected at a pinned commit and not run.
- **Not tested:** any Jev request, retrieval over a real dataset, a full casebook, long context, the selector, a fine-tuned baseline, accuracy, acceptance thresholds or cost.
- **Design limits:** casebooks add input tokens to every call; retrieval quality bounds what examples can teach; a casebook tuned on one model version needs re-testing on the next.

## Adoption questions

### Can Jev be fine-tuned on my labels?

No. TypeSafe's models page says Jev is not fine-tuned or LoRA-adapted with customer data and the same weights serve every account. You customize it through the request: state, instructions, criteria and, as this guide shows, labelled examples placed in the state.

### How many examples should I put in a Jev request?

Start with none and with up to 32 retrieved examples, and compare them on a development split. In the source, 32 retrieved examples helped on all four tasks, while thousands of random examples sometimes did worse. A full casebook won on banking intents but cost far more.

### Do I need long context for a full casebook?

Only if it exceeds the default limits of 64k tokens per request and 32k per question. The long-context header raises both to 262k, and TypeSafe says such requests are slower and less accurate. Log the setting so you know which mode you evaluated.

### How do I stop test labels leaking into the examples?

Split records into training, development and test pools before building the retrieval index, keep related documents and near-duplicates in one pool, and build the index from the training pool only. A test case must never retrieve itself or a copy of itself.

### Is a better casebook enough to automate decisions?

No. In the source, neither highlighted selector found any set of answers that met a 1 percent error target on 200 calibration cases. Fit acceptance thresholds on separate data and report when no useful operating point exists.

### When is fine-tuning a separate model the better choice?

When the task is stable, high-volume and well labelled. In the source a fine-tuned MiniLM scored 92.35 percent on Emotion against 76.00 percent for the Jev selector. Casebooks matter most when boundaries differ by customer or change often.

## Sources, credits and corrections

- **Main source:** [David Bressler's X article](https://x.com/davidwbressler/article/2113374694405509628), 22 October 2026, and its [companion article](https://x.com/davidwbressler/article/2113374717516058674). The experiments, figures, workflow order and request example are Eventum's. The token-budget builder, the rule that the full casebook must come from the same library, and the placement of trained and code baselines are Appit Studio's framing of the source's advice. Eventum is an official TypeSafe technology partner, and TypeSafe's CTO advises Eventum.
- **Further reading linked by the source:** [Eventum's experimental write-up](https://www.eventum.ai/blog/in-context-learning-at-scale-what-jev-changes), [Many-Shot In-Context Learning](https://arxiv.org/abs/2404.11018) and Hamel Husain and Antaripa Saha's [decision-model evaluation article](https://hamel.dev/blog/posts/decision-model-evals/).
- **API references:** [Choice](https://docs.typesafe.ai/primitives/choice) and [models and long context](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connection:** [Jev IDS](https://github.com/jev-sec/jev-ids/tree/6aa5ac4570db1d6d9b88f769f7d16c1cd2c3784a), MIT, suggested by JevList; not named by the source, and no affiliation with its maintainer is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The articles' images are not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement, TypeSafe or Eventum relationship, or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
