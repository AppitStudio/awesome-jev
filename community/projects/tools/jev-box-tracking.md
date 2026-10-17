# jev-box-tracking

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python library and webcam demo for real-time object tracking: Jev Box answers give the absolute position, optical flow tracks motion between answers, and a Kalman filter rewinds and fuses late answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BenCaunt/jev-box-tracking) |
| Maintainer | [BenCaunt](https://github.com/BenCaunt). Independently curated. |
| Format | Python package and CLI (`jev-box-track`) |
| Requirements | Python 3, OpenCV, a camera for the demo, a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/BenCaunt/jev-box-tracking/blob/bc5325796c26f30ec83ba7f2a7d3fefb19174869/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_box_tracking/client.py`](https://github.com/BenCaunt/jev-box-tracking/blob/bc5325796c26f30ec83ba7f2a7d3fefb19174869/src/jev_box_tracking/client.py) at the pinned commit. |

## When to use

- Track a named object ("coffee mug") in a live camera feed without training a detector.
- Learn how to hide model latency by fusing slow, accurate answers with fast local motion estimates.
- Mismatch: every Jev answer is a paid round trip, and Box questions are an experimental TypeSafe feature.

## How it works

`JevClient` posts frames and a Box question to `https://api.typesafe.ai/v1/systemone`. `JevTracker.update()` never blocks on the network: Lucas-Kanade flow updates velocity every frame, and when a Jev answer for an older frame arrives the filter rewinds to that frame, corrects, and replays to now. Integration evidence: [`src/jev_box_tracking/client.py`](https://github.com/BenCaunt/jev-box-tracking/blob/bc5325796c26f30ec83ba7f2a7d3fefb19174869/src/jev_box_tracking/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "git+https://github.com/BenCaunt/jev-box-tracking.git"
export TYPESAFE_API_KEY=...
jev-box-track "iPhone"   # press q to quit
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Library example with `JevTracker` in the README.
- `TrackResult` exposes confidence, latency, replay time and raw Jev answers.

## Limits and data handling

Camera frames go to TypeSafe on your key while tracking. No hosted service; nothing is stored by the library.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit bc5325796c26](https://github.com/BenCaunt/jev-box-tracking/tree/bc5325796c26f30ec83ba7f2a7d3fefb19174869). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
