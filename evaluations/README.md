# Evaluate support routing

Measure the [support router](../projects/support-router/README.md) on tickets you
label before making API calls. Python 3.10+ and its standard library are sufficient.
The default mode uses a uniform synthetic response and requires no API key. Its
metrics test the plumbing; they are **not evidence of Jev's quality**.

```bash
python3 evaluations/run.py \
  --dataset evaluations/sample.jsonl \
  --output-dir /tmp/jev-evaluation-demo
```

The two [format examples](sample.jsonl) are not a representative benchmark. Use a
new or empty output directory for every run: existing results are never overwritten.

## Prepare a private dataset

Keep real tickets and evaluation results outside this repository. Each JSONL line
is one object with these fields:

| Field | Meaning |
| --- | --- |
| `id` | Unique, nonempty string. |
| `split` | `development` or `holdout`. |
| `slice` | A useful subgroup such as `multiple-intents` or `clear-billing`. |
| `message` | The ticket text. |
| `expected_department` | A department key in the router configuration. |
| `expected_urgency` | `high` or `ordinary`. |
| `require_review` | Optional boolean; true when automatic handling is inappropriate. |

Cover clear requests, missing evidence, unrelated requests, overlapping requests,
explicit operational urgency, and ambiguous urgency. Agree on the labeling policy
before inspecting answers. Avoid near duplicates across splits. The model receives
only the ticket text and the configured questions: labels, split, slice, and ticket
ID are excluded from its state.

Use development cases to inspect mistakes and adjust questions or thresholds. Freeze
the configuration before evaluating holdout cases. This runner does not tune any
parameters; do not select settings based on holdout results. If those results inform
a change, author a fresh holdout set for the next assessment.

## Run live or replay saved responses

Set `TYPESAFE_API_KEY` in your shell or secret manager, then explicitly select live
mode. The runner never reads `.env` files or prints credentials.

```bash
python3 evaluations/run.py \
  --dataset /private/jev/tickets.jsonl \
  --output-dir /private/jev/development-run-01 \
  --split development --mode live --max-calls 30
```

Each selected case makes at most one HTTP attempt with a 30-second timeout. There
are no retries, including for rate limits or overload. The default budget is 50 and
`--max-calls` accepts 1–50. Exceeding the budget fails before any request is sent;
nothing is silently sampled. Split a larger dataset into deliberate batches. A
failed request might still have been processed and billed by the provider.

Output paths inside the repository are rejected in every mode, including symlinked
paths. Keep replay files and datasets in a private location too. Use
`--config /private/jev/config.json` for a complete custom router configuration and
`--model` to select an explicitly named model. Both requested and returned model
names are recorded; a mismatch is visible rather than silently normalized.

```bash
python3 evaluations/run.py \
  --dataset /private/jev/tickets.jsonl \
  --output-dir /private/jev/development-replay-01 \
  --split development --mode replay \
  --replay-from /private/jev/development-run-01/records.jsonl
```

Replay uses no network and needs no key. It requires exactly matching requests,
labels, and splits. Development replay can compare threshold changes without new
inference, provided the state and questions remain identical. Holdout replay also
requires the original configuration. Saved service failures remain failures during
replay. Replaying synthetic responses remains marked as synthetic evidence.

## Inspect the results

Each run writes three files to your chosen directory:

- `manifest.json`: configuration, selected dataset fingerprint, question fingerprint,
  requested model, timestamps, and the HTTP attempt count.
- `records.jsonl`: each request, response, decision, expected labels, exact model
  names, token usage, latency, and separate service, contract, or policy errors.
- `summary.json`: overall and per-slice metrics with explicit numerators and denominators.

Coverage and review rate use **all selected cases**, including failures. Their sum
plus the unresolved rate is one. Department accuracy and its confusion matrix use
successful cases; the matrix's rows are expected labels and its columns are raw
predictions before review policy. Wrong automatic assignments use automatic cases
as the denominator. Unsafe automatic decisions also count cases labeled as requiring
review, even when the selected department agrees with its label.

Urgency errors use successful cases with a decided urgency; urgency review is counted
separately. High-urgency downgrades and reviews use successful high-urgency cases.
Cases requiring review use successful cases with `require_review: true`. Inspect
errors alongside these metrics: excluded failures are not successful decisions.
An empty denominator produces JSON `null`, never a misleading zero accuracy.

Token counts cover responses whose usage passed validation. Mock counts are zero;
replay counts represent the saved inference, not new consumption. Live latency covers
the HTTP attempt and local validation; replay preserves it as `source_latency_ms` in
each record and does not mix it with new live measurements. Exit status is nonzero
when any case has a service, contract, or policy error. Quality metrics do not impose
an arbitrary pass/fail gate.

Inspect the raw state, questions, answer distribution, and review reason for each
mistake. A small synthetic dataset verifies an integration and helps find failures;
it does not establish production accuracy, calibrated confidence, or stable latency.
See TypeSafe's [confidence guidance](https://docs.typesafe.ai/confidence) and
[HTTP API reference](https://docs.typesafe.ai/api).

## Test offline

```bash
python3 -m unittest discover -s evaluations/tests -v
```
