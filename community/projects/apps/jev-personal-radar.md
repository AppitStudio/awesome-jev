# Jev Personal Radar

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Privacy-first daily information radar: collect GitHub Trending and Hacker News candidates (plus manual inbox links), ask TypeSafe Jev whether each fits your topics, write up to six picks into a **private** GitHub Issue, and optionally let MiniMax explain the public sources in plain language.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar) |
| Tags | `Source unverified` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar#readme) — public program + private runner template. |
| Pricing and access | Public Go program; run via private GitHub Actions with `TYPESAFE_API_KEY` and `MINIMAX_API_KEY`. No app purchase fee, checked **2026-09-24**. Provider/Actions usage billed separately. |
| Jev evidence | Inspected [`internal/radar/jev.go`](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar/blob/2822a1b6e107f690e902a5fc0b706197da82f264/internal/radar/jev.go): model `jev-1.13.0`, capped daily requests. |
| Disclosure | AI-assisted catalog review; no affiliation. **No SPDX/LICENSE at reviewed tip.** Listing is not an endorsement. Live Jev/MiniMax not run. |
| Maintainer | [zhazhahuiyuxiaoxiao](https://github.com/zhazhahuiyuxiaoxiao). Independently curated. |
| Format | Go CLI (`go run ./cmd/radar`) + private Actions workflow template. |
| Platform and availability | Source build Go 1.25+; dry-run without keys; production intended for private repos. |
| Jev's role | Scores work/life relevance of public titles/descriptions; code selects Issues and calls MiniMax only for winners. |
| Requirements | Go 1.25+; private runner secrets for live mode. |
| License | **Unspecified** at tip (no LICENSE file). Do not assume OSI terms. |

## When to use

Use it for a **private daily digest** of public tech links ranked by Jev. Prefer [Jev Radar](jev-radar.md) / [Paper Radar](paper-radar.md) for other radar UIs.

## How it works

Dry-run ranks by keywords only. Live mode posts public metadata to Jev (capped), writes Issues in the private repo, and may call MiniMax on selected public README/article text. Manual imports never go to Jev.

## Get started

```sh
git clone https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar.git
cd jev-personal-radar
git checkout 2822a1b6e107f690e902a5fc0b706197da82f264
cp runtime-template/config.example.json config.json
go test ./...
go run ./cmd/radar -config config.json -dry-run
# For live digests: follow README private Actions setup (pin this commit SHA)
```

## Examples and demos

- README cost/privacy boundaries and `runtime-template/`.
- Dry-run needs no GitHub token for public trending.

## Limits and data handling

Only public titles/descriptions/topics go to Jev; MiniMax sees selected public bodies. Keep the runner repo private. Empty days stay empty—no padding with old lists.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 2822a1b](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar/tree/2822a1b6e107f690e902a5fc0b706197da82f264). AI-assisted README + `jev.go` inspection. No live provider spend.

Related: [Jev Radar](jev-radar.md), [Paper Radar](paper-radar.md), [Inbox Triage](inbox-triage.md).
