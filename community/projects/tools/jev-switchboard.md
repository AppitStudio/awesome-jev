# jev-switchboard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic communication gate for parallel Claude Code / Codex sessions: local prefilter plus one batched TypeSafe Jev decision chooses who to interrupt, who to drop, and which evidence to inject at the receiver’s next tool boundary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZIJIAN004/jev-switchboard) |
| Maintainer | [ZIJIAN004](https://github.com/ZIJIAN004). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js ≥ 20 CLI/hooks package (`jev-switchboard` 0.1.0): zero runtime deps, adapters for Claude Code/Codex, offline demo. |
| Requirements | Node **≥ 20**. Offline `npm test` / `npm run demo` need no key. Live gating needs `TYPESAFE_API_KEY` (optional `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`). |
| License | [MIT](https://github.com/ZIJIAN004/jev-switchboard/blob/35e6b29f161a12304c6cb349d260929d67b179a2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `node --test` **17 passed**; `npm run demo` OK with mocked Jev. Live multi-agent TypeSafe sessions not run. |

## When to use

Use it when **two or more coding agents** share a repo and you want Jev to decide whether a sender checkpoint should interrupt a peer (with selected evidence) instead of broadcasting everything. Prefer [jev-gateway](jev-gateway.md) when Jev chooses tools inside one agent loop; prefer [agent-chaperone](agent-chaperone.md) / [toolgate](toolgate.md) for tool-call firewalls.

## How it works

[`src/jev.mjs`](https://github.com/ZIJIAN004/jev-switchboard/blob/35e6b29f161a12304c6cb349d260929d67b179a2/src/jev.mjs) posts to `{TYPESAFE_BASE_URL}/v1/systemone` (default `https://api.typesafe.ai`). Local store/segments prefilter candidates; the gate batches one Jev request per sender checkpoint; receivers consume inbox messages via hook `additionalContext`. Demo path uses simulated Jev answers while exercising real routing/persistence/inject code. Live mode sends event/evidence text to TypeSafe.

## Get started

```sh
git clone https://github.com/ZIJIAN004/jev-switchboard.git
cd jev-switchboard
git checkout 35e6b29f161a12304c6cb349d260929d67b179a2
npm test
npm run demo
# Live: set TYPESAFE_API_KEY; see README for Claude Code / Codex hook install
```

## Examples and demos

- Offline `npm test`: **17 passed**.
- `npm run demo`: mocked Jev routes INTERRUPT to `codex-ui` and DROP to `codex-docs`, with injected hook output.

## Limits and data handling

Does not launch agents or broadcast full transcripts. Treat injected peer evidence as untrusted. Live calls incur TypeSafe usage. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 35e6b29](https://github.com/ZIJIAN004/jev-switchboard/tree/35e6b29f161a12304c6cb349d260929d67b179a2): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/jev.mjs`, `src/config.mjs`, gate/runtime, and tests. **`npm test`: 17 passed**; demo OK. No live TypeSafe.

Related: [jev-gateway](jev-gateway.md), [agent-chaperone](agent-chaperone.md), [toolgate](toolgate.md), [JevRouter](jevrouter.md).
