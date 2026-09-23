# Open Jev Bridge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Node MCP server plus Claude Code/Codex hooks: verbatim compaction, evidence-sensitive completion checks, and fourteen System One judgment tools. Bridges hosted Jev, local Kev/Laya, or another compatible `POST /v1/systemone` backend. Distinct from [jev-mcp](jev-mcp.md) and [fast-jev-compaction](fast-jev-compaction.md) (independent reimplementation; not a fork).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/louis-szeto/open-jev-bridge) |
| Maintainer | [louis-szeto](https://github.com/louis-szeto). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI/MCP **open-jev-bridge 0.3.0** (`bin/open-jev-bridge.mjs`; zero npm runtime dependencies). |
| Requirements | Node.js (stdlib only). Default local loopback Kev at `http://127.0.0.1:8009`. Hosted Jev needs `SYSTEM_ONE_URL` / `SYSTEM_ONE_MODEL` / `SYSTEM_ONE_API_KEY` / `SYSTEM_ONE_ALLOW_REMOTE` (does **not** implicitly read `TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/louis-szeto/open-jev-bridge/blob/d96fe53df9e6d1a05e5ed41819a064915315e5f7/LICENSE). Provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, tool/automation summary). Installer/doctor and live System One calls were **not** executed on the review host. |

## When to use

Use it when you want provider-neutral MCP + lifecycle automation (Stop/PreCompact hooks) for compaction and completion gates across Claude Code and Codex. Prefer [jev-mcp](jev-mcp.md) for a Jev-only npm judgment server without the bridge's hook installer.

## How it works

Transport always posts `{model, state, questions}` to `/v1/systemone`. Tools use `system_one_*` names (optional `jev_*` aliases). Version 0.3.0 enables lifecycle automation by default after install and native hook trust; stable hooks create compaction checkpoints and do not claim to replace live history except via an optional Claude function-hook path.

## Get started

```sh
git clone https://github.com/louis-szeto/open-jev-bridge.git
cd open-jev-bridge
git checkout d96fe53df9e6d1a05e5ed41819a064915315e5f7
# Configure SYSTEM_ONE_* for local Kev or hosted Jev, then:
node bin/open-jev-bridge.mjs doctor
node bin/open-jev-bridge.mjs install --host both
```

Pin for review: [commit d96fe53](https://github.com/louis-szeto/open-jev-bridge/tree/d96fe53df9e6d1a05e5ed41819a064915315e5f7).

## Examples and demos

- README hosted-Jev and local-Kev configuration examples.
- `automation-status` / `doctor` CLI checks (not run here).

## Limits and data handling

Judgments are probabilistic, not proofs. Screening is advisory. Hosted Jev sends task/compaction state to TypeSafe when enabled. Default remains loopback with no automatic cloud fallback. This listing did not run install or live calls.

## Review and maintenance

Reviewed on **2026-09-23** at [commit d96fe53](https://github.com/louis-szeto/open-jev-bridge/tree/d96fe53df9e6d1a05e5ed41819a064915315e5f7) (**0.3.0**, MIT). AI-assisted review of README and LICENSE. No live TypeSafe spend.

Related: [jev-mcp](jev-mcp.md), [fast-jev-compaction](fast-jev-compaction.md), [agent-chaperone](agent-chaperone.md).
