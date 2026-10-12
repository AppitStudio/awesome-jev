# Jev Arena

[All projects](../README.md) · [Web apps](README.md#web-apps)

Open-source web arena that runs live head-to-head challenges of TypeSafe Jev against Claude Opus 5.5 (trading, Tetris, lead race, review triage) through OpenRouter, showing real per-decision costs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlanECE/jev-arena) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/AlanECE/jev-arena#readme) |
| Pricing and access | Free Apache/MIT-licensed source build via Docker. Requires your OpenRouter API key; model usage is billed by OpenRouter. Simulation/paper trading only. Checked 2026-10-12. |
| Jev evidence | Decider wiring in [`arena/app/core/deciders.py`](https://github.com/AlanECE/jev-arena/blob/a9312248070750f83ac0463162c30bd8746cb4ee/arena/app/core/deciders.py); scenes under `arena/app/scenes/`. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. App not run on the review host. |
| Maintainer | [AlanECE](https://github.com/AlanECE). Independently curated. |
| Format | Python web app (Docker) |
| Platform and availability | Any host with Docker; browser UI. |
| Jev's role | Jev is one of two live decision players; Opus is the other. Both call OpenRouter for real. |
| Requirements | Docker; OpenRouter API key. |
| License | [MIT](https://github.com/AlanECE/jev-arena/blob/a9312248070750f83ac0463162c30bd8746cb4ee/LICENSE) |

## When to use

- Demo System One vs LLM decisions with visible latency/cost.
- Mismatch: Not a production trading system; paper/sim only.

## How it works

Each scene posts state to both models; UI streams decisions and ledger costs.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AlanECE/jev-arena.git
cd jev-arena
# docker compose per README with OPENROUTER_API_KEY
```

## Limits and data handling

Prompts go to OpenRouter (Jev + Opus); billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit a93122480707](https://github.com/AlanECE/jev-arena/tree/a9312248070750f83ac0463162c30bd8746cb4ee). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
