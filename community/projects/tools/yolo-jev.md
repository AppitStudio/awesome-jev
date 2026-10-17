# YOLO vs Jev: the flying car

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

One notebook that runs YOLO26 and Jev 1.14 on the 34 frames of a clip where a car flies over a car show: Jev finds the car in the air in 17 of 19 frames with no false alarms, and names every boxed vehicle, against YOLO's 0 to 4.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CristianYepes/yolo-jev) |
| Maintainer | [CristianYepes](https://github.com/CristianYepes). Independently curated. |
| Format | Jupyter notebook (uv project) with saved results and an output video |
| Requirements | Python with uv, ffmpeg; `OPENROUTER_API_KEY` only to re-run the Jev parts (about $0.01), otherwise saved answers replay. |
| License | [MIT](https://github.com/CristianYepes/yolo-jev/blob/f4729b6e67bcd8e3eadabd5e465fea8e540a3713/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`config.json`](https://github.com/CristianYepes/yolo-jev/blob/f4729b6e67bcd8e3eadabd5e465fea8e540a3713/config.json) at the pinned commit. |

## When to use

- See where a detector and a decision model complement each other: YOLO finds where, Jev says what.
- Reuse the trap note: through OpenRouter, images reach Jev only on the Decisions API; the System One route silently drops base64 assets.
- Mismatch: one clip and one run, labeled by eye; not a general detection benchmark.

## How it works

For each frame Jev is asked a Noul (is a car in the air?) and a Box (where?), then each YOLO box is cropped and Jev answers a Choice for all crops of a frame in one request, through OpenRouter's Decisions API with `typesafe/jev-1.14`. Everything the test decides is fixed in `config.json`, and each result records the sha256 of the config it depends on. Integration evidence: [`config.json`](https://github.com/CristianYepes/yolo-jev/blob/f4729b6e67bcd8e3eadabd5e465fea8e540a3713/config.json).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
# open yolo_vs_jev.ipynb with the .venv kernel; without a key it replays results/jev.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results tables in the README; saved answers in `results/`.
- Source frames from TypeLLM's cookbook: [typellm.ai/cookbook/locate-vehicles-in-a-video](https://typellm.ai/cookbook/locate-vehicles-in-a-video)

## Limits and data handling

Frames go to OpenRouter and TypeSafe on your key only when you re-run the Jev cells. YOLO26 itself is AGPL-3.0; the notebook code is MIT.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit f4729b6e67bc](https://github.com/CristianYepes/yolo-jev/tree/f4729b6e67bcd8e3eadabd5e465fea8e540a3713). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
