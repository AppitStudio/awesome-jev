# SOLO

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

SOLO (System One Layout Optimizer) runs a natural-language decision over every record of a table and reorders rows and fields so a prefix-caching decision-model backend reuses more input computation, returning decisions in the original row order.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0814wdwd/solo_jev) |
| Maintainer | [0814wdwd](https://github.com/0814wdwd). Independently curated. |
| Format | Python package with a vLLM backend adapter |
| Requirements | Python 3.10+; a prefix-caching backend such as vLLM serving an open Jev-style decision model (README uses AutoTrust JEV-9B) or your own backend; GPU for the included demos. |
| License | [MIT](https://github.com/0814wdwd/solo_jev/blob/c5bed0511f3c90a83774f1a01e37da6b0b60fa22/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Run per-row semantic judgements over large relational tables with repeated context.
- Mismatch: targets self-hosted open decision models rather than the hosted TypeSafe API; throughput figures are the maintainer's synthetic benchmarks.

## How it works

SOLO puts repeated context first and groups correlated fields so consecutive requests share long prefixes; every request still carries the complete record. (Summarized from the upstream [README](https://github.com/0814wdwd/solo_jev/blob/c5bed0511f3c90a83774f1a01e37da6b0b60fa22/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install from a source checkout with `pip install ".[pandas,hub]"` and follow the quickstart.

## Limits and data handling

Data stays on the backend you deploy. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit c5bed0511f3c](https://github.com/0814wdwd/solo_jev/tree/c5bed0511f3c90a83774f1a01e37da6b0b60fa22). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
