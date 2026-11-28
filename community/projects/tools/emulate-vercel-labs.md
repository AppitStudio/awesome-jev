# emulate by Vercel Labs (local API emulators for CI, including a TypeSafe Jev `/v1/systemone` emulator with scripted decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local drop-in API emulators for CI and no-network sandboxes. Its AI service answers OpenAI, Anthropic, Gemini, image, audio and video requests offline, and also emulates decision models: TypeSafe Jev on `POST /v1/systemone`, OpenRouter decisions and others, with deterministic probabilities, scripted decision rules, strict mode and fault injection. Point a Jev client's base URL at it to test without keys or token spend.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vercel-labs/emulate) |
| Maintainer | [Vercel Labs](https://github.com/vercel-labs) (experiment; decision models announced on X by [@lahfir](https://x.com/lahfir)). Independently curated. |
| Format | Node.js CLI + npm package (`emulate`) |
| Requirements | Node.js and npx; no API keys. |
| License | [Apache-2.0](https://github.com/vercel-labs/emulate/blob/8c0306cf59a625a0b4b9b8ed96223ea9b6ecec3f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/lahfir/status/2126478362768285942)). |
| Jev evidence | [`packages/@emulators/ai/src/media/decisions.ts`](https://github.com/vercel-labs/emulate/blob/8c0306cf59a625a0b4b9b8ed96223ea9b6ecec3f/packages/%40emulators/ai/src/media/decisions.ts) at the pinned commit. |

## When to use

- Teams who want Jev calls in CI, demos or sandboxes to run offline and repeat exactly.
- Mismatch: measuring Jev accuracy; the emulator's probabilities are synthetic.

## How it works

`packages/@emulators/ai/src/media/decisions.ts` parses Jev `noul`, `choice`, `score` and `box` questions from `/v1/systemone` requests (including zstd bodies) and answers in Jev's response shape with seeded, repeatable probabilities, or with the answers in a matching `{ type: decision, answers }` rule. It never calls TypeSafe; it stands in for it. Integration evidence: [`packages/@emulators/ai/src/media/decisions.ts`](https://github.com/vercel-labs/emulate/blob/8c0306cf59a625a0b4b9b8ed96223ea9b6ecec3f/packages/%40emulators/ai/src/media/decisions.ts).

## Get started

Start the AI emulator and point your Jev client's base URL at it.

```sh
npx emulate start --service ai --port 4014
# then set your Jev client's base URL to http://localhost:4014 (POST /v1/systemone)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- AI emulator docs: [github.com/vercel-labs/emulate/blob/main/packages/@emulators/ai/README.md](https://github.com/vercel-labs/emulate/blob/main/packages/@emulators/ai/README.md)
- Playground: [emulate.dev/playground](https://emulate.dev/playground)

## Limits and data handling

Answers are deterministic stand-ins, not Jev output, so tests that pass against the emulator say nothing about real decision quality. Marked as a Vercel Labs experiment.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 8c0306cf59a6](https://github.com/vercel-labs/emulate/tree/8c0306cf59a625a0b4b9b8ed96223ea9b6ecec3f). Inspected the README, the `@emulators/ai` README, LICENSE and `decisions.ts` at the pinned commit and confirmed `emulate` 0.15.0 on npm; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
