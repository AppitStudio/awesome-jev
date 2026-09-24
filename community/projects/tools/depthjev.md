# DepthJev

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Embodied navigation agent that turns RGB into metric depth and text facts so TypeSafe Jev can choose navigation actions in EmbodiedBench EB-Navigation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZJUCQR/DepthJev) |
| Maintainer | [ZJUCQR](https://github.com/ZJUCQR). Independently curated. |
| Format | Python research agent + eval scripts. |
| Requirements | Python 3.11 (server) / 3.9.21 (eval); EmbodiedBench; Depth-Anything-3; HF checkpoints; `TYPESAFE_API_KEY`; headless X/GL libs for AI2-THOR. |
| License | [Apache-2.0](https://github.com/ZJUCQR/DepthJev/blob/93cb6e0e98838630c32c5ec44c0ac0184a3d151a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream README reports EB-Navigation success/latency; those metrics were not re-measured here. Live eval not run. |

## When to use

Use to **study Jev as the action chooser** for embodied navigation when perception is reduced to text facts from depth/detection. Prefer general browser agents for web UI automation.

## How it works

Perceive → describe (depth + detections as free-space / distance / constraint facts) → Jev selects among eight navigation actions; loop continues on the next observation (per README).

## Get started

```sh
git clone https://github.com/ZJUCQR/DepthJev.git
cd DepthJev
git checkout 93cb6e0e98838630c32c5ec44c0ac0184a3d151a
# Follow README: clone EmbodiedBench + Depth-Anything-3, create envs, download HF weights
cp .env.example .env   # TYPESAFE_API_KEY
bash scripts/run.sh    # smoke test
```

## Examples and demos

- README architecture diagram and `scripts/run.sh` smoke/full modes.

## Limits and data handling

RGB and derived facts are processed locally; Jev calls send text facts to TypeSafe. Benchmark numbers on the README badge are upstream-reported, not catalog-verified.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 93cb6e0](https://github.com/ZJUCQR/DepthJev/tree/93cb6e0e98838630c32c5ec44c0ac0184a3d151a). AI-assisted README and LICENSE inspection; EmbodiedBench episodes not executed.
