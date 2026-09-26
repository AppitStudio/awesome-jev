# Micdrop

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript packages for real-time voice conversations with AI (browser, React Native, Node server), including official `@micdrop/typesafe` so TypeSafe Jev can classify each user turn before the LLM answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Godefroy/micdrop) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [micdrop.dev](https://micdrop.dev) — docs and package guides. |
| Pricing and access | MIT source build; no app purchase fee. Live demos and production calls need your own provider keys (at least `TYPESAFE_API_KEY` for the Jev classifier, plus STT/LLM/TTS keys such as `OPENAI_API_KEY` in the support demo). Inference and hosting are charged by those providers. Checked **2026-09-26**. |
| Jev evidence | Official package [`@micdrop/typesafe`](https://github.com/Godefroy/micdrop/tree/d85f771b0aa4322ee06fd87c0ef73e380217a6cc/packages/typesafe) (`TypesafeClassifier` via `@typesafe-ai/sdk`); docs at [typesafe integration](https://micdrop.dev/docs/ai-integration/provided-integrations/typesafe); support demo [`examples/demo-support`](https://github.com/Godefroy/micdrop/tree/d85f771b0aa4322ee06fd87c0ef73e380217a6cc/examples/demo-support) wires Jev choice/score/noul routing before the agent replies. |
| Disclosure | AI-assisted catalog review from public GitHub and micdrop.dev docs. No affiliation with the author. Listing is not an endorsement. Live voice calls and live TypeSafe/provider runs were **not** executed on the review host. |
| Maintainer | [Godefroy de Compreignac](https://github.com/Godefroy) ([Godefroy/micdrop](https://github.com/Godefroy/micdrop)). Independently curated. |
| Format | TypeScript monorepo: client/server voice SDK plus provider packages (`@micdrop/typesafe` 1.0.1 and others). |
| Platform and availability | Browser (`@micdrop/web`), React Native, Node server; MIT on GitHub/npm. |
| Jev's role | Optional turn classifier: Jev answers typed choice/score/noul questions about each user turn (documented “few hundred ms”) so application code can route, escalate, or script a reply before the LLM streams. STT, agent LLM, and TTS remain separate providers. |
| Requirements | Node/pnpm (or npm) for examples; `TYPESAFE_API_KEY` for `@micdrop/typesafe`; additional provider keys for the chosen STT/LLM/TTS stack (see each example `.env.example`). |
| License | [MIT](https://github.com/Godefroy/micdrop/blob/d85f771b0aa4322ee06fd87c0ef73e380217a6cc/LICENSE). |

## When to use

Use Micdrop when you want a **self-hosted TypeScript voice loop** (mic, VAD, playback, WebSocket server) and want TypeSafe Jev to classify each customer turn for routing—for example intent, frustration, or “wants a human”—before the agent LLM answers.

Prefer a hosted voice platform if you need telephony/SIP, managed media planes, or no Node server of your own. Prefer a thin TypeSafe SDK alone if you only need Jev judgments without the voice stack.

## How it works

`@micdrop/server` runs the call. With `@micdrop/typesafe`, a `TypesafeClassifier` asks Jev typed questions about `{ history, turn }` (or a custom `state`) through `@typesafe-ai/sdk` `systemOne`. The support demo routes on those answers in `onBeforeAnswer` (block / escalate / scripted outage / retain hint / LLM) so some paths never call the agent model.

Audio capture and playback stay in the client packages; Jev does not generate speech or free-form chat.

## Get started

Source inspection used the pinned commit below. Live calls need credentials and were not run here.

```sh
git clone https://github.com/Godefroy/micdrop.git
cd micdrop
git checkout d85f771b0aa4322ee06fd87c0ef73e380217a6cc
# Support demo (Jev classifier + OpenAI STT/agent/TTS):
# cp examples/demo-support/.env.example examples/demo-support/.env
# fill TYPESAFE_API_KEY and OPENAI_API_KEY, then from repo root:
# pnpm install && pnpm dev:support
# Open the local URL printed by the demo (README: http://localhost:8090).
```

Classifier-only (no full voice stack): `npm install @micdrop/typesafe` and use `TypesafeClassifier` / `classify()` as in the [package README](https://github.com/Godefroy/micdrop/blob/d85f771b0aa4322ee06fd87c0ef73e380217a6cc/packages/typesafe/README.md).

## Examples and demos

- [`examples/demo-support`](https://github.com/Godefroy/micdrop/tree/d85f771b0aa4322ee06fd87c0ef73e380217a6cc/examples/demo-support) — Nova Fiber support line: six Jev questions per turn; routes before the LLM. Needs live `TYPESAFE_API_KEY` and `OPENAI_API_KEY`.
- Package and site docs: [typesafe integration](https://micdrop.dev/docs/ai-integration/provided-integrations/typesafe), [examples index](https://micdrop.dev/docs/examples).
- Upstream also links a general Micdrop/voice-AI talk on YouTube; that is product context, not a measured Jev latency study for this listing.

## Limits and data handling

Turn text (and any custom `state`) is sent to TypeSafe when the classifier runs. STT/LLM/TTS providers receive audio or transcripts according to the chosen packages. Local Whisper/Kokoro/Piper/etc. options avoid those cloud bills for speech pieces but still need `TYPESAFE_API_KEY` if you use `@micdrop/typesafe`. Catalog review did not measure end-to-end call latency or run live voice sessions.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit d85f771](https://github.com/Godefroy/micdrop/tree/d85f771b0aa4322ee06fd87c0ef73e380217a6cc). AI-assisted inspection of README, MIT LICENSE, `packages/typesafe` (README + `TypesafeClassifier.ts`), and `examples/demo-support` (README, `.env.example`, `src/server/call.ts`). Install, `pnpm` build, and live voice/TypeSafe calls were not executed.
