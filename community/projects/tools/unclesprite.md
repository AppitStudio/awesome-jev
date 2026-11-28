# UncleSprite by Suisei (paranoid "weird uncle" agent on a Fly.io Sprite that reviews GitHub issues with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hacksgiving 2026 personal agent that lives in a Fly.io Sprite and holds no API keys: it checkpoints the VM before working, fetches a GitHub issue through a Sprites connector, asks Jev typed questions (unresolved TODOs? security risk? readiness 0-100, category), recalls similar past mistakes from a Pinecone "grudge book", and posts a templated weird-uncle verdict with the Jev findings as a GitHub comment. Falls back to local heuristics when connectors are down.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Alvinagustus/Unclesprite) |
| Maintainer | [Suisei](https://github.com/Alvinagustus) (Alvinagustus). Independently curated. |
| Format | TypeScript CLI agent for Fly.io Sprites |
| Requirements | Node.js, a Fly.io Sprite with GitHub and OpenRouter connectors (Pinecone optional). |
| License | [MIT](https://github.com/Alvinagustus/Unclesprite/blob/e757d44803981d579322b131bfe925adf0fef059/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/AlvinAgustus/status/2126596077801685092)). |
| Jev evidence | [`src/jev.ts`](https://github.com/Alvinagustus/Unclesprite/blob/e757d44803981d579322b131bfe925adf0fef059/src/jev.ts) at the pinned commit. |

## When to use

- Fly.io Sprites users who want a playful, key-free example of an issue-review agent built on Jev.
- Mismatch: serious issue triage; the voice is a joke template.

## How it works

`src/jev.ts` posts `noul`, `score` and `choice` questions about the issue to `/v1/systemone` through the Sprites OpenRouter connector (`typesafe/jev-1.14`); `src/verdict.ts` combines the answers with the grudge memory. Integration evidence: [`src/jev.ts`](https://github.com/Alvinagustus/Unclesprite/blob/e757d44803981d579322b131bfe925adf0fef059/src/jev.ts).

## Get started

Build and test locally, then run the demo inside a Sprite with your connector IDs.

```sh
git clone https://github.com/Alvinagustus/Unclesprite && cd Unclesprite
npm install && npm run build && npm test
export GITHUB_CONN_ID=... OPENROUTER_CONN_ID=... SPRITE_NAME=unclesprite
bash scripts/demo.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hacksgiving 2026: [fly.io/hacksgiving/](https://fly.io/hacksgiving/)

## Limits and data handling

Issue text goes through the OpenRouter connector to TypeSafe; the agent posts comments on the GitHub issue you point it at. Grudge embeddings are a hashing bag-of-words, not a model.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit e757d4480398](https://github.com/Alvinagustus/Unclesprite/tree/e757d44803981d579322b131bfe925adf0fef059). Inspected the README, LICENSE, `sprite.yaml` and `src/jev.ts` at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
