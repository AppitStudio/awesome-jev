# Jev Nav by Abhinav Mishra (spoken walking guidance from a first-person camera, decided by a council of Jev agents)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Prototype that guides someone walking with an FPV camera (stop, wait, slow down, step left or right, stairs): five Jev agents answer typed questions and Box queries about each frame, a code arbiter picks the least-risk action with safety vetoes, and NVIDIA Nemotron explains the decision by voice without changing it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Itsabhinav28/jev-nav) |
| Maintainer | [Itsabhinav28](https://github.com/Itsabhinav28). Independently curated. |
| Format | Python research prototype |
| Requirements | Python; `TYPESAFE_API_KEY`, `OPENROUTER_API_KEY` (Nemotron) and HeyGen for voice; a webcam or video file. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_nav/jev_client.py`](https://github.com/Itsabhinav28/jev-nav/blob/9677f98ef47652e73253d060e70432b1a91056c6/src/jev_nav/jev_client.py) at the pinned commit. |

## When to use

- Study a multi-agent decision design with a code arbiter and safety vetoes on live video.
- Mismatch: real mobility assistance; it is an unvalidated prototype, not a safety device.

## How it works

`src/jev_nav/jev_client.py` wraps TypeSafe's async SDK with the image opt-in header and a concurrency cap; the agents in `src/jev_nav/agents/` ask Choice, Score and Box questions about each frame (perception, hazard, clearance, motion, navigator), and the growth of an object's Jev box gives time to contact; the arbiter weighs a wrong "go" three times a wrong "stop" and vetoes only make actions safer. Integration evidence: [`src/jev_nav/jev_client.py`](https://github.com/Itsabhinav28/jev-nav/blob/9677f98ef47652e73253d060e70432b1a91056c6/src/jev_nav/jev_client.py).

## Get started

Install, add keys and analyze a recorded video offline.

```sh
git clone https://github.com/Itsabhinav28/jev-nav
cd jev-nav
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
# .env: TYPESAFE_API_KEY, OPENROUTER_API_KEY
.venv/bin/jev-nav analyze path/to/fpv.mp4
.venv/bin/pytest   # fake Jev, no cost
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Itsabhinav28/jev-nav/blob/9677f98ef47652e73253d060e70432b1a91056c6/README.md](https://github.com/Itsabhinav28/jev-nav/blob/9677f98ef47652e73253d060e70432b1a91056c6/README.md)
- Eval scripts: [github.com/Itsabhinav28/jev-nav/tree/9677f98ef47652e73253d060e70432b1a91056c6/eval](https://github.com/Itsabhinav28/jev-nav/tree/9677f98ef47652e73253d060e70432b1a91056c6/eval)

## Limits and data handling

Camera frames are sent to TypeSafe and, with audio, to OpenRouter and HeyGen. Not evaluated for people who rely on it; do not use it as a mobility aid. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 9677f98ef476](https://github.com/Itsabhinav28/jev-nav/tree/9677f98ef47652e73253d060e70432b1a91056c6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
