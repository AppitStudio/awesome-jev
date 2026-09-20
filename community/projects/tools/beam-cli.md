# beam-cli (AgentBeam)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local AgentBeam CLI (`beam`): installs native hooks for detected coding agents, captures agent/MCP activity, applies policy locally, and optionally judges proposed actions with TypeSafe Jev (Noul and/or Score). Jev judging is **disabled by default**.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/whyashthakker/beam-cli) |
| Maintainer | [whyashthakker](https://github.com/whyashthakker) (Yash Thakker) / [agentbeam.com](https://www.agentbeam.com). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI **@agent-beam/beam 0.2.16** (npm; `bin` `beam`) plus Skills tree; AGPL-3.0. |
| Requirements | Node.js suitable for the published package; supported agents (Claude Code, Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode, …). Optional Jev needs `TYPESAFE_API_KEY`. Dashboard/device linking is separate from offline scanning. |
| License | [AGPL-3.0](https://github.com/whyashthakker/beam-cli/blob/42c8d1755f8e67e566f2412fba9d8660475db516/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live agent hooks, dashboard sync, and live TypeSafe Jev judging were not run. |

## When to use

Use it when you want a **local monitoring and policy layer** across multiple agent CLIs, with optional TypeSafe Jev action review on top of heuristic redaction/blocking. Prefer [jev-guard](jev-guard.md) / [toolgate](toolgate.md) / [jev-shield](jev-shield.md) for Jev-first tool-call firewalls without the AgentBeam service model. Prefer [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md) for Pi bash-only gates.

## How it works

Core protection uses local hooks, secret redaction, and organization/user policy. Optional Jev integration in [`src/jev.ts`](https://github.com/whyashthakker/beam-cli/blob/42c8d1755f8e67e566f2412fba9d8660475db516/src/jev.ts) posts to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) with Noul risk questions and/or a Score damage rubric (`beam jev configure`). Inputs are size-capped and redacted; modes are `observe` or `enforce`. README notes TypeSafe Jev CLIs are discovery-only in the agent table (ecosystem too fragmented for one hook contract).

## Get started

```sh
npm i -g @agent-beam/beam
# or from the reviewed tip:
git clone https://github.com/whyashthakker/beam-cli.git
cd beam-cli
git checkout 42c8d1755f8e67e566f2412fba9d8660475db516
npm ci --ignore-scripts
npm test
# Optional Jev (sends redacted action summaries to TypeSafe; can incur charges):
# beam jev configure --mode observe --primitive both
```

`beam setup` installs hooks and may connect a device to the AgentBeam dashboard—review upstream docs before running it on a machine you care about. This listing did not run `beam setup` or live Jev.

## Examples and demos

- Offline `npm test` — **20 suites / 256 tests passed** on the review host (includes `tests/jev.test.ts`).
- Upstream README multi-agent table and `beam jev status` / Skills tree.

## Limits and data handling

AGPL-3.0 applies to the CLI. Enabling Jev sends selected redacted action data to TypeSafe. Dashboard sync and org policy are vendor-hosted paths not exercised here. Upstream protection/coverage claims were not independently measured. Auto-delegation-style “Jev agent” discovery is not the same as the optional action-judge feature.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 42c8d17](https://github.com/whyashthakker/beam-cli/tree/42c8d1755f8e67e566f2412fba9d8660475db516): **0.2.16**, AGPL-3.0. AI-assisted source review of README, LICENSE, `src/jev.ts`, `package.json`, and tests. Ran `npm ci --ignore-scripts` and `npm test` (256 pass). No live TypeSafe or `beam setup` runs.

Related: [jev-guard](jev-guard.md), [toolgate](toolgate.md), [jev-shield](jev-shield.md).
