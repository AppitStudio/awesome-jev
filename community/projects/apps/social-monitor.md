# Social Monitor (self-hosted feed that collects X, Reddit, Hacker News, RSS and GitHub posts, with Jev scoring each post's reader value)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted monitor that collects posts and articles across X, Reddit, Hacker News, RSS/Atom, GitHub and Telegram previews for the topics you follow, ranks what matters and turns it into readable AI summaries with source links, daily and four-hour digests and personal interest profiles. Jev (through OpenRouter, with OpenAI Decisions as an alternative) scores each collected post on several reader-value criteria, the database stores the result and code sorts it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/777genius/social-monitor) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://social-monitor.app) |
| Pricing and access | Free source build under Apache-2.0; you pay OpenRouter or OpenAI through your own key and any hosting. The hosted product's pricing was not verified. Checked 2026-11-03. |
| Jev evidence | [`libs/relevance/infrastructure/reader-value/openrouter-reader-value-scorer.ts`](https://github.com/777genius/social-monitor/blob/e5442293fc6d5de6fc2eaae93a6dfade534bdf26/libs/relevance/infrastructure/reader-value/openrouter-reader-value-scorer.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [777genius](https://github.com/777genius). Independently curated. |
| Format | Docker Compose stack (NestJS, Flutter, PostgreSQL, RabbitMQ, Redis) |
| Platform and availability | Self-hosted Docker stack (browser UI); a product site exists. |
| Jev's role | Scores each collected post on reader-value criteria before ranking and summaries. |
| Requirements | Docker with Compose 2.30+; an OpenRouter key (or an OpenAI key with Decisions access) for scoring; provider credentials for X and other sources as documented. |
| License | [Apache-2.0](https://github.com/777genius/social-monitor/blob/e5442293fc6d5de6fc2eaae93a6dfade534bdf26/LICENSE) |

## When to use

- Run your own interest-based feed where a decision model ranks posts before summaries are written.
- Mismatch: RSS and Hacker News work without keys, but Jev scoring and summaries need a provider key, and X collection uses a private collector.

## How it works

`libs/relevance/infrastructure/reader-value/openrouter-reader-value-scorer.ts` posts each post excerpt to `https://openrouter.ai/api/v1/systemone` with the `typesafe/jev-1.13` model and a capability-contrast rubric; the default `jev_primary_v3` mode requires the key and fails at startup rather than silently falling back. Integration evidence: [`libs/relevance/infrastructure/reader-value/openrouter-reader-value-scorer.ts`](https://github.com/777genius/social-monitor/blob/e5442293fc6d5de6fc2eaae93a6dfade534bdf26/libs/relevance/infrastructure/reader-value/openrouter-reader-value-scorer.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/777genius/social-monitor.git
cd social-monitor
./start.sh   # Docker; then open http://localhost:8080/feed
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product site: [social-monitor.app](https://social-monitor.app)
- README with the quick start and provider setup: [github.com/777genius/social-monitor#readme](https://github.com/777genius/social-monitor#readme)

## Limits and data handling

Post excerpts go to OpenRouter (Jev) or OpenAI on your key, and X collection goes through a private collector under that provider's own terms. The repository's own held-out comparison reports for Jev are the author's and not a same-snapshot quality proof. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit e5442293fc6d](https://github.com/777genius/social-monitor/tree/e5442293fc6d5de6fc2eaae93a6dfade534bdf26). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
