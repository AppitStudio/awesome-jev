# jev-tabletop (simulated robot arm that tidies objects into a tray with every perception and task decision from Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Course project where a simulated Franka Panda in MuJoCo tidies objects into a tray from an English or Japanese instruction. Jev answers typed questions about camera images (which box, is anything left, is the gripper holding it) and hand-written motion primitives do the moving; nothing is trained.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yamatakeru/jev-tabletop) |
| Maintainer | [yamatakeru](https://github.com/yamatakeru). Independently curated. |
| Format | Python simulation (MuJoCo + dora-rs) |
| Requirements | uv (installs Python 3.13), ffmpeg for videos; `TYPESAFE_API_KEY` with image input. |
| License | [MIT](https://github.com/yamatakeru/jev-tabletop/blob/b6544fbd95192f4881b11ce2afbda3170e6395c9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tabletop/jev.py`](https://github.com/yamatakeru/jev-tabletop/blob/b6544fbd95192f4881b11ce2afbda3170e6395c9/tabletop/jev.py) at the pinned commit. |

## When to use

- See how far Jev's image questions go for closed-loop pick-and-place.
- Mismatch: simulation course project; not a real-robot controller.

## How it works

`tabletop/jev.py` wraps `typesafe_sdk`'s `TypeSafeClient` with image input; overview, verify, refine and grasp-check queries each send a camera image with box and noul questions in one request, and low-confidence boxes are re-asked on a wider crop. Integration evidence: [`tabletop/jev.py`](https://github.com/yamatakeru/jev-tabletop/blob/b6544fbd95192f4881b11ce2afbda3170e6395c9/tabletop/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/yamatakeru/jev-tabletop.git
cd jev-tabletop
uv sync
RUN_DIR=outputs/demo uv run dora run dataflow.yml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Logged demo runs: [github.com/yamatakeru/jev-tabletop/tree/main/results/demos](https://github.com/yamatakeru/jev-tabletop/tree/main/results/demos)

## Limits and data handling

Rendered camera images and the instruction are sent to TypeSafe on each query. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit b6544fbd9519](https://github.com/yamatakeru/jev-tabletop/tree/b6544fbd95192f4881b11ce2afbda3170e6395c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
