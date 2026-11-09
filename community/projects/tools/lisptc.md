# lisptc (Lisp runtime for self-modifying AI agents with a Jev System One verdict model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Lisp interpreter meant as the deterministic brain of a neuro-symbolic agent; its models package wires `@typesafe-ai/sdk` so semantic checks get typed Jev verdicts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/1hachem/lisptc) |
| Maintainer | [1hachem](https://github.com/1hachem). Independently curated. |
| Format | TypeScript monorepo (MIT) |
| Requirements | Node/pnpm, a chat model provider and an OpenRouter or TypeSafe key for Jev. |
| License | [MIT](https://github.com/1hachem/lisptc/blob/ff0bbfe2b5a4a7a923d7d5c582ee9abdbb6b0377/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/models/src/system-one.ts`](https://github.com/1hachem/lisptc/blob/ff0bbfe2b5a4a7a923d7d5c582ee9abdbb6b0377/packages/models/src/system-one.ts) at the pinned commit. |

## When to use

- Combine an LLM REPL with typed Jev verdicts.
- Study a neuro-symbolic agent architecture.
- Mismatch: research-grade runtime, not a hosted product.

## How it works

`system-one.ts` builds a `TypeSafeClient` (`typesafe/jev-1.14` via OpenRouter's System One endpoint) and `providers.ts` exports it as `jev`; `packages/semantic` uses it for verdicts. Integration evidence: [`packages/models/src/system-one.ts`](https://github.com/1hachem/lisptc/blob/ff0bbfe2b5a4a7a923d7d5c582ee9abdbb6b0377/packages/models/src/system-one.ts).

## Get started

Clone the repo, install dependencies and set the provider keys described in `packages/models/AGENTS.md`.

```sh
git clone https://github.com/1hachem/lisptc.git && cd lisptc
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [d4shi.com/blog/lisptc/](https://d4shi.com/blog/lisptc/)

## Limits and data handling

Semantic-check inputs are sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit ff0bbfe2b5a4](https://github.com/1hachem/lisptc/tree/ff0bbfe2b5a4a7a923d7d5c582ee9abdbb6b0377). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
