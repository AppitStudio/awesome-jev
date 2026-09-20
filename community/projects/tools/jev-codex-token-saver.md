# jev-codex-token-saver

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local Codex plugin/MCP server that gathers workspace or large-file evidence locally, asks TypeSafe Jev to score bounded candidates for relevance, and returns only selected exact excerpts (with a labeled local fallback when Jev is unavailable).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jcressler/jev-codex-token-saver) |
| Maintainer | [jcressler](https://github.com/jcressler). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Codex marketplace plugin + local MCP server **0.3.2**. |
| Requirements | Node.js 22.12+; Codex CLI/Desktop with plugin support; `TYPESAFE_API_KEY` for Jev selection (local fallback works without it). |
| License | [MIT](https://github.com/jcressler/jev-codex-token-saver/blob/a61b91dc3e3207094490d7286dd89b28200c8eed/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; core offline unit tests run. Live Codex + live TypeSafe selection were not run. |

## When to use

Use it when Codex investigations would otherwise dump large search or log results into context and you want Jev to pick a few exact excerpts first. Prefer [jev-codex-router](jev-codex-router.md) for per-turn model/thinking routing, or [jev-in-codex](jev-in-codex.md) for capability/search ranking MCP tools. This is not a replacement for native Codex compaction.

## How it works

Tools such as `search_workspace_evidence` and `read_large_text_evidence` scan only the workspace root supplied to the call, build a bounded candidate packet, and ask TypeSafe Jev for typed relevance selection when the packet is large enough and `TYPESAFE_API_KEY` is set. Small packets bypass Jev; auth/network/malformed failures make one attempt then return a clearly labeled local fallback. An optional recovery pass can re-select with a changed question. Integration evidence: [`src/evidence-service.mjs`](https://github.com/jcressler/jev-codex-token-saver/blob/a61b91dc3e3207094490d7286dd89b28200c8eed/src/evidence-service.mjs).

## Get started

```sh
git clone https://github.com/jcressler/jev-codex-token-saver.git
cd jev-codex-token-saver
git checkout a61b91dc3e3207094490d7286dd89b28200c8eed
npm ci
# Core offline suites (MCP + evidence + investigator):
node --test tests/evidence-service.test.mjs tests/mcp-server.test.mjs tests/investigator.test.mjs
# Install into Codex per upstream README (marketplace add + plugin add); set TYPESAFE_API_KEY in the Codex launch environment.
```

This listing did not call TypeSafe or install into a live Codex session.

## Examples and demos

- Upstream README install/use flow and selector modes (`jev` / `bypass` / `local-fallback`).
- `npm run demo` for a large-output demo path (not required for this review).
- Offline core unit tests on the review host (see Review).

## Limits and data handling

Candidate excerpts and investigation questions leave the host on live Jev calls. Path and size protections are documented upstream; do not put API keys in plugin files or prompts. Full `npm test` includes additional behavioral fixture harnesses that reported 4 failures on the review host (109/113 overall); treat those as an evidence gap, not a silent pass.

## Review and maintenance

Reviewed on **2026-09-20** at [commit a61b91d](https://github.com/jcressler/jev-codex-token-saver/tree/a61b91dc3e3207094490d7286dd89b28200c8eed): **0.3.2**, MIT. AI-assisted source review of README, LICENSE, MCP/plugin config, and `evidence-service.mjs`. Ran `npm ci` and core `node --test` suites: **24 passed**. Full `npm test`: **109 passed / 4 failed** (behavioral fixture harness). Live Codex/TypeSafe paths not executed.

Related: [jev-codex-router](jev-codex-router.md), [jev-in-codex](jev-in-codex.md), [jev-pruner](jev-pruner.md), [winnow](winnow.md).
