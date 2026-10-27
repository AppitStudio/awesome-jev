# decision-model-bench (Jev vs. OpenAI Decisions, ai_decide and decider-2b on support chats)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark comparing typed decision models on the same customer-support chats (ABCD dataset) with the same questions and paired significance tests: hosted Jev, OpenAI's Decisions API and Databricks' ai_decide, plus open decider-2b out of the box, with retrieved examples and fine-tuned with QLoRA, across intent triage and next-action jobs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/manz49b/decision-model-bench) |
| Maintainer | [manz49b](https://github.com/manz49b). Independently curated. |
| Format | Python benchmark with results |
| Requirements | uv; a TypeSafe API key plus the other providers' keys, and a CUDA GPU for the open-model runs. |
| License | [MIT](https://github.com/manz49b/decision-model-bench/blob/cbdaf036f1364c3ae3d577116adae21311ecbc8d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/bench/engines/jev.py`](https://github.com/manz49b/decision-model-bench/blob/cbdaf036f1364c3ae3d577116adae21311ecbc8d/src/bench/engines/jev.py) at the pinned commit. |

## When to use

- Choose between hosted decision APIs and a fine-tuned open model for support triage.
- See how much a few retrieved examples help each engine.
- Mismatch: one dataset; numbers are the author's.

## How it works

`src/bench/engines/jev.py` posts each chat and question to `https://api.typesafe.ai/v1/systemone`; the other engines share the same interface. Integration evidence: [`src/bench/engines/jev.py`](https://github.com/manz49b/decision-model-bench/blob/cbdaf036f1364c3ae3d577116adae21311ecbc8d/src/bench/engines/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/manz49b/decision-model-bench && cd decision-model-bench
uv sync --group dev
cp .env.example .env   # add keys; see the README for data download
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/manz49b/decision-model-bench#readme](https://github.com/manz49b/decision-model-bench#readme)

## Limits and data handling

Benchmark chats go to each hosted provider when rerun. Results are the author's, not verified here.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit cbdaf036f136](https://github.com/manz49b/decision-model-bench/tree/cbdaf036f1364c3ae3d577116adae21311ecbc8d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
