# System One multilingual sentiment benchmark (Jev, Clef and Clef-flash against five LLMs on three-class sentiment in European languages)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Conference study comparing System One decision models (Jev, Clef, Clef-flash) with the five LLMs of Kastrati et al. (2026) on three-class sentiment, zero-shot and few-shot, on 8 European languages (12,970 items), plus a structured question-tuning experiment for Jev. Data for an extension to 35 languages is prepared. Committed results, the LaTeX paper and table scripts are in the repo; in the zero-shot table Jev's mean macro-F1 is 61.7 against 64.0–64.1 for the best LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uran-lajci/system-one-multilingual-sentiment) |
| Maintainer | [uran-lajci](https://github.com/uran-lajci). Independently curated. |
| Format | Python experiments (uv) with committed results and paper |
| Requirements | Python with uv, a TypeSafe key for Jev (plus keys for the other models you rerun), and the public datasets placed in `data/`. |
| License | [CC0-1.0](https://github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`experiments/zero_shot/classify_sentiment.py`](https://github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/experiments/zero_shot/classify_sentiment.py) at the pinned commit. |

## When to use

- See how Jev compares with LLMs and other decision models on sentiment outside English.
- Mismatch: production sentiment scoring; this is a research comparison on fixed test sets.

## How it works

`experiments/zero_shot/classify_sentiment.py` calls `jev-1.14.0` through the TypeSafe Python SDK (`AsyncTypeSafeClient` with a Choice question); `paper/write_tables.py` computes macro-F1 and input-token cost. Integration evidence: [`experiments/zero_shot/classify_sentiment.py`](https://github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/experiments/zero_shot/classify_sentiment.py).

## Get started

Install, add keys, prepare the data, then run the zero-shot classifier.

```sh
git clone https://github.com/uran-lajci/system-one-multilingual-sentiment && cd system-one-multilingual-sentiment
uv sync
cp .env.example .env    # API keys
uv run python -m data_prep.select_paper_test_sets
uv run python -m experiments.zero_shot.classify_sentiment -m jev-1.14.0
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/README.md](https://github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/README.md)
- Zero-shot scores: [github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/results/zero_shot/baseline/scores.csv](https://github.com/uran-lajci/system-one-multilingual-sentiment/blob/85c07f877fc81f50e2ecde15fd15f419915f3b63/results/zero_shot/baseline/scores.csv)

## Limits and data handling

Test items go to TypeSafe and the other providers on your keys. Results are the authors' own and cover 8 languages so far. CC0 covers the repo's own material; datasets keep their original terms.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 85c07f877fc8](https://github.com/uran-lajci/system-one-multilingual-sentiment/tree/85c07f877fc81f50e2ecde15fd15f419915f3b63). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
