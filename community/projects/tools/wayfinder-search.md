# Wayfinder (Jev-powered site search that sends visitors straight to the right page)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Drop-in site search for websites: you describe each page in visitors' words, and Jev (through OpenRouter) picks the one page that answers what someone typed, offers a few options when unsure, and falls back to word matching without a key or when the model is slow; it can only choose from your list, never write answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mou1z/wayfinder) |
| Maintainer | [Mou1z](https://github.com/Mou1z). Independently curated. |
| Format | TypeScript library (npm `wayfinder-search`) with a search box |
| Requirements | Node.js; an OpenRouter API key for Jev (optional, word matching without it). |
| License | [MIT](https://github.com/Mou1z/wayfinder/blob/eef790c3feef7e5ec5120d5fb231435b5c2679a2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/openrouter.ts`](https://github.com/Mou1z/wayfinder/blob/eef790c3feef7e5ec5120d5fb231435b5c2679a2/src/providers/openrouter.ts) at the pinned commit. |

## When to use

- Replace a site's results list with one best page for plain-language queries.
- Keep site search from inventing answers.
- Mismatch: works over a page list you write; not a full-text crawler.

## How it works

`src/providers/openrouter.ts` sends the query and your page list as a choice to OpenRouter with default model `typesafe/jev-1.14`; low-confidence answers return suggestions or the fallback. Integration evidence: [`src/providers/openrouter.ts`](https://github.com/Mou1z/wayfinder/blob/eef790c3feef7e5ec5120d5fb231435b5c2679a2/src/providers/openrouter.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install wayfinder-search
# add a search route with createWayfinder({ apiKey: process.env.OPENROUTER_API_KEY, pages: [...] }) as in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Mou1z/wayfinder#readme](https://github.com/Mou1z/wayfinder#readme)

## Limits and data handling

Visitor queries and page descriptions go to OpenRouter and on to TypeSafe; the README says searches are not logged. Jev is reached through OpenRouter.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit eef790c3feef](https://github.com/Mou1z/wayfinder/tree/eef790c3feef7e5ec5120d5fb231435b5c2679a2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
