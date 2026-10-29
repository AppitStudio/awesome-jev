# Jev Lab by Nijal AI (45-minute French workshop app that pits Jev against an LLM on speed, cost and calibration)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Web workshop for a room of participants on phones or laptops, no account or code: try Jev and an LLM on support, scam and moderation scenarios, play a scam-filter mission where you set allow/review/block limits on 22 fictional messages, then a duel on errors, latency, cost per 1,000 decisions and calibration. Facilitator tab with a leaderboard and a cache-only fallback. French UI; works in simulated mode without keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nijal-AI/jev-lab) |
| Maintainer | [Nijal-AI](https://github.com/Nijal-AI). Independently curated. |
| Format | Python web app (FastAPI, single HTML/JS page) |
| Requirements | Python 3.11+ with uv; a TypeSafe key and an LLM key for live answers (simulated mode needs none). |
| License | [MIT](https://github.com/Nijal-AI/jev-lab/blob/540b1e596985234cea1b5aed36f63fbb1f1f9c9e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lab/providers.py`](https://github.com/Nijal-AI/jev-lab/blob/540b1e596985234cea1b5aed36f63fbb1f1f9c9e/lab/providers.py) at the pinned commit. |

## When to use

- Run a hands-on session that teaches thresholds and question design for decision models.
- Mismatch: French only; a teaching tool, not a benchmark.

## How it works

`lab/providers.py` posts each scenario to `JEV_BASE_URL/systemone` (`https://api.typesafe.ai/v1`, `jev-latest` by default, set in `lab/config.py`) and compares the answer with an LLM's. Integration evidence: [`lab/providers.py`](https://github.com/Nijal-AI/jev-lab/blob/540b1e596985234cea1b5aed36f63fbb1f1f9c9e/lab/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Nijal-AI/jev-lab && cd jev-lab
uv sync
cp .env.example .env   # optional: without keys everything runs simulated
uv run --env-file .env python run.py   # http://localhost:8080/?code=atelier
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (French): [github.com/Nijal-AI/jev-lab#readme](https://github.com/Nijal-AI/jev-lab#readme)

## Limits and data handling

Scenario texts are fictional; in live mode they go to TypeSafe and the LLM provider.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 540b1e596985](https://github.com/Nijal-AI/jev-lab/tree/540b1e596985234cea1b5aed36f63fbb1f1f9c9e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
