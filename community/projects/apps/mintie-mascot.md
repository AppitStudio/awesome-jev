# Mintie by tommyyzhao (open-source talking slime-blob companion in Three.js where a System One model such as Jev decides how it reacts)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser companion built as a showcase for System One. A jelly blob lives in a Three.js (WebGL2) scene, reacts to touch (poke, pat, lift, throw), hears you through a realtime speech model, and answers in its own voice. Each turn a small typed-decision model answers several questions with probabilities (what to do, which of 64 gestures, how to feel), which an `?debug` overlay shows. It runs with no keys using a deterministic rules decider; any `/v1/systemone`-compatible model (hosted Jev, self-hosted OpenJev or another) can be swapped in with two environment variables. There is a hosted demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tommyyzhao/mintie-mascot) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Product homepage](https://mintie.sloprefinery.ai) |
| Pricing and access | Free to open the hosted demo and to build from source; voice and decisions need your own OpenRouter and TypeSafe keys, billed by those providers. Checked 2026-11-18. |
| Jev evidence | [`server/jev.mjs`](https://github.com/tommyyzhao/mintie-mascot/blob/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c/server/jev.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tommyyzhao](https://github.com/tommyyzhao). Independently curated. |
| Format | Node.js server with a Three.js browser app (MIT) |
| Platform and availability | Web (hosted demo at mintie.sloprefinery.ai); self-hostable with Node.js 24+ |
| Jev's role | Answers typed questions each turn (which action, which emote, mood) from the touch or speech event, with the probabilities shown in a debug overlay; a rules decider is the no-key fallback. |
| Requirements | Node.js 24+ and npm; no keys for touch and rules, an OpenRouter key for speech and lines, and a System One endpoint (Jev) for the typed decisions. |
| License | [MIT](https://github.com/tommyyzhao/mintie-mascot/blob/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c/LICENSE) |

## When to use

- Study a game-like character whose behaviour comes from typed decisions with visible probabilities.
- Mismatch: a Jev-only product; Jev is one interchangeable decider and the no-key mode never calls it.

## How it works

`server/jev.mjs` posts each turn's state and questions to the configured `SYSTEM_ONE_URL` (default `https://api.typesafe.ai/v1/systemone`); `server/rules.mjs` is the deterministic fallback and `server/decision.mjs` chooses between them. Integration evidence: [`server/jev.mjs`](https://github.com/tommyyzhao/mintie-mascot/blob/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c/server/jev.mjs).

## Get started

Run it locally with no keys, then add keys in `.env` to turn on voice and the System One decider.

```sh
git clone https://github.com/tommyyzhao/mintie-mascot && cd mintie-mascot
npm ci && npm start    # http://127.0.0.1:8142/ (no keys needed)
# optional: cp .env.example .env, set OPENROUTER_API_KEY and the System One URL and key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [mintie.sloprefinery.ai](https://mintie.sloprefinery.ai)
- Configuration: [github.com/tommyyzhao/mintie-mascot/blob/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c/docs/CONFIGURATION.md](https://github.com/tommyyzhao/mintie-mascot/blob/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c/docs/CONFIGURATION.md)

## Limits and data handling

With keys set, what you say and touch events go to the configured model providers. The author documents which key turns on which feature in `docs/CONFIGURATION.md`. Not run here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit b8a1fb386b3a](https://github.com/tommyyzhao/mintie-mascot/tree/b8a1fb386b3a7c31e6ec947d58f5f09be2f8bf1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
