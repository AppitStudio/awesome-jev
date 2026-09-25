# adecider

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed System One decisions for coding agents: one call sends state plus many Noul/Choice/Score questions and returns calibrated answers; backends are pluggable (local Laya by default, TypeSafe Jev, or OpenAI-compatible escape hatch).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Agents365-ai/adecider) |
| Maintainer | [Agents365-ai](https://github.com/Agents365-ai). Independently curated. |
| Format | TypeScript CLI (`adecider` / `adecider-gate`), MCP, HTTP `/decide`, and pi extension hooks. |
| Requirements | Node toolchain per package; local Laya checkpoint for default path; optional TypeSafe/OpenAI-compatible credentials when those backends are named. |
| License | [MIT](https://github.com/Agents365-ai/adecider/blob/b451dbbaf370992ee3ecdb2d0b38d6dba165ed17/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Laya/Jev paths not run on the review host. |

## When to use

Use when agents need **multi-question typed judgments** with local-first defaults and explicit cloud opt-in. Prefer thinner CLIs when you only need a single hosted Jev call shape.

## How it works

All surfaces call one `judge()` core: validate questions, select backend, adapt dialect, normalize answers, optionally apply threshold/top-k decisions. Named cloud backends do not silently fall back.

## Get started

```sh
git clone https://github.com/Agents365-ai/adecider.git
cd adecider
git checkout b451dbbaf370992ee3ecdb2d0b38d6dba165ed17
# See README for adecider judge / adecider-gate / mcp-config / serve
```

## Examples and demos

- README `adecider judge` JSON example with threshold decisions.
- `adecider mcp-config` for pi, Claude Code, and Codex paste configs.

## Limits and data handling

State is local by default; naming a cloud backend sends state off-machine. No threshold means no verdicts—callers choose cutoffs. Latency figures in README are upstream-reported.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit b451dbb](https://github.com/Agents365-ai/adecider/tree/b451dbbaf370992ee3ecdb2d0b38d6dba165ed17). AI-assisted README and LICENSE inspection; install/live backends not executed.
