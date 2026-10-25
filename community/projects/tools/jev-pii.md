# jev-pii (PII and privacy-regime discovery in DuckDB SQL with typed Jev answers)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DuckDB functions that return Jev's typed answers as SQL columns: per row (`jev_pii_row`, `jev_ask`) or per column from a sample (`jev_pii_table`) to find personal data and the privacy regimes that apply, feeding a keep, mask, hash, drop or review policy written in code; also runs in the browser through Pyodide.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/senthilsweb/jev-pii) |
| Maintainer | [senthilsweb](https://github.com/senthilsweb). Independently curated. |
| Format | Python package, DuckDB UDFs, notebook and browser app |
| Requirements | Python with DuckDB, or a modern browser; a TypeSafe API key (a keyword mock runs without one); a CORS proxy for live browser mode. |
| License | [Apache-2.0](https://github.com/senthilsweb/jev-pii/blob/1a4a4e5acfccd6062023251222a0202849c2e432/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_pii/client.py`](https://github.com/senthilsweb/jev-pii/blob/1a4a4e5acfccd6062023251222a0202849c2e432/jev_pii/client.py) at the pinned commit. |

## When to use

- Profile tables for personal data before sharing or loading them elsewhere.
- Ask your own typed questions about rows from SQL and filter or join on the answers.
- Mismatch: the browser app's default live endpoint is the maintainer's own proxy; deploy the included proxy or call TypeSafe directly.

## How it works

`jev_pii/client.py` posts rows or column samples with Noul and Choice questions to `https://api.typesafe.ai/v1/systemone` (pinned `jev-1.14.0`); a failed call returns `NULL` and sends the column to review. The browser build needs the `proxy/` endpoint because the API does not accept browser origins. Integration evidence: [`jev_pii/client.py`](https://github.com/senthilsweb/jev-pii/blob/1a4a4e5acfccd6062023251222a0202849c2e432/jev_pii/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python data/fetch.py
echo 'TYPESAFE_API_KEY=...' > .env   # without it a keyword mock runs
.venv/bin/jupyter lab pii_discovery.ipynb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/senthilsweb/jev-pii#readme](https://github.com/senthilsweb/jev-pii#readme)
- Proxy: [github.com/senthilsweb/jev-pii/tree/main/proxy](https://github.com/senthilsweb/jev-pii/tree/main/proxy)

## Limits and data handling

Rows or column samples go to TypeSafe, or through the configured proxy. A per-query cap (default 100 calls) limits spend when a `LIMIT` is missing. Not a compliance determination.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 1a4a4e5acfcc](https://github.com/senthilsweb/jev-pii/tree/1a4a4e5acfccd6062023251222a0202849c2e432). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
