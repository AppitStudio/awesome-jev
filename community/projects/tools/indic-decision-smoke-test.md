# Indic decision-model smoke test by Citruz AI (English, Hindi and Tamil sentiment and request routing across Jev, other decision models and chat LLMs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Explainer plus a small live smoke test (n=80 per language) that runs Jev 1.14, Microsoft Decision 1.1, Perplexity and Baseten deciders, Sarvam Prism and several chat LLMs on IndicSentiment and an Amazon MASSIVE routing sample, recording accuracy, latency, billed cost and calibration, with a dry-run cost estimator and spend caps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CitruzAI/indic-decision-models-smoke-test) |
| Maintainer | [Citruz AI](https://github.com/CitruzAI). Independently curated. |
| Format | Python scripts and results |
| Requirements | Python 3.12+, an OpenRouter key (and a Sarvam key for Prism) for live runs; dry runs need no key. |
| License | [MIT](https://github.com/CitruzAI/indic-decision-models-smoke-test/blob/4044649361d4903d6ef6874eb1d8adc3eae0233a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`indic_smoke/config.py`](https://github.com/CitruzAI/indic-decision-models-smoke-test/blob/4044649361d4903d6ef6874eb1d8adc3eae0233a/indic_smoke/config.py) at the pinned commit. |

## When to use

- Get a first look at how decision models behave on Hindi and Tamil text.
- Mismatch: if you need a benchmark or ranking; the authors say it is neither.

## How it works

`indic_smoke/config.py` calls Jev as `typesafe/jev-1.14` through OpenRouter's Decisions API, alongside the other models; no direct TypeSafe calls. Integration evidence: [`indic_smoke/config.py`](https://github.com/CitruzAI/indic-decision-models-smoke-test/blob/4044649361d4903d6ef6874eb1d8adc3eae0233a/indic_smoke/config.py).

## Get started

Create a virtual environment and do a dry run with a cost estimate.

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python run.py --task sentiment --dry-run --estimate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/CitruzAI/indic-decision-models-smoke-test/tree/4044649361d4903d6ef6874eb1d8adc3eae0233a/results](https://github.com/CitruzAI/indic-decision-models-smoke-test/tree/4044649361d4903d6ef6874eb1d8adc3eae0233a/results)

## Limits and data handling

The authors' own smoke test: accuracies sit near the ceiling, so language differences have wide intervals. Jev is reached via OpenRouter (a third-party host); OpenRouter Decisions is an alpha API.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 4044649361d4](https://github.com/CitruzAI/indic-decision-models-smoke-test/tree/4044649361d4903d6ef6874eb1d8adc3eae0233a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
