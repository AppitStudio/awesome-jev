# jev-plays

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Harness and web UI where TypeSafe Jev plays Craftax (JAX Crafter): Jev picks among code-built macro or primitive actions while an optional LLM planner writes objectives and standing rules as facts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mansicer/jev-plays) |
| Maintainer | [mansicer](https://github.com/mansicer). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package under `craftax_agent/` plus local web viewer/server. |
| Requirements | Python; Craftax/JAX stack per `requirements.txt`; `TYPESAFE_API_KEY` for Jev policies; optional OpenAI-compatible key for the planner/LLM agent. |
| License | [Apache-2.0](https://github.com/mansicer/jev-plays/blob/35e4cd51e428a4d977101c795137c4c6f701f89a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Source inspected (`jev_policy.py`); full Craftax/JAX install and live play not run on the review host. |

## When to use

Use it when you want to **study System One game control** (macro vs raw actions, planner-as-facts) on Craftax with inspectable option tables. Prefer [jev-zork](jev-zork.md) for classic IF, or [TypeSafe Mario](typesafe-mario.md) for emulator telemetry demos. Reported achievement numbers are upstream experiment claims, not re-measured here.

## How it works

Code builds candidate tables and legality; `TypeSafeClient.system_one` chooses among macros/actions. Planner text is injected as facts, not advice. Low-confidence fallbacks and pathing stay in code. A local UI replays logs and shows per-step probabilities.

## Get started

```sh
git clone https://github.com/mansicer/jev-plays.git
cd jev-plays
git checkout 35e4cd51e428a4d977101c795137c4c6f701f89a
# Follow upstream README: create .env (TYPESAFE_API_KEY, optional OPENAI_*), install requirements, run viewer/agent
# Example (needs deps + key): python -m craftax_agent.run_agent --policy jev_macro --steps 100 --seeds 0
```

Live Jev steps send game-state facts and option text to TypeSafe and may incur charges; planner calls use your OpenAI-compatible endpoint. This listing did not install Craftax/JAX or call TypeSafe.

## Examples and demos

- Upstream README: multi-agent GIF, architecture diagram, and web UI screenshots from logged episodes.
- Integration evidence: [`craftax_agent/jev_policy.py`](https://github.com/mansicer/jev-plays/blob/35e4cd51e428a4d977101c795137c4c6f701f89a/craftax_agent/jev_policy.py) constructs `TypeSafeClient` and issues Choice/Noul `system_one` calls.

## Limits and data handling

Game facts and option descriptions leave the host on live Jev; planner prompts leave for the LLM provider. Episode logs may retain decisions—keep them private if they include sensitive keys. Harness results depend on seeds, option wording, and planner settings.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 35e4cd5](https://github.com/mansicer/jev-plays/tree/35e4cd51e428a4d977101c795137c4c6f701f89a): Apache-2.0. AI-assisted source review of README, LICENSE, `craftax_agent/jev_policy.py`, `run_agent.py`. No Craftax install or live TypeSafe on the review host.

Related: [jev-zork](jev-zork.md), [TypeSafe Mario](typesafe-mario.md), [Jev Lab](jev-lab.md).
