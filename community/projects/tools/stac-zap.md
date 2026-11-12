# stac-zap (one-prompt satellite imagery search where Jev picks the STAC catalog, place and dates)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Development Seed's zap mode for stac-map: type one request such as "Sentinel-2 over Cotopaxi in December 2025 with less than 30% clouds" and Jev selects one option from each list the app gives it, so every search is a valid STAC query, with each selection and its probability shown above the prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/developmentseed/stac-zap) |
| Maintainer | [developmentseed](https://github.com/developmentseed). Independently curated. |
| Format | Static web app with a Cloudflare Worker proxy (TypeScript; no license file) |
| Requirements | A browser for the hosted demo; to run it yourself, pnpm and an OpenRouter key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The repository has no license file; no reuse rights are implied. |
| Jev evidence | [`src/zap/decide.ts`](https://github.com/developmentseed/stac-zap/blob/1c5425ecc9af38962bdfa87003e3ecdbd66406a3/src/zap/decide.ts) at the pinned commit. |

## When to use

- Find satellite or aerial imagery from a plain-language request.
- See why each search field was chosen, with probabilities.
- Mismatch: no license file, so reuse terms are unclear.

## How it works

`src/zap/decide.ts` builds a decisions request for `typesafe/jev-1.14` (overridable) with the situation and one question per field, sent through OpenRouter's decisions API; a Cloudflare Worker keeps the key server-side and also forwards Clairic extraction calls for place, time and cloud cover. Integration evidence: [`src/zap/decide.ts`](https://github.com/developmentseed/stac-zap/blob/1c5425ecc9af38962bdfa87003e3ecdbd66406a3/src/zap/decide.ts).

## Get started

Try the hosted demo, or install dependencies, put your OpenRouter key in `.env` and start the dev server.

```sh
pnpm install
echo 'OPENROUTER_API_KEY=sk-or-...' > .env
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [developmentseed.org/stac-zap/](https://developmentseed.org/stac-zap/)

## Limits and data handling

Prompts go to OpenRouter (Jev and Clairic); the hosted demo uses the maintainer's key through their Worker.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 1c5425ecc9af](https://github.com/developmentseed/stac-zap/tree/1c5425ecc9af38962bdfa87003e3ecdbd66406a3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
