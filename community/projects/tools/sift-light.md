# sift-light

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Evidence-first search tool for coding agents (Pi, OMP, Claude Code/Codex via MCP) with exact, concept and hybrid modes and an optional Jev semantic judge that classifies retained concept candidates to improve ordering.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lightsifter/sift-light) |
| Maintainer | [lightsifter](https://github.com/lightsifter). Independently curated. |
| Format | Agent plugin and MCP server with bundled search engine; optional local embedding model |
| Requirements | Node.js 22.19+ (or Bun 1.4+ for Pi). The semantic judge needs `TYPESAFE_API_KEY` in the server environment and an explicit `semanticJudge.enabled: true`. |
| License | [AGPL-3.0](https://github.com/lightsifter/sift-light/blob/f0168c04abe5707203175b631c68ceb79897c41c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give coding agents search results with evidence and bookmarks instead of raw grep output.
- Add a remote typed judgment only to the hybrid/concept path, keeping exact searches local and fast.
- Mismatch: the judge sends candidate text to TypeSafe; leave it disabled (the default) for local-only search.

## How it works

Exact searches stay local; concept/hybrid search uses an optional local embedding model. When `semanticJudge` is enabled, up to `maxCandidates` (default 20) retained concept candidates are sent to Jev (`jev-latest`) for classification, which reorders them but never replaces local matching, pagination or verification. Results expose `semanticJudge.status` and `judgedCandidates`, and the server fails at startup when an enabled configuration has no key rather than silently claiming Jev ran ([README](https://github.com/lightsifter/sift-light/blob/f0168c04abe5707203175b631c68ceb79897c41c/README.md#optional-semantic-judge)).

## Get started

Register the MCP server (or install the Pi/OMP plugin), then enable the judge in `sift-light.json` (live TypeSafe calls on hybrid searches):

```sh
claude mcp add sift-light -- npx -y --package sift-light@latest sift-light-mcp --stdio
# or: pi install npm:sift-light
# sift-light.json: "semanticJudge": {"enabled": true, "provider": "jev", "apiKeyEnv": "TYPESAFE_API_KEY", "model": "jev-latest"}
# MCP: set SIFT_LIGHT_CONFIG=/absolute/path/to/sift-light.json
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Optional semantic judge* configuration and status fields.

## Limits and data handling

AGPL-3.0. Judge input (candidate passages) leaves the machine. `jev-latest` is an alias that moves with releases. The npm package currently publishes prerelease versions (1.0.3-4 on 2026-10-06); not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit f0168c04abe5](https://github.com/lightsifter/sift-light/tree/f0168c04abe5707203175b631c68ceb79897c41c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
