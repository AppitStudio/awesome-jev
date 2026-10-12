# CrawlHive

[All projects](../README.md) · [Web apps](README.md#web-apps)

Swarm of user-owned crawlers that watch X accounts, Telegram channels and new Solana pairs for memecoin signals; TypeSafe Jev rates every crawler find before a safety scan and an optional Grok Bot review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/h100envy/crawl-hive) |
| Tags | `Open source` · `Pricing unverified` |
| Product homepage | [crawlhive.xyz](https://crawlhive.xyz) |
| Pricing and access | Live app at crawlhive.xyz; pricing and the planned project-token mechanics are not documented as of 2026-10-13. MIT source can be self-hosted with your own OpenRouter/TypeSafe and Grok keys. |
| Jev evidence | [`src/lib/server/crawl/jev.ts`](https://github.com/h100envy/crawl-hive/blob/de06b1c4ce06fd3e294860d1128ce154019ff795/src/lib/server/crawl/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [h100envy](https://github.com/h100envy). Independently curated. |
| Format | Web app (Next.js 16, TypeScript) · MIT |
| Platform and availability | Web (Next.js) · Solana / Robinhood Chain wallets |
| Jev's role | Jev scores each crawler find ("concrete memecoin signal worth a trader's attention?"); low-probability finds are skipped, the rest are scanned most-promising first, and Jev's look/watch/avoid take is final above 70% before Grok is called. |
| Requirements | Node.js; Postgres/Docker per README; OpenRouter key for `typesafe/jev-1.13` for self-hosting. |
| License | [MIT](https://github.com/h100envy/crawl-hive/blob/de06b1c4ce06fd3e294860d1128ce154019ff795/LICENSE) |

## When to use

- Filter noisy social/on-chain crawl results down to signals worth a human look, with a cheap typed gate before expensive LLM research.
- Mismatch: Crypto-trading context; status MVP and a project token is planned. Not financial advice; nothing here was verified against real outcomes.

## How it works

Crawlers fetch sources on a schedule; each find goes to Jev through OpenRouter with a yes/no signal question; the probability gates the safety scan and the optional Grok Bot step, and named tokens are later checked against price. (Summarized from the upstream [README](https://github.com/h100envy/crawl-hive/blob/de06b1c4ce06fd3e294860d1128ce154019ff795/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): open [crawlhive.xyz](https://crawlhive.xyz) or clone the repo and follow the Docker/Next.js setup in the README.

## Limits and data handling

Crawled posts and finds go to OpenRouter/TypeSafe (and to Grok when enabled). Wallet connections and trading decisions are your responsibility. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit de06b1c4ce06](https://github.com/h100envy/crawl-hive/tree/de06b1c4ce06fd3e294860d1128ce154019ff795). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
