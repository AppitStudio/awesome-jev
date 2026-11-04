# Anyhour (open-source AI for your website that answers visitors, catches leads and pings you on WhatsApp, with Jev cleaning crawled page text)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Open-source website assistant that answers customers from your pages, files and notes, catches leads (who they are and what they want), pings you on your own WhatsApp or Slack, and shows monthly proof from visitors to chats to leads to won. Jev is used in its website text cleanup: each crawled text block gets a knowledge, action, noise or uncertain decision, and only confident noise is removed; a retrieval script also compares search with and without Jev reranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mshahbazm/anyhour.app) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/mshahbazm/anyhour.app#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under AGPL-3.0; you supply providers, hosting and database. Any hosted plan or pricing was not verified. Checked 2026-11-04. |
| Jev evidence | [`packages/api/src/services/knowledge/cleanup/jevRequests.ts`](https://github.com/mshahbazm/anyhour.app/blob/8285909462a4e14239c41155d7e4305c4dd22a75/packages/api/src/services/knowledge/cleanup/jevRequests.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mshahbazm](https://github.com/mshahbazm). Independently curated. |
| Format | Bun workspace (Hono API, React dashboard, PostgreSQL with pgvector) |
| Platform and availability | Self-hosted web app and API with a WhatsApp or Slack channel; a hosted instance may exist (not verified). |
| Jev's role | Optional classifier that labels crawled text blocks and removes confident noise before indexing. |
| Requirements | Bun, PostgreSQL with pgvector, auth and email settings from `.env.example`, and `TYPESAFE_API_KEY` for Jev cleanup. |
| License | [AGPL-3.0](https://github.com/mshahbazm/anyhour.app/blob/8285909462a4e14239c41155d7e4305c4dd22a75/LICENSE) |

## When to use

- Run your own lead-catching website assistant and keep your chats and leads.
- Mismatch: AGPL-3.0, so network use of a modified copy carries source-sharing duties, and Jev cleanup is optional.

## How it works

`packages/api/src/services/knowledge/cleanup/jevRequests.ts` pins `jev-1.13.0` and sends ordered text blocks with nearby context to `https://api.typesafe.ai/v1/systemone`; only valid noise decisions with confidence of at least 0.95 are removed, and missing credentials or invalid responses keep all text. Integration evidence: [`packages/api/src/services/knowledge/cleanup/jevRequests.ts`](https://github.com/mshahbazm/anyhour.app/blob/8285909462a4e14239c41155d7e4305c4dd22a75/packages/api/src/services/knowledge/cleanup/jevRequests.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
# fill packages/api/.env from .env.example, create the pgvector database, then:
bun run db:migrate && bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the setup and cleanup design: [github.com/mshahbazm/anyhour.app#readme](https://github.com/mshahbazm/anyhour.app#readme)

## Limits and data handling

Crawled website text goes to TypeSafe on your key when cleanup is enabled; the README notes provider calls can repeat after a failure. A hosted instance is referenced in the production notes, but its plans and terms were not verified. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 8285909462a4](https://github.com/mshahbazm/anyhour.app/tree/8285909462a4e14239c41155d7e4305c4dd22a75). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
