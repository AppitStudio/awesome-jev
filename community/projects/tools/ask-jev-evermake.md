# Ask Jev by evermake (finds relevant passages in public llms.txt documentation with Jev, returning the docs as written)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

pnpm workspace with an Effect library, a Cloudflare Worker + SQLite Durable Object API and a React playground: it walks a site's llms.txt and Markdown pages best-first, asks Jev which sections are relevant, and returns the documentation passages as written instead of a generated answer. Visitors bring their own TypeSafe key and pay for their own searches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/evermake/ask-jev) |
| Maintainer | [evermake](https://github.com/evermake). Independently curated. |
| Format | TypeScript monorepo: library, Cloudflare Worker API and React playground (no license file) |
| Requirements | Node.js 24+, pnpm, a Cloudflare account to deploy, and a TypeSafe key per visitor. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ask-jev/src/SystemOne.ts`](https://github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/ask-jev/src/SystemOne.ts) at the pinned commit. |

## When to use

- Pull the exact documentation passages an agent or person needs from an llms.txt site.
- Mismatch: if you want synthesized answers; it only returns source passages.

## How it works

`ask-jev/src/SystemOne.ts` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default (`jev-preview` selectable in the playground). All fetching, caching and Jev calls run in the Durable Object; the visitor's key is request-scoped and the displayed budget is an estimate, not a billing cap. Integration evidence: [`ask-jev/src/SystemOne.ts`](https://github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/ask-jev/src/SystemOne.ts).

## Get started

Install the workspace and run the playground locally, as described in the README and ARCHITECTURE.md.

```sh
git clone https://github.com/evermake/ask-jev && cd ask-jev
pnpm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/README.md](https://github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/README.md)
- Architecture: [github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/ARCHITECTURE.md](https://github.com/evermake/ask-jev/blob/f6305e0110545e011e70c79caaa5065c8b840fca/ARCHITECTURE.md)

## Limits and data handling

Your search query and documentation sections go to TypeSafe on the visitor's key; only approved documentation hostnames are fetched.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit f6305e011054](https://github.com/evermake/ask-jev/tree/f6305e0110545e011e70c79caaa5065c8b840fca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
