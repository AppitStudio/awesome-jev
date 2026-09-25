# agent-chaperone

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Calibrated firewall for AI agent tool calls: screens MCP traffic through a proxy and a client's built-in tools through hooks, with policy thresholds and a local judgment log. Default screening uses TypeSafe Jev; starts in shadow mode (blocks nothing until you tune).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agent-chaperone/agent-chaperone) |
| Maintainer | [agent-chaperone](https://github.com/agent-chaperone) / [Sepehr Safari](https://github.com/sepehr-safari). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`agent-chaperone` 0.3.1** (CLI bin `agent-chaperone`); MCP wrap + hooks adapter. |
| Requirements | Node.js (see package engines). Live screening needs `TYPESAFE_API_KEY` for calibrated Jev probabilities. Optional `OPENROUTER_API_KEY` / `AI_GATEWAY_API_KEY` run non-calibrated general models (upstream warns thresholds were chosen against Jev). |
| License | [Apache-2.0](https://github.com/agent-chaperone/agent-chaperone/blob/4220149bed35d4c9402adb9a0b9a5d41874cf144/LICENSE). TypeSafe (or other provider) usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pnpm test`: **1160 passed**. No live TypeSafe calls here. Distinct from [jev-shield](jev-shield.md) / [JevShield](jevshield.md) (different packaging and gateway paths). |

## When to use

Use it when you want a second opinion on MCP tool calls/results and on client-native Bash/Edit/Write/WebFetch hooks, with allow/deny lists plus model screening and a readable shadow log. Prefer OS isolation for sandboxing; prefer [jev-shield](jev-shield.md) if you specifically want that Vercel AI Gateway skill/firewall shape.

## How it works

[`src/backends/typesafe.ts`](https://github.com/agent-chaperone/agent-chaperone/blob/4220149bed35d4c9402adb9a0b9a5d41874cf144/src/backends/typesafe.ts) talks to TypeSafe via `@typesafe-ai/sdk` (`TYPESAFE_API_KEY`). The CLI wraps an MCP server (`agent-chaperone -- …`) and exposes `hook pre` / `hook post` for client hooks. Deterministic rules still run without a key; model judgments are logged with probabilities. Secret-shaped strings are redacted before screening leaves the host.

## Get started

```sh
npm install -g agent-chaperone
# From source at the reviewed commit:
git clone https://github.com/agent-chaperone/agent-chaperone.git
cd agent-chaperone
git checkout 4220149bed35d4c9402adb9a0b9a5d41874cf144
pnpm install --frozen-lockfile
pnpm test
```

Live screening sends tool arguments/results to the configured backend and can incur charges. Start in shadow mode and read the log before enforce.

## Examples and demos

- Site guides and measured results: [agentchaperone.dev](https://agentchaperone.dev).
- Offline Vitest suite under `src/**/*.test.ts` (fake backends; no live key required for `pnpm test`).

## Limits and data handling

Not a sandbox and not a replacement for client permission prompts. Adaptive attacks can miss; upstream publishes miss rates. Screened content leaves the machine unless a server is excluded. This listing did not run live MCP wrap or hooks against a real agent.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4220149](https://github.com/agent-chaperone/agent-chaperone/tree/4220149bed35d4c9402adb9a0b9a5d41874cf144) (`agent-chaperone` 0.3.1, Apache-2.0). AI-assisted source review of README, LICENSE, `src/backends/typesafe.ts`, CLI/hooks docs. Offline `pnpm test`: 1160 passed / 44 files. No live provider calls.

Related: [jev-shield](jev-shield.md), [JevShield](jevshield.md), [toolgate](toolgate.md), [pi-jev-permit](pi-jev-permit.md).

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Guard LangChain agent tool calls with Jev and human approval](../../knowledge-base/articles/building-a-jev-agent-harness.md) — Independently suggested by JevList; not an endorsement by Sydney Runkle. Compare a separate MCP/hook screening layer with the LangChain middleware path.
<!-- knowledge:backlinks:end -->
