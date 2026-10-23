# jev-voice-agent (voice agent with no LLM: Deepgram Flux plus Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reference voice agent for an IT service desk where Deepgram Flux handles speech and turn-taking, Jev picks the next branch of a human-written script, and Flux TTS speaks the chosen line, so the agent can only say lines you have approved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dg-coreylweathers/jev-voice-agent) |
| Maintainer | [dg-coreylweathers](https://github.com/dg-coreylweathers). Independently curated. |
| Format | TypeScript reference project (Node.js) |
| Requirements | Node.js; Deepgram and TypeSafe API keys for live mode (an offline fixture demo needs neither). |
| License | [MIT](https://github.com/dg-coreylweathers/jev-voice-agent/blob/98fc321908a5ea3e9824b41da381e43268b9b18c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge/typesafe.ts`](https://github.com/dg-coreylweathers/jev-voice-agent/blob/98fc321908a5ea3e9824b41da381e43268b9b18c/src/judge/typesafe.ts) at the pinned commit. |

## When to use

- Build phone or voice flows where every reply must come from an approved script.
- Study confidence gating, reprompt budgets and barge-in in a voice loop.
- Mismatch: open-ended conversation; the README says where to bring an LLM back.

## How it works

`src/judge/typesafe.ts` calls `client.systemOne` from `@typesafe-ai/sdk` (directly or through Vercel AI Gateway) with four questions per turn: branch, answered, escalating and clarity. `src/decide.ts` then gates the result in code. Integration evidence: [`src/judge/typesafe.ts`](https://github.com/dg-coreylweathers/jev-voice-agent/blob/98fc321908a5ea3e9824b41da381e43268b9b18c/src/judge/typesafe.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/dg-coreylweathers/jev-voice-agent
cd jev-voice-agent
npm install
npm run demo:offline
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Deepgram article on five Jev projects: [deepgram.com/learn/audio-decision-composition-five-open-source-jev-projects](https://deepgram.com/learn/audio-decision-composition-five-open-source-jev-projects)
- README walkthrough: [github.com/dg-coreylweathers/jev-voice-agent#readme](https://github.com/dg-coreylweathers/jev-voice-agent#readme)

## Limits and data handling

The author says the live path has not been run against the real APIs yet; latency figures come from fixture mode. Transcripts are sent to Deepgram and TypeSafe in live mode.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 98fc321908a5](https://github.com/dg-coreylweathers/jev-voice-agent/tree/98fc321908a5ea3e9824b41da381e43268b9b18c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
