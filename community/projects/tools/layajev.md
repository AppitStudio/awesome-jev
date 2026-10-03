# layajev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local Jev-compatible `/v1/systemone` server running verified Laya in-process (Go/ONNX; subset API).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/metalagman/layajev) |
| Maintainer | [metalagman](https://github.com/metalagman). Independently curated. |
| Format | Go · npm (`@metalagman/layajev`, MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/metalagman/layajev/blob/9a5e1c138e8f8e782b7e1e354607362a63fa15b2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Compatibility subset of System One on local Laya—not TypeSafe-hosted Jev. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/metalagman/layajev.git
cd layajev
git checkout 9a5e1c138e8f8e782b7e1e354607362a63fa15b2
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 9a5e1c138e8f](https://github.com/metalagman/layajev/tree/9a5e1c138e8f8e782b7e1e354607362a63fa15b2). AI-assisted README and license inspection; install/live paths not executed.
