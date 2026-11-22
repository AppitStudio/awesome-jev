# ReflexBench by Brida (open benchmark of Jev and other System One engines on typed Choice, Score and Noul decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

ReflexBench v1.0.0 is a provider-neutral benchmark and harness for System One and typed decision engines such as TypeSafe Jev, Laya, Reflex/Qwen, Kev, jeff and Verdict. It reports semantic accuracy, calibration (NLL, Brier, ECE), option-order stability, multilingual consistency, failures and latency separately instead of one score, and keeps a separate lane for how much a tiny deterministic Reflex Core policy adds on the same response.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brida-ai/reflexbench) |
| Maintainer | [brida-ai](https://github.com/brida-ai). Independently curated. |
| Format | Python harness (standard library) + frozen corpora and results |
| Requirements | Python 3.11+; a System One-compatible HTTP endpoint and its key to run live engines (Jev was measured through the Vercel AI Gateway route). |
| License | [Apache-2.0](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`reflexbench/systemone_http.py`](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/reflexbench/systemone_http.py) at the pinned commit. |

## When to use

- Compare Jev with open decision models on the same frozen cases, including calibration and option-order robustness.
- Mismatch: a single leaderboard number; the project deliberately reports each dimension separately.

## How it works

`reflexbench/systemone_http.py` is a small client for any `/v1/systemone` endpoint used by `systemone_reflex_runner.py`; `engines.v1.json` records each engine's identity, route and revision, with hosted Jev kept distinct from third-party look-alikes. Results, manifests and hashes are committed under `results/` and `release/`. Integration evidence: [`reflexbench/systemone_http.py`](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/reflexbench/systemone_http.py).

## Get started

Run the offline test suite, then point the runner at a System One-compatible endpoint.

```sh
git clone https://github.com/brida-ai/reflexbench && cd reflexbench
PYTHONPATH=reflexbench python -m unittest discover -s tests -p 'test_*.py' -v
PYTHONPATH=reflexbench python reflexbench/systemone_reflex_runner.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/RESULTS.md](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/RESULTS.md)
- Methodology: [github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/METHODOLOGY.md](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/METHODOLOGY.md)
- Submit a model: [github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/SUBMIT_A_MODEL.md](https://github.com/brida-ai/reflexbench/blob/39b78f0fd6fd6720fd8452ec532d62fc9788dc28/SUBMIT_A_MODEL.md)

## Limits and data handling

Results are the authors' own same-corpus measurements (for example 73.0% raw semantic accuracy for TypeSafe Jev on the 111-case public-hard cohort), not a universal ranking. It was first built for Brida Reflex, a hosted service that has since been archived. Cases are sent to whichever engine you run.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 39b78f0fd6fd](https://github.com/brida-ai/reflexbench/tree/39b78f0fd6fd6720fd8452ec532d62fc9788dc28). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
