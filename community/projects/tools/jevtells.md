# JevTells (open-source tool that turns interview and speech videos into annotated clips, with Jev judging confidence, focus and intent per window)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Chinese and English video-analysis tool: MediaPipe finds people and hand keypoints, OCR or faster-whisper supplies subtitles, librosa measures voice, and Jev judges expression state, intent and emotion for each speaking window as scores and classes, which a separate language model turns into commentary. It renders landscape and portrait videos with gesture labels, a judgment panel and quoted phrases, and has a browser workbench (`jevtells ui`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yxtzan/jevtells) |
| Maintainer | [yxtzan](https://github.com/yxtzan). Independently curated. |
| Format | Python 3.11 CLI and local web UI |
| Requirements | Python 3.11, ffmpeg with libx264 and an OpenRouter API key; macOS (Apple silicon tested) or Linux; about 2 GB for models. |
| License | [MIT](https://github.com/yxtzan/jevtells/blob/1217e8963089a061e0865021ebe9520cf06e92a7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevtells/stages/judge.py`](https://github.com/yxtzan/jevtells/blob/1217e8963089a061e0865021ebe9520cf06e92a7/src/jevtells/stages/judge.py) at the pinned commit. |

## When to use

- Produce annotated analysis videos where a typed model supplies the scored judgments and code and other models supply detection and commentary.
- Mismatch: it analyses people in videos, so mind consent and the rights to your source clips; the README shows an example built from a third-party interview.

## How it works

`src/jevtells/stages/judge.py` builds per-window state descriptions and posts typed questions from `config/jev_questions.yaml` to OpenRouter's decisions endpoint with `typesafe/jev-1.13` by default, caching raw responses per window. Integration evidence: [`src/jevtells/stages/judge.py`](https://github.com/yxtzan/jevtells/blob/1217e8963089a061e0865021ebe9520cf06e92a7/src/jevtells/stages/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/yxtzan/jevtells.git && cd jevtells
pip install -r requirements.txt && pip install -e .
jevtells doctor
jevtells ui
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with the pipeline, UI and cost notes: [github.com/yxtzan/jevtells#readme](https://github.com/yxtzan/jevtells#readme)

## Limits and data handling

Scene descriptions, Jev judgments and commentary go through OpenRouter on your key; detection, transcription and rendering run locally. The README reports about $0.005 for a 30-second clip in October 2026, which varies. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 1217e8963089](https://github.com/yxtzan/jevtells/tree/1217e8963089a061e0865021ebe9520cf06e92a7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
