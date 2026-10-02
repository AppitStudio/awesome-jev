# Kestra TypeSafe plugin

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Official-style Kestra plugin that runs TypeSafe System One typed evaluations inside orchestrated workflows.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kestra-io/plugin-typesafe) |
| Maintainer | [kestra-io](https://github.com/kestra-io). Independently curated. |
| Format | Java · Kestra plugin (Apache-2.0) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`Apache-2.0`](https://github.com/kestra-io/plugin-typesafe/blob/23cee938c53602acd975c39c4b095e18ac97e217/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Official-style Kestra plugin that runs TypeSafe System One typed evaluations inside orchestrated workflows. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/kestra-io/plugin-typesafe.git
cd plugin-typesafe
git checkout 23cee938c53602acd975c39c4b095e18ac97e217
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README Why section: TypeSafe evaluation steps via /v1 systemone-style judgments in Kestra flows. ([upstream evidence](https://github.com/kestra-io/plugin-typesafe/blob/23cee938c53602acd975c39c4b095e18ac97e217/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 23cee938c536](https://github.com/kestra-io/plugin-typesafe/tree/23cee938c53602acd975c39c4b095e18ac97e217). AI-assisted README and license inspection; install/live paths not executed.
