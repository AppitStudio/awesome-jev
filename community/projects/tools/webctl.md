# webctl

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Smart web-search CLI for agents: query multiple search backends, then use TypeSafe Jev to score, judge, and optionally chunk-score page content so the agent reads less junk.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dorkitude/webctl) |
| Maintainer | [dorkitude](https://github.com/dorkitude). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go CLI (`webctl`); also installable via Homebrew, apt, npm wrapper, or `go install`. |
| Requirements | Go toolchain for from-source builds; live judging uses a TypeSafe/Jev key via `webctl setup`. Search backends may need their own API keys (Brave preferred). |
| License | [MIT](https://github.com/dorkitude/webctl/blob/903f0f4ddf30cac84ffedc7e4e53dff36fc4846a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `go test` inspected. Live TypeSafe and live web-search calls were not run for this listing. |

## When to use

Use it when an agent needs web search results filtered by topic/goal before consuming them, or when optional scrape+chunk scoring should shrink long pages. Prefer a plain search API or [jegrep](jegrep.md)/[sgrep](sgrep.md) when you are searching a local codebase instead of the public web.

## How it works

Search providers return candidate results; [`internal/jev`](https://github.com/dorkitude/webctl/tree/903f0f4ddf30cac84ffedc7e4e53dff36fc4846a/internal/jev) posts typed System One questions (`jev-latest` prompts under `prompts/`) for relevance, source quality, dedupe assist, and optional chunk scoring. Application code owns provider selection, deterministic dedupe, scrape parsing, and what the agent sees. Without a Jev key, search can still run against keyless providers with throttling—scoring paths that need Jev will not apply the same filter quality.

## Get started

```sh
git clone https://github.com/dorkitude/webctl.git
cd webctl
git checkout 903f0f4ddf30cac84ffedc7e4e53dff36fc4846a
go test ./...
# Live path (charges TypeSafe + any keyed search providers):
# go install ./cmd/webctl && webctl setup && webctl search "…" --goal "…"
```

Upstream also documents Homebrew/apt/npm installs. Do not paste real API keys into the catalog tree.

## Examples and demos

- README quick-start and schematics for filter-only vs scrape+chunk flows.
- Offline unit coverage under `internal/jev`, `evals`, and `cmd/webctl/cli` (fake Jev HTTP).

## Limits and data handling

Queries, goals, result metadata, and optionally scraped page chunks leave the host on live Jev and search-provider calls. Cost/latency claims in upstream docs are author-reported, not remeasured here. Provider rate limits and keyless cooldowns apply.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 903f0f4](https://github.com/dorkitude/webctl/tree/903f0f4ddf30cac84ffedc7e4e53dff36fc4846a): MIT. AI-assisted source review of the Jev client, prompts, and README. **`go test ./...`** passed offline (packages including `internal/jev`, `evals`, `internal/provider`, `cmd/webctl/cli`). No live TypeSafe or live search calls.

Related: [jegrep](jegrep.md), [sgrep](sgrep.md), [jev-reranker](jev-reranker.md).
