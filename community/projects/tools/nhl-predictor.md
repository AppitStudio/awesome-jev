# NHL Predictor (daily NHL predictions and paper betting with an xG model, LLM news and TypeSafe Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Daily-updated NHL match predictor and fixed-stake paper-betting simulation that combines an xG model with news read by an LLM and screened by TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CR0ZER/NHL-Predictor) |
| Maintainer | [CR0ZER](https://github.com/CR0ZER). Independently curated. |
| Format | Python pipeline + GitHub Pages site (no SPDX license file on the reviewed commit) |
| Requirements | Python 3 and a TypeSafe API key for the news step. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`news.py`](https://github.com/CR0ZER/NHL-Predictor/blob/48455bf576ff1781734b95efeb4c1cb01c0ae5c7/news.py) at the pinned commit. |

## When to use

- Follow daily NHL predictions with a public track record.
- Study Jev as a news-screening signal in a sports model.
- Mismatch: paper betting only; French docs; no OSI license on the reviewed commit.

## How it works

`news.py` uses `typesafe_sdk.TypeSafeClient.system_one(..., model="jev-latest")` with `Choice`/`Noul` questions to classify team news. Integration evidence: [`news.py`](https://github.com/CR0ZER/NHL-Predictor/blob/48455bf576ff1781734b95efeb4c1cb01c0ae5c7/news.py).

## Get started

Clone, set TYPESAFE_API_KEY, and run the pipeline or browse the published site.

```sh
git clone https://github.com/CR0ZER/NHL-Predictor.git && cd NHL-Predictor
export TYPESAFE_API_KEY=...
pip install -r requirements.txt && python nhl.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/CR0ZER/NHL-Predictor/blob/48455bf576ff1781734b95efeb4c1cb01c0ae5c7/README.md](https://github.com/CR0ZER/NHL-Predictor/blob/48455bf576ff1781734b95efeb4c1cb01c0ae5c7/README.md)

## Limits and data handling

Not betting advice. News text is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 48455bf576ff](https://github.com/CR0ZER/NHL-Predictor/tree/48455bf576ff1781734b95efeb4c1cb01c0ae5c7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
