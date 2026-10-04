# Skylos

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first PR scanner for dead code, security bugs, and secrets with an optional Jev-only or Jev-plus-LLM review mode for dead-code findings (pinned `jev-1.13.0`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/duriantaco/skylos) |
| Product homepage | [skylos.dev](https://skylos.dev/) |
| Maintainer | [duriantaco](https://github.com/duriantaco). Independently curated. |
| Format | CLI / PR scanner; Jev mode is optional and experimental |
| Requirements | Python and `pip install skylos`. Normal scans need no Jev key; the Jev review/runner needs an explicit flag and `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/duriantaco/skylos/blob/14dfba20247ce1ac0eccf4eeb7407319496dc4b6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Reduce false positives in dead-code reports by letting Jev judge each static finding before cleanup.
- Run a local PR gate for security bugs and secrets, with Jev added only where you opt in.
- Mismatch: if you want no remote calls at all, keep the default static-only mode.

## How it works

Skylos finds candidates statically; the optional review path ([dead-code review docs](https://github.com/duriantaco/skylos/blob/main/docs/dead-code-review.md)) sends fixture/source context to TypeSafe for typed Jev judgments, alone or combined with an LLM. Upstream documents bounded, resumable runs and records request latency.

## Get started

Install and run a static scan; enable Jev review only with a key and the documented flag:

```sh
pip install skylos
skylos .
# optional: skylos agent verify [PATH] with the Jev-only or Jev-plus-LLM mode (see docs/dead-code-review.md)
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream [Jev benchmark write-up](https://github.com/duriantaco/skylos/blob/main/benchmark_jev.md) and dead-code benchmark guide (maintainer-reported results, not reproduced here).

## Limits and data handling

Jev mode sends code context to TypeSafe and is paid per request; upstream labels the runner experimental. The scanner's other features do not depend on Jev.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 14dfba20247c](https://github.com/duriantaco/skylos/tree/14dfba20247ce1ac0eccf4eeb7407319496dc4b6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
