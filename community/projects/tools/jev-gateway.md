# jev-gateway

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local LLM gateway for coding agents: TypeSafe Jev chooses which tool to call each turn for Codex, Claude Code, OpenCode, or Gemini, while other request content still goes to your usual LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vinilana/jev-gateway) |
| Maintainer | [vinilana](https://github.com/vinilana). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package `jev-gateway` **0.3.1** — launchers (`jev-codex`, `jev-claude`, `jev-opencode`, `jev-gemini`) and a local monitoring dashboard. |
| Requirements | Node.js ≥ 22.15, a TypeSafe API key in `~/.jev-gateway/.env`, and an already-installed Codex, Claude Code, OpenCode, and/or Gemini CLI login. Listens on `127.0.0.1` only. |
| License | [MIT](https://github.com/vinilana/jev-gateway/blob/9463952bf118773fb955427d2725a98f76546233/LICENSE). |

## When to use

Use it when you want Jev to steer tool selection for an existing coding-agent subscription without changing that agent's config files. Prefer leaving routing off (`--routing off`) when you only want token accounting, or skip the gateway when you do not want a local proxy at all.

It complements catalogued routers such as [jev-router](jev-router.md), [jev-codex-router](jev-codex-router.md), and [jev-use](jev-use.md): jev-gateway sits as an OpenAI/Anthropic/Gemini-compatible local proxy rather than an MCP plugin or Codex Router provider.

## How it works

Each turn, the gateway asks Jev which tool fits the pending decision. When Jev is confident, the gateway steers the upstream LLM toward that tool; when it is not, or when Jev is unavailable, the request passes through unchanged. Upstream agent logins stay untouched. Decision logic lives in [`src/decide.ts`](https://github.com/vinilana/jev-gateway/blob/9463952bf118773fb955427d2725a98f76546233/src/decide.ts) and [`src/questions.ts`](https://github.com/vinilana/jev-gateway/blob/9463952bf118773fb955427d2725a98f76546233/src/questions.ts) using `@typesafe-ai/sdk` (default model `jev-latest`).

## Get started

```sh
npm install -g jev-gateway
mkdir -p ~/.jev-gateway
echo "TYPESAFE_API_KEY=your-key-here" > ~/.jev-gateway/.env
jev-codex      # or jev-claude / jev-opencode / jev-gemini
```

Or inspect the reviewed commit:

```sh
git clone https://github.com/vinilana/jev-gateway.git
cd jev-gateway
git checkout 9463952bf118773fb955427d2725a98f76546233
npm install --ignore-scripts
npm test
```

Live launchers can call TypeSafe and your coding-agent upstream. This listing did not run `jev-codex` against a live agent session.

## Examples and demos

- Launchers under [`bin/`](https://github.com/vinilana/jev-gateway/tree/9463952bf118773fb955427d2725a98f76546233/bin) and dashboard HTML in the package.
- [`test/`](https://github.com/vinilana/jev-gateway/tree/9463952bf118773fb955427d2725a98f76546233/test): router, adapters, launcher, and dashboard coverage with a mock Jev path.
- `jev-codex --dashboard` / `--logs` for live routing inspection (requires a running gateway).

## Limits and data handling

Tool-decision state is sent to TypeSafe when routing is on. Agent prompts and tool results still go to your usual LLM upstream. Failures fail open to the LLM. The gateway binds to localhost only; do not expose it on untrusted networks. Routing quality is operational policy, not a measured win rate for your workload.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 9463952](https://github.com/vinilana/jev-gateway/tree/9463952bf118773fb955427d2725a98f76546233): `jev-gateway` **0.3.1**, MIT. AI-assisted source review of decide/questions/adapters, README, and license. On Node.js 24.8.0, **`npm test` (vitest): 90 passed** (9 files). No live TypeSafe or coding-agent sessions were run.

Related: [jev-router](jev-router.md), [jev-codex-router](jev-codex-router.md), [toolgate](toolgate.md).
