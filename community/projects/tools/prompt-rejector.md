# Prompt Rejector

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MCP server and local HTTPS API that screen prompts, skill files, and MCP tool descriptions before an agent acts: deterministic checks plus TypeSafe Jev judgments (configurable reasoning adapters). Your app must call the scanner; install alone does not intercept traffic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/revsmoke/promptrejectormcp) |
| Maintainer | [revsmoke](https://github.com/revsmoke). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`prompt-rejector` 1.2.0** (Node HTTPS API + stdio MCP; optional Codex/Claude Code plugins and `.mcpb`). |
| Requirements | Node.js 24+, npm; `TYPESAFE_API_KEY` (and optional Gemini/other keys) for live scans. Historical replay needs no keys. |
| License | [ISC](https://github.com/revsmoke/promptrejectormcp/blob/752217d26fe9ea86625e844af3435ff145a2c06f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline build + historical Jev replay inspected. Live screening not run. Distinct from [jev-prompt-sentry](jev-prompt-sentry.md) (Anthropic Messages reverse proxy). |

## When to use

Use it when agents or apps should **opt-in scan** prompts/skills/tool descriptors over MCP or `POST /v2/check-prompt`. Prefer [jev-prompt-sentry](jev-prompt-sentry.md) for a transparent Anthropic Messages proxy; prefer [agent-chaperone](agent-chaperone.md) / [toolgate](toolgate.md) for tool-call firewalls.

## How it works

[`src/ai/providers/TypeSafeAdapter.ts`](https://github.com/revsmoke/promptrejectormcp/blob/752217d26fe9ea86625e844af3435ff145a2c06f/src/ai/providers/TypeSafeAdapter.ts) posts to `https://api.typesafe.ai/v1/systemone` with a Bearer key. [`JudgmentService`](https://github.com/revsmoke/promptrejectormcp/blob/752217d26fe9ea86625e844af3435ff145a2c06f/src/services/JudgmentService.ts) and security/skill/descriptor services combine deterministic rules with Jev (default pin `jev-1.13.0` in qualification). Application code owns block/allow policy after the scan.

## Get started

```sh
git clone --branch main https://github.com/revsmoke/promptrejectormcp.git
cd promptrejectormcp
git checkout 752217d26fe9ea86625e844af3435ff145a2c06f
npm ci
npm run build
node dist/test/ai/historicalReplayTests.js   # no keys; replay saved Jev results
# For live scans: configure .env keys, then npm start or MCP/plugin setup per README
```

Live scans send prompt/skill/descriptor text to TypeSafe (and optional reasoners) and can incur charges.

## Examples and demos

- README recorded MCP parameter-injection example (author-reported).
- Historical replay and offline contributor checks (`CONTRIBUTING.md`).
- Docs: `docs/how-we-use-jev-from-typesafe-ai.md`.

## Limits and data handling

Scanned text leaves the host on live inference. Detection quality is not guaranteed by this listing. MCP/plugin packaging paths were not smoke-tested beyond build + historical replay on the review host.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 752217d](https://github.com/revsmoke/promptrejectormcp/tree/752217d26fe9ea86625e844af3435ff145a2c06f): `prompt-rejector` **1.2.0**, ISC. AI-assisted source review of README, LICENSE, TypeSafeAdapter, JudgmentService. Offline: `npm ci` + `npm run build`; `node dist/test/ai/historicalReplayTests.js` → **PASS**. No live TypeSafe calls.

Related: [jev-prompt-sentry](jev-prompt-sentry.md), [agent-chaperone](agent-chaperone.md), [jev-mcp](jev-mcp.md).
