# call-eval

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Post-call customer-experience evaluation for contact-centre transcripts: Jev (or an offline rule extractor) pulls typed facts with evidence spans, deterministic code turns them into satisfaction and sentiment scores, and a calibration layer anchors scores to surveys — all on synthetic data with a sealed holdout.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/henryzhangpku/call-eval) |
| Product homepage | [henryzhangpku.github.io](https://henryzhangpku.github.io/call-eval/) |
| Maintainer | [henryzhangpku](https://github.com/henryzhangpku). Independently curated. |
| Format | Python package and CLI (`python -m calleval`), committed synthetic data, Jev response cache and static demo |
| Requirements | Python 3 with `pip install -e .`; no key for the offline backend; `TYPESAFE_API_KEY` for live Jev calls on cache misses. |
| License | [MIT](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Prototype auditable contact-centre QA where the model extracts facts and code does the scoring.
- Compare a rule-based extractor with Jev on the same synthetic calls, dev split and sealed holdout.
- Mismatch: all data is synthetic (400 generated calls, simulated annotators and surveys); numbers do not describe real callers.

## How it works

[`calleval/extract/jev.py`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/calleval/extract/jev.py) asks Jev typed questions per call segment (was each request resolved, caller effort, stated feeling) with evidence locations; [`calleval/scoring.py`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/calleval/scoring.py) and [`calleval/calibration.py`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/calleval/calibration.py) turn those facts into scores and anchor them to survey answers. The Jev backend replays [`cache/jev_cache.jsonl`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/cache/jev_cache.jsonl) and calls the API only on a miss; design decisions are logged in [`DECISIONS.md`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/DECISIONS.md).

## Get started

Run end to end offline, then with Jev (cache first):

```sh
git clone https://github.com/henryzhangpku/call-eval.git && cd call-eval
python -m venv .venv && .venv/bin/pip install -e ".[dev]"
python -m calleval run --backend offline   # no key, no network
python -m calleval run --backend jev       # replays cache; API only on a miss
python -m calleval evaluate
```

The offline backend and cached Jev runs make no API calls; cache misses are billed to your TypeSafe key.

## Examples and demos

- Static demo site (GitHub Pages) linked as the product homepage; README *What it proves, measured* (kappa vs human ceiling on dev and sealed holdout).
- Methodology: [`METHODOLOGY.md`](https://github.com/henryzhangpku/call-eval/blob/abba9792be56f87c2512e390a7916bdeeb112ab6/METHODOLOGY.md).

## Limits and data handling

Agreement numbers are the maintainer's, on synthetic template-generated calls (optimistic for any extractor); the offline rules were written against those templates. Transcript segments go to TypeSafe on live runs. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit abba9792be56](https://github.com/henryzhangpku/call-eval/tree/abba9792be56f87c2512e390a7916bdeeb112ab6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
