# AI PM Job Radar

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Every open PM role at 36 AI and tech companies, sorted by Jev (via Vercel AI Gateway) into AI PM without ML, AI PM with ML, non-AI PM and not-a-PM-role.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aakashg/ai-pm-job-radar) |
| Maintainer | [aakashg](https://github.com/aakashg). Independently curated. |
| Format | Node.js pipeline + Next.js site |
| Requirements | Node.js; Vercel AI Gateway key. |
| License | [MIT](https://github.com/aakashg/ai-pm-job-radar/blob/82f3114f87c5158533415455f5c00268914ea601/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/label.mjs`](https://github.com/aakashg/ai-pm-job-radar/blob/82f3114f87c5158533415455f5c00268914ea601/pipeline/label.mjs) at the pinned commit. |

## When to use

- Browse AI product-manager openings sorted better than title regexes.
- Reuse the labeling pipeline for other job-classification tasks.
- Mismatch: covers a fixed list of companies.

## How it works

The pipeline fetches postings, then sends each to Jev through Vercel AI Gateway with choice, score and yes/no questions; labels drive the site's groups. Integration evidence: [`pipeline/label.mjs`](https://github.com/aakashg/ai-pm-job-radar/blob/82f3114f87c5158533415455f5c00268914ea601/pipeline/label.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env
npm run fetch
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pipeline spec: `pipeline/spec.json`.

## Limits and data handling

Job postings (public data) are sent to Jev via Vercel AI Gateway and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 82f3114f87c5](https://github.com/aakashg/ai-pm-job-radar/tree/82f3114f87c5158533415455f5c00268914ea601). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
