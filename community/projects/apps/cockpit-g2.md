# Cockpit G2 by oblomovunleashed (voice-first three-mind assistant for Even Realities G2 glasses; Jev routes each thought to Work, Personal or Interests)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hackathon app for Even Realities G2 smart glasses: hold to speak, and Jev routes each utterance to one of three minds (Work, Personal, Interests) in a few hundred milliseconds, so quick notes go straight to Notion without waiting on an LLM, while research questions wake a slower DeepSeek pass that returns one sourced card. Includes two-way Notion sync with one-swipe undo, a read-only equity-research example workflow and a zero-key mock mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/oblomovunleashed/Cockpit-G2) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/oblomovunleashed/Cockpit-G2#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build with a prebuilt simulator `.ehpk` on GitHub Releases; no licence file. Live mode needs your own OpenRouter key (Jev, Whisper, DeepSeek) and a Notion token. Checked 2026-11-28. |
| Jev evidence | [`backend/app/services/jev_router.py`](https://github.com/oblomovunleashed/Cockpit-G2/blob/b5259fd3a076ce811cfd099412abb2ac9bcd530a/backend/app/services/jev_router.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/oblomovius/status/2126440711252070819)). |
| Maintainer | [oblomovunleashed](https://github.com/oblomovunleashed) (on X as [@oblomovius](https://x.com/oblomovius)). Independently curated. |
| Format | Even Hub glasses app + Python backend |
| Platform and availability | Even Realities G2 via Even Hub (Vite/TypeScript WebView app) with a local Python FastAPI backend; tested in the Even Hub Simulator. |
| Jev's role | Router. Each transcribed utterance gets a Jev decision on mind and action type that picks the tier (local save, async enrichment or blocking synthesis); code handles dates, storage and Notion writes. |
| Requirements | Python 3.11+, Node 22; for live mode an OpenRouter key and a Notion integration token. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Even Realities G2 owners and developers who want a fast voice-to-Notion assistant to build on.
- Mismatch: investment advice or trading; the Work example is read-only research.

## How it works

`backend/app/services/jev_router.py` asks Jev (`~typesafe/jev-latest` through OpenRouter, set in `backend/app/config.py`) to classify each utterance into a mind and action; the result decides whether the backend saves locally, enriches in the background or calls DeepSeek with retrieval or web search. Integration evidence: [`backend/app/services/jev_router.py`](https://github.com/oblomovunleashed/Cockpit-G2/blob/b5259fd3a076ce811cfd099412abb2ac9bcd530a/backend/app/services/jev_router.py).

## Get started

Run the offline mock mode first, then add keys for live mode.

```sh
git clone https://github.com/oblomovunleashed/Cockpit-G2 && cd Cockpit-G2
make setup && cp .env.example .env   # COCKPIT_MOCK_MODE=true by default
make backend   # terminal 1
make glasses   # terminal 2
make sim       # terminal 3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video: [www.youtube.com/watch?v=ISgrmFkWsOQ](https://www.youtube.com/watch?v=ISgrmFkWsOQ)
- Architecture: [github.com/oblomovunleashed/Cockpit-G2/blob/main/docs/architecture.md](https://github.com/oblomovunleashed/Cockpit-G2/blob/main/docs/architecture.md)

## Limits and data handling

In live mode, voice audio goes to OpenRouter for transcription, transcripts to Jev and DeepSeek, and saved items to your Notion workspace. Built during the Even Realities hackathon (23–29 Nov 2026); the release package targets a local desktop backend. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit b5259fd3a076](https://github.com/oblomovunleashed/Cockpit-G2/tree/b5259fd3a076ce811cfd099412abb2ac9bcd530a). Inspected the README, `backend/app/config.py` and `jev_router.py` at the pinned commit; no licence file present. Not built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
