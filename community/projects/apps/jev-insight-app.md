# jev-insight-app (Japanese web app for exhibition booths that judges each spoken remark with Jev to keep only the visitor's real problems)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Phone-based web app for trade-show booth staff: record a conversation, transcribe it, and have Jev score every utterance for relevance, problem severity (1–5) and concreteness so only problem statements are kept as cards. Jev also picks the next question to ask (scale, budget, timing, decision-maker), and a local LLM writes the visitor's summary. UI and README are in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Takashi-Matsumura/jev-insight-app) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Takashi-Matsumura/jev-insight-app#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you supply your own TypeSafe key and run the local speech and LLM servers. Checked 2026-11-05. |
| Jev evidence | [`lib/jev.ts`](https://github.com/Takashi-Matsumura/jev-insight-app/blob/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Takashi-Matsumura](https://github.com/Takashi-Matsumura). Independently curated. |
| Format | Next.js web app with SQLite, local whisper-server and llama-server |
| Platform and availability | Web app you host yourself (source build); used from a phone browser |
| Jev's role | Judges each transcribed remark for relevance, severity and concreteness and picks the next question to ask. |
| Requirements | Node.js, a `TYPESAFE_API_KEY`, whisper-server and llama-server running locally, and optional Cloudflare Access for phone use. |
| License | [MIT](https://github.com/Takashi-Matsumura/jev-insight-app/blob/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5/LICENSE) |

## When to use

- Capture and rank customer problems from live conversations while keeping transcription and summaries local.
- See a per-utterance Jev gate with a relevance threshold (`RELEVANCE_THRESHOLD`, default 0.5).
- Mismatch: Japanese-language docs and UI; recording people needs consent.

## How it works

`lib/jev.ts` posts typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); `lib/jev-questions.ts` defines the relevance, severity and next-question questions. Integration evidence: [`lib/jev.ts`](https://github.com/Takashi-Matsumura/jev-insight-app/blob/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5/lib/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.local.example .env.local   # set TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese) with setup and environment variables: [github.com/Takashi-Matsumura/jev-insight-app/blob/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5/README.md](https://github.com/Takashi-Matsumura/jev-insight-app/blob/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5/README.md)

## Limits and data handling

Transcribed utterances go to TypeSafe for judging (audio and summaries stay local per the README); get consent before recording. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit d22ecd363e4e](https://github.com/Takashi-Matsumura/jev-insight-app/tree/d22ecd363e4ef50ec1d9df9ba8b54df63bdd03f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
