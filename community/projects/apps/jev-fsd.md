# Jev FSD

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser driving simulator on real OpenStreetMap streets where TypeSafe Jev makes every maneuver choice, with a decision inspector and benchmark

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BrendanH18/jev_fsd) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/BrendanH18/jev_fsd#readme) |
| Pricing and access | Free source build. Without a TypeSafe key the Rules driver runs offline at no cost; Jev driving needs `TYPESAFE_API_KEY` (early access). Checked 2026-09-29. |
| Jev evidence | [Upstream README](https://github.com/BrendanH18/jev_fsd/blob/d3d3633dfeeb643ee040cb743f313c8ec00af421/README.md) describes Jev as the autopilot over typed multiple-choice maneuvers; decision panel exports `curl` for each ask. Distinct from [JevPilot](../tools/jevpilot.md). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Research/demo only — not a real self-driving system. Live browser/Jev not run on the review host. |
| Maintainer | [BrendanH18](https://github.com/BrendanH18). Independently curated. |
| Format | JavaScript · Three.js browser sim + small Python/`uv` server (MIT). |
| Platform and availability | Desktop browser with WebGL; `uv run server.py` → `http://127.0.0.1:8322`. |
| Jev's role | Jev selects driving maneuvers; code owns map, physics, traffic, and scoring. Switchable Rules driver for comparison. |
| Requirements | [uv](https://docs.astral.sh/uv/) (Python 3.10+); optional `TYPESAFE_API_KEY` in `.env`. |
| License | [MIT](https://github.com/BrendanH18/jev_fsd/blob/d3d3633dfeeb643ee040cb743f313c8ec00af421/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when studying fast typed driving decisions on real OSM geometry with inspectable asks. Prefer [JevPilot](../tools/jevpilot.md) for a lighter path-sampling demo.

## How it works

Click a minimap destination; the autopilot drives through traffic/signals. A panel shows each Jev question, answer, confidence, and cost. A benchmark suite scores drivers on safety, comfort, legality, and cost.

## Get started

```sh
git clone https://github.com/BrendanH18/jev_fsd.git
cd jev_fsd
git checkout d3d3633dfeeb643ee040cb743f313c8ec00af421
uv run server.py
# open http://127.0.0.1:8322 ; optional: cp .env.example .env and set TYPESAFE_API_KEY
```

## Examples and demos

README screenshots (day/night drives) and decision-panel JSON export. No live drive was run on the review host.

## Limits and data handling

Not for controlling real vehicles. Live TypeSafe paths not executed on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit d3d3633](https://github.com/BrendanH18/jev_fsd/tree/d3d3633dfeeb643ee040cb743f313c8ec00af421). AI-assisted README + LICENSE inspection; install/live paths not executed.
