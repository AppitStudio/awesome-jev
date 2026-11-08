# Skybridge (TypeScript MCP Apps framework with a TypeSafe Jev eval judge example)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Full-stack TypeScript framework for MCP Apps and ChatGPT Apps; its evals docs and example grade conversations with TypeSafe Jev via `toPassJudgment` and a custom judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alpic-ai/skybridge) |
| Maintainer | [alpic-ai](https://github.com/alpic-ai). Independently curated. |
| Format | TypeScript framework + Vitest evals (MIT) |
| Requirements | Node, the example's dependencies and a `TYPESAFE_API_KEY` (the Jev scenario skips without it). |
| License | [MIT](https://github.com/alpic-ai/skybridge/blob/9afa5fa52522923022de30f27a4b785df68104c3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/evals/evals/typesafe-judge.ts`](https://github.com/alpic-ai/skybridge/blob/9afa5fa52522923022de30f27a4b785df68104c3/examples/evals/evals/typesafe-judge.ts) at the pinned commit. |

## When to use

- Grade MCP App conversations with a typed Jev judgment.
- Compare Jev and LLM judges on the same answer.
- Mismatch: the Jev judge is an example, not core runtime.

## How it works

`typesafe-judge.ts` uses `@typesafe-ai/sdk` (`TypeSafeClient`, `noul`) to answer a typed question about the conversation; `judgment.eval.ts` runs it only when a key is present. Integration evidence: [`examples/evals/evals/typesafe-judge.ts`](https://github.com/alpic-ai/skybridge/blob/9afa5fa52522923022de30f27a4b785df68104c3/examples/evals/evals/typesafe-judge.ts).

## Get started

Open `examples/evals`, install dependencies, set `TYPESAFE_API_KEY`, and run the eval suite.

```sh
git clone https://github.com/alpic-ai/skybridge.git && cd skybridge
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evals docs: [github.com/alpic-ai/skybridge/blob/9afa5fa52522923022de30f27a4b785df68104c3/docs/test/evals.mdx](https://github.com/alpic-ai/skybridge/blob/9afa5fa52522923022de30f27a4b785df68104c3/docs/test/evals.mdx)

## Limits and data handling

Conversation transcripts are sent to TypeSafe when the Jev eval runs.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 9afa5fa52522](https://github.com/alpic-ai/skybridge/tree/9afa5fa52522923022de30f27a4b785df68104c3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
