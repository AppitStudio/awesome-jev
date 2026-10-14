# JEVPFN

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research code testing whether label-free Jev features extracted from text improve tabular predictors such as TabPFN and CatBoost on MulTaBench text datasets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andreasgoethals/JEVPFN) |
| Maintainer | [andreasgoethals](https://github.com/andreasgoethals). Independently curated. |
| Format | Research repository (Python) |
| Requirements | Python; TypeSafe key for feature extraction; tabular model dependencies. |
| License | [MIT](https://github.com/andreasgoethals/JEVPFN/blob/7002eaf4faaded54f1f1414c5636792a221c88a0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/extraction.py`](https://github.com/andreasgoethals/JEVPFN/blob/7002eaf4faaded54f1f1414c5636792a221c88a0/src/jev/extraction.py) at the pinned commit. |

## When to use

- Reproduce Jev-derived text features for tabular ML benchmarks.
- Mismatch: research exploration; results are author-reported.

## How it works

Jev answers typed questions about each text field; code turns probabilities into features and compares fixed predictors on identical folds. Integration evidence: [`src/jev/extraction.py`](https://github.com/andreasgoethals/JEVPFN/blob/7002eaf4faaded54f1f1414c5636792a221c88a0/src/jev/extraction.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see README and config/ for experiment runs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configs: `config/`.
- Notebooks: `notebooks/`.

## Limits and data handling

Dataset text is sent to TypeSafe during extraction.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 7002eaf4faad](https://github.com/andreasgoethals/JEVPFN/tree/7002eaf4faaded54f1f1414c5636792a221c88a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
