# Jev-Interaction (full-duplex voice turn-taking decided by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Full-duplex voice agent built from a cascade (speech recognition, Jev, any LLM, any TTS) where every turn-taking choice, such as waiting, yielding, backchanneling or picking a call back up, is a plain-language question Jev answers in tens of milliseconds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/native-bond-lab/Jev-Interaction) |
| Maintainer | [native-bond-lab](https://github.com/native-bond-lab). Independently curated. |
| Format | Voice agent framework and server (Python, Apache-2.0) |
| Requirements | Python 3.10+, `JEV_API_KEY`, an OpenAI-compatible LLM endpoint, and ElevenLabs keys for speech. |
| License | [Apache-2.0](https://github.com/native-bond-lab/Jev-Interaction/blob/a86adc321ffb1d8248a412875769439e08a3f079/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_interaction/judge/client.py`](https://github.com/native-bond-lab/Jev-Interaction/blob/a86adc321ffb1d8248a412875769439e08a3f079/jev_interaction/judge/client.py) at the pinned commit. |

## When to use

- Add natural interruptions and backchannels to a cascaded voice agent.
- Write turn-taking rules as questions instead of training a model.
- Mismatch: alpha; needs hosted Jev and paid speech services.

## How it works

`jev_interaction/judge/client.py` posts to `https://api.typesafe.ai/v1/systemone` (override with `JEV_URL`); the turn-taking questions live in `jev_interaction/judge/questions.py` and can be changed per profile. Integration evidence: [`jev_interaction/judge/client.py`](https://github.com/native-bond-lab/Jev-Interaction/blob/a86adc321ffb1d8248a412875769439e08a3f079/jev_interaction/judge/client.py).

## Get started

Clone, install the server extra, fill in `.env`, then run a profile.

```sh
git clone https://github.com/native-bond-lab/Jev-Interaction && cd Jev-Interaction
pip install -e ".[server]" && cp .env.example .env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision questions: [github.com/native-bond-lab/Jev-Interaction/blob/a86adc321ffb1d8248a412875769439e08a3f079/jev_interaction/judge/questions.py](https://github.com/native-bond-lab/Jev-Interaction/blob/a86adc321ffb1d8248a412875769439e08a3f079/jev_interaction/judge/questions.py)

## Limits and data handling

Live transcript and conversation state go to TypeSafe for each decision; audio goes to your speech provider.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit a86adc321ffb](https://github.com/native-bond-lab/Jev-Interaction/tree/a86adc321ffb1d8248a412875769439e08a3f079). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
