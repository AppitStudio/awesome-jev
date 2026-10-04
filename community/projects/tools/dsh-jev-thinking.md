# dsh-jev-thinking

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin: TypeSafe Jev Choice sets reasoningEffort from the route's offered levels (one question per prompt; MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kyan001/DSH-Jev-Thinking) |
| Maintainer | [kyan001](https://github.com/kyan001). Independently curated. |
| Format | DeepSeek Harness plugin: Jev picks reasoningEffort (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/kyan001/DSH-Jev-Thinking/blob/1f015ec76586a40c5bb1a3217b1e1e70a0da9ad3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from Jeffort/jev-effort (Claude-focused)—DSH plugin that reads route-offered levels. Sends previous assistant turn context to TypeSafe. Live install/inference not run on the review host. |

## When to use

Use in DeepSeek Harness to pick reasoning effort per prompt. Prefer Jeffort/jev-effort for Claude Code effort control.

## How it works

One Choice question per user prompt using the route's effort options; writes reasoningEffort or falls back on timeout/error/missing key.

## Get started

```sh
git clone https://github.com/kyan001/DSH-Jev-Thinking.git
cd DSH-Jev-Thinking
git checkout 1f015ec76586a40c5bb1a3217b1e1e70a0da9ad3
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 1f015ec76586](https://github.com/kyan001/DSH-Jev-Thinking/tree/1f015ec76586a40c5bb1a3217b1e1e70a0da9ad3). AI-assisted README and license inspection; install/live paths not executed.
