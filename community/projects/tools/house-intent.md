# House Intent by Zachary Goodale-Pirkle (Home Assistant voice-command router where one Jev call classifies intent and targets before a guarded service call)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Voice-command router for Home Assistant: each transcript becomes a spoken reply, a confirmation chime or a Home Assistant service call. One Jev request per turn classifies the intent and targets, and the router checks the result against your rooms, exposed entities and a denylist before it acts. Optional Hermes or OpenAI backends answer open-ended questions. Ships a Home Assistant custom component and a demo home for tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zacharyGoodale/house-intent) |
| Maintainer | [Zachary Goodale-Pirkle](https://github.com/zacharyGoodale). Independently curated. |
| Format | Python service + Home Assistant custom component |
| Requirements | Python 3.12+, uv, a TypeSafe API key and a Home Assistant instance (a fictional demo home is included for tests). |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ha_jev/jev.py`](https://github.com/zacharyGoodale/house-intent/blob/4222c2dbc0c6e755c7037acbf5e1c26a8fc3d0e2/src/ha_jev/jev.py) at the pinned commit. |

## When to use

- Home Assistant users who want fast, checked voice control without a chat model deciding every action.
- Mismatch: a ready add-on; it is a self-hosted service you set up yourself.

## How it works

`src/ha_jev/jev.py` uses the TypeSafe SDK to ask `choice` and `noul` questions built in `questions.py`; code applies the policy, so locks and sensors stay read-only and denylisted entities are never called. Integration evidence: [`src/ha_jev/jev.py`](https://github.com/zacharyGoodale/house-intent/blob/4222c2dbc0c6e755c7037acbf5e1c26a8fc3d0e2/src/ha_jev/jev.py).

## Get started

Run the offline tests on the demo home, then try the CLI with a key.

```sh
git clone https://github.com/zacharyGoodale/house-intent && cd house-intent
uv sync --locked
uv run pytest
export TYPESAFE_API_KEY=...
uv run ha-jev ask "turn on the living room lights" --area living_room --no-llm
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration guide: [github.com/zacharyGoodale/house-intent/blob/main/docs/configuration.md](https://github.com/zacharyGoodale/house-intent/blob/main/docs/configuration.md)
- Demo home: [github.com/zacharyGoodale/house-intent/tree/main/demo](https://github.com/zacharyGoodale/house-intent/tree/main/demo)

## Limits and data handling

Transcripts and the list of rooms and exposed entities go to TypeSafe on every turn; optional backends get open-ended questions. No licence file, so no reuse rights are granted. Not run on the review host.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 4222c2dbc0c6](https://github.com/zacharyGoodale/house-intent/tree/4222c2dbc0c6e755c7037acbf5e1c26a8fc3d0e2). Inspected the README, configuration docs and `src/ha_jev/jev.py` at the pinned commit; no licence file present. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
