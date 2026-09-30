# Semble + Jev (semble-jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Code search CLI for agents: Semble retrieves local snippets; TypeSafe Jev scores relevance; CLI returns selected original source with locations (`sj`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fatelei/semble-jev) |
| Maintainer | [fatelei](https://github.com/fatelei). Independently curated. |
| Format | Python CLI (`sj`) via uv tool install; Apache-2.0. |
| Requirements | Python 3.11+; uv; `TYPESAFE_API_KEY` (or `sj auth`); local repo path. |
| License | [Apache-2.0](https://github.com/fatelei/semble-jev/blob/664b9f7a8c1c5ae1b89acfb1b1292d855766c973/LICENSE). TypeSafe usage may incur charges; `--local` skips Jev. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream token-reduction figures are small tests—not re-measured here. Live TypeSafe searches not run on the review host. |

## When to use

Use when an agent needs retrieval-then-Jev-filter over a local checkout. Prefer embedding-only search when you cannot call TypeSafe.

## How it works

Semble indexes/retrieves locally; default search sends candidates to `https://api.typesafe.ai/v1/systemone` for relevance scoring; returns original source with scores and reading leads. Failures can fall back to unfiltered candidates unless `--strict`.

## Get started

```sh
git clone https://github.com/fatelei/semble-jev.git
cd semble-jev
git checkout 664b9f7a8c1c5ae1b89acfb1b1292d855766c973
uv tool install .
sj auth
# sj search "…" /path/to/repo
```

## Examples and demos

- Upstream README CLI examples and cost calculator notes.
- Author-reported token reduction tables (not re-run here).

## Limits and data handling

Default mode sends candidate snippets to TypeSafe. Semble ignore rules do not guarantee secrets are excluded. Catalog checks did not run live searches.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 664b9f7](https://github.com/fatelei/semble-jev/tree/664b9f7a8c1c5ae1b89acfb1b1292d855766c973). AI-assisted README and license inspection; install/live paths not executed.
