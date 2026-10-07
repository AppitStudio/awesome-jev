# JevSceneMiner

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Mines driving maneuvers from Autoware rosbags and nuPlan logs with TypeSafe Jev: motion, lane geometry and object interactions become a readable script, Jev classifies lateral and longitudinal labels with probabilities, and answers merge into timestamped scenes with a camera/BEV/timeline review viewer and ground-truth editor.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bskkimm/JevSceneMiner) |
| Maintainer | [bskkimm](https://github.com/bskkimm). Independently curated. |
| Format | Python package with `jevsceneminer` CLI and local web viewer |
| Requirements | Linux, Python 3.10+ and uv; Autoware MCAP + Lanelet2 or nuPlan SQLite + map for real data; a TypeSafe key for live classification (the synthetic demo needs none). |
| License | [Apache-2.0](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Find lane changes, turns and speed phases in recorded driving logs for review or dataset curation.
- Edit plain-language labels in `labels.yaml` instead of training a classifier.
- Mismatch: camera review needs your own nuPlan sources; scenes are classifier output to review, not ground truth.

## How it works

Preprocessing under [`src/jevsceneminer/evidence/`](https://github.com/bskkimm/JevSceneMiner/tree/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/src/jevsceneminer/evidence) builds facts and a script around each moment; Jev answers the [label questions](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/labels.yaml) with probabilities, and lateral scenes are merged with consecutive speed phases. See the [sample](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/examples/sample.json) and its [Jev input](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/examples/sample.txt).

## Get started

Run the synthetic pipeline without an API key (README *Quick start*):

```sh
git clone https://github.com/bskkimm/JevSceneMiner.git && cd JevSceneMiner
uv sync --frozen
uv run python examples/pipeline_demo.py --source rosbag --out out/demo
uv run jevsceneminer view out/demo --gt out/demo-gt --port 8650
```

The demo uses cached answers and blocks API requests; live runs send one or more Jev requests per sample, billed by TypeSafe.

## Examples and demos

- README *Boston demo* (real nuPlan footage with Jev results).
- [Usage](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/docs/usage.md) and [schema](https://github.com/bskkimm/JevSceneMiner/blob/9d8b03e74fb419cd5c903ac082c65c72676ff0b1/docs/schema.md) docs.

## Limits and data handling

Scene text derived from your logs goes to TypeSafe on live runs; camera images stay local for review. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 9d8b03e74fb4](https://github.com/bskkimm/JevSceneMiner/tree/9d8b03e74fb419cd5c903ac082c65c72676ff0b1). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
