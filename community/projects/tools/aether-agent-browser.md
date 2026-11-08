# Aether Agent Browser (self-hosted Chrome for AI agents with TypeSafe Jev handoff decisions)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Self-hosted Chrome for AI agents with a Python client whose Jev helper uses TypeSafe Jev (via OpenRouter) to choose between agent handoff, human takeover, or a small set of next actions. Distinct from other agent-browser projects listed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AetherAI3/agent-browser) |
| Maintainer | [AetherAI3](https://github.com/AetherAI3). Independently curated. |
| Format | Self-hosted browser + Python client (Apache-2.0) |
| Requirements | Docker or a host for the browser, Python 3, and an OpenRouter key with TypeSafe Jev access. |
| License | [Apache-2.0](https://github.com/AetherAI3/agent-browser/blob/23f050c5a163923ce4624053cc0466c69b72bc51/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`clients/python/src/aether_browser/jev.py`](https://github.com/AetherAI3/agent-browser/blob/23f050c5a163923ce4624053cc0466c69b72bc51/clients/python/src/aether_browser/jev.py) at the pinned commit. |

## When to use

- Run a browser your agents control with fast Jev action picks.
- Decide when to hand a session to a human.
- Mismatch: Jev is an optional client helper.

## How it works

`clients/python/src/aether_browser/jev.py` posts to `https://openrouter.ai/api/v1/systemone` with `typesafe/jev-1.13`; `docs/JEV.md` describes the single `Choice` for handoff/takeover/actions. Integration evidence: [`clients/python/src/aether_browser/jev.py`](https://github.com/AetherAI3/agent-browser/blob/23f050c5a163923ce4624053cc0466c69b72bc51/clients/python/src/aether_browser/jev.py).

## Get started

Run the browser per README, install the Python client, and follow `docs/JEV.md`.

```sh
git clone https://github.com/AetherAI3/agent-browser.git && cd agent-browser
export OPENROUTER_API_KEY=...
pip install -e clients/python
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AetherAI3/agent-browser/blob/23f050c5a163923ce4624053cc0466c69b72bc51/README.md](https://github.com/AetherAI3/agent-browser/blob/23f050c5a163923ce4624053cc0466c69b72bc51/README.md)

## Limits and data handling

Page state for decisions is sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 23f050c5a163](https://github.com/AetherAI3/agent-browser/tree/23f050c5a163923ce4624053cc0466c69b72bc51). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
