# Metis Suite (self-hosted mail and calendar client with an optional Jev decision model)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted mail, calendar and drive client with an AI agent and workflows for Gmail, Outlook, Zoho or any IMAP/SMTP and CalDAV server; an optional decision model (TypeSafe's Jev by default for the `systemone` driver) labels inbox mail, gates thread summaries and powers workflow Ask and Branch steps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trymetis/metis) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/trymetis/metis#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (AGPL-3.0); free to self-host. Decision calls use your own TypeSafe key, OpenAI key or a local server. Checked 2026-10-25. |
| Jev evidence | [`apps/web/src/services/decision/drivers/systemone.ts`](https://github.com/trymetis/metis/blob/13a08f13703adf2c6681af378ef4d72355a34ea9/apps/web/src/services/decision/drivers/systemone.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [trymetis](https://github.com/trymetis). Independently curated. |
| Format | Self-hosted web app (TypeScript, Bun) |
| Platform and availability | Self-hosted web app; local SQLite or Turso database. |
| Jev's role | Optional: each decision-model feature (inbox labels, summary gate, workflow Ask and Branch) has its own switch, all off by default; the LLM still writes text. |
| Requirements | Bun, mail provider OAuth credentials or an IMAP/CalDAV server, an LLM configured; a TypeSafe key (or a local /systemone server) for the decision model. |
| License | [AGPL-3.0](https://github.com/trymetis/metis/blob/13a08f13703adf2c6681af378ef4d72355a34ea9/LICENSE) |

## When to use

- Run your own AI mail client and label incoming mail cheaply with Jev.
- Add yes/no and pick-one branches to mail workflows.
- Mismatch: AGPL-3.0; distinct from the listed Metis GitHub issue-triage Action.

## How it works

`drivers/systemone.ts` uses `@ai-sdk/typesafe-ai` with base URL `https://api.typesafe.ai/v1` by default, or any `/systemone` server such as Ollama 0.35+; the decision model is checked against its server before settings are saved. Integration evidence: [`apps/web/src/services/decision/drivers/systemone.ts`](https://github.com/trymetis/metis/blob/13a08f13703adf2c6681af378ef4d72355a34ea9/apps/web/src/services/decision/drivers/systemone.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp apps/web/.env.example apps/web/.env.local   # database, secrets, one mail provider
bun run db:push && bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- AI models guide: [github.com/trymetis/metis/blob/main/apps/docs/content/self-hosting/02-configure/04-ai-models.mdx](https://github.com/trymetis/metis/blob/main/apps/docs/content/self-hosting/02-configure/04-ai-models.mdx)
- README: [github.com/trymetis/metis#readme](https://github.com/trymetis/metis#readme)

## Limits and data handling

With a decision feature on, sender, subject, a snippet and (where a feature asks) the body go to the decision server, only for mailboxes whose AI toggle is on.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 13a08f13703a](https://github.com/trymetis/metis/tree/13a08f13703adf2c6681af378ef4d72355a34ea9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
