# Albanian sentiment analysis with Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible study classifying Albanian COVID-19 Facebook comments (AlbAna, three-annotator labels) with TypeSafe Jev and no training, re-running the 20 classifiers of Kastrati et al. (2021) on the paper's own test split; maintainer reports Jev at 75.71 weighted F1 vs 72.08 for mBERT, with paired-bootstrap intervals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uran-lajci/albanian-sentiment-analysis-jev) |
| Maintainer | [uran-lajci](https://github.com/uran-lajci). Independently curated. |
| Format | Python package `sentiment` (uv) with stored predictions in `results/` |
| Requirements | uv; `TYPESAFE_API_KEY` only to re-run Jev classification (the comparison runs from stored results). |
| License | [MIT](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/blob/4cc3a83414e20d157d5ed10e46637ba744764a5e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Evaluate Jev for sentiment in a language with little training data.
- Reuse the split, baselines and bootstrap comparison for your own dataset.
- Mismatch: one dataset and domain; results are the maintainer's.

## How it works

[`sentiment/classify.py`](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/blob/4cc3a83414e20d157d5ed10e46637ba744764a5e/sentiment/classify.py) asks Jev for neutral/positive/negative per comment; [`train_baselines.py`](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/blob/4cc3a83414e20d157d5ed10e46637ba744764a5e/sentiment/train_baselines.py) and [`train_mbert.py`](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/blob/4cc3a83414e20d157d5ed10e46637ba744764a5e/sentiment/train_mbert.py) re-run the paper's models over 5 seeds; [`compare_with_paper.py`](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/blob/4cc3a83414e20d157d5ed10e46637ba744764a5e/sentiment/compare_with_paper.py) produces the tables.

## Get started

Reproduce the reported numbers from stored results (README *Reproduce*):

```sh
git clone https://github.com/uran-lajci/albanian-sentiment-analysis-jev.git && cd albanian-sentiment-analysis-jev
uv sync
uv run python -m sentiment.compare_with_paper
```

Re-running Jev classification over the test split is billed to your TypeSafe key; the comparison from stored results is free.

## Examples and demos

- README *Results* (weighted/macro F1, accuracy, bootstrap intervals) and *Evaluation setup*.

## Limits and data handling

Maintainer-measured results on the 2021 AlbAna release; comment text is sent to TypeSafe when re-running. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 4cc3a83414e2](https://github.com/uran-lajci/albanian-sentiment-analysis-jev/tree/4cc3a83414e20d157d5ed10e46637ba744764a5e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
