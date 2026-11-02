# PaperWing (open-web reader organised by topic, with Jev grading how heated a discussion is)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Ad-free reader that pulls Hacker News, Lobsters, Bluesky, RSS, arXiv and engineering blogs into topics rather than sources, merges duplicate links and ranks across sources with a recipe that runs on your device. Jev powers an optional spice rating: a score question and four yes/no questions grade how heated a thread's discussion is.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jordan-simonovski/paperwing) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://tech-reader-nine.vercel.app) |
| Pricing and access | Free hosted app with no accounts or ads (reader donations via Ko-fi); free source build under Apache-2.0. Checked 2026-11-02. |
| Jev evidence | [`api/_lib/spice.ts`](https://github.com/jordan-simonovski/paperwing/blob/acc1b6c7d4d169452fa6d80cfb01039a72739af9/api/_lib/spice.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jordan-simonovski](https://github.com/jordan-simonovski). Independently curated. |
| Format | Web app (Vite + serverless API) |
| Platform and availability | Web; self-host from source. |
| Jev's role | Grades how heated a thread's discussion is. |
| Requirements | A browser for the hosted app; Node.js to self-host; `TYPESAFE_API_KEY` and Upstash for spice grading. |
| License | [Apache-2.0](https://github.com/jordan-simonovski/paperwing/blob/acc1b6c7d4d169452fa6d80cfb01039a72739af9/LICENSE) |

## When to use

- Read tech and news discussions by topic and see which threads are heated.
- Mismatch: Jev is only the spice grader; the rest of the reader works without it.

## How it works

`api/_lib/spice.ts` sends the trimmed top of a discussion to Jev with one score question and four noul questions, and code turns the answers into a chilli level; a daily limit caps cost. Integration evidence: [`api/_lib/spice.ts`](https://github.com/jordan-simonovski/paperwing/blob/acc1b6c7d4d169452fa6d80cfb01039a72739af9/api/_lib/spice.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted app: [tech-reader-nine.vercel.app](https://tech-reader-nine.vercel.app)

## Limits and data handling

Discussion text is sent to TypeSafe for spice grading. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit acc1b6c7d4d1](https://github.com/jordan-simonovski/paperwing/tree/acc1b6c7d4d169452fa6d80cfb01039a72739af9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
