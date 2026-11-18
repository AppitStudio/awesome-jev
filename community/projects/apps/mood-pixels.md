# Mood Pixels by mahshid (mood tracker where Jev reads a few words about your day and suggests a mood, energy and self-care nudge)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Small self-hosted mood tracker (Next.js, PostgreSQL, Drizzle, Better Auth with Google sign-in). Write a few words about your day and Jev classifies the mood (Sparkly, Cozy, Tired, Sad or Frustrated), suggests an energy level and an optional nudge; you review and edit before saving. Monthly calendar and a Year in Pixels view. Guests get a limited number of AI trials; saved entries keep the date, mood, energy and nudge, not your original text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mahshid/mood-pixels) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/mahshid/mood-pixels#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-18. |
| Jev evidence | [`src/app/api/jev/route.ts`](https://github.com/mahshid/mood-pixels/blob/26e8dfb9de2c464b56ba3549ec8717baa862feb4/src/app/api/jev/route.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mahshid](https://github.com/mahshid). Independently curated. |
| Format | Next.js web app with PostgreSQL and Docker Compose (MIT) |
| Platform and availability | Self-hosted web app (localhost or Docker); no hosted instance verified |
| Jev's role | Classifies the check-in text into one of five moods and suggests energy and a self-care nudge with typed questions; the user confirms before saving. |
| Requirements | Node.js, npm, Docker, a Google OAuth client, and `TYPESAFE_API_KEY` for suggestions (manual mood picking works without it). |
| License | [MIT](https://github.com/mahshid/mood-pixels/blob/26e8dfb9de2c464b56ba3549ec8717baa862feb4/LICENSE) |

## When to use

- Run a private mood journal where an AI suggestion is a starting point you can override.
- Mismatch: mental-health care; it is a small journal, not a clinical tool.

## How it works

`src/app/api/jev/route.ts` validates the text (1 to 2000 characters), then uses the TypeSafe SDK's `systemOne` call with a choice question for the mood and further questions for energy and nudge. Integration evidence: [`src/app/api/jev/route.ts`](https://github.com/mahshid/mood-pixels/blob/26e8dfb9de2c464b56ba3549ec8717baa862feb4/src/app/api/jev/route.ts).

## Get started

Copy `.env.example` to `.env`, set the Google, Better Auth, database and TypeSafe values, start PostgreSQL, migrate and run the app.

```sh
git clone https://github.com/mahshid/mood-pixels && cd mood-pixels
cp .env.example .env   # fill in values
npm ci && docker compose up -d db && npx drizzle-kit migrate && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mahshid/mood-pixels/blob/26e8dfb9de2c464b56ba3549ec8717baa862feb4/README.md](https://github.com/mahshid/mood-pixels/blob/26e8dfb9de2c464b56ba3549ec8717baa862feb4/README.md)

## Limits and data handling

Text you submit for a suggestion is sent to TypeSafe on the configured key; the README states the original text is not stored with the entry. Accounts use Google sign-in. It is a hobby-scale project and was not run here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 26e8dfb9de2c](https://github.com/mahshid/mood-pixels/tree/26e8dfb9de2c464b56ba3549ec8717baa862feb4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
