# Jevers

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Zero-dependency Node client for decision models: chain TypeSafe Jev with fallbacks (Liquid d1, Perplexity pplx-decider, Fastino GLiDE, Microsoft Decision-1, OpenAI Decisions, Cloudflare Clef, OpenRouter routes, local llama-server) and ask choice, noul or score questions over text, JSON, images or audio.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/clasen/Jevers) |
| Maintainer | [clasen](https://github.com/clasen). Independently curated. |
| Format | JavaScript library (npm `jevers`) plus agent skills |
| Requirements | Node.js 20+; a TypeSafe key for Jev (and keys for any fallback providers). |
| License | [MIT](https://github.com/clasen/Jevers/blob/3776f9b4846e8bb487777bad82349131ec695308/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/martinclasen/status/2110803929898291647)). |
| Jev evidence | [`lib/providers/system-one.js`](https://github.com/clasen/Jevers/blob/3776f9b4846e8bb487777bad82349131ec695308/lib/providers/system-one.js) at the pinned commit. |

## When to use

- Route a support ticket or pre-screen a message with Jev, falling back to another decision model when the provider is down or rate limited.
- Benchmark several decision models on the same questions with the bundled benchmark skill.
- Mismatch: provider-neutral; benchmark statements in the author's X post were not reproduced here.

## How it works

A chainable builder (`Jevers.new().jev().glide()...`) collects state parts and typed questions; the System One provider posts them to `https://api.typesafe.ai/v1/systemone` (or OpenRouter's `systemone` route) and returns per-option probabilities, moving to the next attached model on failure or rate limit. Integration evidence: [`lib/providers/system-one.js`](https://github.com/clasen/Jevers/blob/3776f9b4846e8bb487777bad82349131ec695308/lib/providers/system-one.js).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm add jevers
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage example in the README (support-ticket `choice` with a GLiDE fallback).
- Skills: `npx skills add [github.com/clasen/Jevers](https://github.com/clasen/Jevers) --skill jevers --skill jevers-benchmark`.

## Limits and data handling

State text, JSON, images or audio go to each provider in the chain, billed to the matching key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 3776f9b4846e](https://github.com/clasen/Jevers/tree/3776f9b4846e8bb487777bad82349131ec695308). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
