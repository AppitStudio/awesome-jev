# nifi-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Apache NiFi RouteWithJev processor: semantic yes/no routing via TypeSafe Jev with yes/no/review/failure relations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/nifi-jev) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Java · Apache NiFi processor (MIT) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`MIT`](https://github.com/gbesse/nifi-jev/blob/f17cdb25f2983cfebbfb4727976574173776d3d3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Apache NiFi RouteWithJev processor: semantic yes/no routing via TypeSafe Jev with yes/no/review/failure relations. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/gbesse/nifi-jev.git
cd nifi-jev
git checkout f17cdb25f2983cfebbfb4727976574173776d3d3
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: posts to api.typesafe.ai/v1/systemone; relations yes/no/review/failure. ([upstream evidence](https://github.com/gbesse/nifi-jev/blob/f17cdb25f2983cfebbfb4727976574173776d3d3/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit f17cdb25f298](https://github.com/gbesse/nifi-jev/tree/f17cdb25f2983cfebbfb4727976574173776d3d3). AI-assisted README and license inspection; install/live paths not executed.
