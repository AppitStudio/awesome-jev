# robo-jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Robotics / embodied decision bench configs that include TypeSafe Jev (`~typesafe/jev-latest` and related ids) among decision-model baselines for evaluating fast typed policies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/STEERIX-home/robo-jev) |
| Maintainer | [STEERIX-home](https://github.com/STEERIX-home). Independently curated. |
| Format | Bench configs + eval harness (see repo) |
| Requirements | Follow README hardware/sim deps; TypeSafe key when running Jev arms. |
| License | [Apache-2.0](https://github.com/STEERIX-home/robo-jev/blob/1a596b8f10c3fd903c966ef08474d2b28033421f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`configs/bench/bench-v0.yaml`](https://github.com/STEERIX-home/robo-jev/blob/1a596b8f10c3fd903c966ef08474d2b28033421f/configs/bench/bench-v0.yaml) at the pinned commit. |

## When to use

- Compare Jev against other decision models in a robotics-oriented bench.
- Need declared model ids in YAML bench configs.
- Mismatch: research bench; not a product robot stack.

## How it works

Bench YAML lists decision-model arms including `~typesafe/jev-latest`. The harness loads those ids when running comparative evaluations (see the project site, robo-jev.dev). Integration evidence: [`configs/bench/bench-v0.yaml`](https://github.com/STEERIX-home/robo-jev/blob/1a596b8f10c3fd903c966ef08474d2b28033421f/configs/bench/bench-v0.yaml).

## Get started

Clone and follow the README and the project site for environment and bench commands.

```sh
git clone https://github.com/STEERIX-home/robo-jev && cd robo-jev
# see README for bench commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [robo-jev.dev/](https://robo-jev.dev/)
- configs/bench/bench-v0.yaml

## Limits and data handling

Embodied deps can be heavy. Alias models may move; pin when you need reproducibility.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1a596b8f10c3](https://github.com/STEERIX-home/robo-jev/tree/1a596b8f10c3fd903c966ef08474d2b28033421f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
