# Misogi

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Second-opinion sidecar for Claude Code/Codex/Kimi: TypeSafe Jev judges each "done" claim before you accept it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nadsous/Misogi) |
| Maintainer | [nadsous](https://github.com/nadsous). Independently curated. |
| Format | TypeScript · coding-agent sidecar (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/nadsous/Misogi/blob/fc7e1e5806fbefc2e22a4846049a286b4fece13b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/nadsous/Misogi.git
cd Misogi
git checkout fc7e1e5806fbefc2e22a4846049a286b4fece13b
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit fc7e1e5806fb](https://github.com/nadsous/Misogi/tree/fc7e1e5806fbefc2e22a4846049a286b4fece13b). AI-assisted README and license inspection; install/live paths not executed.
