# Open Medical Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jev-class medical judgments from frozen open models—no fine-tuning—with routing gates and published exam comparisons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FeiLiuEM/open-medical-jev) |
| Maintainer | [FeiLiuEM](https://github.com/FeiLiuEM). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Research protocol + Python recipes for dual frozen readers and routing. |
| Requirements | Python; local GGUF/open-model inference resources per upstream; optional hosted Jev for comparisons. |
| License | [MIT](https://github.com/FeiLiuEM/open-medical-jev/blob/81c6f866e2f635dccbe5a6d3065306b49ae76bbc/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent research; not official Jev weights. |

## When to use

Use when studying open-model System One–style medical judgments without training. Prefer hosted TypeSafe Jev for production medical decisions.

## How it works

Two frozen open readers answer yes/no per option; a fit-free router combines agreement into confidence, auto-release, and conformal candidate sets. Independent of official Jev weights. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/FeiLiuEM/open-medical-jev.git
cd open-medical-jev
git checkout 81c6f866e2f635dccbe5a6d3065306b49ae76bbc
# follow upstream README for install/run; configure local models as documented
```

Pin revision `81c6f866e2f635dccbe5a6d3065306b49ae76bbc` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent research; not official Jev weights. Benchmark tables are upstream-reported. Live inference/provider paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 81c6f86](https://github.com/FeiLiuEM/open-medical-jev/tree/81c6f866e2f635dccbe5a6d3065306b49ae76bbc). AI-assisted README and LICENSE inspection; install/live paths not executed.
