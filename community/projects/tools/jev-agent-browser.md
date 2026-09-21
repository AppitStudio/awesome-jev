# jev-agent-browser

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript sidecar that helps [`agent-browser`](https://github.com/vercel-labs/agent-browser) choose the next safe browser action: Jev sees a compact accessibility snapshot and goal, returns a typed decision, then code validates and `agent-browser` executes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mhingston/jev-agent-browser) |
| Maintainer | [mhingston](https://github.com/mhingston). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`@mhingston5/jev-agent-browser` 0.3.1** (CLI `jev-agent-browser` + library). |
| Requirements | Node.js ≥ 20; `agent-browser` 0.31.x+ on `PATH`; credentials for TypeSafe (`TYPESAFE_API_KEY`) or Vercel/Cloudflare/custom Jev providers. |
| License | [MIT](https://github.com/mhingston/jev-agent-browser/blob/26f8ea108b07aefc4a3ce31182533b263c71b67e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline Vitest inspected. Live browser/TypeSafe loops not run. Distinct from [Footwork](footwork.md) (browser-use dual-process) and [jevdevice](jevdevice.md) (Android/shell MCP). |

## When to use

Use it for a **confidence-gated action loop** around Vercel’s `agent-browser` CLI. Prefer [Footwork](footwork.md) when you want browser-use System 2 behind Jev System 1; prefer [Hearth](../apps/hearth.md) for marketplace shortlist browsers.

## How it works

[`src/router.ts`](https://github.com/mhingston/jev-agent-browser/blob/26f8ea108b07aefc4a3ce31182533b263c71b67e/src/router.ts) and [`toolRouter.ts`](https://github.com/mhingston/jev-agent-browser/blob/26f8ea108b07aefc4a3ce31182533b263c71b67e/src/toolRouter.ts) call `createJevClient` / `choice` / `noul` from `@mhingston5/jev-cli` (default TypeSafe model `jev-1.13.0`). Provider adapters can target TypeSafe, Vercel AI Gateway, Cloudflare AI, or a custom System One-shaped endpoint. Candidate extraction, confidence/risk gates, and snapshot freshness stay in application code across providers.

## Get started

```sh
npm install -g agent-browser && agent-browser install
npm install -g @mhingston5/jev-agent-browser
# From source at reviewed commit:
git clone https://github.com/mhingston/jev-agent-browser.git
cd jev-agent-browser
git checkout 26f8ea108b07aefc4a3ce31182533b263c71b67e
npm ci
npm test
export TYPESAFE_API_KEY=...   # or other provider creds
jev-agent-browser doctor
# Live (charges apply):
# jev-agent-browser --url https://example.com --goal "Open the example link" --expect-text "Example Domain"
```

## Examples and demos

- README provider table and `run` / `route` / `research` CLI modes.
- Offline Vitest under `tests/` (executed for this listing).

## Limits and data handling

Accessibility snapshots and goals leave the host on live Jev calls. Browser automation can navigate arbitrary URLs—treat goals as privileged. This listing did not run `agent-browser` against live sites or call TypeSafe.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 26f8ea1](https://github.com/mhingston/jev-agent-browser/tree/26f8ea108b07aefc4a3ce31182533b263c71b67e): `@mhingston5/jev-agent-browser` **0.3.1**, MIT. AI-assisted source review of README, LICENSE, router/CLI/policy. Offline `npm test` (vitest): **45 passed** (8 files). No live TypeSafe or browser sessions.

Related: [Footwork](footwork.md), [jevdevice](jevdevice.md), [Jevaluate](jevaluate.md).
