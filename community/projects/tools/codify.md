# Codify (cg)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent workflow CLI (`cg`) with a spec engine, code graph, and memory; `cg jev` asks TypeSafe Jev for typed judgments such as memory classification, flaky-failure triage, and finding ranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sidiora-Labs/codify) |
| Product homepage | [codify.centra.ag](https://codify.centra.ag/) |
| Maintainer | [Sidiora-Labs](https://github.com/Sidiora-Labs). Independently curated. |
| Format | CLI with MCP tools; Jev features are optional |
| Requirements | Linux x86_64 installer or source build (`make`). Jev calls use `typesafe/jev-1.13` over OpenRouter (key per upstream [docs/jev.md](https://github.com/Sidiora-Labs/codify/blob/main/docs/jev.md)). |
| License | [MIT](https://github.com/Sidiora-Labs/codify/blob/c20c06b9ad09117652eb2a6f89f323a522f9f31d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Classify agent memories into skills/decisions/constraints/facts/noise with a confidence.
- Triage failing verify commands or rank guard findings with a typed judgment.
- Mismatch: the core spec/graph loop works without Jev; only Jev-backed features need a key.

## How it works

Codify keeps its graph, memory, and task loop local. `cg jev ask` sends a state and typed questions to Jev (via OpenRouter) and logs request id, tokens, cost, and latency in `.codegraph/jev.log`. Upstream states no Jev answer changes an exit code.

## Get started

Install, then check the Jev leg before use:

```sh
curl -fsSL https://codify.centra.ag/install | bash   # or build from source: make && sudo make install
cg jev doctor --probe
cg memory classify --unclassified
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README command tables and [docs/jev.md](https://github.com/Sidiora-Labs/codify/blob/main/docs/jev.md).

## Limits and data handling

Jev requests send note/failure text to OpenRouter/TypeSafe and are billed per call. Review the installer script before piping it to a shell.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit c20c06b9ad09](https://github.com/Sidiora-Labs/codify/tree/c20c06b9ad09117652eb2a6f89f323a522f9f31d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
