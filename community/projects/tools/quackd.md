# quackd

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Multi-robot CLI: LLM pilots pick one allowed skill per turn from adapter manifests; optional `--jev` puts TypeSafe Jev in front as a discrete stepper for closed-set verb choices (off by default).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rokbenko/quackd) |
| Maintainer | [Rok Benko / rokbenko](https://github.com/rokbenko). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **quackd 0.10.0** (`pip`/`uv`; extras such as `[jev]`, `[lerobot]`, `[mujoco]`). |
| Requirements | Python ≥ 3.11; an LLM provider for piloting. Optional Jev stepper needs `quackd[jev]` and `TYPESAFE_API_KEY` (default model `jev-1.13.0`). |
| License | [Apache-2.0](https://github.com/rokbenko/quackd/blob/6073829048b4c8152b7260d3c1d2af62709bfd02/LICENSE). |

## When to use

Use it to drive registered robots (or simulators) from goals/`*.duck` files with a hard skill allowlist, budgets, and confirm gates. Prefer [jev-libero](jev-libero.md) for LIBERO tabletop study loops without quackd’s multi-body CLI. Enable `--jev` only when you want Jev to score closed-set calls; free-form joint angles and prose stay with the LLM pilot.

## How it works

[`quackd/agent/jev.py`](https://github.com/rokbenko/quackd/blob/6073829048b4c8152b7260d3c1d2af62709bfd02/quackd/agent/jev.py) loads `typesafe_sdk` lazily when `--jev` is on, posts Choice questions for verbs whose parameters are a closed set, and escalates below confidence floors (`brake`/`read`/`motion`/`confirm`). [`docs/jev.md`](https://github.com/rokbenko/quackd/blob/6073829048b4c8152b7260d3c1d2af62709bfd02/docs/jev.md) documents install, shadow mode, and env vars (`TYPESAFE_API_KEY`, `TYPESAFE_DEFAULT_MODEL`, `TYPESAFE_BASE_URL`). The stepper never authors joint angles or sentences.

## Get started

```sh
uv pip install "quackd[jev]"
# cartoon sim without hardware:
# see README “No robot yet? Try it in 60 seconds”
export TYPESAFE_API_KEY=…   # only if enabling --jev
quackd --help
# or inspect:
git clone https://github.com/rokbenko/quackd.git
cd quackd
git checkout 6073829048b4c8152b7260d3c1d2af62709bfd02
```

Live robot or live Jev runs send observations/goals to providers and (when enabled) TypeSafe. This listing did not move hardware or call TypeSafe.

## Examples and demos

- README SO-101 arm hero run (LLM pilot) and simulator quickstarts.
- [`docs/jev.md`](https://github.com/rokbenko/quackd/blob/6073829048b4c8152b7260d3c1d2af62709bfd02/docs/jev.md) for `--jev` / shadow measuring.
- Offline tests: `tests/test_jev.py`, `tests/fake_typesafe.py` (live: `tests/test_live_jev.py`).

## Limits and data handling

Camera frames, goals, and tool traces may leave the machine for the LLM and TypeSafe when Jev is on. Upstream hardware status is uneven (one real arm path; other bodies mocked/simulated)—read “Which robots work”. Speed/cost comparisons in `docs/jev.md` were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 60738290](https://github.com/rokbenko/quackd/tree/6073829048b4c8152b7260d3c1d2af62709bfd02): **0.10.0**, Apache-2.0. AI-assisted source review of README, `docs/jev.md`, `quackd/agent/jev.py`, `pyproject.toml`, and license. Offline pytest / live TypeSafe / hardware were not run on the review host.

Related: [jev-libero](jev-libero.md), [jev-drone](jev-drone.md).
