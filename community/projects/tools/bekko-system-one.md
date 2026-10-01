# bekko-system-one

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small System One decision models (17M–400M) for Yes/No, Choice, and Score (independent open weights).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hotchpotch/bekko-system-one) |
| Maintainer | [hotchpotch](https://github.com/hotchpotch). Independently curated. |
| Format | Python · local models (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/hotchpotch/bekko-system-one/blob/0fccbb8568b67d47745d820319fe9a4a04e7fa95/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/hotchpotch/bekko-system-one.git
cd bekko-system-one
git checkout 0fccbb8568b67d47745d820319fe9a4a04e7fa95
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 0fccbb8568b6](https://github.com/hotchpotch/bekko-system-one/tree/0fccbb8568b67d47745d820319fe9a4a04e7fa95). AI-assisted README and license inspection; install/live paths not executed.
