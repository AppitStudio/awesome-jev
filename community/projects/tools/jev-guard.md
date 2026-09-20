# jev-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Security hook for coding agents: TypeSafe Jev risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results, and scans instruction files.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leepokai/jev-guard) |
| Maintainer | [leepokai](https://github.com/leepokai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js npm package **jev-guard 0.3.1** — zero runtime dependencies; CLI + adapters for Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, pi, OpenCode, and ACP. |
| Requirements | Node.js ≥ 20.3; TypeSafe key (`JEV_API_KEY` / `jev-guard key`) or Vercel AI Gateway key. Live gating incurs provider usage. |
| License | [MIT](https://github.com/leepokai/jev-guard/blob/94996ea80b6b308327ac2077706a29ce6abd3ba0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live agent hooks and live Jev were not run. |

## When to use

Use it when you want Claude Code–style auto-mode judgments across many coding agents with one shared policy and session memory. Prefer [toolgate](toolgate.md) for YAML static rules plus Claude Code / MCP firewalling, or [typesafe-agent-gates](typesafe-agent-gates.md) for LangChain middleware. Complements Pi-native guards ([pi-jev](pi-jev.md), [pi-jev-sentinel](pi-jev-sentinel.md)) rather than replacing them.

## How it works

[`src/guard.js`](https://github.com/leepokai/jev-guard/blob/94996ea80b6b308327ac2077706a29ce6abd3ba0/src/guard.js) asks narrow typed questions (risk score, approval, user-requested, untrusted/injection) via [`src/jev.js`](https://github.com/leepokai/jev-guard/blob/94996ea80b6b308327ac2077706a29ce6abd3ba0/src/jev.js) posting to `https://api.typesafe.ai/v1/systemone` (or the Vercel AI Gateway). Code maps probabilities to deny / ask / allow and remembers untrusted session content. Separate instruction-file questions cover unexpected skill/plugin behavior. Thin host adapters translate each agent's hook payload.

## Get started

```sh
git clone https://github.com/leepokai/jev-guard.git
cd jev-guard
git checkout 94996ea80b6b308327ac2077706a29ce6abd3ba0
npm i -g .
jev-guard key "…"   # TypeSafe or vck_… Gateway key
jev-guard install claude   # or codex|copilot|gemini|cursor|pi|opencode
jev-guard check Bash '{"command":"rm -rf ~/"}'
```

Live checks send tool-call text and session context to the provider and can incur charges. This listing did not install hooks into an agent or call live Jev.

## Examples and demos

- Upstream launch video and README agent install matrix.
- Offline `test/guard.test.js` — not executed on the review host.

## Limits and data handling

Tool arguments, results, and skill file contents can leave the host for TypeSafe or the Gateway. Keys live in `~/.jev-guard/config.json` (mode 0600) or env vars; upstream states they are not given to the coding agent. Upstream price/latency claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 94996ea](https://github.com/leepokai/jev-guard/tree/94996ea80b6b308327ac2077706a29ce6abd3ba0): **0.3.1**, MIT. AI-assisted source review of README, LICENSE, `src/jev.js`, `src/guard.js`, and `package.json`. No live TypeSafe or agent-hook runs.

Related: [toolgate](toolgate.md), [jev-preflight](jev-preflight.md), [pi-jev-sentinel](pi-jev-sentinel.md).
