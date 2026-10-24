# ChatJev by JamesANZ (ask Jev to judge a document or web lookup in plain language)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app where you upload a document or ask about the web: a fast LLM turns your question into Jev yes/no, choice or score judgments, can attach web excerpts as evidence, and then restates only Jev's numbers, with a verdict card showing each judgment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JamesANZ/ChatJev) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Product homepage](https://chatjev.vercel.app) |
| Pricing and access | Open source (MIT); free source build with your own keys. A hosted demo is at chatjev.vercel.app (reachable 2026-10-24; access terms not verified). |
| Jev evidence | [`src/core/typesafe-client.ts`](https://github.com/JamesANZ/ChatJev/blob/09702099cb5059e61951ae38e51ced017f1e908e/src/core/typesafe-client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [JamesANZ](https://github.com/JamesANZ). Independently curated. |
| Format | Web app (Next.js, TypeScript) |
| Platform and availability | Web; hosted demo plus self-hosting from source. |
| Jev's role | Core: every verdict comes from Jev; the LLM only writes the questions and restates the numbers. |
| Requirements | Node 22+; a TypeSafe key plus an LLM key (DeepSeek by default, or OpenAI via Vercel AI Gateway) and optionally a web lookup key. |
| License | [MIT](https://github.com/JamesANZ/ChatJev/blob/09702099cb5059e61951ae38e51ced017f1e908e/LICENSE) |

## When to use

- Check claims in a document with typed judgments you can inspect.
- See how an LLM and a decision model can split the work.
- Mismatch: image input is experimental.

## How it works

`src/core/typesafe-client.ts` uses `@typesafe-ai/sdk` with `jev-latest` by default; keys stay on the server. Integration evidence: [`src/core/typesafe-client.ts`](https://github.com/JamesANZ/ChatJev/blob/09702099cb5059e61951ae38e51ced017f1e908e/src/core/typesafe-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
# .env.local: TYPESAFE_API_KEY, DEEPSEEK_API_KEY (or CHATJEV_LLM_PROVIDER=openai)
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [chatjev.vercel.app](https://chatjev.vercel.app)
- README: [github.com/JamesANZ/ChatJev#readme](https://github.com/JamesANZ/ChatJev#readme)

## Limits and data handling

Uploaded text goes to TypeSafe and to the LLM provider; web lookups go to the lookup service.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 09702099cb50](https://github.com/JamesANZ/ChatJev/tree/09702099cb5059e61951ae38e51ced017f1e908e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
