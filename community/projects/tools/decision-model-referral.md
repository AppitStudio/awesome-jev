# Decision-model referral on medical exams

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, recorded runs and manuscript for a preprint (Sangzin Ahn, 2026) comparing TypeSafe Jev, OpenAI Decisions and Cloudflare Clef on 435 KorMedMCQA and 1,273 MedQA questions, using each model's selected-option probability to refer its least confident 20% of answers to a stronger model versus random and oracle referral.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mahlernim/decision-model-referral) |
| Maintainer | [mahlernim](https://github.com/mahlernim). Independently curated. |
| Format | Python analysis scripts, per-request run records and manuscript sources |
| Requirements | Python 3.12+ and `requirements.txt`; no API access to reproduce the analysis. Collecting new responses needs TypeSafe, OpenAI and Cloudflare credentials. |
| License | [MIT](https://github.com/mahlernim/decision-model-referral/blob/50e7e325cb7a47d3e9855978af9106b2f4e2bb8a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Check how well Jev's answer probabilities support referral of uncertain answers on a hard benchmark.
- Reuse the referral analysis on your own decision-model runs.
- Mismatch: medical exam questions are a benchmark, not clinical use; results are the author's preprint, not verified here.

## How it works

[`paper/evidence.py`](https://github.com/mahlernim/decision-model-referral/blob/50e7e325cb7a47d3e9855978af9106b2f4e2bb8a/paper/evidence.py) recomputes every reported number from `runs/` and `docs/`; [`jevbench/medical_order.py`](https://github.com/mahlernim/decision-model-referral/blob/50e7e325cb7a47d3e9855978af9106b2f4e2bb8a/jevbench/medical_order.py) collected Jev option-rotation and repeat requests.

## Get started

Recompute the evidence offline (README *Reproducing the paper*):

```sh
git clone https://github.com/mahlernim/decision-model-referral && cd decision-model-referral
pip install -r requirements.txt
cd paper && python evidence.py && python validate.py
```

Reproducing the analysis makes no API calls; collection scripts call paid providers.

## Examples and demos

- README *Layout* and *Reproducing the paper*.
- Per-question results: [`docs/comparator-refresh-v1/unified/`](https://github.com/mahlernim/decision-model-referral/tree/50e7e325cb7a47d3e9855978af9106b2f4e2bb8a/docs/comparator-refresh-v1/unified).

## Limits and data handling

KorMedMCQA questions are CC BY-NC 2.0 (no commercial use); MedQA is MIT; physician ratings keep their original terms. Reported accuracy and referral results are upstream claims; analysis not rerun on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 50e7e325cb7a](https://github.com/mahlernim/decision-model-referral/tree/50e7e325cb7a47d3e9855978af9106b2f4e2bb8a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
