# Jev Assist (cloud Home Assistant voice assistant where Jev decides the intent, device and action, and an LLM handles only compound requests and conversation)

[All projects](../README.md) · [Home automation](README.md#home-automation)

HACS custom integration that adds a conversation agent plus speech-to-text and text-to-speech entities: each request goes to Jev once with the exposed devices, asking request type, target device or room, device type and action; clear commands call Home Assistant services directly with no LLM, while compound or unclear requests go to Claude Haiku. Everything runs through one OpenRouter key; README is in Czech.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KiskaLE/home-assistant) |
| Maintainer | [KiskaLE](https://github.com/KiskaLE). Independently curated. |
| Format | Home Assistant custom integration via HACS (Python, MIT) |
| Requirements | Home Assistant 2026.10+, HACS and an OpenRouter API key (Jev, LLM and ElevenLabs voice models are all billed through OpenRouter). |
| License | [MIT](https://github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`custom_components/jev_assist/const.py`](https://github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/custom_components/jev_assist/const.py) at the pinned commit. |

## When to use

- Voice-control a Home Assistant home with fast, cheap intent and device decisions.
- Mismatch: local-only or offline voice control; every request goes to cloud models.

## How it works

`const.py` sets the OpenRouter Decisions endpoint (`/api/alpha/decisions`) and default decision model `~typesafe/jev-latest`; `decision.py` compares Jev's probabilities with thresholds to act directly, split the request through the LLM, or hand off. The design follows TypeSafe's smart-home demo. Integration evidence: [`custom_components/jev_assist/const.py`](https://github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/custom_components/jev_assist/const.py).

## Get started

Add the repository to HACS as a custom integration, install Jev Assist, then add it with your OpenRouter key and pick it as the voice assistant's agent.

```sh
# HACS → ⋮ → Custom repositories → https://github.com/KiskaLE/home-assistant (Integration)
# Settings → Devices & services → Add integration → Jev Assist (OpenRouter key)
# Settings → Voice assistants → choose Jev Assist for agent, STT and TTS
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Czech): [github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/README.md](https://github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/README.md)
- Decision logic: [github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/custom_components/jev_assist/decision.py](https://github.com/KiskaLE/home-assistant/blob/9c211008d74b6ce185ee8db31e40067bcc7226b2/custom_components/jev_assist/decision.py)

## Limits and data handling

Each spoken request, its transcript and the list of exposed entities go to OpenRouter (Jev, an LLM and voice models) on your key. Nothing runs locally. Thresholds are configurable; misfires can toggle the wrong device.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 9c211008d74b](https://github.com/KiskaLE/home-assistant/tree/9c211008d74b6ce185ee8db31e40067bcc7226b2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
