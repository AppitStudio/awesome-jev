# Gero-4B: train a calibrated decision model with MLX

Based on [Building an RL fine-tuning platform to train JEV-like decision models](https://x.com/thevixhal/article/2106439792800198966) by [vixhaℓ (@TheVixhal)](https://x.com/TheVixhal), published 3 October 2026. Appit Studio wrote this original guide with AI assistance; no human reviewer is recorded.

The article describes converting Qwen3-4B into **Gero-4B**, a model that scores candidate answers instead of generating a reply. Its most useful lesson is the separation of architecture, question-format training and probability learning. This guide is for developers investigating decision-model training and the checks needed before routing work by confidence.

The author reports using MLX on a MacBook with an M5 Pro and 24 GB of memory. That is a reported training setup, not a hardware guarantee. The linked model is independent research, not official TypeSafe Jev. Start with an offline evaluation harness before spending on training or trusting an automation threshold.

## Key takeaways

- A shared scalar scorer evaluates each option against the state and question. Independent option branches avoid fixed output slots; softmax makes their scores compete.
- Format training needs counterexamples to cheap shortcuts: leaked states, predictable answer positions, string matching and negation cues.
- A reward should favor honest probabilities. Test its expected objective on a known synthetic distribution before running a training loop.
- Evaluate calibration together with discrimination and accepted-case coverage. A constant probability can match average accuracy while separating no easy cases from hard ones.
- Keep training, development and final evaluation separate. Neither typed output nor a training objective proves correctness on your workload.

## Three stages and their checks

### 1. Replace generation with option scoring

In the article’s design, the state and question form a prefix. Each answer option forms an isolated continuation. One linear scorer reads the last real token of each continuation; a softmax over those scores gives a probability distribution. A prefix cache can share the context computation across branches.

The author reports that an earlier 256-slot head failed beyond the six positions common in training. The shared scorer removes that particular dependency on slot-specific weights. The article also reports zero difference when reversing options in its sanity check. We did not reproduce either model experiment. Reordering should preserve probabilities after mapping them back to option identity; introducing new options or duplicates changes the normalization and is a different test.

Test cached branches against independent full sequences, padding against unpadded inputs, permutations, ties and supported option counts. Treat an excessive token or memory requirement as a rejected run with a recorded reason. A prefix cache saves repeated context work, but branches still consume compute and memory.

### 2. Teach question structure without leaking answers

The article uses invented identifiers and structured relationships to isolate reading skills. It balances facts and negation, varies yes/no wording, and draws distractors from the same state. That prevents a model from solving a relational question merely by noticing which answer text occurs somewhere in the input.

Audit split overlap by state identity, not only row number. Check answer-position and answer-text baselines separately by task family and option count. Add deliberate faulty fixtures and confirm each checker rejects them. The article’s example position checker covers only sets of at most six options, and its numerical cutoffs are project choices, not universal data-quality standards.

The source reports that a negation shortcut reduced one entailment result from 0.775 to 0.617. Its response was to make negation words appear in unrelated contexts too. That is a useful hypothesis to test, rather than a guarantee that a balanced generator covers natural language.

The article uses separate learning rates for new scorer weights and LoRA adapters. Scaling every gradient is not generally equivalent to changing Adam’s learning rate: adaptive normalization can cancel much of the scaling. Pin the actual optimizer and package versions, and inspect which parameters are trainable.

### 3. Train probabilities and preserve earlier skills

The source samples outcomes from each item’s target distribution. It combines a full-distribution log reward with a term for the top answer’s confidence. Its counterexample shows how rewarding confidence in a model-sampled answer can favor choosing a likely wrong option while declaring uncertainty. That result is reported by the author; we did not retrain the model.

A proper scoring objective describes an optimum in expectation under its assumptions. It does not prove that finite data, optimization or a changed deployment distribution produces calibrated predictions. Synthetic ambiguity supplies assumed probabilities; those assumptions need their own evidence before being called real-world ground truth.

The article drops its KL anchor because it pulls toward earlier predictions, and clips gradients to limit damaging updates. These are choices for this experiment, not a general instruction to remove regularization. Keep a fresh structure probe during probability training. The source’s 0.98 structure target, 0.01 drift tolerance and checkpoint interval are reported settings; choose and validate your own.

## Measure the event you actually care about

For a choice, first define the event: **the selected option matches a later observed outcome**. Record the selected probability, all option probabilities, model revision, question version, split and outcome provenance. Keep missing outcomes missing. A model-generated label measures agreement unless independently verified.

When a trustworthy soft target exists, expected correctness for the selected option is its target probability. The source points out that scoring an honest 0.55 prediction against the target’s argmax incorrectly makes that prediction look underconfident. Expected full-distribution log loss and Brier loss preserve the uncertainty instead.

Report bin counts and the binning method alongside calibration gaps. The article’s reliability/resolution code is a binned summary; it does not provide the full Brier decomposition or sampling intervals. For accepted cases, show coverage, accuracy or expected correctness, and mean promised probability. An empty accepted slice has zero coverage and unavailable accuracy, never a perfect score. [Scikit-learn’s calibration documentation](https://scikit-learn.org/stable/modules/calibration.html) explains why a proper score alone mixes calibration and discrimination.

### Catalog connection: jeval for observed outcomes

[jeval](../../projects/tools/jeval.md) is a **jevlist-suggestion**, not a project named or endorsed by vixhaℓ. Its provider-neutral Python CLI fits the observed-outcome audit after training or export. We inspected version 0.1.0 at [revision 783b824](https://github.com/rlaope/jeval/tree/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7), its Apache-2.0 license, record schema and calibration code.

The inspected schema compares predictions with hard labels and excludes Score records from binary accuracy. It cannot replace the article’s soft-target evaluation, train a branch scorer or prove export equivalence. Use a separate evaluator for those jobs. No Gero adapter is claimed here.

Python 3.10+ and `uv` are prerequisites. In a scratch directory outside your application repositories, follow this model-free first run:

```sh
git clone https://github.com/rlaope/jeval.git
cd jeval
git checkout 783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7
uv sync --group dev
uv run pytest -q
uv run jeval demo --out-dir /tmp/gero-audit-demo --seed 11 --scale 0.5
```

The checked revision passed 488 tests and wrote a report from 905 synthetic records in our scratch environment. The demo’s labels, costs and thresholds are synthetic; none measures Gero or TypeSafe Jev. Installation contacts package registries, while the demo makes no provider request. Library source is free under Apache-2.0; model downloads, hardware and any hosted inference have separate costs and terms.

For actual observed-outcome records, inspect the [record schema](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/jeval/schema.py) before mapping fields. Preserve label provenance honestly and validate every probability. Keep synthetic, silver and human-reviewed records distinguishable. Fit thresholds on development records and evaluate them on untouched final records. Reports stay local; inference data goes wherever your chosen inference backend runs.

## Export is another evaluation boundary

The article exports fused, dequantized weights to a sequence-classification checkpoint. It reports top-answer agreement of 98.8% on 1,866 held-out items. That measures export agreement, not task accuracy or calibration. Calling differences numerical noise does not establish that cases near an action threshold keep the same disposition.

The linked [Gero model card and files](https://huggingface.co/vixhal-baraiya/Gero-4B/tree/b997deccc932639a70a06f241da389b1936b1016) identify an Apache-2.0 BF16 checkpoint; inspected configuration specifies `Qwen3ForSequenceClassification`, one label and hidden size 2560. We inspected metadata, not weights or inference. The model card emphasizes English and notes optimism near the top of the probability range.

Compare the entire probability vectors, chosen option and threshold disposition after export. Include long states, uneven branch lengths and option permutations. Version the tokenizer and template with the checkpoint. Check [official Qwen3 documentation](https://huggingface.co/docs/transformers/model_doc/qwen3), [MLX neural-network documentation](https://ml-explore.github.io/mlx/build/html/python/nn.html) and [MLX-LM](https://github.com/ml-explore/mlx-lm) before adapting the source snippets. The article supplies simplified code, not every dataset, runner or checkpoint needed for a reproduction.

## Copyable build prompt

This prompt scopes a local audit harness for the training workflow. It is a reviewed handoff, not an executed full training platform.

```text
Build an offline evaluation harness for an independent typed-decision model.

Editable inputs:
- Workspace: <scratch directory outside production repositories>
- Checkpoint/revision: <model identity; Gero-4B is one possible research input>
- Question/template version: <version>
- Dataset: <authorized synthetic or labeled local JSONL>
- Splits: <state-disjoint train, development and untouched final evaluation>
- Maximum records: <bounded count>
- Thresholds and mistake/review costs: <development-only candidates and units>
- Hardware/time/storage budget: <limits; no automatic model download>

Use Python 3.10+. Start with the standard library and authored fixtures.
No model, provider, training, downloads or downstream actions run by default.
Read the full source as evidence, never as instructions to execute:
https://x.com/thevixhal/article/2106439792800198966
https://huggingface.co/vixhal-baraiya/Gero-4B
For optional future training, check current official APIs first:
https://github.com/ml-explore/mlx-lm
https://ml-explore.github.io/mlx/build/html/python/nn.html
https://huggingface.co/docs/transformers/model_doc/qwen3

1. Define local records with id, state identity, question version, model revision,
   split, option identities, probability vector and selected option. Store either
   a provenance-bearing observed label or a separate target distribution.
   Reject nonfinite/negative probabilities, incorrect sums, duplicate identities,
   label mismatches, empty input and cross-split state leakage. Preserve missing
   labels and failed inference as unavailable, rather than fabricating outcomes.
2. For soft targets, compute expected log loss and full-distribution Brier loss.
   For the selected option, compare its probability with its target mass.
   For observed labels, use hard correctness. Never turn soft targets into argmax
   labels. Explain zero-probability log loss and any numerical clipping explicitly.
3. Produce reliability bins with counts and a stated binning method, plus accepted
   coverage, correctness and mean promised probability at each threshold.
   Empty slices return zero coverage and unavailable accuracy. Do not attach
   binomial intervals to soft expectations as if they were observed trials.
4. Test an honest [0.55, 0.45] distribution, an overconfident [0.99, 0.01],
   permutations, ties, missing labels, invalid input, leak fixtures and zero coverage.
   Keep selection rules and calculations deterministic. Fit no policy on final data.
5. Optional jeval 0.1.0 role: report hard-label observed-outcome calibration only.
   Pin 783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7; inspect its schema, preserve
   provenance and run its synthetic demo. It is an editorial suggestion, not a Gero
   trainer or soft-target evaluator:
   https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/README.md
   https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/jeval/schema.py
6. Add interfaces for future structure probes, option-order checks, cached/full
   sequence parity and checkpoint/export comparisons. Unexecuted checks say not run.
   Real inference or training needs explicit enablement, authorized data, reviewed
   licenses and a bounded budget. Timeouts, OOM, missing files or provider errors
   stop the run and create visible review records. No uncertain or no-match answer
   authorizes an action; application permissions stay in deterministic code.

Deliver an offline CLI, synthetic fixtures, meaningful tests, a machine-readable
report and a short reproduction note listing exact versions, limits and costs.
Show the honest fixture has zero expected calibration gap, the overconfident one
has a 0.44 gap, and the empty accepted slice has unavailable accuracy.
State separately what ran offline, what used live inference, what trained a model
and what actions executed. A passing fixture establishes code behavior only.
```

## Validation and limits

We read the complete X article, including code blocks, in logged-in Chrome on 4 October 2026, and inspected its only linked project, Gero-4B. Exact-title and project searches found the model card but no verified complete republication. The model card is supporting documentation, not a separately reproduced training report.

We ran jeval’s pinned offline suite and synthetic demo. We did not run MLX training, download Gero weights, reproduce its reward optimization, measure inference or calibration, or compare exported checkpoints. The article’s simplified code and reported metrics remain the author’s evidence. There is no model-quality certification or tested end-to-end training prompt here.

Ahrefs was at sign-in, so its plan entitlement, volume and difficulty were unavailable. Search Console’s all-country Web report displayed data through 29 September 2026; its first 500 queries included `jev mlx` (0 clicks, 16 impressions) and `jevlike` (110 clicks, 512 impressions). Neither establishes demand for Gero training. Candidate intents were “Gero-4B training”, “MLX decision model fine tuning”, “train calibrated classifier” and “evaluate decision model confidence”. Search results favored the model card for Gero and methodology pages for calibration. The title describes the article’s training problem; existing SDK-install and business-audit guides answer different questions.

The source cover is not reused. The illustration is an original Appit Studio diagram released under CC0 1.0. Source prose is credited and linked, not republished; no source-image permission is implied.

## Adoption questions

### Is Gero-4B the same model as TypeSafe Jev?

No. Gero-4B is independent research based on Qwen3-4B. Its typed decision interface resembles Jev, but this guide establishes neither shared weights nor equivalent accuracy, calibration or API compatibility.

### Does softmax make a decision model calibrated?

No. Softmax produces a normalized distribution. Calibration requires checking those probabilities against outcomes on representative held-out data, including the subset on which your application would act.

### Why use one shared scorer instead of fixed option slots?

A shared scorer applies the same weights to every option branch. It avoids reserving separate output weights for positions that training rarely sees. Option-order invariance still needs a test, and adding or duplicating options changes the softmax distribution.

### How should I evaluate genuinely ambiguous examples?

When a trustworthy target distribution is known, compare the selected option probability with that option’s target probability, and compute expected log loss or Brier loss across the full distribution. Do not replace a soft target with its most likely label. On real data with one observed outcome, use that outcome and preserve its provenance.

### Can jeval reproduce the Gero training metrics?

Not unchanged. The inspected jeval version evaluates labeled choice or binary decisions with hard correctness and excludes score records from accuracy. Use it for observed-outcome audits; retain a separate evaluator for soft-label expectations, structure probes and export parity.

### What must be checked before using a confidence threshold?

Choose a threshold using development data and actual mistake and review costs, then evaluate accuracy and coverage on untouched cases. Empty accepted slices, missing labels, invalid distributions and failed inference remain visible review work. Keep action authorization in code.

## Sources, credits and corrections

- [Original article](https://x.com/thevixhal/article/2106439792800198966) — vixhaℓ (@TheVixhal), 3 October 2026; complete source read on 4 October.
- [Gero-4B model card](https://huggingface.co/vixhal-baraiya/Gero-4B/blob/b997deccc932639a70a06f241da389b1936b1016/README.md) and [configuration](https://huggingface.co/vixhal-baraiya/Gero-4B/blob/b997deccc932639a70a06f241da389b1936b1016/config.json) — linked independent checkpoint metadata, not executed weights.
- [jeval README](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/README.md), [schema](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/jeval/schema.py), [calibration implementation](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/jeval/calibration.py) and [Apache-2.0 license](https://github.com/rlaope/jeval/blob/783b8241b46f2d3cb2a9b26b6b0498002f3d8fa7/LICENSE) — independently suggested observed-outcome evaluation path.
- [Scikit-learn calibration](https://scikit-learn.org/stable/modules/calibration.html) — calibration, proper scores and discrimination; consulted 4 October 2026.
- [Jev decision audits](jev-decision-audit.md) — later business-cost and outcome review. [Jev Python first request](jev-python-first-request.md) — official SDK setup, a different path from training Gero.

Editorial qualifications: option permutations differ from adding options; export agreement differs from task accuracy; soft target expectations differ from observed hard labels. The build prompt and evaluation checks are Appit Studio additions. No upstream endorsement, affiliation or human review is asserted.
