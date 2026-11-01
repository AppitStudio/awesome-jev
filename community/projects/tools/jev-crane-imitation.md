# Jev-guided CRANE+ imitation learning (Gazebo pick-and-place data generation where Jev selects the phase, then ACT training)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Course project that generates image-conditioned pick-and-place demos in Gazebo: Jev selects the high-level phase, MoveIt 2 plans the trajectory and ROS 2 controllers execute it; recordings become a LeRobot dataset for ACT training. The README reports limits honestly, including incomplete full-task results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment) |
| Maintainer | [uhiron55](https://github.com/uhiron55). Independently curated. |
| Format | ROS 2 + Python packages |
| Requirements | ROS 2, Gazebo, MoveIt 2; a TypeSafe key for live phase selection. |
| License | [Apache-2.0](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment/blob/249d88d67537338166d85a2049159ae2dbafc6f8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_crane_data_generator/jev_crane_data_generator/phase_selector.py`](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment/blob/249d88d67537338166d85a2049159ae2dbafc6f8/src/jev_crane_data_generator/jev_crane_data_generator/phase_selector.py) at the pinned commit. |

## When to use

- See Jev as a phase selector for robot data generation.
- Mismatch: coursework; the trained policy did not complete the full task.

## How it works

`phase_selector.py` sends camera-grounded state to `https://api.typesafe.ai/v1/systemone` and maps the answer to a pick-and-place phase; `generate_episode.py` records Jev decisions with the trajectories. Integration evidence: [`src/jev_crane_data_generator/jev_crane_data_generator/phase_selector.py`](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment/blob/249d88d67537338166d85a2049159ae2dbafc6f8/src/jev_crane_data_generator/jev_crane_data_generator/phase_selector.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see the README for the ROS 2 workspace build and episode generation scripts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment#readme](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment#readme)

## Limits and data handling

Images and state are sent to TypeSafe in live mode. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 249d88d67537](https://github.com/uhiron55/physical-ai-2026-advanced-1-final-assignment/tree/249d88d67537338166d85a2049159ae2dbafc6f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
