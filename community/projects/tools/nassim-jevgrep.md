# jevgrep (Jev-powered semantic code search for agents via CLI or MCP)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic code search aimed at coding agents: find behavior across repositories with exact source excerpts and line numbers, using TypeSafe Jev in the evaluation path, exposed as a CLI and MCP server (distinct from dzhng/jevgrep and kyu1204/jgrep).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nassim-arifette/jevgrep) |
| Maintainer | [nassim-arifette](https://github.com/nassim-arifette). Independently curated. |
| Format | CLI + MCP (MIT) |
| Requirements | Runtime per upstream install docs and a TypeSafe key for Jev evaluation. |
| License | [MIT](https://github.com/nassim-arifette/jevgrep/blob/77fd1ffd030074bae4c5c6285458efdb323e9899/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/evaluation/jev.ts`](https://github.com/nassim-arifette/jevgrep/blob/77fd1ffd030074bae4c5c6285458efdb323e9899/src/evaluation/jev.ts) at the pinned commit. |

## When to use

- Search code by behavior rather than exact strings.
- Expose semantic search to an agent over MCP.
- Mismatch: separate from other projects named jevgrep; compare benchmarks before swapping.

## How it works

`src/evaluation/jev.ts` drives TypeSafe Jev (`jev-1.13.0` / `api.typesafe.ai`) for semantic evaluation of candidate excerpts. Integration evidence: [`src/evaluation/jev.ts`](https://github.com/nassim-arifette/jevgrep/blob/77fd1ffd030074bae4c5c6285458efdb323e9899/src/evaluation/jev.ts).

## Get started

Install per the README and run a CLI or MCP search with a TypeSafe key.

```sh
git clone https://github.com/nassim-arifette/jevgrep.git && cd jevgrep
export TYPESAFE_API_KEY=...
# see README for CLI/MCP
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nassim-arifette/jevgrep/blob/77fd1ffd030074bae4c5c6285458efdb323e9899/README.md](https://github.com/nassim-arifette/jevgrep/blob/77fd1ffd030074bae4c5c6285458efdb323e9899/README.md)

## Limits and data handling

Code excerpts under evaluation are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 77fd1ffd0300](https://github.com/nassim-arifette/jevgrep/tree/77fd1ffd030074bae4c5c6285458efdb323e9899). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
