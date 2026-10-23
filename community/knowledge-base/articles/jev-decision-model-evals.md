# Use Jev as an eval judge: tune thresholds and check calibration

An automated eval asks the same yes-or-no question about every trace: did this agent run contain a real failure? Decision models such as Jev can answer it with a probability, at a fraction of an LLM judge's cost. Whether that probability is usable depends on two things this guide makes routine: a threshold chosen on labelled traces against minimum precision and recall, and a check that the scores mean what they appear to mean.

**Based on:** [“How To Use Decision Models for Evals”](https://hamel.dev/blog/posts/decision-model-evals/) by Hamel Husain ([@HamelHusain](https://x.com/HamelHusain)) and Antaripa Saha, published on hamel.dev on **20 October 2026** and read in full on **23 October 2026**. The post compares Jev 1.13 with five other decision models and publishes its saved scores and labels. Guide by **Appit Studio**, with AI-assisted research, drafting and an offline reproduction of the post's Jev numbers; no human reviewer is recorded.

## Key takeaways

- **Write binary pass/fail criteria first.** The authors recommend a pass/fail judge per failure mode, with explicit qualifying and non-qualifying evidence.
- **Set minimums before optimising.** For an alerting use, they require at least 80% precision and 80% recall, and rule out models that cannot reach both.
- **Tune on saved scores with cross-validation.** No new model calls are needed; use the same splits for every model you compare.
- **Check calibration separately.** A score of 0.8 is a confidence estimate only if about 80% of similar traces actually fail.
- **On this dataset, Jev was well calibrated but below the 80/80 bar.** Measure your own task; the authors note that results vary substantially across tasks.

For thresholds on document triage rather than evals, see [the research triage guide](jev-research-paper-triage.md). For grading content drafts, see [the content grader](jev-content-grader.md).

## What the source measured

The dataset is 100 traces from an apartment-leasing support agent, with 98 scored after two internal QA traces were excluded: 61 known failures and 37 traces without a labelled failure. Each model returned a failure probability per trace. Jev received the criteria as a structured [Noul](https://docs.typesafe.ai/primitives/noul) with separate definitions of true and false, reproduced in the post's appendix. The other models received an equivalent plain prompt. The traces themselves are private.

With precision and recall weighted equally via F1, OpenAI Decisions was strongest at F1 0.87 and the highest cost, 3.72 cents per 100 runs. Perplexity Decider and Liquid d1-ultra were the other models to reach the 80/80 region, at lower cost and F1. Jev and Clef Flash were not among those candidates. On calibration, the authors report Jev and Liquid d1-ultra as already well calibrated, with Jev's Brier score 0.187 before and 0.188 after Platt scaling. Clef Flash was badly miscalibrated: one group averaging about 8% predicted failure contained 60% failures. Mean response times are given in a footnote, with the caveat that they came from separate runs and do not establish comparative throughput.

The authors are careful about scope: one broad failure question, a small dataset, and results they say vary across tasks. They recommend narrower judges per failure mode in practice and expect model gaps to shrink with them.

### What we reproduced for Jev

The post publishes its saved scores and labels as JSON. Recomputing Jev's numbers from that file, without model calls:

| Jev 1.13 on 98 traces | Precision | Recall | F1 |
| --- | --- | --- | --- |
| Default threshold 0.50, full sample | 0.711 | 0.885 | 0.788 |
| Tuned by cross-validation, held-out average (ours) | 0.718 | 0.867 | 0.779 |
| Tuned by cross-validation, held-out average (post) | 0.711 | 0.867 | 0.781 |

No single threshold on the full sample gives Jev both 80% precision and 80% recall. Its best in-sample F1, 0.817 at a threshold of 0.40, does not survive cross-validation. For Jev on this task, tuning did not beat the default, because its scores were already centred near 0.50. That is a useful negative result: tuning is a check you run, not a guaranteed gain. The post's other models show the opposite case, with large gains from moving far below 0.50.

## Build a Jev eval judge

### 1. Write one pass/fail question per failure mode

Use the appendix's structure as a template: a task question, context about the trace, evaluation rules, and criteria for `true` and `false` with examples of what does and does not count. The post's rules include evaluating the assistant rather than the customer, using only evidence visible in the trace, and treating inconclusive traces as not failing. Pin a dated version such as `jev-1.13.0`, the one the post tested: the [models page](https://docs.typesafe.ai/models) says the `jev-latest` alias moves, and a threshold tuned on one version is not evidence for the next. Record the version with every saved score.

### 2. Label traces and save scores once

Label traces as pass or fail without seeing model scores. Score each trace once and store the trace ID, label, raw `noul` probability, model ID and prompt version. Everything after this step runs on the saved file.

### 3. Tune the threshold with cross-validation against minimums

The post includes a copyable coding-agent prompt for this step. The core is short:

```python
import random

def prf(rows, t):
    tp = sum(1 for s, y in rows if s >= t and y); fp = sum(1 for s, y in rows if s >= t and not y)
    fn = sum(1 for s, y in rows if s < t and y)
    p = tp / (tp + fp) if tp + fp else 0.0; r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)

def cv_threshold(rows, min_p=0.8, min_r=0.8, repeats=20, seed=0):
    """rows: (score, is_failure). Returns held-out (p, r, f1) per fold and whether minimums were feasible."""
    rng, results = random.Random(seed), []
    pos = [x for x in rows if x[1]]; neg = [x for x in rows if not x[1]]
    for _ in range(repeats):
        rng.shuffle(pos); rng.shuffle(neg)
        folds = [pos[k::5] + neg[k::5] for k in range(5)]
        for k in range(5):
            train = [x for j, f in enumerate(folds) if j != k for x in f]
            cuts = sorted({s for s, _ in train})
            ok = [t for t in cuts if prf(train, t)[0] >= min_p and prf(train, t)[1] >= min_r]
            t = max(ok or cuts, key=lambda c: prf(train, c)[2])
            results.append((prf(folds[k], t), bool(ok)))
    return results
```

When no threshold meets both minimums on a training fold, this falls back to the best F1 and marks the fold infeasible, which is what the post's audit does. Count infeasible folds and report them. A model that is infeasible in most folds does not meet your requirements, whatever its average F1. Reuse the same splits for every model you compare. Replace F1 with a weighted metric if a missed failure and a false alarm do not cost the same; the authors explicitly warn against using F1 just because their post did.

### 4. Check calibration before reading scores as confidence

If you will act on a score itself, for example paging someone only above 0.9, group traces by predicted probability and compare each group's mean prediction with its observed failure rate. The post's second prompt fits Platt scaling inside cross-validation and reports Brier scores before and after. Keep the adjusted mapping only if it improves held-out Brier score: Jev barely changed in the post, and OpenAI Decisions got slightly worse with the version of Platt scaling used. TypeSafe's [confidence documentation](https://docs.typesafe.ai/confidence) notes that a Noul returns a probability and no separate `confidence` field. Calibration on your labels is what turns that probability into something you can quote.

### 5. Put the tuned threshold into CI

[jev-judge](../../projects/tools/jev-judge.md) is an **independent JevList suggestion**, not named by the authors, that runs Jev Noul and Score assertions from YAML in CI and compares each probability with a threshold. At the catalog's pinned commit, an assertion without its own threshold uses 0.75. Set each threshold from step 3 instead. Re-tune whenever the prompt, the model version or the kind of traces changes, and keep a held-out set of labelled traces outside prompt iteration, as the authors advise for prompt optimisation.

## Copyable build prompt

```text
Build a decision-model eval for one failure mode with Jev.

Inputs:
- Failure mode and pass/fail criteria: [TRUE/FALSE DEFINITIONS WITH EXAMPLES]
- Labelled traces: [JSONL OF trace_id, trace, is_failure] (labels written
  without seeing model scores)
- Minimums: precision >= [0.80], recall >= [0.80]; cost of a miss vs a
  false alarm: [RATIO]
- Pinned model: jev-1.13.0 (or the dated version you will deploy)

Read first:
- https://hamel.dev/blog/posts/decision-model-evals/ (method, prompts, appendix)
- https://docs.typesafe.ai/primitives/noul and https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/models

Steps:
1. One structured Noul per trace following the post's appendix layout.
   Score every trace once; save trace_id, label, noul, model ID, prompt
   version. Count and report errors; never record a failed call as pass.
2. On saved scores only: stratified 5-fold CV, 20 repeats, fixed seed.
   Choose the threshold on training folds among those meeting both
   minimums; if none, fall back to best F1 and mark the fold infeasible.
3. Report held-out precision, recall, F1 and infeasible-fold count, and
   the same at the 0.50 default. Use identical splits for any other model.
4. Calibration: reliability table of ~5 groups, Brier score before and
   after cross-validated Platt scaling on log-odds; keep it only if
   held-out Brier improves.
5. Write the chosen threshold and prompt version to a config file used by
   CI.
6. Offline tests on fixture scores: all-pass labels, infeasible minimums,
   ties at the threshold.

Do not call the model during tuning. Do not relax the minimums silently.
State that results apply to this dataset, prompt and model version.
```

## Validation and limits

- **Source inspected:** the complete post with footnotes and appendix, and its published JSON files. The traces are private, so the scores could be recomputed but not regenerated. The post states no sponsorship; the tested models are its subject, not its funders.
- **Offline reproduction:** from the post's `chart-data.json`, Jev's default-threshold precision, recall and F1, the absence of a full-sample 80/80 threshold, and the raw Brier score 0.187 match the post. An independent cross-validation with our own seed gave held-out F1 0.779, close to the post's 0.781. The condensed sketch above, run on the same file, gives held-out F1 0.778, with 70 of 100 training folds unable to meet both minimums.
- **Not tested:** any decision-model call, new traces or labels, a calibration fit, latency or cost. Every non-Jev figure is the authors'.
- **Design limits:** 98 traces with 61 failures give wide uncertainty; one broad question mixes many failure modes; cross-validation on one dataset does not predict another.

## Adoption questions

### Can Jev replace an LLM judge in my evals?

Sometimes. In the source's 98-trace failure-finding eval, Jev 1.13 scored an F1 near 0.79 but never reached the authors' minimum of 80 percent precision and recall together. Measure it against your own labelled traces and requirements before swapping judges.

### Why not keep the default 0.50 threshold?

Because a model's scores may sit anywhere between 0 and 1 for your task. The source shows models whose best threshold was far from 0.50. For Jev on that dataset the default happened to be near its tuned value, so tuning changed little.

### How should I tune a threshold without fooling myself?

Save the model's scores once, then use stratified cross-validation: pick the threshold on training folds, measure on the held-out fold, and use the same splits for every model. Report when no threshold meets your minimums rather than relaxing them.

### Is a Jev Noul probability a calibrated confidence?

Check it on your labels. In the source, Jev's probabilities were already well calibrated on its dataset and Platt scaling barely changed its Brier score. That is one small dataset; a reliability chart on your own traces is the evidence that matters.

### Should one judge check every failure mode?

No. The authors kept one broad question to make model differences visible, but recommend a separate judge for each failure mode in practice. Narrower questions with specific criteria are easier to label, tune and debug.

### Does tuning need new model calls?

No. Threshold tuning and calibration run on the scores you already saved alongside human labels. Re-score only when the prompt, the model version or the kind of traces changes.

## Sources, credits and corrections

- **Main source:** [“How To Use Decision Models for Evals”](https://hamel.dev/blog/posts/decision-model-evals/), Hamel Husain and Antaripa Saha, 20 October 2026, with its published scores, labels, calibration data and threshold audit. The method, minimums, prompts, model comparison and calibration results are the authors'. The Jev reproduction table, the condensed cross-validation sketch and the CI hand-off are Appit Studio's additions.
- **API references:** [Noul](https://docs.typesafe.ai/primitives/noul), [confidence](https://docs.typesafe.ai/confidence) and [models](https://docs.typesafe.ai/models), checked 23 October 2026.
- **Editorial connection:** [jev-judge](https://github.com/00200200/jev-judge/tree/5d4ac63cad80a87b4c7930aeb49fd607372fb671), MIT, suggested by JevList; not named by the source, and no affiliation with its maintainer is claimed.
- **Image:** original Appit Studio diagram, dedicated to CC0 1.0. The post's charts and cover are not reused.

Appit Studio wrote this guide with AI assistance; no human reviewer, source-author endorsement or paid placement is claimed. Propose evidence-backed corrections through the [contribution process](../../../CONTRIBUTING.md).
