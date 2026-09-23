# opencode-jev-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode 2 plugin: every local `shell` (and FarHand remote shell) command is judged by TypeSafe Jev before run—overall verdict plus host-litter / global-install / global-config / harmful / privacy risks. Distinct from [leepokai/jev-guard](jev-guard.md) multi-agent hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CogFlux/opencode-jev-guard) |
| Maintainer | [CogFlux](https://github.com/CogFlux). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript OpenCode plugin **opencode-jev-guard 0.1.0** (`jev-guard.ts`; private package layout). |
| Requirements | OpenCode 2; TypeSafe API key via plugin options or env. Fail-ask when Jev is unreachable (never silent allow). |
| License | [MIT](https://github.com/CogFlux/opencode-jev-guard/blob/8c304cbcd97ec670152e8ede93d10b98fc760332/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, package, plugin entry). Live OpenCode/FarHand/Jev runs were **not** executed on the review host. |

## When to use

Use it when OpenCode (optionally with FarHand) should confirm risky shell before execution with typed Jev categories you can retune. Prefer [jev-guard](jev-guard.md) for multi-host agent installs; prefer [fast-jev-opencode](fast-jev-opencode.md) for request compaction rather than shell permission.

## How it works

Before shell/MCP remote shell execute, the plugin asks Jev six questions (verdict + five risk noul-style categories). Safe only if verdict is `run` above `minConfidence` and all risks below thresholds; otherwise OpenCode’s permission prompt (with a transcript note, because OpenCode’s prompt body may omit reasons). Global vs project `jev-guard.jsonc`: project files can only tighten. `/jev on|off|status|risks` session commands.

## Get started

```sh
git clone https://github.com/CogFlux/opencode-jev-guard.git
cd opencode-jev-guard
git checkout 8c304cbcd97ec670152e8ede93d10b98fc760332
npm test   # node --test; offline fixtures
# Install/register as an OpenCode 2 plugin per upstream README; set TypeSafe key
```

## Examples and demos

- `jev-guard.example.jsonc` documented options.
- `bench/cases.jsonl` + `bench/run.ts`; `test/` fixtures including FarHand project sample.

## Limits and data handling

Command text (and remote host/workdir context for FarHand) leave the machine for TypeSafe. `/jev off` disables confirmation (deny rules in OpenCode permission config still apply). This listing did not install OpenCode or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 8c304cb](https://github.com/CogFlux/opencode-jev-guard/tree/8c304cbcd97ec670152e8ede93d10b98fc760332) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, package. No live TypeSafe spend.

Related: [jev-guard](jev-guard.md), [fast-jev-opencode](fast-jev-opencode.md), [agent-chaperone](agent-chaperone.md).
