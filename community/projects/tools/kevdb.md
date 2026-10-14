# KevDB

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Semantic SQL functions in DuckDB powered by open-weight decision models, benchmarked under pre-registered criteria against the Jev API and LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ElyasEbrahim/KevDB) |
| Maintainer | [ElyasEbrahim](https://github.com/ElyasEbrahim). Independently curated. |
| Format | Python library + DuckDB extension functions and experiments |
| Requirements | Python 3.12+; TypeSafe key only for the Jev comparison runs. |
| License | [MIT](https://github.com/ElyasEbrahim/KevDB/blob/5f7a9f9c8f3225163dfb9593f64826fc2e25c176/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/kevdb/backends.py`](https://github.com/ElyasEbrahim/KevDB/blob/5f7a9f9c8f3225163dfb9593f64826fc2e25c176/src/kevdb/backends.py) at the pinned commit. |

## When to use

- Run typed per-row decisions (noul / choice / score) inside SQL queries.
- Compare open decision models (Kev, Clef-flash, Laya) against Jev on the same request format.
- Mismatch: research project; results are the author's.

## How it works

KevDB registers SQL functions that send each row as Jev-format state to a backend; the Jev backend calls TypeSafe while open-model backends run locally, and experiments record agreement and cost. Integration evidence: [`src/kevdb/backends.py`](https://github.com/ElyasEbrahim/KevDB/blob/5f7a9f9c8f3225163dfb9593f64826fc2e25c176/src/kevdb/backends.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ElyasEbrahim/KevDB.git
cd KevDB
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m pytest -q
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Experiments: `experiments/` (classification, query plan, joins).

## Limits and data handling

Rows sent to the Jev backend go to TypeSafe and are billed to your key; open-model runs are local.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 5f7a9f9c8f32](https://github.com/ElyasEbrahim/KevDB/tree/5f7a9f9c8f3225163dfb9593f64826fc2e25c176). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
