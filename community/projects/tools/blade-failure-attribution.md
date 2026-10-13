# BLADE

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper code for failure attribution in LLM multi-agent systems: every dependency and contract-audit judgment is a multiple-choice question answered by TypeSafe Jev with option probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GXG-CS/BLADE) |
| Maintainer | [GXG-CS](https://github.com/GXG-CS). Independently curated. |
| Format | Python research code |
| Requirements | Python; TypeSafe key; benchmark trajectories per README. |
| License | [MIT](https://github.com/GXG-CS/BLADE/blob/a3d95cf5d2cfd31651dc65a0a6298e05daa987d9/LICENSE) |
| Jev evidence | [`blade/jev/api.py`](https://github.com/GXG-CS/BLADE/blob/a3d95cf5d2cfd31651dc65a0a6298e05daa987d9/blade/jev/api.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reproduce or extend probability-based blame localization for agent trajectories.
- Mismatch: research artifact for the paper, not a product.

## How it works

Five operators reconstruct dependencies, audit how receiving decisions use sources, and combine the evidence; each judgment uses Jev (`jev-1.13.0`) option probabilities. (Summarized from the upstream [README](https://github.com/GXG-CS/BLADE/blob/a3d95cf5d2cfd31651dc65a0a6298e05daa987d9/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install requirements and run the experiment scripts per the README.

## Limits and data handling

Trajectory text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit a3d95cf5d2cf](https://github.com/GXG-CS/BLADE/tree/a3d95cf5d2cfd31651dc65a0a6298e05daa987d9). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
