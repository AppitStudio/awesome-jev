# jev-polymarket-test

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Tests whether a Jev Noul ("this market resolves Yes") beats the Polymarket price on resolved markets, with blind vs priced variants and a memorisation check across months before and after the `jev-1.13.0` release.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/truongxxxx/jev-polymarket-test) |
| Maintainer | [truongxxxx](https://github.com/truongxxxx). Independently curated. |
| Format | Python research scripts + data + report |
| Requirements | Python 3.11+, `typesafe-sdk`, numpy/scipy/scikit-learn/matplotlib; `TYPESAFE_API_KEY` to re-run Jev. |
| License | [MIT](https://github.com/truongxxxx/jev-polymarket-test/blob/e3e0f2757267184c0f743ed8dcfcd848a38e45ed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Sanity-check claims that Jev can spot mispriced prediction markets.
- Reuse the Brier/log-loss/AUC and blend evaluation for your own forecasts.
- Mismatch: Maintainer's single study; not trading advice.

## How it works

Public Gamma/CLOB data are fetched, Jev is asked one Noul plus a category Choice per market, and evaluate.py scores Jev, the market and a cross-validated blend. Jev integration: [`jev/run_jev.py`](https://github.com/truongxxxx/jev-polymarket-test/blob/e3e0f2757267184c0f743ed8dcfcd848a38e45ed/jev/run_jev.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/truongxxxx/jev-polymarket-test.git
cd jev-polymarket-test
pip install typesafe-sdk numpy scipy scikit-learn matplotlib
python jev/run_jev.py --variant blind --dry-run
```

## Limits and data handling

Market text goes to TypeSafe on live runs (billed). Results in `jev/report.md` are the maintainer's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit e3e0f2757267](https://github.com/truongxxxx/jev-polymarket-test/tree/e3e0f2757267184c0f743ed8dcfcd848a38e45ed). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
