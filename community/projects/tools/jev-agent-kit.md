# jev-agent-kit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Node CLI and MCP server (`jev` / `jev-mcp`) that wraps TypeSafe Jev as small typed tools agents can call in a loop: check, choose, score, judge, route, triage, guard, grep, rank, and compact. Distinct from the Rust CLI also named [jevkit](jevkit.md) and from purpose-built [jev-mcp](jev-mcp.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/walidboulanouar/jev-agent-kit) |
| Maintainer | [walidboulanouar](https://github.com/walidboulanouar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`@walidboulanouar/jevkit` 0.2.0** (bins `jev`, `jevkit`, `jev-mcp`); zero runtime dependencies. |
| Requirements | Node.js ≥ 18.17. Live calls need `TYPESAFE_API_KEY` (or `~/.config/jev/key`). Optional `JEV_MODEL` / `JEV_API_URL`. |
| License | [MIT](https://github.com/walidboulanouar/jev-agent-kit/blob/214407ba2f377db794bc36218f52a928bce94a1c/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `npm test` (`node --test`): **55 passed**, **1 skipped** (live). No live TypeSafe calls here. |

## When to use

Use it when an agent or shell pipeline needs many cheap typed judgments (gates, triage batches, semantic grep) without pulling a heavier SDK. Prefer [jev-mcp](jev-mcp.md) for a different ten-tool MCP surface; prefer Rust [jevkit](jevkit.md) for offline `jev lint` of question sets before spend.

## How it works

[`client.js`](https://github.com/walidboulanouar/jev-agent-kit/blob/214407ba2f377db794bc36218f52a928bce94a1c/src/client.js) posts `state` + `questions` to `https://api.typesafe.ai/v1/systemone`. [`tools.js`](https://github.com/walidboulanouar/jev-agent-kit/blob/214407ba2f377db794bc36218f52a928bce94a1c/src/tools.js) / [`cli.js`](https://github.com/walidboulanouar/jev-agent-kit/blob/214407ba2f377db794bc36218f52a928bce94a1c/src/cli.js) map each command to Noul/Choice/Score (and multi-question judge). MCP mode exposes the same tools over stdio. Exit codes distinguish definite “no” (1) from errors so scripts under `set -e` behave predictably.

## Get started

```sh
export TYPESAFE_API_KEY=your_key   # live doctor only
npx @walidboulanouar/jevkit@0.2.0 --help
# From source at the reviewed commit:
git clone https://github.com/walidboulanouar/jev-agent-kit.git
cd jev-agent-kit
git checkout 214407ba2f377db794bc36218f52a928bce94a1c
npm test
```

Live commands send input text to TypeSafe and can incur charges. `doctor` is a live connectivity check.

## Examples and demos

- `examples/` — shell snippets (`ci-gate.sh`, `inbox-triage.sh`, `route-skill.sh`).
- Offline unit tests under `test/` (mocked transport).

## Limits and data handling

CLI/MCP payloads leave the host on live calls. Path tools refuse home-directory roots and harden against secret-shaped content in some gates (see tests). This listing did not run live `doctor` or MCP against a real agent.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 214407b](https://github.com/walidboulanouar/jev-agent-kit/tree/214407ba2f377db794bc36218f52a928bce94a1c) (`@walidboulanouar/jevkit` 0.2.0, MIT). AI-assisted source review of README, LICENSE, `client.js`, `tools.js`, `cli.js`. Offline `npm test`: 55 passed / 1 skipped. No live provider calls.

Related: [jevkit](jevkit.md) (Rust), [jev-mcp](jev-mcp.md), [askjev](askjev.md), [daf-jev](daf-jev.md).
