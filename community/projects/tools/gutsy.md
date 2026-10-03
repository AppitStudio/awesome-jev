# gutsy

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local calibrated decision model (gutsy-0.8b) with Jev-style /v1/systemone and Decisions APIs on CPU via llama.cpp (independent of hosted Jev).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kouhxp/gutsy) |
| Maintainer | [kouhxp](https://github.com/kouhxp). Independently curated. |
| Format | Python · local decision server + HF GGUF (Apache-2.0) |
| Requirements | See upstream README; provider keys when using live hosted paths. |
| License | [`Apache-2.0`](https://github.com/kouhxp/gutsy/blob/dde8b927165295bdbd65ce3519d5d7fea8dfce1a/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Independent of hosted TypeSafe Jev. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Local calibrated decision model (gutsy-0.8b) with Jev-style /v1/systemone and Decisions APIs on CPU via llama.cpp (independent of hosted Jev). This is independent research, not an official TypeSafe release. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/kouhxp/gutsy.git
cd gutsy
git checkout dde8b927165295bdbd65ce3519d5d7fea8dfce1a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: Jev-style Decisions format; POST /v1/systemone; HF kouhxp/gutsy weights. ([upstream evidence](https://github.com/kouhxp/gutsy/blob/dde8b927165295bdbd65ce3519d5d7fea8dfce1a/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit dde8b9271652](https://github.com/kouhxp/gutsy/tree/dde8b927165295bdbd65ce3519d5d7fea8dfce1a). AI-assisted README and license inspection; install/live paths not executed.
