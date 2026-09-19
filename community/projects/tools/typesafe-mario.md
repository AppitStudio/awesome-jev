# TypeSafe Mario

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Study a Jev controller that selects existing NES input combinations from structured Super Mario Bros. telemetry.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fhshaik/typesafe-mario) |
| Maintainer | [fhshaik](https://github.com/fhshaik). |
| Format | Experimental Python controller, emulator harness and telemetry dashboard. |
| Jev's role | Choice selects a controller macro; Noul estimates jump usefulness and Score describes immediate danger for display. |
| Requirements | Python 3.13+, `typesafe-sdk`; emulator/dashboard extras for gameplay and `TYPESAFE_API_KEY` for live Jev control. |
| Access and costs | Source checkout; TypeSafe usage can incur charges. Game/emulator assets and their access rights are separate. |
| License | No project license file or license declaration was found at the reviewed commit; reuse terms are unspecified. |

## When to use

Use this as a reference for turning emulator RAM and telemetry into typed decision
inputs, visualizing Choice probabilities and comparing asynchronous versus
stepwise control. The built-in state demo is a smaller entry point than running
the game. This is experimental simulation code, not a validated game-playing
benchmark or a general vision agent.

## How it works

The [parser](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/src/typesafe_mario/state.py)
builds object-centric state describing motion, terrain, enemies, trajectory,
recent actions and response delay. Arithmetic and geometry stay in code. Jev sees
structured state rather than screenshots; the fuller grid remains in debug data.

The [policy](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/src/typesafe_mario/policy.py)
uses Python `TypeSafeClient.system_one` with Choice, Noul and Score questions in
one call. Choice maps to seven existing controller macros; the other answers are
telemetry, not separate action permissions. The SDK dependency is unpinned and
no explicit model is supplied, so the installed SDK/provider default determines
which Jev version runs.

The [runner](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/src/typesafe_mario/runner.py)
advances a configured number of frames per decision in headless/game modes. The
live dashboard instead continues stepping while one background request is pending,
using the previous action or an initial no-op. These modes have different timing
semantics and should not be treated as interchangeable measurements.

## Get started

The following cross-platform source path was inspected, not executed. Installing
packages downloads dependencies; the state demo itself makes no provider calls
and does not start the emulator.

```sh
git clone https://github.com/fhshaik/typesafe-mario.git
cd typesafe-mario
python3.13 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/typesafe-mario state-demo
```

On Windows, use the upstream [PowerShell instructions](https://github.com/fhshaik/typesafe-mario#setup).
The demo prints JSON plus a text view from fabricated RAM and telemetry. It needs
no API key or game files.

For gameplay, install the `mario` extra and provide a lawful local game/emulator
setup as required upstream. Configure `TYPESAFE_API_KEY` privately. The following
explicit live run can make up to five policy invocations; SDK retries, if enabled
by the installed version, are additional requests and costs:

```sh
.venv/bin/python -m pip install -e '.[mario]'
.venv/bin/typesafe-mario play --display none --max-decisions 5
```

The default environment is `SuperMarioBros-1-1-v0`. Inspect the JSONL record under
`artifacts/` for state, selected action, probabilities and outcome. The optional
`--policy heuristic` avoids Jev calls but still requires the emulator/game setup.

## Examples and demos

- [State-demo implementation](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/src/typesafe_mario/cli.py) supplies the synthetic first-run input.
- [State tests](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/tests/test_state.py) cover deterministic telemetry interpretation; dashboard tests cover formatting/display helpers.
- The [README](https://github.com/fhshaik/typesafe-mario#setup) describes interactive play and recording. No separate hosted demo was verified.

## Limits and data handling

Live calls send parsed game state to TypeSafe and can repeat throughout an episode.
The default budget is 2,000 decisions; choose a smaller explicit budget for initial
inspection. Logs retain canonical/debug state and extracted decision fields, but
not the complete raw provider response or resolved model identifier.

There is no confidence-based abstention gate. Missing answer IDs, invalid action
names or provider failures raise errors; the runner has cleanup logic but no
automatic model-failure fallback. Model instructions describe an eight-frame
minimum even though the CLI allows other frame counts. The SDK is unpinned and
emulator compatibility was not tested. No level-completion or performance result
was reproduced.

## Review and maintenance

Source-reviewed **2026-09-19** at
[`ca22449ed187118d19326d1f54b01b6636578aa4`](https://github.com/fhshaik/typesafe-mario/commit/ca22449ed187118d19326d1f54b01b6636578aa4).
Inspected README/setup, package metadata/license inventory, policy, CLI, runner and
representative state-test fixtures. No dependency installation, tests, game assets,
emulator launch or provider requests were performed. See [validation scope](../../../docs/validation.md#community-project-checks).

AI-assisted catalog review; contributor affiliation/commercial relationships
were not supplied. Listing is not an endorsement.
