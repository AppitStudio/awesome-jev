# duckbatch (batched, efficiency-first RL for Pollen's Microduck robot, with Jev measured as one judge of the runs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Training harness for Pollen Robotics' Microduck walker in simulation: many small attempts share one simulator batch on a 4 GB laptop GPU and a pre-registered kill order prunes them, while decision models (Jev and GLiNER2.5-Decide) are measured as judges of the records rather than trusted as one. Its b002 student is 7.5x smaller than the default walker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/craigm26/duckbatch) |
| Maintainer | [craigm26](https://github.com/craigm26). Independently curated. |
| Format | Python research harness with CLI, records and a Hugging Face arena (Apache-2.0) |
| Requirements | Python via uv, an NVIDIA GPU for training, and a `TYPESAFE_API_KEY` only for the Jev judge step. |
| License | [Apache-2.0](https://github.com/craigm26/duckbatch/blob/3cc42870039b58c2a22a1931144f12bb38a48fa6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/duckbatch/batch/jev.py`](https://github.com/craigm26/duckbatch/blob/3cc42870039b58c2a22a1931144f12bb38a48fa6/src/duckbatch/batch/jev.py) at the pinned commit. |

## When to use

- See how a cheap decision model holds up as a judge of robotics training runs.
- Mismatch: real hardware; nothing has run on a real Microduck.

## How it works

`src/duckbatch/batch/jev.py` (ported from the maintainer's bounded-answer-lab) posts to `https://api.typesafe.ai/v1/systemone`; `duckbatch rejudge` compares decision-model verdicts with the pre-registered outcomes. Integration evidence: [`src/duckbatch/batch/jev.py`](https://github.com/craigm26/duckbatch/blob/3cc42870039b58c2a22a1931144f12bb38a48fa6/src/duckbatch/batch/jev.py).

## Get started

Sync the environment, probe your GPU, run a menu, then re-judge the records.

```sh
git clone https://github.com/craigm26/duckbatch && cd duckbatch
uv sync --extra sim --extra decide --extra dev
uv run duckbatch probe --envs 256,512,1024
uv run duckbatch rejudge records/b002-student-size-longer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/craigm26/duckbatch/blob/3cc42870039b58c2a22a1931144f12bb38a48fa6/README.md](https://github.com/craigm26/duckbatch/blob/3cc42870039b58c2a22a1931144f12bb38a48fa6/README.md)
- Walker arena: [huggingface.co/spaces/craigm26/microduck-arena](https://huggingface.co/spaces/craigm26/microduck-arena)

## Limits and data handling

Judge calls send run summaries to TypeSafe on your key. Simulation only; results are the maintainer's own runs.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 3cc42870039b](https://github.com/craigm26/duckbatch/tree/3cc42870039b58c2a22a1931144f12bb38a48fa6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
