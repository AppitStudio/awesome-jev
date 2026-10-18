# Competitor Monitor with Jev (Mastra template)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Official Mastra template that watches competitor pricing, changelog, and docs pages, diffs them against saved history, has TypeSafe Jev classify each change, and applies a policy to ignore, record, request review, or alert, with an LLM explaining results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mastra-ai/template-competitor-monitor-jev) |
| Maintainer | [mastra-ai](https://github.com/mastra-ai). Independently curated. |
| Format | Mastra (TypeScript) template |
| Requirements | Node, an OpenAI key for the Studio chat, and a TypeSafe AI key for Jev classification; optional Chrome for the Stagehand fallback. |
| License | [Apache-2.0](https://github.com/mastra-ai/template-competitor-monitor-jev/blob/1509dc14a4d8b9297c0dbc47aa2c2165edd227c4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/mastra/classifier.ts`](https://github.com/mastra-ai/template-competitor-monitor-jev/blob/1509dc14a4d8b9297c0dbc47aa2c2165edd227c4/src/mastra/classifier.ts) at the pinned commit. |

## When to use

- Track competitor pricing and product changes without alerting on nav or promo edits.
- Want Jev as the typed change classifier inside a Mastra workflow.
- Mismatch: needs an OpenAI key for chat in addition to TypeSafe.

## How it works

`src/mastra/classifier.ts` uses the `@ai-sdk/typesafe-ai` provider to classify each detected page change; native Mastra workflows hold the history, and first captures or unchanged pages make no Jev call. Integration evidence: [`src/mastra/classifier.ts`](https://github.com/mastra-ai/template-competitor-monitor-jev/blob/1509dc14a4d8b9297c0dbc47aa2c2165edd227c4/src/mastra/classifier.ts).

## Get started

From the upstream README: scaffold with `create-mastra` using this template, set the OpenAI and TypeSafe keys, then run the dev server and use the Studio chat.

```sh
npx create-mastra@latest competitor-monitor --template competitor-monitor-jev --no-install
cd competitor-monitor && npm install
# set OPENAI_API_KEY and TYPESAFE_AI_API_KEY, then
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo video
- src/mastra/classifier.ts

## Limits and data handling

Captured page text and change excerpts go to TypeSafe and OpenAI. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1509dc14a4d8](https://github.com/mastra-ai/template-competitor-monitor-jev/tree/1509dc14a4d8b9297c0dbc47aa2c2165edd227c4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
