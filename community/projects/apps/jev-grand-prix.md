# Jev Grand Prix

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local F1 racing game where TypeSafe Jev picks the racing line and pedals several times a second; code steers and brake-by-wires the car, remembers corner history, and plans the next lap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enoyola/jev-grand-prix) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/enoyola/jev-grand-prix#readme) — local browser race; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Requires your TypeSafe API key. TypeSafe inference is billed separately. |
| Jev evidence | Inspected [`server.py`](https://github.com/enoyola/jev-grand-prix/blob/351ebb50f9d94d255ad50e37433da62f0ba6cdf9/server.py): `typesafe_sdk` `Choice` (line, pedals) + `Noul` (trouble) in one `system_one` request; lap planner builds per-corner Choices. Live TypeSafe not run. |
| Disclosure | Free source access does not include TypeSafe usage. AI-assisted, independently curated listing; no commercial relationship declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [enoyola](https://github.com/enoyola). |
| Format | Python **`jev-grand-prix` 0.1.0** (`uv run server.py`) serving static `web/` at localhost:8765. |
| Platform and availability | Source build; open [http://localhost:8765](http://localhost:8765). Optional film mode query params for clip recording. |
| Jev's role | Chooses lateral line, pedal, and off-track risk; application code owns physics, steering/brake execution, corner timing memory, and next-lap plans. |
| Requirements | [uv](https://docs.astral.sh/uv/), Python ≥ 3.12 (installed by uv), `TYPESAFE_API_KEY` in `.env`. |
| License | [MIT](https://github.com/enoyola/jev-grand-prix/blob/351ebb50f9d94d255ad50e37433da62f0ba6cdf9/LICENSE). |

## When to use

Use it when you want a visual demo of **Jev deciding goals, code executing control** under latency (same pattern as the Pokémon/Minecraft bots). Prefer [JevPilot](../tools/jevpilot.md) or [TypeSafe Mario](../tools/typesafe-mario.md) for other sim demos; prefer agent routers when you need library integration.

## How it works

Several times a second the browser posts telemetry; [`server.py`](https://github.com/enoyola/jev-grand-prix/blob/351ebb50f9d94d255ad50e37433da62f0ba6cdf9/server.py) turns numbers into race-engineer wording and asks three typed questions in one request. Code steers toward the chosen line at 120 Hz and stops braking once target corner speed is reached—direct wheel steering from Jev weaved under ~0.27 s latency. Between laps, code compares corner times/off-tracks and asks Jev for the next-lap plan.

## Get started

```sh
git clone https://github.com/enoyola/jev-grand-prix.git
cd jev-grand-prix
git checkout 351ebb50f9d94d255ad50e37433da62f0ba6cdf9
echo "TYPESAFE_API_KEY=your_key_here" > .env
uv run server.py
# Open http://localhost:8765 — Start race; optional Race Jev yourself
```

Live racing sends telemetry-derived state to TypeSafe and incurs charges. This listing did not start a live race.

## Examples and demos

- Local browser UI under `web/` (physics, HUD, race-engineer panel).
- Film mode: `http://localhost:8765/?film=1&laps=3&auto=1`.
- README documents an author-run 8-lap live Jev series; treat times as author-reported, not re-measured here.

## Limits and data handling

Telemetry-derived race state leaves the host on live decide/plan calls. There is no automated test suite in-repo. Quality of racing lines is not measured in this listing. No live TypeSafe calls were made on the review host.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 351ebb5](https://github.com/enoyola/jev-grand-prix/tree/351ebb50f9d94d255ad50e37433da62f0ba6cdf9): `jev-grand-prix` **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `server.py`, `web/`. Offline: `server.py` Python AST parse OK. No live TypeSafe calls.

Related: [JevPilot](../tools/jevpilot.md), [TypeSafe Mario](../tools/typesafe-mario.md), [Jev Lab](../tools/jev-lab.md).
