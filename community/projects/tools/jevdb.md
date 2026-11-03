# JEVDB (semantic SQL on DuckDB where filters, joins, classification and scoring run on Jev decisions)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic database built on DuckDB that runs semantic filters, semantic joins, classification and scoring over text and images inside ordinary SQL. By default it batches decisions on a Jev model in one stage and returns probabilities, labels and scores directly; an OpenAI-compatible backend and optional key pruning and cascades are also available. It does not generate text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PDAIS/JEVDB) |
| Maintainer | [PDAIS](https://github.com/PDAIS). Independently curated. |
| Format | DuckDB extension with a Python package (`pip install jevdb`) |
| Requirements | Python or DuckDB 1.4.3; a Jev API key in `JEV_API_KEY` (or an OpenAI-compatible endpoint for the LLM backend). |
| License | [MIT](https://github.com/PDAIS/JEVDB/blob/5a17c023d83e304aba5280832c933388e6f1863d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_client.cpp`](https://github.com/PDAIS/JEVDB/blob/5a17c023d83e304aba5280832c933388e6f1863d/src/jev_client.cpp) at the pinned commit. |

## When to use

- Filter, join and classify table rows by meaning from plain SQL without per-row prompts.
- Mismatch: every semantic row or pair is a model call that uses your quota; extraction and summarisation are out of scope.

## How it works

`src/jev_client.cpp` is the extension's client for the Jev `systemone` endpoint behind the `jev_holds`, `jev_probability`, `jev_choose` and `jev_score` SQL functions, which batch decisions and reuse answers within a query; the extension reads the key from a DuckDB secret so it never appears in SQL. Integration evidence: [`src/jev_client.cpp`](https://github.com/PDAIS/JEVDB/blob/5a17c023d83e304aba5280832c933388e6f1863d/src/jev_client.cpp).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jevdb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [www.jevdb.org/](https://www.jevdb.org/)
- Paper: [arxiv.org/pdf/2610.02046](https://arxiv.org/pdf/2610.02046)
- Colab notebook: [colab.research.google.com/github/PDAIS/JEVDB/blob/main/examples/jevdb_colab.ipynb](https://colab.research.google.com/github/PDAIS/JEVDB/blob/main/examples/jevdb_colab.ipynb)

## Limits and data handling

Row text (and image data for `jev_media`) is sent to the Jev API on your key and uses your quota on every rerun. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 5a17c023d83e](https://github.com/PDAIS/JEVDB/tree/5a17c023d83e304aba5280832c933388e6f1863d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
