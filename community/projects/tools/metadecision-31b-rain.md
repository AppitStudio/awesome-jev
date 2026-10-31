# MetaDecision-31B-Rain (self-hosted /v1/systemone decision service built for JevBench)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted decision service that serves `POST /v1/systemone` for the unchanged `typesafe` adapter of the official JevBench harness, using the pinned MeTask-Rain Gemma-4-31B LoRA weights. The entry changes only how the service uses them: a drafting pass for a share of decisions with a 9 s deadline, order-reversed re-reads for close choices, per-type post-calibration and a cost fuse.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chenyuwang166-oss/MetaDecision-31B-Rain) |
| Maintainer | [chenyuwang166-oss](https://github.com/chenyuwang166-oss). Independently curated. |
| Format | Python server + benchmark client |
| Requirements | A GPU able to serve Gemma-4-31B W4A16; the JevBench harness for evaluation. |
| License | [MIT](https://github.com/chenyuwang166-oss/MetaDecision-31B-Rain/blob/6b8ed2d0f20ef4369cd9ecd553c65ff65d4bf407/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.py`](https://github.com/chenyuwang166-oss/MetaDecision-31B-Rain/blob/6b8ed2d0f20ef4369cd9ecd553c65ff65d4bf407/server.py) at the pinned commit. |

## When to use

- Study how serving-time policy (drafting, re-reads, calibration) changes JevBench results for a fixed model.
- Mismatch: an evaluation entry, not a general product.

## How it works

`server.py` implements the System One wire format and `bench.py` is a sequential, model-free HTTP client that validates the `/v1/systemone` route before benchmarking. Integration evidence: [`server.py`](https://github.com/chenyuwang166-oss/MetaDecision-31B-Rain/blob/6b8ed2d0f20ef4369cd9ecd553c65ff65d4bf407/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/fstandhartinger/jevbench.git jevbench
# start server.py with the pinned model folder, then point the typesafe adapter at it
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pinned weights: [huggingface.co/MeTask-Rain/metask-jev-rain-31B-trained](https://huggingface.co/MeTask-Rain/metask-jev-rain-31B-trained)

## Limits and data handling

Runs locally. Results and cost figures are the maintainers'. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 6b8ed2d0f20e](https://github.com/chenyuwang166-oss/MetaDecision-31B-Rain/tree/6b8ed2d0f20ef4369cd9ecd553c65ff65d4bf407). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
