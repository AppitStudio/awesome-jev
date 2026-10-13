# Goatside

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted personal finance tracker: type spending in plain words and the agent files it, with TypeSafe Jev choosing category and direction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joshxfi/goatside) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/joshxfi/goatside#readme](https://github.com/joshxfi/goatside#readme) |
| Pricing and access | Free MIT source; Vercel, Turso, AI Gateway and TypeSafe usage on your own accounts. |
| Jev evidence | [`packages/ai/src/categorize.ts`](https://github.com/joshxfi/goatside/blob/e321797e2112e2c350ac405c09c52f3299504970/packages/ai/src/categorize.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [joshxfi](https://github.com/joshxfi). Independently curated. |
| Format | Web app (TypeScript monorepo) |
| Platform and availability | Web (self-hosted on Vercel + Turso) |
| Jev's role | Code parses amount, date, split and account; Jev picks the category and money in/out, asking a one-tap question when unsure. |
| Requirements | Vercel; Turso database; AI Gateway; TypeSafe key. |
| License | [MIT](https://github.com/joshxfi/goatside/blob/e321797e2112e2c350ac405c09c52f3299504970/LICENSE) |

## When to use

- Log expenses quickly from a phone and review them on a dashboard.
- Mismatch: Single-user self-hosted only.

## How it works

Entries are parsed deterministically; the Jev filing policy categorizes and learns from confirmed entries; uncertain entries get a quick question. (Summarized from the upstream [README](https://github.com/joshxfi/goatside/blob/e321797e2112e2c350ac405c09c52f3299504970/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): deploy your own copy to Vercel with Turso and keys per the README.

## Limits and data handling

Entry text and amounts go to TypeSafe for filing. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e321797e2112](https://github.com/joshxfi/goatside/tree/e321797e2112e2c350ac405c09c52f3299504970). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
