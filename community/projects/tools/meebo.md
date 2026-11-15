# Meebo (meeting-referee box on an ESP32-S3 that keeps a live score and speaks up when Jev judges the talk has left the agenda)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Junction 2026 hackathon build: a small box on the meeting-room table reads the goal and agenda from the calendar event, listens, keeps a live meeting score, and speaks up when the room drifts off agenda, runs over time or one voice dominates; afterwards it explains the score. Jev answers the on-topic question for each stretch of talk against the agenda and parked topics; without a key it falls back to an LLM with logprobs, then keywords. Includes firmware, a printable enclosure and a laptop simulator.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zabrodsk/meebo) |
| Maintainer | [zabrodsk](https://github.com/zabrodsk). Independently curated. |
| Format | Python brain service plus ESP32-S3 firmware (Atech Big Kit) and CAD |
| Requirements | Python 3.12 with uv; ElevenLabs and Gemini keys for voice and language; `TYPESAFE_API_KEY` for Jev topic checks; an Atech Big Kit (ESP32-S3) box or the included simulator. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`brain/meebo/llm.py`](https://github.com/zabrodsk/meebo/blob/828d9a6d0a2baad3754054a45feccedcf2d36a15/brain/meebo/llm.py) at the pinned commit. |

## When to use

- Prototype a physical device that uses Jev for a fast, cheap yes/no relevance check on live speech.
- Mismatch: a finished product; it is a hackathon build for one hardware kit.

## How it works

`brain/meebo/llm.py` posts the meeting goal, agenda, parked topics and latest talk to `https://api.typesafe.ai/v1/systemone` as one Noul question (`jev-latest` by default from `config.py`) and uses the probability as the on-topic score. Integration evidence: [`brain/meebo/llm.py`](https://github.com/zabrodsk/meebo/blob/828d9a6d0a2baad3754054a45feccedcf2d36a15/brain/meebo/llm.py).

## Get started

Install the brain service, add keys, run the dashboard, and use the simulator if you have no hardware.

```sh
git clone https://github.com/zabrodsk/meebo && cd meebo/brain
uv venv --python 3.12 && uv pip install -e '.[sim,calendar]'
cp .env.example .env    # ELEVENLABS_API_KEY, GEMINI_API_KEY, TYPESAFE_API_KEY, ...
.venv/bin/python -m meebo.server    # dashboard on http://127.0.0.1:8765
.venv/bin/python sim_device.py      # no hardware
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and demo video: [github.com/zabrodsk/meebo/blob/828d9a6d0a2baad3754054a45feccedcf2d36a15/README.md](https://github.com/zabrodsk/meebo/blob/828d9a6d0a2baad3754054a45feccedcf2d36a15/README.md)

## Limits and data handling

Meeting transcripts and calendar details go to TypeSafe and the configured voice/LLM providers on your keys. The maker's 52-snippet topic test is a small internal check, not a benchmark. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 828d9a6d0a2b](https://github.com/zabrodsk/meebo/tree/828d9a6d0a2baad3754054a45feccedcf2d36a15). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
