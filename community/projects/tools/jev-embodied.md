# jev-embodied by ZephyrZ (robotics experiments on what role Jev can play next to VLMs and VLA policies)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Embodied-AI comparison project (Chinese docs) asking where Jev fits in a robot stack: choosing structured skills against GPT-6 Astra in MuJoCo, Meta-World and LIBERO, picking among continuous action chunks proposed by a VLM, and deciding when a VLA policy such as π0.5 should replan in RoboTwin 2. Reports closed-loop success from the simulators' own task checks (for example 377/500 with Jev + VLA replanning against 355/500 for the plain policy) and says plainly that a same-checkpoint direct-replan control did not show an independent Jev advantage.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zyh3699/jev-embodied) |
| Maintainer | [ZephyrZ](https://github.com/zyh3699) (zyh3699). Independently curated. |
| Format | Python experiments + local web console |
| Requirements | Python, the simulators per experiment (MuJoCo, LIBERO, RoboTwin 2), GPUs for the VLA runs, and a TypeSafe API key for hosted Jev. |
| License | [MIT](https://github.com/zyh3699/jev-embodied/blob/04532677745a84e4f413b80f6cfdad3889b9ba7a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/embodied_jev/policies.py`](https://github.com/zyh3699/jev-embodied/blob/04532677745a84e4f413b80f6cfdad3889b9ba7a/src/embodied_jev/policies.py) at the pinned commit. |

## When to use

- Robotics researchers deciding whether a decision model belongs in a planning or replanning loop.
- Mismatch: a ready robot controller; this is a set of experiments.

## How it works

`src/embodied_jev/policies.py` sends the decision state to `https://api.typesafe.ai/v1/systemone` (model from `TYPESAFE_MODEL`, default `jev-latest`); a local `/v1/systemone` endpoint can be configured instead for the fine-tuned decider experiments. Integration evidence: [`src/embodied_jev/policies.py`](https://github.com/zyh3699/jev-embodied/blob/04532677745a84e4f413b80f6cfdad3889b9ba7a/src/embodied_jev/policies.py).

## Get started

Copy the env example, add a TypeSafe key and follow the experiment guide.

```sh
git clone https://github.com/zyh3699/jev-embodied && cd jev-embodied
cp .env.example .env   # TYPESAFE_API_KEY=..., TYPESAFE_MODEL=jev-latest
# see docs/EXPERIMENTS.md for each experiment's commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Experiment guide: [github.com/zyh3699/jev-embodied/blob/main/docs/EXPERIMENTS.md](https://github.com/zyh3699/jev-embodied/blob/main/docs/EXPERIMENTS.md)
- RoboTwin full 50-task run: [github.com/zyh3699/jev-embodied/blob/main/docs/ROBOTWIN2_FULL50_DLC.md](https://github.com/zyh3699/jev-embodied/blob/main/docs/ROBOTWIN2_FULL50_DLC.md)

## Limits and data handling

Simulation results only. Hosted Jev runs send task state to TypeSafe. Third-party simulators, models and datasets keep their own terms (see THIRD_PARTY_NOTICES.md).

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 04532677745a](https://github.com/zyh3699/jev-embodied/tree/04532677745a84e4f413b80f6cfdad3889b9ba7a). Inspected the README, LICENSE and `policies.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
