# jeveloper

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin / skill: System-1 reflex layer powered by TypeSafe Jev via OpenRouter or TypeSafe—route/gate tool calls, verify tool output, judge completion, and optional driver mode that lets Jev pick the next action while Claude executes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pur4v/jeveloper) |
| Maintainer | [pur4v](https://github.com/pur4v). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code marketplace plugin **jeveloper 0.2.0** (hooks, skills, `/jeveloper:*` commands). |
| Requirements | Claude Code. Live reflexes need `OPENROUTER_API_KEY` or `TYPESAFE_API_KEY` (installer can store OpenRouter key in the OS keychain). Without a key, upstream runs MOCK mode. |
| License | [MIT](https://github.com/pur4v/jeveloper/blob/48567f129a1ac4f852b30b270d1831181fc43a70/LICENSE). Provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, plugin.json, hooks/skills layout). Plugin install and live Jev were **not** executed on the review host. Upstream latency/cost claims were not re-measured. |

## When to use

Use it when Claude Code should get cheap typed reflexes (gate/verify/done) around every turn, or driver mode that offloads action choice to Jev. Prefer lighter PreToolUse-only gates ([claude-code-jev](claude-code-jev.md), [toolgate](toolgate.md)) when you do not want a full reflex loop.

## How it works

Hooks call Jev to decide/gate/verify and hold the loop until completion judgments pass. `/jeveloper:drive` has Claude enumerate candidate actions; Jev picks one; Claude executes; check/warden hooks verify. Per-project `.jeveloper.json` can narrow or disable reflexes.

## Get started

```text
/plugin marketplace add pur4v/jeveloper
/plugin install jeveloper
# Restart Claude Code so hooks register; supply OpenRouter or TypeSafe key
```

Pin for review: [commit 48567f1](https://github.com/pur4v/jeveloper/tree/48567f129a1ac4f852b30b270d1831181fc43a70) (**0.2.0**).

## Examples and demos

- `bash demo.sh` / `/jeveloper:demo` (not run here).
- `/jeveloper:stats`, decision-tree examples under `examples/`.

## Limits and data handling

Heavy by design (Jev around many actions). Live calls send loop state to OpenRouter/TypeSafe. Keys should stay in keychain/env, not the repo. This listing did not install the plugin or call Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 48567f1](https://github.com/pur4v/jeveloper/tree/48567f129a1ac4f852b30b270d1831181fc43a70) (MIT). AI-assisted review of README, LICENSE, and plugin manifest. No live TypeSafe spend.

Related: [claude-code-jev](claude-code-jev.md), [toolgate](toolgate.md), [agent-chaperone](agent-chaperone.md), [compact-adviser](compact-adviser.md).
