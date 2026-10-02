# pi-verdict

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Minimal Pi permission gate (allow/ask/deny) with an optional TypeSafe Jev decisions-model classifier adapter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jesset/pi-verdict) |
| Maintainer | [jesset](https://github.com/jesset). Independently curated. |
| Format | TypeScript · Pi extension (`pi-verdict`, MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/jesset/pi-verdict/blob/34d1ea0de26b85db4fbbe1add8150aeb6b8749cf/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Jev classifier adapter is optional; rule floor remains primary. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/jesset/pi-verdict.git
cd pi-verdict
git checkout 34d1ea0de26b85db4fbbe1add8150aeb6b8749cf
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 34d1ea0de26b](https://github.com/jesset/pi-verdict/tree/34d1ea0de26b85db4fbbe1add8150aeb6b8749cf). AI-assisted README and license inspection; install/live paths not executed.
