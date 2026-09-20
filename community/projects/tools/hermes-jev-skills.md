# Hermes Jev Skills

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skills and a `jev` CLI that use TypeSafe Jev for model routing, memory filtering, compaction, skill selection, triage, and computer/browser action choice on Hermes, Claude Code, and Codex.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kerpopule/hermes-jev-skills) |
| Maintainer | [kerpopule](https://github.com/kerpopule). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python skills package with `install.py`, `jevkit` client, Hermes plugin, and optional routing dashboard (changelog **0.10.0**). |
| Requirements | Python ≥ 3.9, a TypeSafe API key via `jev setup-key` (OS keychain / Hermes `.env`), and Hermes and/or Claude Code / Codex for skill install. |
| License | [MIT](https://github.com/kerpopule/hermes-jev-skills/blob/e2a179d232310ff6c55465e071460ad5d310aa2c/LICENSE). |

## When to use

Use it when you want Jev to handle small agent decisions (which model, which memory passages, which skill, next safe GUI/browser action) so a larger model keeps writing and planning. Prefer a single-purpose router such as [jev-gateway](jev-gateway.md) or [SkillRanker](skillranker.md) when you only need one of those workflows.

## How it works

[`jevkit/client.py`](https://github.com/kerpopule/hermes-jev-skills/blob/e2a179d232310ff6c55465e071460ad5d310aa2c/jevkit/client.py) posts typed questions to `https://api.typesafe.ai/v1/systemone`. Skills under `skills/` and the Hermes plugin call that client for routing, memory, compaction, skill pick, triage, and computer/browser choices. Fixed acknowledgements can skip Jev. Key setup stores the TypeSafe key outside the agent chat.

## Get started

```sh
git clone https://github.com/kerpopule/hermes-jev-skills.git
cd hermes-jev-skills
git checkout e2a179d232310ff6c55465e071460ad5d310aa2c
python3 -m unittest discover -s tests -v
python3 install.py --check
```

Live install needs an agent host and `jev setup-key`. This listing did not run live Hermes/Claude/Codex sessions or call TypeSafe.

## Examples and demos

- Skill folders under [`skills/`](https://github.com/kerpopule/hermes-jev-skills/tree/e2a179d232310ff6c55465e071460ad5d310aa2c/skills) and Hermes plugin under [`hermes/plugin/hermes-jev`](https://github.com/kerpopule/hermes-jev-skills/tree/e2a179d232310ff6c55465e071460ad5d310aa2c/hermes/plugin/hermes-jev).
- Offline unit tests in [`tests/`](https://github.com/kerpopule/hermes-jev-skills/tree/e2a179d232310ff6c55465e071460ad5d310aa2c/tests) (routing middleware, client shapes, skill content).
- Optional [`router-dashboard`](https://github.com/kerpopule/hermes-jev-skills/tree/e2a179d232310ff6c55465e071460ad5d310aa2c/router-dashboard).

## Limits and data handling

Decision state (prompts, memory passages, action tables) is sent to TypeSafe when a skill calls Jev. Keys are meant to stay in the OS secret store or Hermes `.env`, not in chat. Routing and skill-pick quality are operational; README timing/cost figures are upstream anecdotes, not catalog benchmarks. Failures and “off” modes are documented upstream—confirm before relying on fail-open behavior for your risk posture.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e2a179d](https://github.com/kerpopule/hermes-jev-skills/tree/e2a179d232310ff6c55465e071460ad5d310aa2c): changelog **0.10.0**, MIT. AI-assisted source review of `jevkit/client.py`, skills layout, README, and license. On Python 3.12+, **`python3 -m unittest discover -s tests -v`: 184 tests OK**. No live TypeSafe or agent-host sessions were run.

Related: [jev-gateway](jev-gateway.md), [SkillRanker](skillranker.md), [jev-use](jev-use.md).
