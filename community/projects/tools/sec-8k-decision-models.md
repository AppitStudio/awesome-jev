# 8-K Filings and Decision Models

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jev rated 26,962 S&P 500 8-K filings (2013 to 2026) from very bad to very good for $2.32; within item group and year the rating's rank correlation with the next two days' market-adjusted return is +0.025, positive in 13 of 14 years, and the move is mostly gone by the next open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/magilliam27/sec-8k-filings-and-decision-models) |
| Maintainer | [magilliam27](https://github.com/magilliam27). Independently curated. |
| Format | Python research package with report, figures, 402 offline tests and hashed results |
| Requirements | Python 3.10+; a TypeSafe key only for the `--score` steps; SEC EDGAR and price data as described in the report. |
| License | [MIT](https://github.com/magilliam27/sec-8k-filings-and-decision-models/blob/05bbea3d01806e928b0928be258c865a464b04aa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/sec8k/jev.py`](https://github.com/magilliam27/sec-8k-filings-and-decision-models/blob/05bbea3d01806e928b0928be258c865a464b04aa/src/sec8k/jev.py) at the pinned commit. |

## When to use

- See how a decision model's probability-weighted ratings of filings line up with short-term returns, with the method and limits written out.
- Reuse the pipeline: filing fetch, Jev scoring, item-group comparisons and a word-list baseline.
- Mismatch: a small, fast effect on daily prices; not a trading system, and the author flags possible look-ahead from the model's training data.

## How it works

`jev.py` asks a five-option Score question per filing and keeps the full probability distribution so ratings can be ranked; the analysis compares ratings only within the same 8-K item group and year and tests against SPY-adjusted returns, with a Loughran-McDonald tone score as baseline. Integration evidence: [`src/sec8k/jev.py`](https://github.com/magilliam27/sec-8k-filings-and-decision-models/blob/05bbea3d01806e928b0928be258c865a464b04aa/src/sec8k/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -e ".[dev]"
pytest                                   # 402 tests, no network or keys
python grading/scripts/check_hashes.py   # verify published results
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full report: `docs/REPORT.md` (method, results, limitations, costs).
- Docs, figures and results are CC BY 4.0 (`LICENSE-docs.md`); code is MIT.

## Limits and data handling

Only public SEC filings go to TypeSafe on your key. Results are research, not investment advice.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 05bbea3d0180](https://github.com/magilliam27/sec-8k-filings-and-decision-models/tree/05bbea3d01806e928b0928be258c865a464b04aa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
