# VexJoy Agent

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent toolkit for Claude Code, Codex, and related hosts: `/do` routes plain-English work to specialist agents and skills; optional `/d` uses TypeSafe Jev to classify and gate intent before dispatch.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/notque/vexjoy-agent) |
| Maintainer | [notque](https://github.com/notque). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python agent toolkit **vexjoy-agent 1.0.0** (agents, skills, hooks, scripts; install via upstream `install.sh` / Makefile). |
| Requirements | Python ≥ 3.10; a coding-agent host (Claude Code `/do`, Codex `$do`, and related); for `/d`, `TYPESAFE_API_KEY` and/or `AI_GATEWAY_API_KEY` (`JEV_TRANSPORT` = `direct` / `vercel` / `auto`). |
| License | [MIT](https://github.com/notque/vexjoy-agent/blob/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1/LICENSE). |

## When to use

Use it when you want a large domain-agent and skill catalog driven from short requests, with hooks and scripts for verification. Prefer a single-purpose model router such as [jev-router](jev-router.md) or [jev-gateway](jev-gateway.md) when you only need model/tool selection without the VexJoy agent/skill library.

## How it works

`/do` pairs agents and skills from a live routing manifest. `/d` is the Jev-backed A/B path: [`scripts/jev-route.py`](https://github.com/notque/vexjoy-agent/blob/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1/scripts/jev-route.py) runs a deterministic force-route guard, then staged TypeSafe Jev Choice/Noul calls over manifest candidates (wide rank, then shortlist rerank). [`hooks/jev-route-injector-userprompt.py`](https://github.com/notque/vexjoy-agent/blob/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1/hooks/jev-route-injector-userprompt.py) can run that script at UserPromptSubmit and inject `JEV_RESULT` before the model generates. On transport failure or low confidence, `/d` falls open to full `/do`. Intent-alignment receipts can be logged without raw request text.

## Get started

```sh
git clone https://github.com/notque/vexjoy-agent.git
cd vexjoy-agent
git checkout 8ad68453bb6738abb1d1d665f3bb70f7cb18bde1
# follow upstream install for your host; then try /do or /d inside Claude Code / Codex
```

Live `/d` needs a TypeSafe or Vercel AI Gateway key (provider charges may apply). This listing did not call TypeSafe or install into a live agent host.

## Examples and demos

- Command docs [`commands/d.md`](https://github.com/notque/vexjoy-agent/blob/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1/commands/d.md) and [`commands/do.md`](https://github.com/notque/vexjoy-agent/blob/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1/commands/do.md).
- Hook tests under `hooks/tests/` and plugin tests under `plugins/jev-auto-compact/tests/` (not executed on the review host).
- Essays at [vexjoy.com](https://vexjoy.com).

## Limits and data handling

`/d` sends request text and truncated/full skill or agent descriptions to TypeSafe or the configured gateway. The injector fails open on timeout or mismatch. The broader toolkit includes many agents, hooks, and scripts beyond Jev routing; treat Jev as optional for `/d` only. Do not ship API keys in client-side apps.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 8ad6845](https://github.com/notque/vexjoy-agent/tree/8ad68453bb6738abb1d1d665f3bb70f7cb18bde1): **1.0.0**, MIT. AI-assisted source review of README, `/d` command, `jev-route.py`, and the UserPromptSubmit injector. No live TypeSafe route and no host install.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [jev-gateway](jev-gateway.md), [SkillRanker](skillranker.md).
