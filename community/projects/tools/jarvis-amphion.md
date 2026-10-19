# Jarvis (Amphion)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research system and paper ("Coordination Deserves a Brain of Its Own") for full-duplex voice agents: JEV decides each turn (answer, memory, worker, clarify, control, ignore or wait) so you can keep talking while background tasks run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AmphionTeam/Jarvis) |
| Maintainer | [AmphionTeam](https://github.com/AmphionTeam). Independently curated. |
| Format | Python system + paper |
| Requirements | Linux, Python 3.11, NVIDIA GPUs with BF16; `WORKER_API_KEY` and `TYPESAFE_API_KEY` (or JEV as a local service). |
| License | [Apache-2.0](https://github.com/AmphionTeam/Jarvis/blob/42cb8798462f35b1e72a76ae179388e45de72d30/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jarvis/core/jev.py`](https://github.com/AmphionTeam/Jarvis/blob/42cb8798462f35b1e72a76ae179388e45de72d30/jarvis/core/jev.py) at the pinned commit. |

## When to use

- Study or build voice agents that coordinate tasks while the conversation continues.
- Use a decision model as the turn-level coordinator instead of the chat model.
- Mismatch: research stack with heavy GPU requirements.

## How it works

`jarvis/core/jev.py` uses the TypeSafe Python SDK (`AsyncTypeSafeClient` with Choice, Noul and Score) to route each transcript update to FAST, MEMORY, WORKER, CLARIFY, CONTROL, IGNORE or WAIT, and to decide read-only prefetch from speech prefixes. JEV also chooses task operations from a versioned task ledger. Integration evidence: [`jarvis/core/jev.py`](https://github.com/AmphionTeam/Jarvis/blob/42cb8798462f35b1e72a76ae179388e45de72d30/jarvis/core/jev.py).

## Get started

From the upstream README: install into a Python 3.11 virtualenv, fill in `.env`, download models, and run the services.

```sh
git clone https://github.com/AmphionTeam/Jarvis.git && cd Jarvis
python3.11 -m venv .venv && source .venv/bin/activate
python -m pip install . && cp .env.example .env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [arxiv.org/abs/2610.23804](https://arxiv.org/abs/2610.23804)
- [amphionteam.github.io/Jarvis-Demo/](https://amphionteam.github.io/Jarvis-Demo/)

## Limits and data handling

Transcripts go to TypeSafe when hosted JEV is used. Results come from the authors' setup and models.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 42cb8798462f](https://github.com/AmphionTeam/Jarvis/tree/42cb8798462f35b1e72a76ae179388e45de72d30). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
