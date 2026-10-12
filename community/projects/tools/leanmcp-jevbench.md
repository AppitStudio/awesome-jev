# JevBench (Leanmcp)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open framework and dataset for benchmarking typed decision models (Jev 1.13, Liquid D1, djev, Laya, Clef, pplx-decider and others) across science, tool calling, business, selection, ranking and judging clusters, with a paper and results site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Leanmcp/jevbench) |
| Maintainer | [Leanmcp](https://github.com/Leanmcp). Independently curated. |
| Format | Python benchmark framework + Hugging Face dataset |
| Requirements | Python 3.11+, uv; `TYPESAFE_API_KEY` for the Jev endpoint (other endpoints need their own keys). |
| License | [MIT](https://github.com/Leanmcp/jevbench/blob/353b2543c6dedf708bfd4d7e443ef68c6b3c2dbb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Compare Jev with other decision models on public datasets before choosing one.
- Dry-run request building without sending anything.
- Mismatch: Index scores are the maintainers'; some clusters incomplete for some models. Distinct from JevBench (metamorphic) and dhruvmehra/jevbench.

## How it works

`run_eval.py` builds requests per dataset and endpoint (`--endpoint jev` uses TypeSafe) and scoring scripts compute the index with bootstrap intervals. Jev integration: [`jev_bench/workspace/run_eval.py`](https://github.com/Leanmcp/jevbench/blob/353b2543c6dedf708bfd4d7e443ef68c6b3c2dbb/jev_bench/workspace/run_eval.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Leanmcp/jevbench.git
cd jevbench/jev_bench
uv run workspace/run_eval.py --dry-run
```

## Limits and data handling

Live runs send dataset items to each provider (billed). Not run on the review host. Dataset: [Hugging Face](https://huggingface.co/datasets/Leanmcp/jevbench).

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 353b2543c6de](https://github.com/Leanmcp/jevbench/tree/353b2543c6dedf708bfd4d7e443ef68c6b3c2dbb). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
