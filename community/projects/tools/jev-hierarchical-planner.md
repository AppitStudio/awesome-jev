# Jev Hierarchical Planner (simulated delivery drone where Jev picks what to do next, a 3D A* planner picks the route and a MuJoCo controller flies it)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Research demo of a judgment layer for autonomy: in a MuJoCo city simulation, Jev answers typed questions about competing goals stated in words (medical deadlines, battery reserve, hazards) to choose the next job, while classical planning and control handle geometry and flight. Includes Monte-Carlo evaluation over 120 rollouts per campaign against a rule-based dispatcher, cost comparisons with LLMs, an annotated demo video and 195 tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haggler3/jev-hierarchical-planner) |
| Maintainer | [haggler3](https://github.com/haggler3). Independently curated. |
| Format | Python simulation, evaluation scripts and results (Apache-2.0) |
| Requirements | Python 3.9+ and an OpenRouter key for live Jev (`--policy rules` runs offline). |
| License | [Apache-2.0](https://github.com/haggler3/jev-hierarchical-planner/blob/05705ebcca29a89f431ce7696aee7410ea3ab6f9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevplanner/jev_client.py`](https://github.com/haggler3/jev-hierarchical-planner/blob/05705ebcca29a89f431ce7696aee7410ea3ab6f9/jevplanner/jev_client.py) at the pinned commit. |

## When to use

- Study how a typed-decision model can sit above classical planners in a robotics stack.
- Mismatch: real flight; it is simulation only.

## How it works

`jevplanner/jev_client.py` posts to OpenRouter's Decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with default model `typesafe/jev-1.13`; the maintainer reports about $0.0016 per mission. Integration evidence: [`jevplanner/jev_client.py`](https://github.com/haggler3/jev-hierarchical-planner/blob/05705ebcca29a89f431ce7696aee7410ea3ab6f9/jevplanner/jev_client.py).

## Get started

Install, add your OpenRouter key, run the demo.

```sh
git clone https://github.com/haggler3/jev-hierarchical-planner && cd jev-hierarchical-planner
python -m venv .venv && .venv/bin/pip install -r requirements.txt
echo OPENROUTER_API_KEY=sk-or-... > .env
python run_demo.py                  # live Jev
python run_demo.py --policy rules   # offline baseline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results and video: [github.com/haggler3/jev-hierarchical-planner/blob/05705ebcca29a89f431ce7696aee7410ea3ab6f9/README.md](https://github.com/haggler3/jev-hierarchical-planner/blob/05705ebcca29a89f431ce7696aee7410ea3ab6f9/README.md)

## Limits and data handling

Mission state descriptions go to OpenRouter on your key. Results come from the maintainer's simulated campaigns.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 05705ebcca29](https://github.com/haggler3/jev-hierarchical-planner/tree/05705ebcca29a89f431ce7696aee7410ea3ab6f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
