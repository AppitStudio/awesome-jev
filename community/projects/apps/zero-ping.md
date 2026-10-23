# Zéro Ping (local inbox for lead developers ranked with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local inbox that replaces GitHub notification emails with a ranked list of reviews, replies, PRs and sprint items; Jev ranks lists and gives each PR KPI cards such as production risk, review effort and merge readiness.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Alexandredc/zero-ping) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Product homepage](https://alexandredc.github.io/zero-ping/) |
| Pricing and access | Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-24. |
| Jev evidence | [`src/server/ai/models.ts`](https://github.com/Alexandredc/zero-ping/blob/e138202f78acfa10d050e60774d004c24ff9b65c/src/server/ai/models.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Alexandredc](https://github.com/Alexandredc). Independently curated. |
| Format | Local web app (Next.js) and macOS app |
| Platform and availability | Runs locally on macOS (browser UI, optional Dock app). |
| Jev's role | Ranks inbox lists and scores PR and issue KPIs; urgency estimated by Jev feeds the priority score. |
| Requirements | Node.js 22+ and pnpm; GitHub CLI; optional TypeSafe key for Jev ranking. |
| License | [MIT](https://github.com/Alexandredc/zero-ping/blob/e138202f78acfa10d050e60774d004c24ff9b65c/LICENSE) |

## When to use

- Triage GitHub reviews and mentions in one ranked list.
- See risk and effort at a glance before opening a PR.
- Mismatch: built around GitHub and a local coding agent.

## How it works

`src/server/ai/models.ts` uses `@ai-sdk/typesafe-ai` with `typesafe:jev-latest` by default (`AI_DECISION_MODEL`); Jev is called only when an item's content hash changes. Integration evidence: [`src/server/ai/models.ts`](https://github.com/Alexandredc/zero-ping/blob/e138202f78acfa10d050e60774d004c24ff9b65c/src/server/ai/models.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
pnpm demo   # fictional data, http://localhost:3100
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site: [alexandredc.github.io/zero-ping/](https://alexandredc.github.io/zero-ping/)

## Limits and data handling

Item content is sent to TypeSafe when Jev is configured. No backend run by the author.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit e138202f78ac](https://github.com/Alexandredc/zero-ping/tree/e138202f78acfa10d050e60774d004c24ff9b65c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
