# SlidePilot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Slidev addon plus Cloudflare Worker: streams presenter voice through Workers AI STT, asks TypeSafe Jev whether the current slide is complete, and advances only when TypeScript policy and safety guards agree.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/harshil1712/slidepilot) |
| Maintainer | [harshil1712](https://github.com/harshil1712). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | pnpm monorepo **0.1.0** — `slidev-addon-slidepilot` package + Cloudflare Agents worker + demo deck. npm package release not yet published; clone to run. |
| Requirements | Node ≥ 20, pnpm, Cloudflare account (Workers AI); optional `TYPESAFE_API_KEY` (without it the Worker uses a deterministic mock policy). |
| License | [MIT](https://github.com/harshil1712/slidepilot/blob/8ba4e89b56e4f9a08be2f1f69346240cab95a7b6/LICENSE). |

## When to use

Use it to rehearse Slidev decks with voice-driven semantic auto-advance while keeping keyboard/clicker navigation. Prefer [Jev Voice](../apps/jev-voice.md) for general macOS voice commands, or [Jev Voice Browser](jev-voice-browser.md) for Playwright voice experiments. Upstream marks the project experimental—keep manual navigation available for live talks.

## How it works

[`apps/worker/src/decision.ts`](https://github.com/harshil1712/slidepilot/blob/8ba4e89b56e4f9a08be2f1f69346240cab95a7b6/apps/worker/src/decision.ts) builds four typed questions (advance Choice plus complete / still-explaining / transitioning Noul) via `@typesafe-ai/sdk` `systemOne` with default model `jev-latest`. TypeScript—not the model—applies cooldown, stale-decision, and continue-speaking vetoes before `useNav().nextSlide()`.

## Get started

```sh
git clone https://github.com/harshil1712/slidepilot.git
cd slidepilot
git checkout 8ba4e89b56e4f9a08be2f1f69346240cab95a7b6
pnpm install
# Deploy Worker (wrangler) or run locally:
# Terminal 1: pnpm dev:worker
# Terminal 2: pnpm dev:slides
# Optional: set TYPESAFE_API_KEY / wrangler secret for real Jev (else mock policy)
```

Live Jev mode sends slide titles/content/notes and recent utterances to TypeSafe and can incur charges; STT uses Cloudflare Workers AI. This listing did not deploy a Worker or call TypeSafe.

## Examples and demos

- Included Slidev demo under `apps/demo/`.
- Worker health endpoint and `decision.test.ts` offline policy tests.
- README architecture diagram (addon → VoiceClient → Flux STT → Jev → policy).

## Limits and data handling

Microphone audio and transcripts leave the presenter machine for Cloudflare; slide text and utterances go to TypeSafe when a key is configured. Mock mode avoids TypeSafe spend but is not a quality claim. Package is not on npm yet—install from this repository until a release is published.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 8ba4e89b](https://github.com/harshil1712/slidepilot/tree/8ba4e89b56e4f9a08be2f1f69346240cab95a7b6): **0.1.0**, MIT. AI-assisted source review of README, `decision.ts`, addon package metadata, and license. `pnpm` install, Worker deploy, mic rehearsal, and live TypeSafe calls were not run on the review host.

Related: [Jev Voice Browser](jev-voice-browser.md), [Jev Voice](../apps/jev-voice.md).
