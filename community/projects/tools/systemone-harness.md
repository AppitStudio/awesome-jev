# System One Harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python controller that turns a System One decision model into an agent loop: observe an environment, compile a finite action space into typed questions, gate by confidence, execute one action per step, and record a full trace. First supported model is TypeSafe Jev (OpenRouter or TypeSafe API).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HarnessRouter/SystemOneHarness) |
| Maintainer | [HarnessRouter](https://github.com/HarnessRouter). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package `systemone-harness` **0.4.0** with `s1` CLI; optional MCP and browser extras. |
| Requirements | Python ≥ 3.10; `httpx`, `pyyaml`. Live runs need `OPENROUTER_API_KEY` or `TYPESAFE_API_KEY`. Optional `mcp` / `browser-use` extras for those environments. |
| License | [Apache-2.0](https://github.com/HarnessRouter/SystemOneHarness/blob/ab8e8f08b4a6268c0633a474423d556599ee06a4/LICENSE). Provider inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest` (with `[mcp]`): **44 passed**, 2 skipped. Live OpenRouter/TypeSafe runs not executed. |

## When to use

Use it when you want a finite-action agent loop where Jev only chooses among environment-declared actions and parameters, with confidence gates and step traces. Prefer [jev-harness](jev-harness.md) / [jev-layer](jev-layer.md) for TypeScript policy libraries, or [Jev Ultrafast](jev-ultrafast.md) for a browser-only research loop. Distinct focus: pluggable environments (Python, MCP, browser) behind one System One controller.

## How it works

[`provider.py`](https://github.com/HarnessRouter/SystemOneHarness/blob/ab8e8f08b4a6268c0633a474423d556599ee06a4/systemone_harness/provider.py) posts typed decisions to OpenRouter (`/api/alpha/decisions`, default `~typesafe/jev-latest`) or TypeSafe (`/v1/systemone`, default `jev-latest`). The controller compiles the environment’s action space into Choice/Score/Noul-style questions, applies confidence gates, executes the chosen action, and records latency/cost/trace. Built-in example: `s1 run --env order:ship_fastest_gift`.

## Get started

```sh
git clone https://github.com/HarnessRouter/SystemOneHarness.git
cd SystemOneHarness
git checkout ab8e8f08b4a6268c0633a474423d556599ee06a4
pip install -e '.[mcp]'
pytest
# live (bills provider):
# export OPENROUTER_API_KEY=…   # or TYPESAFE_API_KEY=…
# s1 run --env order:ship_fastest_gift
```

## Examples and demos

- Upstream README documents order-fulfilment quickstart, realtime browser gameplay demo, and UHP serving.
- This listing: `pytest` with MCP extra → **44 passed**, 2 skipped. No live provider call.

## Limits and data handling

Live steps send environment state and typed questions to OpenRouter or TypeSafe. The harness does not invent free-form actions—only environment-declared ones. Optional browser/MCP paths need those extras. Cost/latency figures in upstream demos were not re-measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit ab8e8f0](https://github.com/HarnessRouter/SystemOneHarness/tree/ab8e8f08b4a6268c0633a474423d556599ee06a4): **0.4.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `systemone_harness/provider.py`, and offline tests. No live TypeSafe/OpenRouter call.

Related: [jev-harness](jev-harness.md), [jev-layer](jev-layer.md), [super-jev](super-jev.md), [Jev Ultrafast](jev-ultrafast.md).
