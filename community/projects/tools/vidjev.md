# vidjev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

System One–style decisions on live video: CARLA drone following and zero-shot CCTV anomaly detection with open vision-language models (and a djev adapter)—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/numinousmuses/vidjev) |
| Maintainer | [numinousmuses](https://github.com/numinousmuses). Independently curated. |
| Format | Research code + demo clips; MIT. Sponsored by Brainbase (per upstream). |
| Requirements | Per-upstream GPU/CARLA/UCF-Crime setup for full runs; demo media in-repo. |
| License | [MIT](https://github.com/numinousmuses/vidjev/blob/dd6e127c1a2ec3ef2f89004665e64e62db758b1e/LICENSE). Independent open-model path—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream tables are author-reported; not re-run here. Live CARLA/CCTV paths not run on the review host. |

## When to use

Use when studying typed box/choice/noul decisions over video frames with open models. Prefer hosted Jev demos when you need the commercial System One API.

## How it works

Models answer typed questions (boxes, incident choices, yes/no checks); ordinary code turns answers into drone control or anomaly scores. Compares Qwen sizes and djev on CARLA and UCF-Crime.

## Get started

```sh
git clone https://github.com/numinousmuses/vidjev.git
cd vidjev
git checkout dd6e127c1a2ec3ef2f89004665e64e62db758b1e
# see upstream for CARLA/CCTV reproduction; media/ has demo clips
```

## Examples and demos

- `media/hero_collage.mp4` and related clips.
- Upstream result tables (author-reported).

## Limits and data handling

Runs are local/self-hosted on open models. Catalog checks did not execute CARLA or CCTV pipelines.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit dd6e127](https://github.com/numinousmuses/vidjev/tree/dd6e127c1a2ec3ef2f89004665e64e62db758b1e). AI-assisted README and license inspection; install/live paths not executed.
