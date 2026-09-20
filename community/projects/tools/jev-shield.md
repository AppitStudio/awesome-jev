# jev-shield

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic MCP firewall and agent skill: screens tool calls, tool results, and tool descriptions with TypeSafe Jev via Vercel AI Gateway `experimental_evaluate`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/caiovicentino/jev-shield) |
| Maintainer | [caiovicentino](https://github.com/caiovicentino). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js package **jev-shield 0.1.0** — CLI, MCP wrap proxy, Claude Code / opencode hooks (opt-in), and installable agent skill. |
| Requirements | Node.js ≥ 20; `AI_GATEWAY_API_KEY` for live checks (Vercel AI Gateway model `typesafe-ai/jev`). |
| License | [MIT](https://github.com/caiovicentino/jev-shield/blob/ea13a3be94c6af4ace7912de5909678e5e24941f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live MCP wrap, hooks, and live Jev were not run. Upstream eval recall figures are vendor-reported. |

## When to use

Use it when you want MCP-centric semantic screening (calls, results, and catalog descriptions) plus a cooperative `/verify` skill, with optional hook enforcement. Prefer [toolgate](toolgate.md) for YAML static rules plus Claude Code / MCP proxying against TypeSafe direct or Gateway. Prefer [jev-guard](jev-guard.md) for multi-agent risk scoring with session memory. Complements rather than replaces those listings.

## How it works

[`src/verify.mjs`](https://github.com/caiovicentino/jev-shield/blob/ea13a3be94c6af4ace7912de5909678e5e24941f/src/verify.mjs) runs boolean/score batteries (exfiltration, destructive action, injection in args/results, secrets, severity) through Vercel AI SDK `experimental_evaluate` with `typesafe-ai/jev`. [`src/firewall.mjs`](https://github.com/caiovicentino/jev-shield/blob/ea13a3be94c6af4ace7912de5909678e5e24941f/src/firewall.mjs) wraps an upstream MCP server so every `tools/call` and result is screened. Opt-in hooks/plugins enforce deny/ask; local Read/Grep/Glob-style tools are exempt by default. Policy lives in `config/policies.json`.

## Get started

```sh
git clone https://github.com/caiovicentino/jev-shield.git
cd jev-shield
git checkout ea13a3be94c6af4ace7912de5909678e5e24941f
export AI_GATEWAY_API_KEY=…
npx -y github:caiovicentino/jev-shield verify   # or: node bin/jev-shield.mjs …
# optional enforcement:
npx -y github:caiovicentino/jev-shield install-hooks
```

Live checks send tool names, arguments, and results to the Gateway and can incur charges. This listing did not wrap an MCP server or call live Jev.

## Examples and demos

- `demo/attack.mjs` and `eval/run.mjs` (offline harness present; not executed on the review host).
- README skill install for Claude Code / opencode / Codex MCP wrap.

## Limits and data handling

Tool payloads leave the host for Vercel AI Gateway / Jev. Kill switches: `JEV_HOOK_OFF=1`, uninstall-hooks, fail-open/closed via `JEV_FAIL_MODE`. Upstream 94% block-recall / cost claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ea13a3b](https://github.com/caiovicentino/jev-shield/tree/ea13a3be94c6af4ace7912de5909678e5e24941f): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/verify.mjs`, `src/firewall.mjs`, `config/policies.json`, and `package.json`. No live Gateway or agent-hook runs.

Related: [toolgate](toolgate.md), [jev-guard](jev-guard.md), [jev-sift](jev-sift.md).
