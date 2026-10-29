# Jev Video Lab (ask structured questions about video footage with Jev and evaluate it on annotated clips)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Experimental local app for asking video questions with Jev: event search across indexed videos (before, after, overlap), multiple-choice questions on a segment, object presence and Box locations drawn on frames, procedure checks that flag missed steps for a person, recording alignment, human review and exports. The author's first study on Perception Test reports 463 of 658 questions right (70.4%) and weak precise event localization.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EventumAI/jev-video-lab) |
| Maintainer | [EventumAI](https://github.com/EventumAI). Independently curated. |
| Format | Python package and local web app |
| Requirements | Python 3.11+, FFmpeg and a TypeSafe API key; no GPU. |
| License | [MIT](https://github.com/EventumAI/jev-video-lab/blob/ae83f40d0ad8d9fb9e80322d4a6d1d0b0b121623/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_video_lab/client.py`](https://github.com/EventumAI/jev-video-lab/blob/ae83f40d0ad8d9fb9e80322d4a6d1d0b0b121623/src/jev_video_lab/client.py) at the pinned commit. |

## When to use

- Explore what a decision model can and cannot answer about footage.
- Mismatch: experimental; results are the author's on one dataset.

## How it works

`src/jev_video_lab/client.py` posts sampled frames and questions to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.14.0`, storing versioned calls and raw responses. Integration evidence: [`src/jev_video_lab/client.py`](https://github.com/EventumAI/jev-video-lab/blob/ae83f40d0ad8d9fb9e80322d4a6d1d0b0b121623/src/jev_video_lab/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/EventumAI/jev-video-lab.git && cd jev-video-lab
python -m venv .venv && source .venv/bin/activate
pip install .
jev-video sample   # fetches the eight-video sample
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with study results: [github.com/EventumAI/jev-video-lab#readme](https://github.com/EventumAI/jev-video-lab#readme)

## Limits and data handling

Video frames you analyze go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit ae83f40d0ad8](https://github.com/EventumAI/jev-video-lab/tree/ae83f40d0ad8d9fb9e80322d4a6d1d0b0b121623). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
