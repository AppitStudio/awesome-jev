# JEV ToC search (search a PDF through its own table of contents, with Jev ordering each branch of a depth-first walk)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Experiment in long-document search inspired by PageIndex: parse a PDF with Datalab, recover its real table of contents and match printed page numbers to PDF pages, then let Jev order the branches at each level of a depth-first search. Low-probability branches are never pruned, and in the worst case every page is checked before it says no evidence was found. Includes grounded answer evaluation and interactive traces.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bakubay/jev-dfs-document-search) |
| Maintainer | [bakubay](https://github.com/bakubay). Independently curated. |
| Format | Python scripts |
| Requirements | Python, a Datalab API key and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/bakubay/jev-dfs-document-search/blob/b30e6bbb72634782e6b969e28eb19f7b53638b6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`datalab_dfs_search.py`](https://github.com/bakubay/jev-dfs-document-search/blob/b30e6bbb72634782e6b969e28eb19f7b53638b6a/datalab_dfs_search.py) at the pinned commit. |

## When to use

- Try exhaustive, explainable search over long text PDFs that have a usable table of contents.
- Mismatch: experimental prototype; the author says it is not a final retrieval design.

## How it works

`datalab_dfs_search.py` asks `jev-1.13.0` one choice question per ToC level to order the child branches, then visits them depth-first. Integration evidence: [`datalab_dfs_search.py`](https://github.com/bakubay/jev-dfs-document-search/blob/b30e6bbb72634782e6b969e28eb19f7b53638b6a/datalab_dfs_search.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add DATALAB and TYPESAFE keys
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the pipeline: [github.com/bakubay/jev-dfs-document-search#readme](https://github.com/bakubay/jev-dfs-document-search#readme)

## Limits and data handling

PDF text goes to Datalab for parsing and section text goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit b30e6bbb7263](https://github.com/bakubay/jev-dfs-document-search/tree/b30e6bbb72634782e6b969e28eb19f7b53638b6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
