# jevclean (Pandas text cleaning)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library that maps messy Pandas text values onto your own vocabulary and classifies text into described categories, resolving exact matches, aliases and optional fuzzy matches locally and sending only distinct unresolved values to Jev, with caching and a review queue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hariPrasadCoder/jevclean) |
| Maintainer | [hariPrasadCoder](https://github.com/hariPrasadCoder). Independently curated. |
| Format | Python library (Pandas, RapidFuzz) |
| Requirements | Python 3.10+; `TYPESAFE_API_KEY` only for the optional Jev extra. |
| License | [MIT](https://github.com/hariPrasadCoder/jevclean/blob/08b99ab2c2b0e11fe68893c476e810a30eee06f3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevclean/jev.py`](https://github.com/hariPrasadCoder/jevclean/blob/08b99ab2c2b0e11fe68893c476e810a30eee06f3/src/jevclean/jev.py) at the pinned commit. |

## When to use

- Canonicalize country, product or company columns before analysis.
- Keep uncertain model proposals in a review queue instead of writing them straight in.
- Mismatch: experimental alpha, not on PyPI; live Jev quality is not benchmarked per the README.

## How it works

`Cleaner().canonicalize` resolves what it can locally; with the `[jev]` extra, the remaining distinct values go to Jev as Choice questions (`src/jevclean/jev.py`) and answers are cached and routed to accept or review by confidence. Integration evidence: [`src/jevclean/jev.py`](https://github.com/hariPrasadCoder/jevclean/blob/08b99ab2c2b0e11fe68893c476e810a30eee06f3/src/jevclean/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hariPrasadCoder/jevclean.git && cd jevclean
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[jev]'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Walkthrough notebook: [github.com/hariPrasadCoder/jevclean/blob/main/notebooks/jevclean_walkthrough.ipynb](https://github.com/hariPrasadCoder/jevclean/blob/main/notebooks/jevclean_walkthrough.ipynb)
- Usage guide: [github.com/hariPrasadCoder/jevclean/blob/main/docs/usage.md](https://github.com/hariPrasadCoder/jevclean/blob/main/docs/usage.md)

## Limits and data handling

Unresolved values are sent to TypeSafe when Jev is enabled. The walkthrough's model responses are simulated. Independent project, not affiliated with TypeSafe AI.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 08b99ab2c2b0](https://github.com/hariPrasadCoder/jevclean/tree/08b99ab2c2b0e11fe68893c476e810a30eee06f3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
