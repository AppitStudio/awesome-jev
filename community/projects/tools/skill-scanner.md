# skill-scanner

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Offline static analysis for Agent Skills (prompt-injection, exfil, hidden text) before install; optional TypeSafe Jev second opinion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FrancoisChastel/skill-scanner) |
| Maintainer | [FrancoisChastel](https://github.com/FrancoisChastel). Independently curated. |
| Format | TypeScript · npm (`@french-castle/skill-scanner`, MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/FrancoisChastel/skill-scanner/blob/8965ecd362f532219aaf4b80d85e1959cee8c238/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/FrancoisChastel/skill-scanner.git
cd skill-scanner
git checkout 8965ecd362f532219aaf4b80d85e1959cee8c238
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 8965ecd362f5](https://github.com/FrancoisChastel/skill-scanner/tree/8965ecd362f532219aaf4b80d85e1959cee8c238). AI-assisted README and license inspection; install/live paths not executed.
