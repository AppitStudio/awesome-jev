# Jev Showcase by Szymon Bakunowicz (one local hub that runs nine Jev demos: support routing, RAG routing, vision, image references and four browser extensions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tabbed local hub that starts and stops a set of Jev demos against the live TypeSafe API, with no mock modes: support-desk routing, a RAG router that decides when retrieval is needed, a vision playground with Box, a hotdog classifier, pictures used inside questions as references, and four browser-extension backends (a headline lens for Polish news sites, a LinkedIn BS detector, YouTube comment insights and an AI-image filter).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tez-Szymon/jev-showcase) |
| Maintainer | [Szymon Bakunowicz](https://github.com/tez-Szymon) (tez-Szymon). Independently curated. |
| Format | Node.js demo hub + browser extensions |
| Requirements | Node.js, a TypeSafe key (some demos use `jev-preview` for images), and an OpenRouter or OpenAI key for the RAG demo. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/vision/server/questions.ts`](https://github.com/tez-Szymon/jev-showcase/blob/82fb0eb8690b172877e940a330c5969a94c070d9/apps/vision/server/questions.ts) at the pinned commit. |

## When to use

- Developers who want to see many Jev patterns, including image questions, running side by side.
- Mismatch: a library; these are demos.

## How it works

Each demo's server calls `https://api.typesafe.ai/v1/systemone` with its own questions; the vision demo's `apps/vision/server/questions.ts` builds Box, Noul, Choice and Score questions, and the hub shows each backend's model and request counters from `/health`. Integration evidence: [`apps/vision/server/questions.ts`](https://github.com/tez-Szymon/jev-showcase/blob/82fb0eb8690b172877e940a330c5969a94c070d9/apps/vision/server/questions.ts).

## Get started

Set your keys, install every demo and start the hub.

```sh
git clone https://github.com/tez-Szymon/jev-showcase && cd jev-showcase
cp .env.example .env   # TYPESAFE_API_KEY, OPENROUTER_API_KEY
npm run setup
npm start   # http://127.0.0.1:4310
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demos: [github.com/tez-Szymon/jev-showcase/tree/main/apps](https://github.com/tez-Szymon/jev-showcase/tree/main/apps)

## Limits and data handling

Every demo makes live, billed TypeSafe calls, and the extensions send page text (news headlines, LinkedIn posts, YouTube comments, images) to your local backend and on to TypeSafe. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 82fb0eb8690b](https://github.com/tez-Szymon/jev-showcase/tree/82fb0eb8690b172877e940a330c5969a94c070d9). Inspected the README, `.env.example` and the vision demo server at the pinned commit; no licence file present. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
