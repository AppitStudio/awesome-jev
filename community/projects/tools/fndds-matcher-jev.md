# fndds-matcher-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Match food descriptions to USDA FNDDS codes via hybrid retrieval plus TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/braydenabo/fndds-matcher-jev) |
| Maintainer | [braydenabo](https://github.com/braydenabo). Independently curated. |
| Format | Python · matcher (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/braydenabo/fndds-matcher-jev/blob/292dd935519f7a8d5d946a20d5f55a97ee25a084/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/braydenabo/fndds-matcher-jev.git
cd fndds-matcher-jev
git checkout 292dd935519f7a8d5d946a20d5f55a97ee25a084
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 292dd935519f](https://github.com/braydenabo/fndds-matcher-jev/tree/292dd935519f7a8d5d946a20d5f55a97ee25a084). AI-assisted README and license inspection; install/live paths not executed.
