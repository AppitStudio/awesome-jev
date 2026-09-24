# jev-robotics-eval

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Evaluation harness for robot control with a JEV-compatible decision service on MetaWorld and RoboTwin tasks (text and vision modes, privilege levels, primitive action spaces).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lose4578/jev-robotics-eval) |
| Maintainer | [lose4578](https://github.com/lose4578). Independently curated. |
| Format | Python package (`jev-robo-eval` / `jev_robo_eval`). |
| Requirements | Python 3.10+; MetaWorld/MuJoCo and/or RoboTwin assets; a decision service exposing `/v1/decision` (and vision endpoint when used); optional `JEV_API_KEY`. |
| License | [MIT](https://github.com/lose4578/jev-robotics-eval/blob/b3924eba71e09f061099247a3feb0c89e0ce3681/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Simulator episodes and task-success claims not executed on the review host. |

## When to use

Use to **benchmark a JEV-shaped controller** on registered MetaWorld/RoboTwin task subsets with explicit observation privilege levels. Prefer EmbodiedBench agents such as [DepthJev](depthjev.md) for navigation-focused suites.

## How it works

The CLI builds observations, asks the configured JEV client for typed decisions, and maps them through primitive-action adapters. L0–L3 privilege levels and optional L3 oracle guides are documented; full `--benchmark` covers only registered tasks (per README).

## Get started

```sh
git clone https://github.com/lose4578/jev-robotics-eval.git
cd jev-robotics-eval
git checkout b3924eba71e09f061099247a3feb0c89e0ce3681
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[metaworld]'
export JEV_MODEL=jev
MUJOCO_GL=egl jev-robo-eval \
  --task reach-v3 --mode text --privilege-level 2 \
  --jev-url http://127.0.0.1:8186/v1/decision \
  --seed 2 --max-decisions 120
```

## Examples and demos

- README MetaWorld text/vision command examples.
- Expanded task registration notes (registration ≠ proven task success).

## Limits and data handling

Model weights and RoboTwin assets are external. Observations may include images sent to a vision-decision endpoint. Dual-arm/rotation scopes are limited as documented upstream.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit b3924eb](https://github.com/lose4578/jev-robotics-eval/tree/b3924eba71e09f061099247a3feb0c89e0ce3681). AI-assisted README and LICENSE inspection; MuJoCo/RoboTwin runs not executed.

Related: [DepthJev](depthjev.md), [CUA-JEV (ZJU-REAL)](cua-jev-zju.md).
