# Fraud and IVR intent benchmark by GopalAlag (Jev zero-shot against gradient boosting and four LLMs on card-fraud classification, plus an IVR intent-routing study)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experiment comparing classic gradient boosting, zero-shot Jev and four LLMs (Claude Haiku 5.5 and Sonnet 5.5, GPT-6 Luna, Gemini 3.1 Flash-Lite with few-shot prompts and caching) on simulated card transactions, over three fresh data draws with thresholds tuned on a separate calibration slice. In the final run Jev was the cheapest and fastest by a wide margin (about $0.02 per 1,000 transactions, 0.13 s) but the least accurate (F1 0.685 against 0.941 for gradient boosting and 0.83 for the best LLM); the author suggests it as a first-pass filter or router. A second study covers IVR intent routing; slide decks and per-call audit logs are included.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GopalAlag/FrontierLLMvsJEV) |
| Maintainer | [GopalAlag](https://github.com/GopalAlag). Independently curated. |
| Format | Python research code (pyproject) with results, report and slide decks |
| Requirements | Python, `TYPESAFE_API_KEY` and the LLM providers' keys (systems without a key are skipped), and the public Hugging Face dataset. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_fraud/jev_module.py`](https://github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/src/jev_fraud/jev_module.py) at the pinned commit. |

## When to use

- See where a zero-shot Jev Noul sits against trained and prompted models on a tabular fraud task.
- Mismatch: production fraud models; the data is simulated and fraud-enriched to 20%.

## How it works

`src/jev_fraud/jev_module.py` uses `langchain-typesafe`'s `TypeSafeClassifier` with a Noul question for P(fraud) and `jev-latest`, recording cost from the real usage field; `src/ivr_intent/models/jev.py` does the same for intent routing. Integration evidence: [`src/jev_fraud/jev_module.py`](https://github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/src/jev_fraud/jev_module.py).

## Get started

Install the package, add keys and run the experiment.

```sh
git clone https://github.com/GopalAlag/FrontierLLMvsJEV && cd FrontierLLMvsJEV
pip install -e .
cp .env.example .env    # TYPESAFE_API_KEY, ANTHROPIC_API_KEY, ...
python -m jev_fraud.run_experiment --iterations 3 --n-eval 300
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/README.md](https://github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/README.md)
- Full report: [github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/REPORT.md](https://github.com/GopalAlag/FrontierLLMvsJEV/blob/79f29bba12123cd291488defd7df17d8added47c/REPORT.md)

## Limits and data handling

Only authorisation-time fields go to the models; names, card numbers and addresses are never sent. Small samples (48–53 fraud cases per iteration) per the author's own limitations section. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 79f29bba1212](https://github.com/GopalAlag/FrontierLLMvsJEV/tree/79f29bba12123cd291488defd7df17d8added47c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
