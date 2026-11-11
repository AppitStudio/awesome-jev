# Club CMP 170HX (recipes and benchmarks, including a Jev-compatible endpoint on a CMP 170HX)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Community-tested recipes, diagnostics and benchmarks for AI workloads on NVIDIA CMP 170HX cards, including a run that serves Qwen3.8-27B W4A16 as a no-train Jev-compatible `/v1/systemone` endpoint on one card, with calibration notes and production receipts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PixelML/club-170hx) |
| Maintainer | [PixelML](https://github.com/PixelML). Independently curated. |
| Format | Recipes, notebooks and benchmark results (Apache-2.0) |
| Requirements | An NVIDIA CMP 170HX card (unlock and cooling notes in the repo) and the vLLM sm80 setup described in the result README. |
| License | [Apache-2.0](https://github.com/PixelML/club-170hx/blob/c375fe520147635ec2f81f3535095e0aa6acf24f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md`](https://github.com/PixelML/club-170hx/blob/c375fe520147635ec2f81f3535095e0aa6acf24f/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md) at the pinned commit. |

## When to use

- Run a self-hosted Jev-compatible decision endpoint on low-cost SM80 hardware.
- Check calibration and latency numbers before trusting a local decision endpoint.
- Mismatch: hobbyist mining-card hardware; results are the community's own; Jev itself is not called.

## How it works

The 2026-09-20 result serves a stock W4A16 checkpoint read-only behind a `/v1/systemone` endpoint and reads exact per-option probabilities without generating tokens; the README and receipts report latency, a 19,045-annotation production pilot, and a Laya-vs-Jev agreement check. Integration evidence: [`results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md`](https://github.com/PixelML/club-170hx/blob/c375fe520147635ec2f81f3535095e0aa6acf24f/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md).

## Get started

Read the result README and its harness folder before reproducing on your own card.

```sh
git clone https://github.com/PixelML/club-170hx.git && cd club-170hx
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Result write-up: [github.com/PixelML/club-170hx/blob/c375fe520147635ec2f81f3535095e0aa6acf24f/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md](https://github.com/PixelML/club-170hx/blob/c375fe520147635ec2f81f3535095e0aa6acf24f/results/2026-09-20-qwen3.8-27b-w4a16-jev-1card-vllm/README.md)

## Limits and data handling

Self-hosted; requests stay on your card unless you run the comparison against hosted Jev.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit c375fe520147](https://github.com/PixelML/club-170hx/tree/c375fe520147635ec2f81f3535095e0aa6acf24f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
