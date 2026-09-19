# jev-drone

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Study typed Jev judgments inside a MuJoCo quadrotor simulation, with perception and fast flight control implemented separately in Python.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RomanSlack/jev-drone) |
| Maintainer | [RomanSlack](https://github.com/RomanSlack). |
| Format | Experimental Python/MuJoCo simulation, telemetry video and replay scripts. |
| Jev's role | Main course: advisory maneuver Choice, risk Score and target-loss Noul. Separate tunnel experiment maps Score answers into navigation commands. |
| Requirements | Python, Bash, Git, an OpenGL-capable MuJoCo environment, NumPy and `typesafe-sdk>=1.0`; setup fetches the Skydio X2 model from MuJoCo Menagerie. |
| Access and costs | Local simulation; `TYPESAFE_API_KEY` or `JEV_API_KEY` for live Jev. Provider usage can incur charges. A no-Jev mode runs without inference. |
| License | [MIT application code](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/LICENSE); the downloaded airframe and assets retain their separate upstream terms. |

## When to use

Use this reference to explore the boundary between slower semantic judgments and
fast deterministic control, including how observation content and result age affect
what a controller can use. It also supplies a model-disabled baseline and replay
path for inspecting an experiment without repeating inference.

This repository controls a simulated quadrotor. It does not supply verified
physical-drone integration or real-flight safety evidence. The separate tunnel
experiment is explicitly described upstream as incomplete.

## How it works

The [perception and controller module](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/flight.py)
uses MuJoCo depth/segmentation data to summarize obstacles and target visibility.
Jev receives symbolic JSON rather than images. Local code handles attitude,
thrust, geometry and controller timing.

The [main tactical layer](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/tactics.py)
uses Python `TypeSafeClient.system_one` with `jev-latest`. It offers six maneuver
choices, a three-level risk Score and a target-loss Noul. A background worker
caches the latest result; scene fingerprints and call cadence avoid some repeated
requests. The [guidance loop](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/run.py)
uses fresh results, interprets thresholds and can override maneuvers with a local
collision reflex. Confidence is recorded but does not gate adoption.

The [tunnel policy](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/tunnel_tactics.py)
is a different experiment: concurrent workers ask for graded steering, height and
risk. It lacks the main course's obstacle-avoidance reflex. Do not transfer claims
or fallback expectations between the two modes.

## Get started

These commands are an inspected upstream setup path, not an executed result.
The setup script creates a virtual environment, installs packages, downloads the
Skydio X2 model and links its assets. It does not run a Jev evaluation itself.

```sh
git clone https://github.com/RomanSlack/jev-drone.git
cd jev-drone
bash setup.sh
```

Choose a compatible rendering backend using the [run instructions](https://github.com/RomanSlack/jev-drone#run-it),
such as `MUJOCO_GL=glfw` on a desktop or an appropriately configured `egl` backend
on a headless machine. Start with the explicit **provider-free simulation**:

```sh
.venv/bin/python run.py --no-jev --fast --seconds 5 --seeds 0
```

It prints a JSON summary from the simulated episode. No API key is needed, but
MuJoCo, rendering support and downloaded model assets are still required.

For an explicit live experiment, configure a provider key privately, omit
`--no-jev` and use a short duration. The following sends symbolic scene state to
TypeSafe; `--budget` counts successful evaluations and is not a strict cap on
requests or charges:

```sh
.venv/bin/python run.py --seconds 5 --seeds 0 --budget 5
```

The default run uses Jev. Leave `--fast` off when measuring a network model in the
loop, since simulation time otherwise advances differently from wall-clock time.

## Examples and demos

- The [README course screenshots](https://github.com/RomanSlack/jev-drone) illustrate the simulated obstacle course; they are upstream material, not independently reproduced runs.
- `run.py --video course.mp4` is a live run unless paired with `--no-jev`; it writes video and a local `.tape.npy` record.
- [Replay tools](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/replay.py) are supplied for existing recordings. No dedicated automated test suite was found in the reviewed tracked files.

## Limits and data handling

TypeSafe receives mission, aircraft capabilities and symbolic observed scene.
Local video/tape output includes simulation state, extracted judgments and
telemetry. This path retains selected probabilities, scores and usage totals,
not full raw typed responses with resolved model versions.

Main-course provider errors replace the judgment with an error/default result;
ordinary guidance and the reflex continue. Judgments older than 1.5 simulation
seconds are ignored. These safeguards are experimental implementation behavior,
not a demonstrated safety guarantee or calibrated probability policy.

The budget counter increments only after successful evaluation. Failures and SDK
retries are not counted, and queued/in-flight work can exceed the nominal count;
tunnel concurrency adds further exposure. SDK version ranges and external assets
are not locked to a fully reproduced environment. Upstream reports small live
experiments and acknowledges variance; their speed, success and safety claims
were not independently evaluated here.

## Review and maintenance

Source-reviewed **2026-09-19** at
[`cbeb53ce4f17a06ea490ae43effcdad231143610`](https://github.com/RomanSlack/jev-drone/commit/cbeb53ce4f17a06ea490ae43effcdad231143610).
Inspected README/setup, requirements, MIT license, tactical questions/workers,
main guidance and CLI, tunnel worker/error handling and tracked test inventory.
No packages/models were downloaded, tests or simulations run, or provider calls
made. See [validation scope](../../../docs/validation.md#community-project-checks).

AI-assisted catalog review; contributor affiliation/commercial relationships
were not supplied. Listing is not an endorsement.
