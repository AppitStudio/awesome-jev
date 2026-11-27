# Call Companion by Adilet Gaparov (Pipecat voice agent that shares a screen with the caller; Jev maps spoken choices to on-screen options)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prototype framework for voice agents that text the caller a link mid-call to a small page showing the current step, so the caller can talk, tap or type and the agent and page stay in sync. Flows are YAML pages whose actions are both buttons and agent tools. With a TypeSafe key, Jev maps phrases like "the afternoon one" to the right option in about 150 ms and decides when a tap needs a spoken reply; without it the LLM does everything.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adgapar/multi-modal-agent-framework) |
| Maintainer | [Adilet Gaparov](https://github.com/adgapar) (adgapar). Independently curated. |
| Format | Python framework (Pipecat + Pipecat Flows) with a browser demo |
| Requirements | Python 3.12+ with uv; OpenAI, Deepgram and ElevenLabs keys; TypeSafe key optional. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/adgapar/status/2126436046909079701)). |
| Jev evidence | [`call_companion/services.py`](https://github.com/adgapar/multi-modal-agent-framework/blob/cfe05a575393114c0ae883078fbc7975f2c825dd/call_companion/services.py) at the pinned commit. |

## When to use

- Voice-agent builders who need callers to pick options, times or enter details that are awkward by voice.
- Mismatch: production telephony; real phone numbers via Twilio are listed as next steps.

## How it works

`call_companion/services.py` registers Pipecat's `JevClassifier` as the default classifier when `TYPESAFE_API_KEY` is set; `call_companion/judge.py` asks a `choice` over the current screen's options plus a yes/no on whether the caller chose anything, and applies the action only when both are confident, while the LLM keeps the conversation. Integration evidence: [`call_companion/services.py`](https://github.com/adgapar/multi-modal-agent-framework/blob/cfe05a575393114c0ae883078fbc7975f2c825dd/call_companion/services.py).

## Get started

Add keys, start the server and open the local demo.

```sh
git clone https://github.com/adgapar/multi-modal-agent-framework && cd multi-modal-agent-framework
cp .env.example .env   # OpenAI, Deepgram, ElevenLabs; TYPESAFE_API_KEY optional
uv sync
uv run call-companion   # http://localhost:7860
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Flow guide: [github.com/adgapar/multi-modal-agent-framework/blob/main/docs/flows.md](https://github.com/adgapar/multi-modal-agent-framework/blob/main/docs/flows.md)

## Limits and data handling

Caller audio goes to Deepgram, the conversation to OpenAI and ElevenLabs, and caller turns to TypeSafe when Jev is on. Early prototype, one commit. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit cfe05a575393](https://github.com/adgapar/multi-modal-agent-framework/tree/cfe05a575393114c0ae883078fbc7975f2c825dd). Inspected the README, `call_companion/services.py` and `judge.py` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
