# System One Agent (agent loop where Jev picks the next tool and the context a worker LLM sees, benchmarked against direct tool calling)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python research agent that lets Jev choose each next action and which files and observations a worker LLM receives, with a direct ChatGPT tool-calling baseline, offline tests and recorded benchmark runs (Bank and Workflow Scheduler).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MahmoudMoubarez/system-one-agent) |
| Maintainer | [MahmoudMoubarez](https://github.com/MahmoudMoubarez). Independently curated. |
| Format | Python research code |
| Requirements | Python 3.12+; offline tests need no keys. Live runs need a `TYPESAFE_API_KEY`, Git, Node.js 22.15+ and an eligible ChatGPT account via the Sign in with ChatGPT DevKit. |
| License | [MIT](https://github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/jev.py) at the pinned commit. |

## When to use

- Study whether a decision model can steer an agent loop and trim worker context, with reproducible baselines.
- Mismatch: a production coding agent; it is a small benchmark harness.

## How it works

`jev.py` asks Jev `choice` questions for the next tool and its arguments and `noul` questions for each candidate worker input, and the host validates the selections before running tools; `providers.py` posts to `https://api.typesafe.ai/v1/systemone`. Integration evidence: [`jev.py`](https://github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/jev.py).

## Get started

Run the offline tests, then a live comparison.

```sh
git clone https://github.com/MahmoudMoubarez/system-one-agent
cd system-one-agent
python -m unittest discover -s tests -v   # offline, no keys
cp .env.example .env   # add TYPESAFE_API_KEY for live runs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Recorded results: [github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/results/README.md](https://github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/results/README.md)
- README: [github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/README.md](https://github.com/MahmoudMoubarez/system-one-agent/blob/6b2d7181e264ed78bf8b719cc107537d0dd35ea5/README.md)

## Limits and data handling

The recorded results (for example, all checks passed in both loops and Jev + LLM cost less in three single runs) are author-reported and were not reproduced. Live runs send workspace context to TypeSafe and ChatGPT.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 6b2d7181e264](https://github.com/MahmoudMoubarez/system-one-agent/tree/6b2d7181e264ed78bf8b719cc107537d0dd35ea5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
