# jev-in-codex

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Codex MCP integration: local candidate retrieval plus TypeSafe Jev relevance ranking for capability/skill selection, workspace search, and output triage. Codex keeps final decisions; the server does not execute tools or replace compaction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/teempai/jev-in-codex) |
| Maintainer | [teempai](https://github.com/teempai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript MCP server **jev-in-codex 0.1.0** (private package; companion Codex plugin + skill). |
| Requirements | Node.js **≥ 22**, npm, **ripgrep (`rg`)** on PATH. Live Jev needs `TYPESAFE_API_KEY` (optional `JEV_MODEL`); without a key, tools use explicit local fallback. |
| License | [MIT](https://github.com/teempai/jev-in-codex/blob/f463dc1efbe2c1cdea4c5bcb0e92d1d546fde9ff/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm run check` inspected; live Codex UI and live TypeSafe ranking were not run. Ranking quality/time savings are explicitly unbenchmarked upstream. |

## When to use

Use it when a Codex session should **ask Jev to rank** supplied tools/skills, search hits, or saved output excerpts without handing over execution. Prefer [jev-codex-router](jev-codex-router.md) for per-turn model/thinking routing; prefer [jev-layer](jev-layer.md) / [Foreman](foreman.md) for broader harness supervision; prefer [Jev Review](jev-review.md) for quality-rubric MCP scores.

## How it works

[`src/jev.ts`](https://github.com/teempai/jev-in-codex/blob/f463dc1efbe2c1cdea4c5bcb0e92d1d546fde9ff/src/jev.ts) posts to `https://api.typesafe.ai/v1/systemone` when a key is configured. MCP tools `jev_select_capability`, `jev_search`, and `jev_triage` gather bounded local candidates (ripgrep / catalogs / artifacts), ask Jev relevance questions, and return original evidence plus coverage. Without a key, local fallback is explicit.

## Get started

```sh
git clone https://github.com/teempai/jev-in-codex.git
cd jev-in-codex
git checkout f463dc1efbe2c1cdea4c5bcb0e92d1d546fde9ff
npm ci --ignore-scripts
npm run check
# Then follow docs/INSTALL.md for Codex plugin + MCP wiring.
```

Live ranking sends selected excerpts to TypeSafe and can incur charges. Animated `docs/assets/jev-demo.gif` uses synthetic/simulated responses—not a live Codex capture. This listing ran offline checks only.

## Examples and demos

- Offline `npm run check` — typecheck + **31 tests passed** on the review host.
- Upstream demo GIF/PNG under `docs/assets/` (simulated TypeSafe responses).

## Limits and data handling

Selected code/log excerpts leave the host when Jev is enabled. Experimental MVP: no ranking-quality or token-savings claims verified here. Does not intercept arbitrary Codex tool calls or expose Codex’s internal catalogs.

## Review and maintenance

Reviewed on **2026-09-20** at [commit f463dc1](https://github.com/teempai/jev-in-codex/tree/f463dc1efbe2c1cdea4c5bcb0e92d1d546fde9ff): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, `package.json`, and tests. Ran `npm ci --ignore-scripts` and `npm run check` (31 pass). No live TypeSafe or Codex sessions.

Related: [jev-codex-router](jev-codex-router.md), [jev-layer](jev-layer.md), [Jev Review](jev-review.md).
