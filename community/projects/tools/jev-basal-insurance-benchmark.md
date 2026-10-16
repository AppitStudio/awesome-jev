# Jev vs Basal insurance benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Polish motor-insurance (autocasco) decision benchmark: 325 synthetic typed decisions built from public policy terms, with code-computed labels, run against Jev, Basal 2.0 and Gemini models with accuracy, calibration (ECE) and latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marcinnowak79/jev-basal-insurance-benchmark) |
| Maintainer | [marcinnowak79](https://github.com/marcinnowak79). Independently curated. |
| Format | Python scripts + dataset (`zestaw.jsonl`) and raw results; README in Polish with English summary |
| Requirements | Python; a TypeSafe key to rerun Jev; GPU and Basal engine for the Basal runs; Gemini key for Gemini runs. |
| License | [MIT](https://github.com/marcinnowak79/jev-basal-insurance-benchmark/blob/a691c6602fa18ca20eac2ffc3c43587194424d4e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/mnowak13/status/2110736273556324647)). |
| Jev evidence | [`uruchom.py`](https://github.com/marcinnowak79/jev-basal-insurance-benchmark/blob/a691c6602fa18ca20eac2ffc3c43587194424d4e/uruchom.py) at the pinned commit. |

## When to use

- See how Jev handles deadline, start-of-cover, total-loss and exclusion rules compared with an open decision model and general LLMs.
- Reuse the generator and `/v1/systemone`-format dataset to test your own decision model.
- Mismatch: one insurer's rules and synthetic data; results are the author's (15 Oct 2026) and were not reproduced here.

## How it works

`zbuduj.py` generates the dataset with a fixed seed; `uruchom.py` posts each line as a `/v1/systemone` request (`jev-latest` at `api.typesafe.ai`, or a local Basal server), and `analiza.py` reports per-family accuracy, cascade thresholds, twin consistency and ECE. Integration evidence: [`uruchom.py`](https://github.com/marcinnowak79/jev-basal-insurance-benchmark/blob/a691c6602fa18ca20eac2ffc3c43587194424d4e/uruchom.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/marcinnowak79/jev-basal-insurance-benchmark.git && cd jev-basal-insurance-benchmark
python zbuduj.py
python uruchom.py Jev https://api.typesafe.ai/v1/systemone typesafe_key.txt 4
python analiza.py wynik_Jev.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Raw results for every model: `wyniki/`.

## Limits and data handling

Only synthetic cases are sent, to TypeSafe or Google on your keys; Basal runs locally.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit a691c6602fa1](https://github.com/marcinnowak79/jev-basal-insurance-benchmark/tree/a691c6602fa18ca20eac2ffc3c43587194424d4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
