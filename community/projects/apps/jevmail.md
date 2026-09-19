# Jevmail

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local read-only Gmail triage into Needs reply / Updates / Promos / Sales / Spam trays using TypeSafe Jev over the Vercel AI Gateway, with urgency and personal-mail scores kept beside corrections.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fazlerocks/jevmail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/fazlerocks/jevmail#readme) — local Next.js app; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Requires Google OAuth (Gmail API), a Vercel AI Gateway key (`vck_…`), and a local `AUTH_SECRET`. Gateway free-tier rate limits apply unless you buy credits; Gmail API quotas apply. |
| Jev evidence | Inspected [`src/lib/classify.ts`](https://github.com/fazlerocks/jevmail/blob/f6f20af9c2805efd924c29cbea59547e72c558fc/src/lib/classify.ts): one `experimental_evaluate` call to model `typesafe-ai/jev` with parallel choice (tray), score (urgency), and boolean (personal) questions. Live Gmail/Gateway classification was not run. |
| Disclosure | Free source access does not include Google or Gateway usage. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [fazlerocks](https://github.com/fazlerocks). |
| Format | Next.js application (`jevmail` 0.1.0) with local SQLite (Drizzle), Gmail sync, and keyboard-driven reading UI. |
| Platform and availability | Source build with pnpm; Node as required by Next.js 16 tooling in the lockfile. Binds for local `pnpm dev` (default [http://localhost:3000](http://localhost:3000)). Experimental personal tool—tokens and mail cache stay on the machine that runs it. |
| Jev's role | Classifies each fetched message into a tray and scores urgency/personalness; application code stores probabilities, supports human corrections without overwriting Jev's original answer, and never sends mail (read-only). |
| Requirements | pnpm, Google Cloud OAuth Web client with redirect `http://localhost:3000/api/auth/callback/google`, `AI_GATEWAY_API_KEY`, and `AUTH_SECRET`. |
| License | [MIT](https://github.com/fazlerocks/jevmail/blob/f6f20af9c2805efd924c29cbea59547e72c558fc/LICENSE). |

## When to use

Use it for a personal localhost Gmail sorter with tray UI and Gateway-hosted Jev, especially when you want corrections retained separately from model answers. Prefer [Jev Mail Classifier](jev-mail-classifier.md) when you need IMAP/TUI automation that can move or flag messages rather than a read-only web UI.

## How it works

Sync pulls bounded newest messages (and later history/Fetch more), stores them locally, then the drain loop classifies pending rows through [`classify.ts`](https://github.com/fazlerocks/jevmail/blob/f6f20af9c2805efd924c29cbea59547e72c558fc/src/lib/classify.ts). Free-tier pacing defaults keep concurrency low; paid Gateway credits raise throughput. The UI is read-only against Gmail—open-in-Gmail links out rather than sending replies.

## Get started

```sh
git clone https://github.com/fazlerocks/jevmail.git
cd jevmail
git checkout f6f20af9c2805efd924c29cbea59547e72c558fc
pnpm install
cp .env.example .env.local   # AUTH_SECRET, Google client, AI_GATEWAY_API_KEY
pnpm dev
```

Live fetch/sort sends email-derived state to the Vercel AI Gateway / TypeSafe Jev path and reads Gmail. This listing did not complete OAuth or classify live mail.

Offline tests skip without a Gateway key:

```sh
pnpm test   # 6 skipped when AI_GATEWAY_API_KEY is unset
```

## Examples and demos

- Upstream README setup and tray descriptions.
- [`src/lib/classify.test.ts`](https://github.com/fazlerocks/jevmail/blob/f6f20af9c2805efd924c29cbea59547e72c558fc/src/lib/classify.test.ts): live-gated classification cases (skip without key).

## Limits and data handling

Sender, subject, headers, and trimmed body text leave the machine on classify. OAuth tokens and SQLite stay local. Google testing-mode refresh tokens can expire (~7 days). Free Gateway limits throttle large mailboxes. Tray accuracy is not measured here. Read-only against Gmail—still treat OAuth scopes and cached mail as sensitive.

## Review and maintenance

Reviewed on **2026-09-20** at [commit f6f20af](https://github.com/fazlerocks/jevmail/tree/f6f20af9c2805efd924c29cbea59547e72c558fc): `jevmail` **0.1.0**, MIT. AI-assisted source review of classify/drainer/Gmail sync paths, README, and license. On Node.js 24.8.0 with pnpm, **`pnpm test`: 6 skipped** (no `AI_GATEWAY_API_KEY`). No live Gmail, Gateway, or TypeSafe calls were performed.

Related: [Jev Mail Classifier](jev-mail-classifier.md) (IMAP/TUI with mailbox actions).
