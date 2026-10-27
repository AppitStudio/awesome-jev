# Decide (Jev's native decision API as a Go CLI and MCP server)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI and MCP server that exposes Jev's native question types (`noul`, `choice`, `score`, experimental `box`, and multi-question `systemone`) to shell scripts and coding agents, with offline request previews, caller-defined acceptance gates, ordered JSONL batches and one-command MCP and skill install for Claude Code, Codex, Cursor, OpenCode and others.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/koltyakov/decide) |
| Maintainer | [koltyakov](https://github.com/koltyakov). Independently curated. |
| Format | Go CLI and MCP server |
| Requirements | A TypeSafe API key, or a Jev connection through Vercel AI Gateway, OpenRouter or DigitalOcean. |
| License | [MIT](https://github.com/koltyakov/decide/blob/267714dad26972141fda05cd9ad9e7bde73b2ebe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/provider.go`](https://github.com/koltyakov/decide/blob/267714dad26972141fda05cd9ad9e7bde73b2ebe/internal/jev/provider.go) at the pinned commit. |

## When to use

- Give a coding agent typed yes/no, choice and rubric decisions as MCP tools.
- Use Jev from shell pipelines and batch files.
- Mismatch: an independent community project, not affiliated with TypeSafe.

## How it works

`internal/jev/provider.go` defines provider connections, with the official one posting to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, `TYPESAFE_API_KEY`); the CLI and MCP tools keep Jev's native request and response format. Integration evidence: [`internal/jev/provider.go`](https://github.com/koltyakov/decide/blob/267714dad26972141fda05cd9ad9e7bde73b2ebe/internal/jev/provider.go).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/koltyakov/decide/main/scripts/install.sh | sh
decide install-mcp claude   # or codex, cursor, opencode, ...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/koltyakov/decide#readme](https://github.com/koltyakov/decide#readme)
- Releases: [github.com/koltyakov/decide/releases](https://github.com/koltyakov/decide/releases)

## Limits and data handling

The statements, options and any images you pass go to the selected provider. Credentials stay outside agent configuration.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 267714dad269](https://github.com/koltyakov/decide/tree/267714dad26972141fda05cd9ad9e7bde73b2ebe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
