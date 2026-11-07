# jev-boe-demo (Spain BOE gazette triage demo powered by TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Daily demo that categorizes and scores Spain's official gazette (BOE) dispositions for citizens using TypeSafe Jev via `@typesafe-ai/sdk`, with an Astro front-end and recorded pipeline/web demos.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Tatuck/jev-boe-demo) |
| Maintainer | [Tatuck](https://github.com/Tatuck). Independently curated. |
| Format | Astro site + TypeScript pipeline using @typesafe-ai/sdk (no SPDX license file on the reviewed commit) |
| Requirements | Node 20+, pnpm, and a TypeSafe API key for live pipeline runs. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/questions.ts`](https://github.com/Tatuck/jev-boe-demo/blob/b575c63f61b91b2a21faf8c8d01ff310123b0743/pipeline/questions.ts) at the pinned commit. |

## When to use

- See Jev triage public-law gazette items into citizen-facing categories.
- Replay recorded demos without spending key quota.
- Mismatch: no OSI license on the reviewed commit; Spanish BOE-focused demo.

## How it works

`pipeline/questions.ts` builds typed questions with `@typesafe-ai/sdk` (`choice`/`noul`/`score`); the pipeline runs with `TYPESAFE_API_KEY` and default model `jev-latest`. Integration evidence: [`pipeline/questions.ts`](https://github.com/Tatuck/jev-boe-demo/blob/b575c63f61b91b2a21faf8c8d01ff310123b0743/pipeline/questions.ts).

## Get started

Clone, copy `.env.example`, set TYPESAFE_API_KEY, and run `pnpm pipeline` or the Astro site per README.

```sh
git clone https://github.com/Tatuck/jev-boe-demo.git && cd jev-boe-demo
export TYPESAFE_API_KEY=...
pnpm i && pnpm pipeline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Tatuck/jev-boe-demo/blob/b575c63f61b91b2a21faf8c8d01ff310123b0743/README.md](https://github.com/Tatuck/jev-boe-demo/blob/b575c63f61b91b2a21faf8c8d01ff310123b0743/README.md)

## Limits and data handling

No open-source license file on the reviewed commit—do not treat as OSI OSS. BOE text is sent to TypeSafe on your key during live runs.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit b575c63f61b9](https://github.com/Tatuck/jev-boe-demo/tree/b575c63f61b91b2a21faf8c8d01ff310123b0743). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
