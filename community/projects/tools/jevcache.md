# jevcache

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenAI-compatible local cache proxy: TypeSafe Jev (via OpenRouter Decisions) admits paraphrased chat prompts as same-intent hits so expensive upstream completions can be skipped; fails open when Jev errors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kushals256/jevcache) |
| Maintainer | [kushals256](https://github.com/kushals256). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript / Node.js CLI and proxy (`@kushalicious/jevcache` **0.1.5**); optional Docker image. |
| Requirements | Node.js ≥ 22.5 (uses `node:sqlite`); `OPENROUTER_API_KEY` for live Jev admits and upstream chat (or `MOCK_JEV` / `MOCK_UPSTREAM` for local demos). |
| License | [MIT](https://github.com/kushals256/jevcache/blob/b0e0418fa3eae9cb550c9e43572b28477cc1f524/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, build, and offline unit tests inspected. Live OpenRouter/Jev traffic was not run. Distinct from any other “jevcache” product without this MIT source. |

## When to use

Use it when OpenAI-compatible clients should reuse prior answers for paraphrased prompts judged same-intent by Jev, instead of cosine-only semantic cache. Prefer exact-match or other routers when you do not want a decision model in the admit path. Do not treat upstream demo timing or dollar-saved figures as measured on this review host.

## How it works

The proxy fingerprints prompts, asks Jev a Noul (`same_intent`) plus Choice (`best` candidate id) over redacted NEW vs CANDIDATES state via OpenRouter’s decisions API (default model `typesafe/jev-1.13`), and on admit returns the stored completion. [`src/jev_admit.ts`](https://github.com/kushals256/jevcache/blob/b0e0418fa3eae9cb550c9e43572b28477cc1f524/src/jev_admit.ts) implements admit; Jev HTTP failures fail open to the upstream model. `MOCK_JEV=1` substitutes a local token-overlap heuristic.

## Get started

```sh
git clone https://github.com/kushals256/jevcache.git
cd jevcache
git checkout b0e0418fa3eae9cb550c9e43572b28477cc1f524
npm ci --ignore-scripts
npm run build
npm test
# optional offline-shaped demo (no live Jev):
MOCK_JEV=1 MOCK_UPSTREAM=1 npx --yes . doctor
```

Published shortcut (needs keys for real admits): `npx @kushalicious/jevcache@latest start --demo`. Point clients at `http://127.0.0.1:8080/v1`.

## Examples and demos

- Upstream [`docs/demo.gif`](https://github.com/kushals256/jevcache/blob/b0e0418fa3eae9cb550c9e43572b28477cc1f524/docs/demo.gif) and [`AGENT_SETUP.md`](https://github.com/kushals256/jevcache/blob/b0e0418fa3eae9cb550c9e43572b28477cc1f524/AGENT_SETUP.md) agent paste prompt.
- [`examples/openai_sdk.mjs`](https://github.com/kushals256/jevcache/blob/b0e0418fa3eae9cb550c9e43572b28477cc1f524/examples/openai_sdk.mjs): wire `baseURL` to the proxy.
- Offline Vitest covers fingerprint and store paths (no live Jev).

## Limits and data handling

Prompt text (redacted heuristics applied) is sent to OpenRouter for Jev admits and upstream completions when not mocked. Cache contents live in local SQLite. Admit quality depends on threshold and candidate set; paraphrases can still miss. Fail-open means Jev outages do not block chat—they spend upstream tokens instead.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b0e0418](https://github.com/kushals256/jevcache/tree/b0e0418fa3eae9cb550c9e43572b28477cc1f524): **0.1.5**, MIT. AI-assisted source review of `jev_admit.ts`, config, README, and LICENSE. On Node.js 22.23.2: **`npm run build`** passed; **`npm test`**: **12 passed** (2 files). No live OpenRouter or TypeSafe calls.

Related: [invalidate](invalidate.md), [Yoshi](yoshi.md), [Distill](distill.md).
