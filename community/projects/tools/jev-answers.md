# jev-answers

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server + CLI: send files and typed questions to TypeSafe Jev and get the raw answer back (one session folder per request).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AmooEbrahim/jev-answers) |
| Maintainer | [AmooEbrahim](https://github.com/AmooEbrahim). Independently curated. |
| Format | TypeScript · MCP server + CLI (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/AmooEbrahim/jev-answers/blob/48c60e799d23506a9ce5fdd60c8b8fa0152ca94d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/AmooEbrahim/jev-answers.git
cd jev-answers
git checkout 48c60e799d23506a9ce5fdd60c8b8fa0152ca94d
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 48c60e799d23](https://github.com/AmooEbrahim/jev-answers/tree/48c60e799d23506a9ce5fdd60c8b8fa0152ca94d). AI-assisted README and license inspection; install/live paths not executed.
