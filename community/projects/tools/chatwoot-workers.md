# chatwoot-workers

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Cloudflare Workers for Chatwoot: Discord relay plus ticket router that triages new tickets with TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Phala-Network/chatwoot-workers) |
| Maintainer | [Phala-Network](https://github.com/Phala-Network). Independently curated. |
| Format | TypeScript · Cloudflare Workers monorepo (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [`MIT`](https://github.com/Phala-Network/chatwoot-workers/blob/7f9318cca59f870e8c04a32545992974d6b5f2c2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/Phala-Network/chatwoot-workers.git
cd chatwoot-workers
git checkout 7f9318cca59f870e8c04a32545992974d6b5f2c2
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 7f9318cca59f](https://github.com/Phala-Network/chatwoot-workers/tree/7f9318cca59f870e8c04a32545992974d6b5f2c2). AI-assisted README and license inspection; install/live paths not executed.
