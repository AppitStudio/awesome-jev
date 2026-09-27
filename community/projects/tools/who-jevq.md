# jevq

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Jev-based filter sidecar for jq: structure with jq, semantic yes/no with Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/who/jevq) |
| Maintainer | [who](https://github.com/who). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI published as `jevq`. |
| Requirements | Python 3; `TYPESAFE_API_KEY` unless `--pass`. |
| License | [MIT](https://github.com/who/jevq/blob/48024011b5165f22c4566d3d24a2f727632f0369/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to semantically filter JSONL after jq reshaping. Prefer jq alone for exact field predicates.

## How it works

Each stdin JSON value becomes System One state for a Noul question; thresholding stays in the CLI. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
uv tool install jevq
export TYPESAFE_API_KEY=…
jq -c '.[]' tickets.json | jevq "Is this an open refund request?"
```

Pin revision `48024011b5165f22c4566d3d24a2f727632f0369` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Sends each selected JSON payload to TypeSafe. Not a structured-query engine. Live filtering not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 4802401](https://github.com/who/jevq/tree/48024011b5165f22c4566d3d24a2f727632f0369). AI-assisted README and LICENSE inspection; install/live paths not executed.
