# Jev Graph Search

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

CLI and agent skill that retrieves evidence from local Obsidian vaults, Logseq folders, or JSON memory snapshots: a local shortlist is reranked by Jev (TypeSafe or OpenRouter).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Emlembow/jev-graph-search) |
| Maintainer | [Emlembow](https://github.com/Emlembow). Independently curated. |
| Format | Node CLI (`npx`/global install) with a skills.sh agent skill |
| Requirements | Node.js; TypeSafe or OpenRouter key entered at `setup` (stored in a per-user config file). `--offline` uses local lexical ranking only. |
| License | [MIT](https://github.com/Emlembow/jev-graph-search/blob/72adcac4e8db064376a3846fbb9e9a96ed5344ae/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding agent grounded retrieval over a personal knowledge base without uploading the whole vault.
- Compare lexical vs Jev-reranked recall on your own notes (`--offline` toggle).
- Mismatch: for large shared corpora a vector database may be a better primary index.

## How it works

The CLI builds a candidate shortlist locally, then sends those passages and the question to Jev for reranking; results keep source paths. The README reports a tax-code graph benchmark where top-five recall rose from 63.9% to 81.8% with Jev (maintainer-reported).

## Get started

Run setup and search a vault (live Jev calls):

```sh
npx --yes --package=jev-graph-search@0.2.2 jev-graph-search setup
npx --yes --package=jev-graph-search@0.2.2 jev-graph-search search "Why did we choose this database?" --input ./ObsidianVault
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `examples/memory.json` with `--offline`; agent skill via `npx skills add Emlembow/jev-graph-search --skill jev-graph-search`.

## Limits and data handling

Shortlisted passages are sent to TypeSafe or OpenRouter and billed. Benchmark numbers are upstream-reported.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 72adcac4e8db](https://github.com/Emlembow/jev-graph-search/tree/72adcac4e8db064376a3846fbb9e9a96ed5344ae). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
