# olla-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ollama-style local CLI/server for Hugging Face System One models behind the Jev /v1/systemone API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nvkudva/olla-jev) |
| Maintainer | [nvkudva](https://github.com/nvkudva). Independently curated. |
| Format | Python · CLI/server (Apache-2.0) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/nvkudva/olla-jev/blob/56d00c2040c7f16f524176f6cd6d981cc5cf4181/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/nvkudva/olla-jev.git
cd olla-jev
git checkout 56d00c2040c7f16f524176f6cd6d981cc5cf4181
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 56d00c2040c7](https://github.com/nvkudva/olla-jev/tree/56d00c2040c7f16f524176f6cd6d981cc5cf4181). AI-assisted README and license inspection; install/live paths not executed.
