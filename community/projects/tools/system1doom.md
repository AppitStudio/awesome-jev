# s1doom (System1Doom)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Harness where text-only System One models (TypeSafe Jev or open-weight Laya) play DOOM through ViZDoom: code computes geometry, the model makes the judgment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PanikParty/System1Doom) |
| Maintainer | [PanikParty](https://github.com/PanikParty). Independently curated. |
| Format | Python harness (uv) |
| Requirements | Python (uv), ViZDoom; TypeSafe key for the Jev backend. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1doom/backends/jev.py`](https://github.com/PanikParty/System1Doom/blob/7fa2243d92f1609ecfeab4c32fad870329e2e621/src/s1doom/backends/jev.py) at the pinned commit. |

## When to use

- Compare Jev and Laya as typed-decision game controllers.
- Mismatch: no LICENSE file; results in `runs/report.md` are the author's.

## How it works

A deterministic controller turns engine state into typed questions; the backend answers; code executes actions. Integration evidence: [`src/s1doom/backends/jev.py`](https://github.com/PanikParty/System1Doom/blob/7fa2243d92f1609ecfeab4c32fad870329e2e621/src/s1doom/backends/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run pytest -q
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plan: `PLAN.md`.
- Backend config: `configs/backends/jev.yaml`.

## Limits and data handling

Game state text goes to TypeSafe for the Jev backend.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 7fa2243d92f1](https://github.com/PanikParty/System1Doom/tree/7fa2243d92f1609ecfeab4c32fad870329e2e621). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
