# Jev Ledger (personal income statement, balance sheet and cash flow from bank statements, with Jev classification behind auditor-style controls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-file Python tool that turns Chase PDF statements or CSV exports into an income statement, balance sheet and bank cash flow, with a controls report and audit trail; Jev picks each transaction's statement line and flags own-account transfers, and code checks completeness, cutoff, materiality and calibration before trusting an answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kayyoo-naru/jev-ledger) |
| Maintainer | [kayyoo-naru](https://github.com/kayyoo-naru). Independently curated. |
| Format | Python script |
| Requirements | Python 3; `pdfplumber` for PDFs; a `TYPESAFE_API_KEY` (or `--mock` to test without API calls). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_ledger.py`](https://github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/jev_ledger.py) at the pinned commit. |

## When to use

- See how to wrap Jev classifications in accounting controls so every number has an audit trail.
- Mismatch: tax or bookkeeping software; PDF parsing covers Chase statements only, and there is no license file.

## How it works

`jev_ledger.py` posts a `choice` question over your statement lines and a `noul` transfer question per transaction to `/v1/systemone`; confidence thresholds scale with the amount (75% under 100, 90% under 1,000, always reviewed above), and disagreements between code and Jev go to a review queue. Integration evidence: [`jev_ledger.py`](https://github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/jev_ledger.py).

## Get started

Try it with mock answers first, then with your key.

```sh
git clone https://github.com/kayyoo-naru/jev-ledger
cd jev-ledger
python3 jev_ledger.py . --mock   # folder with accounts.csv + transactions.csv, no API calls
export TYPESAFE_API_KEY=...
python3 jev_ledger.py . --rules rules.csv
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/README.md](https://github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/README.md)
- Example report: [github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/report.html](https://github.com/kayyoo-naru/jev-ledger/blob/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa/report.html)

## Limits and data handling

Transaction descriptions and amounts are sent to TypeSafe. The README refers to a `sample/` folder that is not in the reviewed commit; the CSVs sit at the repository root. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 05df778e1b4a](https://github.com/kayyoo-naru/jev-ledger/tree/05df778e1b4ad083f695ec986c6c8c9f1ffd62fa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
