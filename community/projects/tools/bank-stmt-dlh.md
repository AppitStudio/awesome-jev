# bank-stmt-dlh (bank statement PDFs to a reconciled ledger, with Jev only for payments rules can't place)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Turns HDFC Bank current-account statement PDFs into a reconciled ledger with category, recurring-payment, cash and runway reports, on a laptop with DuckDB or as a scheduled Databricks job with a dashboard and weekly email. Parsing, reconciliation, rules and reports are plain code and SQL; the one optional AI step sends leftover payments to Jev behind a 0.9 confidence gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/senthilsweb/bank-stmt-dlh) |
| Maintainer | [senthilsweb](https://github.com/senthilsweb). Independently curated. |
| Format | Python with DuckDB or Databricks |
| Requirements | Python with uv; a TypeSafe API key only for the optional Jev step. |
| License | [MIT](https://github.com/senthilsweb/bank-stmt-dlh/blob/5de3522951738f8af177f7124aa9f386cfebd649/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/categorize.py`](https://github.com/senthilsweb/bank-stmt-dlh/blob/5de3522951738f8af177f7124aa9f386cfebd649/src/categorize.py) at the pinned commit. |

## When to use

- Categorize business bank payments with an auditable, mostly deterministic pipeline.
- Mismatch: parser built for the HDFC layout.

## How it works

`src/categorize.py` posts unplaced payments as Choice questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and accepts answers at 0.9 confidence or more. Integration evidence: [`src/categorize.py`](https://github.com/senthilsweb/bank-stmt-dlh/blob/5de3522951738f8af177f7124aa9f386cfebd649/src/categorize.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/senthilsweb/bank-stmt-dlh && cd bank-stmt-dlh
make setup
make gold   # uses Jev only if TYPESAFE_API_KEY is set
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with synthetic sample statements: [github.com/senthilsweb/bank-stmt-dlh#readme](https://github.com/senthilsweb/bank-stmt-dlh#readme)

## Limits and data handling

Only leftover payment descriptions go to TypeSafe, and only with a key set. Statements stay local or in your bucket.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 5de352295173](https://github.com/senthilsweb/bank-stmt-dlh/tree/5de3522951738f8af177f7124aa9f386cfebd649). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
