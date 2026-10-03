# Leash

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered coding-agent guardrail that judges each turn against un-lintable project rules with a one-way accepted-debt ratchet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CMaintz/leash) |
| Maintainer | [CMaintz](https://github.com/CMaintz). Independently curated. |
| Format | TypeScript · CLI/npm (`leash`, MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/CMaintz/leash/blob/e2ec093bdb4df1afd6580304f1306b54868bd02b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/CMaintz/leash.git
cd leash
git checkout e2ec093bdb4df1afd6580304f1306b54868bd02b
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit e2ec093bdb4d](https://github.com/CMaintz/leash/tree/e2ec093bdb4df1afd6580304f1306b54868bd02b). AI-assisted README and license inspection; install/live paths not executed.
