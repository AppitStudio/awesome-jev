# jev-lite by Nefelim584 (395M ModernBERT typed decision model benchmarked against the Jev API)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small typed decision model built to replace an LLM-as-a-judge on narrow checks: given a state and bool, choice or score questions, it returns calibrated probabilities and a confidence score from a ModernBERT-large encoder with three heads. Scripts run the same sampled test records through Jev's API for paired accuracy, speed and repeatability comparisons with NLI and Laya baselines. Distinct from Atulmishra22/jev-lite.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nefelim584/JEV_Judge) |
| Maintainer | [Nefelim584](https://github.com/Nefelim584). Independently curated. |
| Format | Python package (`jevlite`) + Hugging Face model |
| Requirements | Python with uv or pip; a CUDA or Apple Silicon machine for local runs; `typesafe-sdk` and `TYPESAFE_API_KEY` only for the Jev comparison. |
| License | [Apache-2.0](https://github.com/Nefelim584/JEV_Judge/blob/fc07ec879a4d394586c8014fbcbef33a642abffc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/predict_jev_api.py`](https://github.com/Nefelim584/JEV_Judge/blob/fc07ec879a4d394586c8014fbcbef33a642abffc/scripts/predict_jev_api.py) at the pinned commit. |

## When to use

- Run cheap local narrow-judge checks and see where they match hosted Jev.
- Mismatch: English only; trained for its own templates and sources.

## How it works

`scripts/predict_jev_api.py` samples stratified test records, sends them to Jev with `typesafe-sdk`, and stores predictions that `scripts/compare_paired.py` scores against jev-lite, NLI and Laya; Apple Silicon notebooks time Jev's API latency next to local models. Integration evidence: [`scripts/predict_jev_api.py`](https://github.com/Nefelim584/JEV_Judge/blob/fc07ec879a4d394586c8014fbcbef33a642abffc/scripts/predict_jev_api.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "jevlite @ git+https://github.com/Nefelim584/JEV_Judge.git@v0.2.0"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model: [huggingface.co/Nefelim584/jev-lite](https://huggingface.co/Nefelim584/jev-lite)

## Limits and data handling

Only the comparison scripts call TypeSafe. The README states the project is not affiliated with TypeSafe AI.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit fc07ec879a4d](https://github.com/Nefelim584/JEV_Judge/tree/fc07ec879a4d394586c8014fbcbef33a642abffc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
