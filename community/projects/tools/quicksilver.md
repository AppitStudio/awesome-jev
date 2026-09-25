# Quicksilver

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill that hands bulk judgment and shortlist calls to TypeSafe Jev so Claude spends tokens on harder reasoning.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/UditAkhourii/quicksilver) |
| Maintainer | [UditAkhourii](https://github.com/UditAkhourii). Independently curated. |
| Format | Claude Code skill + plugin; zero npm runtime deps; Node 18+. |
| Requirements | Node 18+; `JEV_API_KEY` or `TYPESAFE_API_KEY` (installer can prompt once). |
| License | [MIT](https://github.com/UditAkhourii/quicksilver/blob/5d6fe5cd4f9d9a9d086a81c797e59b77c0724043/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream token-saving benchmarks are author-reported and were not re-run on the review host. Live Claude Code / TypeSafe paths not executed. |

## When to use

Use when Claude Code sessions spend many tokens **reading to decide a little** (log triage, ticket routing, codebase discovery shortlists). Prefer plain Claude tooling when the task is generative writing rather than typed judgment.

## How it works

The skill routes bulk yes/no, label, and score questions to TypeSafe Jev in parallel and returns shortlists plus confidence for Claude to continue with.

## Get started

```sh
npx github:UditAkhourii/quicksilver
# or pin:
git clone https://github.com/UditAkhourii/quicksilver.git
cd quicksilver
git checkout 5d6fe5cd4f9d9a9d086a81c797e59b77c0724043
```

## Examples and demos

- Upstream README benchmark table and `bench/` materials (author-reported).
- Plugin install via `/plugin marketplace add UditAkhourii/quicksilver`.

## Limits and data handling

Candidate text and labels go to TypeSafe for Jev. Benchmark claims are upstream-reported. Distinct from other projects named Quicksilver.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 5d6fe5c](https://github.com/UditAkhourii/quicksilver/tree/5d6fe5cd4f9d9a9d086a81c797e59b77c0724043). AI-assisted README and LICENSE inspection; live install/Claude Code paths not run.
