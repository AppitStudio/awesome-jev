# System One vs classical ML (customer-triage benchmark of Laya against logistic regression and XGBoost)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Controlled benchmark on 3,000 synthetic Turkish customer messages: five triage decisions handled by classical ML (logistic regression, XGBoost) and by the Laya System One model, zero-shot and fine-tuned, with F1, calibration error and reliability diagrams. Laya uses the Jev question format (choice, score, noul). Includes the data generator, scripts and a write-up.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dursunkoc/system-one-vs-classical-ml-demo) |
| Maintainer | [dursunkoc](https://github.com/dursunkoc). Independently curated. |
| Format | Python scripts, synthetic data and charts |
| Requirements | Python with uv; a GPU (or Apple MPS) for fine-tuning. |
| License | [MIT](https://github.com/dursunkoc/system-one-vs-classical-ml-demo/blob/4e03d0654c4a6a59597b777ae1b6e946a25a840e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`02_laya.py`](https://github.com/dursunkoc/system-one-vs-classical-ml-demo/blob/4e03d0654c4a6a59597b777ae1b6e946a25a840e/02_laya.py) at the pinned commit. |

## When to use

- Decide whether a System One model beats a trained classifier for your triage task, and when.
- Mismatch: synthetic data in Turkish; evaluates Laya, not TypeSafe's Jev.

## How it works

`02_laya.py` loads `laya-multilingual` and asks the triage questions in Jev-style typed form; `03_compare.py` builds the comparison charts. Integration evidence: [`02_laya.py`](https://github.com/dursunkoc/system-one-vs-classical-ml-demo/blob/4e03d0654c4a6a59597b777ae1b6e946a25a840e/02_laya.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/dursunkoc/system-one-vs-classical-ml-demo && cd system-one-vs-classical-ml-demo
uv sync
uv run python 01_classical_ml.py && uv run python 02_laya.py && uv run python 03_compare.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [github.com/dursunkoc/system-one-vs-classical-ml-demo/blob/main/article.md](https://github.com/dursunkoc/system-one-vs-classical-ml-demo/blob/main/article.md)

## Limits and data handling

Runs locally; nothing goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 4e03d0654c4a](https://github.com/dursunkoc/system-one-vs-classical-ml-demo/tree/4e03d0654c4a6a59597b777ae1b6e946a25a840e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
