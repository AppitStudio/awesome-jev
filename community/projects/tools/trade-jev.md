# trade-jev (backtest TypeSafe Jev as a BUY/SELL/HOLD trader on NQ L10 order-book data)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research harness that calls TypeSafe Jev once per run on Databento NQ L10 order-book days, stores answers, then replays settings offline, views runs in a local web app, and can paper-trade a live feed without placing orders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justinhe16/trade-jev) |
| Maintainer | [justinhe16](https://github.com/justinhe16). Independently curated. |
| Format | Python research harness with local web view (MIT) |
| Requirements | Python/`uv`, optional Databento day files, and `TYPESAFE_API_KEY` for live runs (sample data smoke tests available). |
| License | [MIT](https://github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/trade_jev/run.py`](https://github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/src/trade_jev/run.py) at the pinned commit. |

## When to use

- Measure Jev as a trading signal on order-book features.
- Replay stored answers under new cutoffs without new API spend.
- Mismatch: research/paper only; published findings are author-run.

## How it works

The harness posts trading questions to Jev (`jev-latest`), stores answers under `runs/`, and re-scores offline; live mode signals only. Integration evidence: [`src/trade_jev/run.py`](https://github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/src/trade_jev/run.py).

## Get started

`uv sync`, add a key, smoke-test on sample data, then read `results/FINDINGS.md`.

```sh
uv sync
echo TYPESAFE_API_KEY=... >> .env
TRADE_JEV_DATA=data/sample uv run python -m trade_jev.run --days 2026-06-23 --policies hold,random,imbalance
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/README.md](https://github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/README.md)
- Findings: [github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/results/FINDINGS.md](https://github.com/justinhe16/trade-jev/blob/93553ccf691c0de74684f72fb5e4ca9479600d7b/results/FINDINGS.md)

## Limits and data handling

Order-book features derived for questions are sent to TypeSafe on your key. Not investment advice; no live order placement.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 93553ccf691c](https://github.com/justinhe16/trade-jev/tree/93553ccf691c0de74684f72fb5e4ca9479600d7b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
