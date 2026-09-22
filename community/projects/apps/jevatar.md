# Jevatar

[All projects](../README.md) · [Apps](README.md) · [Web apps](README.md#web-apps)

Local companion that replies only with facial expressions: TypeSafe Jev picks one of 16 moods for your message; blobatar morphs the face—no text replies or visible chat history.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AppChainAI/Jevatar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Jevatar project homepage](https://github.com/AppChainAI/Jevatar) — source-build entry; no separate commercial site reviewed. |
| Pricing and access | No app purchase fee for the MIT source build reviewed **2026-09-22**. Bring a TypeSafe API key (`TYPESAFE_API_KEY`). Provider usage can incur charges. No packaged hosted product reviewed. |
| Jev evidence | [`server.ts`](https://github.com/AppChainAI/Jevatar/blob/9ddc924a4a5c25293ccbb498a5475da7ce246cf4/server.ts) posts Choice questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); low confidence falls back to `unsure`, errors to `sick`. |
| Disclosure | Independently curated; no affiliation. Listing is not endorsement. AI-assisted catalog review. Offline `bun test` passed after `bun install` on the review host. Live companion/TypeSafe chat was not run. |
| Maintainer | [AppChainAI](https://github.com/AppChainAI). Independently curated; not an upstream submission. |
| Format | Bun + Vite/React local web app with a small API server. |
| Platform and availability | Local Node/Bun toolchain; browser UI. Early source distribution. |
| Jev's role | Chooses a discrete facial expression from fixed criteria given the user message and short in-memory history; code renders blobatar. No generative text reply. |
| Requirements and costs | Bun; `TYPESAFE_API_KEY` on the server only (not sent to the browser). TypeSafe inference charges possible. |
| License | [MIT](https://github.com/AppChainAI/Jevatar/blob/9ddc924a4a5c25293ccbb498a5475da7ce246cf4/LICENSE). |

## When to use

Use it when you want a **face-only** reaction companion powered by typed Jev choices. Prefer [Jev Asks Until Sure](jev-asks-until-sure.md) for a question-game UI, or chat assistants when you need text replies. Do not treat expressions as verified emotion detection.

## How it works

[`askJev`](https://github.com/AppChainAI/Jevatar/blob/9ddc924a4a5c25293ccbb498a5475da7ce246cf4/server.ts) sends companion state, recent turns, and the latest message to System One with a Choice over 16 expression criteria (14 built-ins plus custom `yes`/`no`). The browser calls `POST /api/react`; the API key stays on the server. [`server.test.ts`](https://github.com/AppChainAI/Jevatar/blob/9ddc924a4a5c25293ccbb498a5475da7ce246cf4/server.test.ts) checks that server criteria keys match frontend expression/label maps.

## Get started

```sh
git clone https://github.com/AppChainAI/Jevatar.git
cd Jevatar
git checkout 9ddc924a4a5c25293ccbb498a5475da7ce246cf4
bun install
bun test
# Live UI (charges possible): set TYPESAFE_API_KEY, then bun run dev
```

Live `/api/react` calls send message text and short history to TypeSafe. This listing did not run a live session.

## Examples and demos

- Offline: `bun test` — **1 pass** on the review host after `bun install`.
- Source: expression map in [`src/expressions.ts`](https://github.com/AppChainAI/Jevatar/blob/9ddc924a4a5c25293ccbb498a5475da7ce246cf4/src/expressions.ts).

## Limits and data handling

Requires a TypeSafe key for live reactions. Recent turns are kept in memory for context only. Errors surface as the `sick` face. Independent of blobatar’s commercial offerings beyond the open `@blobatar/react` dependency.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 9ddc924](https://github.com/AppChainAI/Jevatar/tree/9ddc924a4a5c25293ccbb498a5475da7ce246cf4): MIT. AI-assisted source review of README, LICENSE, `server.ts`, `src/expressions.ts`, and `server.test.ts`. Offline `bun test` **1 pass**. No live TypeSafe spend.

Related: [Jev Asks Until Sure](jev-asks-until-sure.md), [Crush Monitor](crush-monitor.md).
