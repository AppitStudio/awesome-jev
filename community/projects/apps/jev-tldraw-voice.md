# jev-tldraw-voice (voice-controlled tldraw canvas; Jev reads intent, code edits the canvas)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chinese-first web app where speech is interpreted by TypeSafe Jev (`jev-latest` at api.typesafe.ai/v1/systemone) into typed canvas commands; local code applies them on a tldraw canvas (move/add/edit/connect) without inventing geometry in the model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/voidning/jev-tldraw-voice) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/voidning/jev-tldraw-voice#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-07. |
| Jev evidence | [`server/live/interpret.mjs`](https://github.com/voidning/jev-tldraw-voice/blob/d9e2a6179cd3dabce228935bc9ea8636cc83d46a/server/live/interpret.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [voidning](https://github.com/voidning). Independently curated. |
| Format | Vite + Node server web app (TypeScript, MIT) |
| Platform and availability | Self-hosted web app (browser + local Node server). |
| Jev's role | Interprets utterances into typed live commands via `server/live/interpret.mjs` POSTing to TypeSafe System One; the canvas executor applies validated commands. |
| Requirements | Node.js and a TypeSafe API key (`TYPESAFE_API_KEY`) for live voice interpretation. |
| License | [MIT](https://github.com/voidning/jev-tldraw-voice/blob/d9e2a6179cd3dabce228935bc9ea8636cc83d46a/LICENSE) |

## When to use

- Drive tldraw by voice with calibrated Jev intent.
- Keep geometry/execution in local code.
- Mismatch: Chinese-first UI; needs a running local server and mic permissions.

## How it works

`server/live/interpret.mjs` POSTs `{model:'jev-latest', state, questions}` to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`; `jev-validation.ts` validates the returned command before execution. Integration evidence: [`server/live/interpret.mjs`](https://github.com/voidning/jev-tldraw-voice/blob/d9e2a6179cd3dabce228935bc9ea8636cc83d46a/server/live/interpret.mjs).

## Get started

Clone, set `TYPESAFE_API_KEY`, install deps, and start the Vite+server stack per README.

```sh
git clone https://github.com/voidning/jev-tldraw-voice.git && cd jev-tldraw-voice
export TYPESAFE_API_KEY=...
npm install && npm run dev  # follow README scripts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/voidning/jev-tldraw-voice/blob/d9e2a6179cd3dabce228935bc9ea8636cc83d46a/README.md](https://github.com/voidning/jev-tldraw-voice/blob/d9e2a6179cd3dabce228935bc9ea8636cc83d46a/README.md)

## Limits and data handling

Utterances and canvas context under review are sent to TypeSafe on your key. Mic audio may also hit the ASR proxy you configure.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit d9e2a6179cd3](https://github.com/voidning/jev-tldraw-voice/tree/d9e2a6179cd3dabce228935bc9ea8636cc83d46a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
