# decisions-mcp

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server that lets coding agents scan large codebases with OpenRouter decision models (Jev by default) to locate bugs from symptoms and classify or filter files cheaply.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GorOhanyan/decisions-mcp) |
| Maintainer | [GorOhanyan](https://github.com/GorOhanyan). Independently curated. |
| Format | Node.js MCP server (stdio) |
| Requirements | Node.js 18+, OpenRouter API key with access to `typesafe/jev-1.13`. |
| License | [MIT](https://github.com/GorOhanyan/decisions-mcp/blob/4c74a44a1b12b6d66ea0c7a623cc706a14abf4ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/openrouter.js`](https://github.com/GorOhanyan/decisions-mcp/blob/4c74a44a1b12b6d66ea0c7a623cc706a14abf4ad/src/openrouter.js) at the pinned commit. |

## When to use

- Find the file and line matching a bug symptom without the agent reading the whole repository.
- Classify or filter many files with a decision model.
- Mismatch: uses Jev through OpenRouter's Decisions API, not TypeSafe directly.

## How it works

Files are split into overlapping chunks and every chunk is scored by the decision model via OpenRouter; the server returns the top-ranked locations to the agent. Integration evidence: [`src/openrouter.js`](https://github.com/GorOhanyan/decisions-mcp/blob/4c74a44a1b12b6d66ea0c7a623cc706a14abf4ad/src/openrouter.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/GorOhanyan/decisions-mcp.git
cd decisions-mcp && npm install
claude mcp add decisions --scope user -e OPENROUTER_API_KEY=sk-or-... -- node /ABS/PATH/decisions-mcp/src/index.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark: `bench/run.mjs` (author-reported results in README).

## Limits and data handling

Source code chunks are sent to OpenRouter (and the chosen model provider) and billed to your OpenRouter key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 4c74a44a1b12](https://github.com/GorOhanyan/decisions-mcp/tree/4c74a44a1b12b6d66ea0c7a623cc706a14abf4ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
