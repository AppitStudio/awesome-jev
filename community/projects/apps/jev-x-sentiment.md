# Jev X Sentiment Analysis (jev-v8)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted crypto decision-support web terminal: it pulls 50–1,000 recent tweets about a coin plus market data, pre-processes them statistically, and asks Jev four typed questions (trade action, sentiment, squeeze risk, catalyst) to produce a decision card. It never trades automatically.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aikeluargalee-tech/jev-v8) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/aikeluargalee-tech/jev-v8#readme) |
| Pricing and access | Free MIT source build. Requires your own TypeSafe key (billed by TypeSafe) and a TwitterAPI.io key (per-request charges; the README estimates costs). Checked 2026-10-12. |
| Jev evidence | [`app/services/typesafe_service.py`](https://github.com/aikeluargalee-tech/jev-v8/blob/7d0fc77c1c1c17124061c0c5dde1399c46cd537e/app/services/typesafe_service.py) uses `typesafe-sdk` to ask a Choice (trade action), Scores (sentiment, catalyst) and a Noul (squeeze risk) on the combined state. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Not commercial. Listing is not an endorsement and nothing here is financial advice. App not run on the review host. |
| Maintainer | [aikeluargalee-tech](https://github.com/aikeluargalee-tech). Independently curated. |
| Format | Python web app (local server + browser UI) |
| Platform and availability | Self-hosted web app (Python); early release. |
| Jev's role | Core: Jev makes the four typed judgments; Python computes engagement, author diversity, keyword polarity, market indicators and entry/stop/target levels; you execute trades manually. |
| Requirements | Python (see `requirements.txt`); TypeSafe and TwitterAPI.io keys; CCXT market data. |
| License | [MIT](https://github.com/aikeluargalee-tech/jev-v8/blob/7d0fc77c1c1c17124061c0c5dde1399c46cd537e/LICENSE). |

## When to use

- Summarise crowd sentiment on a coin into a calibrated, reviewable decision card.
- Study a tiered pipeline that keeps raw tweets out of the model.
- Mismatch: Trading signals are speculative; not financial advice and no execution.

## How it works

Tweets are ingested with early-stopping de-duplication against a local SQLite store, reduced to statistics and a stratified sample, then sent with market indicators to Jev in one request.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/aikeluargalee-tech/jev-v8.git
cd jev-v8
pip install -r requirements.txt
cp .env.example .env   # add your keys
```

## Limits and data handling

Tweets and market state go to TypeSafe; tweets are cached locally in SQLite. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 7d0fc77c1c1c](https://github.com/aikeluargalee-tech/jev-v8/tree/7d0fc77c1c1c17124061c0c5dde1399c46cd537e). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
