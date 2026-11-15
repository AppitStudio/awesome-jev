# Broccoli (open-source employee operations system that uses Jev decisions to read imported HR files and set up time-off rules)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted Employee Operations System (people records, time off and related HR workflows) by Minari Limited, built for teams that work alongside agents. Its AI layer asks only multiple-choice decision questions: when you import a spreadsheet, Jev decides which row is the header and which column holds which field, and during time-off setup it answers questions about your locations. Personal values are masked as placeholders before a request leaves the install, and answers under a confidence floor are treated as no answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/getbroccoli/broccoli) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://getbroccoli.com) |
| Pricing and access | Self-hosting is free under AGPL-3.0; bring an OpenRouter key or use a free Broccoli AI token (the code references a free period, so terms may change). Hosted pricing not published (waitlist). Checked 2026-11-15. |
| Jev evidence | [`packages/api/src/integrations/ai/decisions.ts`](https://github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/packages/api/src/integrations/ai/decisions.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [getbroccoli](https://github.com/getbroccoli). Independently curated. |
| Format | TypeScript monorepo (pnpm, Docker Compose) |
| Platform and availability | Web (self-hosted with Docker Compose; hosted version via waitlist) |
| Jev's role | Jev answers the multiple-choice decisions behind file imports (header row, column mapping) and time-off setup. |
| Requirements | Docker Compose; for AI decisions either your own OpenRouter key or a free Broccoli AI token issued by the maker's service. |
| License | [AGPL-3.0](https://github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/LICENSE) |

## When to use

- Self-host HR operations where imports are mapped by typed decisions instead of generated text.
- Mismatch: teams wanting a finished hosted product today; the hosted version is waitlist-only.

## How it works

`packages/api/src/integrations/ai/decisions.ts` pins `typesafe/jev-1.13` and requests no-retention providers; `resolvedDecisions.ts` routes each request to OpenRouter with the install's key or to Broccoli AI; `modules/imports/app/fileSourceService.ts` uses it for header-row and column mapping. Integration evidence: [`packages/api/src/integrations/ai/decisions.ts`](https://github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/packages/api/src/integrations/ai/decisions.ts).

## Get started

Start it with Docker Compose and open the app.

```sh
git clone https://github.com/getbroccoli/broccoli && cd broccoli
docker compose up    # http://localhost:8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/README.md](https://github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/README.md)
- Setup guide: [github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/docs/guides/setup-guide.md](https://github.com/getbroccoli/broccoli/blob/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1/docs/guides/setup-guide.md)

## Limits and data handling

Decision requests carry masked placeholders rather than personal values; they go to OpenRouter (no-retention providers) on your key, or through the maker's Broccoli AI service when you use its free token. The Broccoli name and logo are covered by a trademark policy.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit e017a8a3f2d9](https://github.com/getbroccoli/broccoli/tree/e017a8a3f2d9a6d3693e3b812bfc389e0b9f84e1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
