# Routiium (self-hosted OpenAI-compatible LLM gateway with TypeSafe Jev typed-decision routing and judging)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted OpenAI-compatible gateway (managed keys, policy routing, safety judge, rate limits, analytics, MCP tools) that can ask TypeSafe Jev, direct or via OpenRouter, to choose an approved upstream model or judge a request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/labiium/routiium) |
| Maintainer | [labiium](https://github.com/labiium). Independently curated. |
| Format | Rust gateway + npm installer (Apache-2.0) |
| Requirements | Rust or the npm package, upstream provider keys, and a TypeSafe or OpenRouter key for Jev decisions. |
| License | [Apache-2.0](https://github.com/labiium/routiium/blob/d317998118a1376c01346c362228dc9dff1d2deb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision.rs`](https://github.com/labiium/routiium/blob/d317998118a1376c01346c362228dc9dff1d2deb/src/decision.rs) at the pinned commit. |

## When to use

- Route `model: auto` requests to an approved model chosen by Jev.
- Add a typed safety judge in front of your LLM apps.
- Mismatch: Jev is optional; you run and secure the gateway.

## How it works

`src/decision.rs` implements the `DecisionClient` for TypeSafe System One (`https://api.typesafe.ai/v1/systemone`, `jev-latest`) and OpenRouter Decisions; `docs/TYPED_DECISIONS.md` documents routing and judging with Jev. Integration evidence: [`src/decision.rs`](https://github.com/labiium/routiium/blob/d317998118a1376c01346c362228dc9dff1d2deb/src/decision.rs).

## Get started

Install via npm or cargo, configure upstreams, then follow `docs/TYPED_DECISIONS.md` to enable Jev routing.

```sh
git clone https://github.com/labiium/routiium.git && cd routiium
export TYPESAFE_API_KEY=...
cargo build --release
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/labiium/routiium/blob/d317998118a1376c01346c362228dc9dff1d2deb/README.md](https://github.com/labiium/routiium/blob/d317998118a1376c01346c362228dc9dff1d2deb/README.md)

## Limits and data handling

Request content used for decisions is sent to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit d317998118a1](https://github.com/labiium/routiium/tree/d317998118a1376c01346c362228dc9dff1d2deb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
