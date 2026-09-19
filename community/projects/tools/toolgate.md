# toolgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open tool-call firewall for AI agents: static rules first, then TypeSafe Jev risk judgments, shipping as a Claude Code `PreToolUse` hook and an MCP stdio proxy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RiskAverseTech/toolgate) |
| Maintainer | [RiskAverseTech](https://github.com/RiskAverseTech) (Risk Averse Technology Company LLC). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package `@riskaverse/toolgate` **0.7.1** — CLI (`toolgate`), Claude Code hook, and MCP proxy. |
| Requirements | Node.js ≥ 20. Live gating needs `TYPESAFE_API_KEY` or `AI_GATEWAY_API_KEY`. Offline tests use a deterministic `mock` backend. Policy lives in `~/.toolgate/toolgate.yaml` (never the project tree). |
| License | [MIT](https://github.com/RiskAverseTech/toolgate/blob/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/LICENSE). |

## When to use

Use it when you want an auditable allow/ask/deny layer beside Claude Code's own permissions (including auto mode), or when wrapping any MCP server so `tools/call` requests are gated before they reach the server. Prefer static-only hooks when you do not want provider calls.

It complements catalogued Pi guards ([pi-jev](pi-jev.md), [pi-jev-sentinel](pi-jev-sentinel.md), [pi-warden](pi-warden.md)) rather than replacing them: toolgate targets Claude Code hooks and MCP clients with YAML policy and a local audit log.

## How it works

1. **Static rules** (user rules, then built-ins such as `rm -rf /` deny and `curl … | sh` ask) match first with no model call.
2. Tools outside `gated_tools` pass through.
3. Remaining calls go to the decision backend—TypeSafe direct (`https://api.typesafe.ai/v1/systemone`, default `jev-latest`) or Vercel AI Gateway—with parallel risk/context questions; thresholds map probabilities to deny / ask / allow, with authorization softening rules documented upstream.
4. Unattended Claude permission modes can escalate ask→deny by default. Model failures follow `fail_mode` (`ask` default). Internal errors never silently allow.

The [TypeSafe backend](https://github.com/RiskAverseTech/toolgate/blob/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/src/backends/typesafe.ts) and [engine](https://github.com/RiskAverseTech/toolgate/blob/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/src/engine.ts) implement this path. Decisions append to `~/.toolgate/audit.jsonl` with redaction heuristics.

## Get started

```sh
npm install -g @riskaverse/toolgate
export TYPESAFE_API_KEY=...
toolgate init    # writes policy + hook into ~/.claude/settings.json and runs doctor
```

Or inspect the reviewed commit:

```sh
git clone https://github.com/RiskAverseTech/toolgate.git
cd toolgate
git checkout 8b38a2faf620d7923505f3c546ebc0c79ca87f1f
npm ci --ignore-scripts
npm run build
npm test
```

`toolgate check --backend mock …` exercises offline heuristics without a key. Live `doctor` / hook paths can make a billable verdict. This listing did not install into Claude Code or wrap a live MCP server.

## Examples and demos

- [`examples/claude-settings.json`](https://github.com/RiskAverseTech/toolgate/blob/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/examples/claude-settings.json) and [`examples/toolgate.yaml`](https://github.com/RiskAverseTech/toolgate/blob/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/examples/toolgate.yaml).
- [test/](https://github.com/RiskAverseTech/toolgate/tree/8b38a2faf620d7923505f3c546ebc0c79ca87f1f/test): policy, engine, hook, install, MCP, and TypeSafe client tests (mock backend for offline paths).
- Upstream `docs/challenge-set-*.md` reports are maintainer challenge results, not catalog-run evaluations.

## Limits and data handling

On the model path, tool name/input (redacted/truncated), cwd, permission mode, and limited transcript prompts can leave the machine to TypeSafe or the AI Gateway. Static matches send nothing. Redaction is heuristic. `allow` remains advisory under Claude Code's own deny/confirm lists. toolgate is defense in depth, not a sandbox. Thresholds and challenge write-ups are not measured guarantees for your workload.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 8b38a2f](https://github.com/RiskAverseTech/toolgate/tree/8b38a2faf620d7923505f3c546ebc0c79ca87f1f): `@riskaverse/toolgate` **0.7.1**, MIT. AI-assisted source review of engine, backends, hook/MCP paths, README, and license. On Node.js 22.19.0, **`npm run build` then `npm test`: 165 passed** (6 files). An initial `npm test` before build failed 8 CLI e2e cases missing `dist/cli.js`—build-first is required. No live TypeSafe/Gateway calls or Claude Code install were performed.

Related: [pi-jev-sentinel](pi-jev-sentinel.md), [pi-jev](pi-jev.md), [pi-warden](pi-warden.md).
