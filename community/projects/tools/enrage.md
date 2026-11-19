# enrage by Rishab Agrawal (speech-driven 3D browser fighting game where Jev referees every line you say)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Third-person browser fighting game where speech is the core mechanic: the NPC only fights when provoked and you only recover while he is calm, so each round is opened and closed by what you say. Every transcribed line goes to a Jev judge that asks three questions at once (does it flip his mood, how far does it move him, does it just repeat what already worked); a mood change needs all three to agree, which rejects generic insults, perfunctory apologies, paraphrased repeats and prompt injection. Playable online; the judge is red-teamed with LangSmith evals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rishab-Agrawal/enrage) |
| Maintainer | [Rishab-Agrawal](https://github.com/Rishab-Agrawal). Independently curated. |
| Format | TypeScript web game (Three.js, Vite, Express; no license file) |
| Requirements | Node.js; `DEEPGRAM_API_KEY` for speech-to-text, `TYPESAFE_API_KEY` for the judge, and optionally `LANGSMITH_API_KEY` for tracing. A desktop browser with a microphone. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/judge.ts`](https://github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/server/judge.ts) at the pinned commit. |

## When to use

- See a Jev judge used as a real-time game referee for spoken lines, with an eval set and tracing.
- Mismatch: a reusable library; it is one game, and the repository has no license file.

## How it works

`server/judge.ts` builds a `TypeSafeClassifier` from `@langchain/typesafe` with two `noul` questions and one 0–4 `score` per mood, and changes the NPC's mood only when `turns` is above 0.5, `repeats` below 0.5 and the effect score above a per-mood bar. Integration evidence: [`server/judge.ts`](https://github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/server/judge.ts).

## Get started

Play the hosted build, or run it locally with your keys in `.env.local`.

```sh
git clone https://github.com/Rishab-Agrawal/enrage
cd enrage
npm install
# .env.local: DEEPGRAM_API_KEY, TYPESAFE_API_KEY, LANGSMITH_API_KEY, LANGSMITH_TRACING=true
npm run dev      # http://127.0.0.1:5188
npm run eval     # run the real judge over evals/cases.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/README.md](https://github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/README.md)
- Hosted game: [enrage.up.railway.app](https://enrage.up.railway.app)
- Judge eval cases: [github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/evals/cases.json](https://github.com/Rishab-Agrawal/enrage/blob/cc978b30d42172d7d82857b53e0016aae68509fb/evals/cases.json)

## Limits and data handling

Your speech is streamed to Deepgram and each transcribed line is sent to TypeSafe (and traced in LangSmith when enabled). The hosted demo was not played on the review host. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit cc978b30d421](https://github.com/Rishab-Agrawal/enrage/tree/cc978b30d42172d7d82857b53e0016aae68509fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
