# jev-pilot (Akramovic1)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin where TypeSafe Jev (or OpenRouter / AI Gateway / builtin) picks reasoning effort, optional subagent model, strategy advice, and one skill per prompt—distinct from the [JevPilot](jevpilot.md) driving simulation demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Akramovic1/jev-pilot) |
| Maintainer | [Akramovic1](https://github.com/Akramovic1). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code plugin **jev-pilot 0.4.4** (`hooks/`, `bin/claude-jev`); MIT LICENSE file present (GitHub SPDX may show NOASSERTION). |
| Requirements | Claude Code **2.1.278+** with `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` (launcher sets it); TypeSafe / OpenRouter / Gateway key as configured. Built on davila7/claude-code-templates mods (credited in LICENSE). |
| License | [MIT](https://github.com/Akramovic1/jev-pilot/blob/f7676e1dc97241ba3a67299a5df81db4ffa24fe6/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, plugin.json, hooks). Live Claude Code/Jev were **not** run on the review host. |

## When to use

Use it when Claude Code should adapt effort/subagents/skills from typed Jev decisions with an optional “pilot” pet UI. Prefer [jev-effort-router](jev-effort-router.md) / [Astra-Ares](astra-ares.md) for other effort routers; prefer [JevPilot](jevpilot.md) only for the unrelated driving demo.

## How it works

Function hooks call Jev before/during turns ([`hooks/jev-pilot.ts`](https://github.com/Akramovic1/jev-pilot/blob/f7676e1dc97241ba3a67299a5df81db4ffa24fe6/hooks/jev-pilot.ts), model/skill routers under `hooks/`). Decisions can be recorded for `/jev-pilot:report`. The pet display talks outside the conversation transcript when enabled.

## Get started

```sh
# Follow upstream install (plugin marketplace / install.sh / claude-jev launcher)
git clone https://github.com/Akramovic1/jev-pilot.git
cd jev-pilot
git checkout f7676e1dc97241ba3a67299a5df81db4ffa24fe6
# configure TypeSafe or OpenRouter key in plugin userConfig; enable function hooks
```

Pin for review: [commit f7676e1](https://github.com/Akramovic1/jev-pilot/tree/f7676e1dc97241ba3a67299a5df81db4ffa24fe6). Live decisions send bounded prompt/context to the chosen backend and may incur charges.

## Examples and demos

- README demo SVG (illustrative numbers).
- Upstream tests under `engine/` and GitHub Actions (not re-run here).

## Limits and data handling

Function hooks are early-access Claude Code surface. Main-model routing is off by default (cache). Timeouts fail open to unchanged behavior. No live TypeSafe spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit f7676e1](https://github.com/Akramovic1/jev-pilot/tree/f7676e1dc97241ba3a67299a5df81db4ffa24fe6) (**0.4.4**, MIT file). AI-assisted source review. No live Claude Code or TypeSafe spend.

Related: [jev-effort-router](jev-effort-router.md), [Astra-Ares](astra-ares.md), [JevPilot](jevpilot.md).
