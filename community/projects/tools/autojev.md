# AutoJev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Desktop local model-router gateway for Codex/Claude Code/Hermes; optional OpenRouter Jev decision routing with local fallback (AGPL-3.0-only).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thinkany-ai/autojev) |
| Maintainer | [thinkany-ai](https://github.com/thinkany-ai). Independently curated. |
| Format | Tauri/React/Rust · desktop local gateway (AGPL-3.0-only) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [AGPL-3.0-only](https://github.com/thinkany-ai/autojev/blob/64f33ec068e644b62a7c36b1ce81564c09a5121a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. LICENSE confirms AGPL-3.0-only (GitHub SPDX NOASSERTION). Commercial license available from ThinkAny per LICENSE. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/thinkany-ai/autojev.git
cd autojev
git checkout 64f33ec068e644b62a7c36b1ce81564c09a5121a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 64f33ec068e6](https://github.com/thinkany-ai/autojev/tree/64f33ec068e644b62a7c36b1ce81564c09a5121a). AI-assisted README and license inspection; install/live paths not executed.
