# nf-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Nextflow plugin that exposes TypeSafe System One (Jev) noul/choice/score judgments as ordinary Nextflow functions so pipelines can branch on calibrated probabilities. Early beta from the `nextflow-io` org.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nextflow-io/nf-jev) |
| Maintainer | [nextflow-io](https://github.com/nextflow-io). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Nextflow plugin **nf-jev 0.1.0** (Groovy; Gradle/`nextflow-plugin` build). |
| Requirements | Nextflow **25.10.0+** (plugin metadata); `TYPESAFE_API_KEY` or `jev.apiKey` in config for live calls. |
| License | [Apache-2.0](https://github.com/nextflow-io/nf-jev/blob/23cf08407dcb4be931df9b63e7b03abd54bdad39/COPYING). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation beyond public-source inspection. Listing is not an endorsement. Source and SPEC inspected; Gradle unit tests not run on the review host (no full Nextflow plugin toolchain). Live TypeSafe pipeline runs were not executed. Beta: APIs may change without a deprecation cycle. |

## When to use

Use it when a Nextflow pipeline needs typed yes/no, choice, or score gates over structured state without calling a text LLM. Prefer [daf-jev](daf-jev.md) or [Advocaat](advocaat.md) for Python/TypeScript batching outside Nextflow. Pin a plugin version; expect revisits while beta.

## How it works

[`JevExtension.groovy`](https://github.com/nextflow-io/nf-jev/blob/23cf08407dcb4be931df9b63e7b03abd54bdad39/src/main/groovy/nextflowio/plugin/JevExtension.groovy) registers `noul`, `choice`, `score`, and batched `jev` functions. [`JevClient.groovy`](https://github.com/nextflow-io/nf-jev/blob/23cf08407dcb4be931df9b63e7b03abd54bdad39/src/main/groovy/nextflowio/plugin/JevClient.groovy) talks to TypeSafe; [`JevCache.groovy`](https://github.com/nextflow-io/nf-jev/blob/23cf08407dcb4be931df9b63e7b03abd54bdad39/src/main/groovy/nextflowio/plugin/JevCache.groovy) caches answers. Pipelines gate on returned probabilities with ordinary Nextflow operators. See upstream [`SPEC.md`](https://github.com/nextflow-io/nf-jev/blob/23cf08407dcb4be931df9b63e7b03abd54bdad39/SPEC.md).

## Get started

```sh
git clone https://github.com/nextflow-io/nf-jev.git
cd nf-jev
git checkout 23cf08407dcb4be931df9b63e7b03abd54bdad39
# In a pipeline nextflow.config:
# plugins { id 'nf-jev@0.1.0' }
# export TYPESAFE_API_KEY=…
```

Follow upstream README examples under `examples/guardrail`, `examples/label-samples`, and `examples/route`. This listing did not run Nextflow or TypeSafe.

## Examples and demos

- `examples/guardrail`, `examples/label-samples`, `examples/route` with README notes.
- Unit tests under `src/test/groovy/nextflowio/plugin/` (WireMock-backed client tests present; not executed here).
- GitHub Actions `build` workflow badge on the upstream README.

## Limits and data handling

Pipeline state used in questions leaves the host on live TypeSafe calls. Beta: function names, answer shapes, and the `jev` config scope may change. Do not treat probabilities as audited scientific claims without your own evaluation. Pin versions in production pipelines.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 23cf084](https://github.com/nextflow-io/nf-jev/tree/23cf08407dcb4be931df9b63e7b03abd54bdad39): **0.1.0**, Apache-2.0. AI-assisted source review of README, SPEC, COPYING, and Groovy plugin sources. Offline Gradle/`nextflow` test suite and live TypeSafe examples were not run on the review host.

Related: [daf-jev](daf-jev.md), [Advocaat](advocaat.md), [n8n-nodes-typesafe](n8n-nodes-typesafe.md), [semgate](semgate.md).
