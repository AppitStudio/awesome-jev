# jev-search (larguesa)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Complementary semantic search CLI and agent skill: Jev scores whether each candidate line expresses the intent you are looking for, so agents find by meaning what keyword search misses across repo docs, LLM wikis and Obsidian notes; in six simulated tasks lexical + Jev recovered 29 of 34 labeled passages vs 22 for lexical alone (author-reported). Not the listed jev-search app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/larguesa/jev-search) |
| Maintainer | [larguesa](https://github.com/larguesa). Independently curated. |
| Format | Python CLI (`uv tool install` / `pipx` from a checkout) + `skills/jev-search/SKILL.md` |
| Requirements | Python, uv or pipx; `JEV_SEARCH_API_KEY` from the selected provider (OpenRouter default `typesafe/jev-1.13`, or TypeSafe `jev-1.13.0`). |
| License | [MIT](https://github.com/larguesa/jev-search/blob/8aa403554d7904d3c14224cfda02a4e2144c0ccd/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Find passages about an idea phrased differently from your query.
- Give coding agents a meaning-based search alongside exact search.
- Mismatch: costs one decision per scanned line; scope inputs to selected files.

## How it works

[`jev_search.py`](https://github.com/larguesa/jev-search/blob/8aa403554d7904d3c14224cfda02a4e2144c0ccd/jev_search.py) sends native decision requests to OpenRouter Decisions or TypeSafe `/v1/systemone` (`--provider` / `JEV_SEARCH_PROVIDER`) and ranks lines by probability.

## Get started

Install from a reviewed checkout (README notes the v0.2.0 tag is not yet published):

```sh
git clone --branch main https://github.com/larguesa/jev-search.git && cd jev-search
uv tool install .   # or: pipx install .
jev-search --help
```

Decision calls billed by OpenRouter or TypeSafe per scanned passage.

## Examples and demos

- README *Early evidence* and agent skill.

## Limits and data handling

Selected passages go to the chosen provider; use dedicated keys with spending limits. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 8aa403554d79](https://github.com/larguesa/jev-search/tree/8aa403554d7904d3c14224cfda02a4e2144c0ccd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
