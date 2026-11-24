# Cry-Agent by muyangtangqq-oss (research prototype that guesses why a baby is crying from audio, posture and context, escalating hard cases to Jev)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Fuses an 8-class cry audio classifier, camera posture, feeding/sleep/diaper context, temperature and noise. Clear cases are answered directly, mid-confidence ones by a local Tachyone model, and genuinely ambiguous ones by Jev in the cloud; both judges speak the System One wire format, so they are interchangeable. Includes feedback-based self-learning and a Jetson deploy script.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muyangtangqq-oss/cry-agent) |
| Maintainer | [muyangtangqq-oss](https://github.com/muyangtangqq-oss). Independently curated. |
| Format | Python pipeline with an API server and dashboard (Docker Compose) |
| Requirements | Python (or Docker), sensors or replay data, and a TypeSafe API key for the Jev tier. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/jev_client.py) at the pinned commit. |

## When to use

- Study a tiered local-then-Jev judgment design on a multimodal sensing problem.
- Mismatch: infant care decisions; it is a research prototype, not a medical device.

## How it works

`jev_client.py` posts fused signals as typed System One questions (`jev-1.14.0`) when the local Tachyone answer is below 0.70 confidence; by default requests go through a Magpie proxy, and `CRY_AGENT_TS_BASE_URL=https://api.typesafe.ai/v1` calls TypeSafe directly. DeepSeek or Ollama judges can replace Jev. Integration evidence: [`jev_client.py`](https://github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/jev_client.py).

## Get started

Read the README and pilot protocol, then run the replay or simulation before any live sensors.

```sh
git clone https://github.com/muyangtangqq-oss/cry-agent.git && cd cry-agent
uv venv --python 3.12 && . .venv/bin/activate
python3 -m pip install -r requirements.txt
CRY_AGENT_TS_MOCK=1 python jev_client.py   # offline smoke test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Whitepaper: [github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/WHITEPAPER.md](https://github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/WHITEPAPER.md)
- Pilot protocol: [github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/PILOT_PROTOCOL.md](https://github.com/muyangtangqq-oss/cry-agent/blob/d178fb044ebb5a4387c03893bc87315ad079858a/PILOT_PROTOCOL.md)

## Limits and data handling

Not a medical device and not validated for care decisions; it suggests likely causes only. Ambiguous cases send sensor-derived context to the configured System One endpoint (a third-party proxy by default, not TypeSafe directly). No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit d178fb044ebb](https://github.com/muyangtangqq-oss/cry-agent/tree/d178fb044ebb5a4387c03893bc87315ad079858a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
