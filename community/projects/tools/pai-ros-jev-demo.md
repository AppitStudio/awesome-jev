# PAI ROS Jev demo (ROS 2 / Gazebo demo where Jev picks the next job for a parts-supply AMR)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Japanese ROS 2 Humble and Gazebo Classic 11 demo: one autonomous mobile robot feeds a four-machine line, collects rejects and ships products, and Jev chooses its next job from candidate facts while code owns shipping timing and a LiDAR safety stop. A recorded Jev run (20 units in 1800 s) can be replayed without a key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fujihoge/PAI-ros-jev_demo) |
| Maintainer | [fujihoge](https://github.com/fujihoge). Independently curated. |
| Format | Python + ROS 2 packages |
| Requirements | ROS 2 Humble, Gazebo Classic 11; a TypeSafe key for live Jev decisions. |
| License | [MIT](https://github.com/fujihoge/PAI-ros-jev_demo/blob/64e63170f563bf9e4641796afb5a12798e2c6926/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`adapters/jev.py`](https://github.com/fujihoge/PAI-ros-jev_demo/blob/64e63170f563bf9e4641796afb5a12798e2c6926/adapters/jev.py) at the pinned commit. |

## When to use

- See Jev as a dispatch chooser in a robot simulation.
- Mismatch: a course demo without comparison baselines.

## How it works

`policies/jev_b1.py` asks one question with per-candidate facts through `adapters/jev.py` (TypeSafe System One); the ROS `decision_node` answers `/factory/state` requests via replay or live Jev. Integration evidence: [`adapters/jev.py`](https://github.com/fujihoge/PAI-ros-jev_demo/blob/64e63170f563bf9e4641796afb5a12798e2c6926/adapters/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
# build ros_ws with colcon, then launch with policy:=replay (default) or policy:=jev_b1x
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README (Japanese): [github.com/fujihoge/PAI-ros-jev_demo#readme](https://github.com/fujihoge/PAI-ros-jev_demo#readme)

## Limits and data handling

Live mode sends line state to TypeSafe. Results are a single run, not a benchmark. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 64e63170f563](https://github.com/fujihoge/PAI-ros-jev_demo/tree/64e63170f563bf9e4641796afb5a12798e2c6926). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
