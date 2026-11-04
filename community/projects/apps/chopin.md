# Chopin (GitHub Next research prototype for writing plans and specs with a repository-grounded agent, with Jev optionally judging chat turns and cards)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted research prototype where people and a hosted agent write one repository-grounded document together, with chat, decisions and research briefs. A decisions classifier, either OpenAI's Decisions API or TypeSafe's Jev (via `JEV_API_KEY`), judges when the agent should speak in group chat, proposes optional conversation cards, and routes explanatory visuals. GitHub calls it experimental research software, not a supported product, and offers no public instance.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/githubnext/chopin) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/githubnext/chopin#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you provide hosting, a GitHub App and your own model keys, and no hosted instance is offered. Checked 2026-11-04. |
| Jev evidence | [`apps/server/src/config.ts`](https://github.com/githubnext/chopin/blob/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f/apps/server/src/config.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [githubnext](https://github.com/githubnext). Independently curated. |
| Format | TypeScript monorepo (Bun, PostgreSQL, GitHub App sign-in) |
| Platform and availability | Self-hosted web app (run locally or on your own server); no hosted instance is offered. |
| Jev's role | Optional decisions classifier for group-chat turn-taking, conversation cards and visual routing. |
| Requirements | Bun, Docker for PostgreSQL, a GitHub App, an agent harness credential, and `OPENAI_API_KEY` or `JEV_API_KEY` for the decisions model. |
| License | [MIT](https://github.com/githubnext/chopin/blob/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f/LICENSE.md) |

## When to use

- Study how a typed decisions model can handle turn-taking and card proposals in a collaborative agent workspace.
- Mismatch: it is experimental, needs a GitHub App and database, and Jev is one of two supported decisions backends.

## How it works

`apps/server/src/config.ts` selects `typesafe/jev-latest` as the decisions model when `JEV_API_KEY` or `TYPESAFE_API_KEY` is set; `conversation-plan/decisions.ts` sends typed questions and turns the answers into scheduling and card decisions. Integration evidence: [`apps/server/src/config.ts`](https://github.com/githubnext/chopin/blob/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f/apps/server/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp .env.example .env   # add GitHub App values and OPENAI_API_KEY or JEV_API_KEY
bun run db:up && bun run migrate && bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the architecture and privacy notes: [github.com/githubnext/chopin#readme](https://github.com/githubnext/chopin#readme)
- Automatic participation and the decisions model: [github.com/githubnext/chopin/blob/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f/docs/conversation-initiative.md](https://github.com/githubnext/chopin/blob/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f/docs/conversation-initiative.md)

## Limits and data handling

With Jev selected, recent chat messages and decision context go to TypeSafe on your key. The README warns of incomplete workflows and breaking changes, and says no public instance exists. Not affiliated with TypeSafe; published by GitHub Next.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 2c3d86cbd17b](https://github.com/githubnext/chopin/tree/2c3d86cbd17b2801fd8d5c756e1598d2aad71e1f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
