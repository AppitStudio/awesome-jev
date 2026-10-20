# Aperture (ranked reading feed)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Single-user, self-hosted intelligence feed that imports Readwise Reader documents and optional public sources (Reddit, GitHub Trending, YouTube, reports, CVEs), has Jev rate each item for quality, personal utility and actionability, and shows a ranked, explainable reading queue with summaries.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/richfairhurst/aperture) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/richfairhurst/aperture#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source; you pay for your own Jev and summary-model calls and hosting. Checked 2026-10-20. |
| Jev evidence | [`src/providers/jev.ts`](https://github.com/richfairhurst/aperture/blob/ddcade772ed37e689287fb0342645b411713ef58/src/providers/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [richfairhurst](https://github.com/richfairhurst). Independently curated. |
| Format | Self-hosted web app (Bun, SQLite) |
| Platform and availability | Self-hosted on a server or VPS; use in any browser. |
| Jev's role | Jev rates each item on the ranking rubric; Aperture orders the queue from those ratings. |
| Requirements | Bun 1.3.11, a TypeSafe key, a Readwise token and a summary model provider; a VPS with Cloudflare Tunnel or a reverse proxy to host it. |
| License | [MIT](https://github.com/richfairhurst/aperture/blob/ddcade772ed37e689287fb0342645b411713ef58/LICENSE) |

## When to use

- Cut a Readwise Reader backlog down to what is useful for your work this week.
- See why an item ranked where it did.
- Mismatch: personal project for one user; not a multi-user service.

## How it works

Collectors normalise new items, and `src/providers/jev.ts` asks Jev at `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) rubric questions such as whether an item is directly useful for work, research or decisions. Ranking combines those answers; a separate server-side model writes the summaries. Answers are validated in `src/validation/jev.ts`. Integration evidence: [`src/providers/jev.ts`](https://github.com/richfairhurst/aperture/blob/ddcade772ed37e689287fb0342645b411713ef58/src/providers/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # provider and auth values
bun install
bun run check
bun run start           # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- config.toml (ranking and cadence defaults)
- tests/jev-client.test.ts and tests/jev-validation.test.ts

## Limits and data handling

Article text goes to TypeSafe and to your summary provider. Magic-link sign-in; public-demo or allowlist modes.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit ddcade772ed3](https://github.com/richfairhurst/aperture/tree/ddcade772ed37e689287fb0342645b411713ef58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
