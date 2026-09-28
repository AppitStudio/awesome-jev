# jevbench (dhruvmehra)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproduce TypeSafe Jev vs LLM/BERT/Laya/NLI text-classification accuracy, calibration, latency, throughput, and cost on public datasets

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dhruvmehra/jevbench) |
| Maintainer | [dhruvmehra](https://github.com/dhruvmehra). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python benchmark harness. |
| Requirements | Python; dataset/provider credentials per README for live arms. |
| License | [MIT](https://github.com/dhruvmehra/jevbench/blob/c983cc4a7dd9fc142ca3b6c7a813cae0e963c902/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md) (`jevbench` CLI) and other benchmark listings. |

## When to use

Use to compare Jev as a text classifier against LLMs, fine-tuned BERT, Laya, and zero-shot NLI on shared public sets. Not a production classifier library.

## How it works

Runs six classifiers over three public datasets and reports side-by-side metrics. Distinct from TokenTrim/jev-agent-failure-benchmark (`jevbench` CLI) and other benches. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/dhruvmehra/jevbench.git
cd jevbench
git checkout c983cc4a7dd9fc142ca3b6c7a813cae0e963c902
```

Pin revision `c983cc4a7dd9fc142ca3b6c7a813cae0e963c902` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit c983cc4](https://github.com/dhruvmehra/jevbench/tree/c983cc4a7dd9fc142ca3b6c7a813cae0e963c902). AI-assisted README and LICENSE inspection; install/live paths not executed.
