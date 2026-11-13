# Hearth (pixel-art village where Jev chooses what 20 villagers do and Luna writes what they say)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local browser simulation of a 20-person pixel-art village: a Python engine runs the world and rejects disallowed choices, Jev picks each villager's next action from 89 options with probabilities, and OpenAI's Luna writes thoughts and speech; a demo mode runs on local rules with no model calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mblukac/hearth) |
| Maintainer | [mblukac](https://github.com/mblukac). Independently curated. |
| Format | Local Python server with a browser UI (no license file) |
| Requirements | Python 3.11+, and for live mode an OpenRouter key (`OPENROUTER_API_KEY`) that pays for both models. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`village/providers.py`](https://github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/providers.py) at the pinned commit. |

## When to use

- Watch a decision model drive agents in a rule-checked simulation.
- See how Jev's action choices and an LLM's prose split the work.
- Mismatch: a finished game with goals; it is a sandbox.

## How it works

`village/providers.py` sends each villager's situation to OpenRouter's Decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with model `typesafe/jev-1.14` and validates the choice against the rules before applying it; Luna (`openai/gpt-6-luna`) handles prose. The app footer shows calls made and what OpenRouter charged in the session; tests make no network calls. Integration evidence: [`village/providers.py`](https://github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/providers.py).

## Get started

Create a virtualenv, install the requirements, add your OpenRouter key, start the server and open the local page, or use `--demo` with no key.

```sh
python3 -m venv .venv
.venv/bin/pip install -r village/requirements.txt
.venv/bin/python -m village.server --demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshot: [github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/README.md](https://github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/README.md)
- Action list: [github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/ACTIONS.md](https://github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/ACTIONS.md)
- Live validation notes: [github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/VALIDATION.md](https://github.com/mblukac/hearth/blob/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad/village/VALIDATION.md)

## Limits and data handling

Villager states go to OpenRouter (Jev and Luna) on your key in live mode; the village saves to a local JSON file.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 3f18d4338f57](https://github.com/mblukac/hearth/tree/3f18d4338f57d34bb5db3a52d2a3d64efdae1aad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
