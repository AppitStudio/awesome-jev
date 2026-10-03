# laya-php

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PHP/Laravel SDK for local Laya typed Choice/Score/Noul decisions (Jev-compatible `/v1/systemone` alternative; self-hosted).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marcreichel/laya-php) |
| Maintainer | [marcreichel](https://github.com/marcreichel). Independently curated. |
| Format | PHP · Composer (`marcreichel/laya-php`, Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/marcreichel/laya-php/blob/6642029c2692bc372affc98e26f8f4bbd7e528e0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Local Laya alternative—not TypeSafe-hosted Jev. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/marcreichel/laya-php.git
cd laya-php
git checkout 6642029c2692bc372affc98e26f8f4bbd7e528e0
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 6642029c2692](https://github.com/marcreichel/laya-php/tree/6642029c2692bc372affc98e26f8f4bbd7e528e0). AI-assisted README and license inspection; install/live paths not executed.
