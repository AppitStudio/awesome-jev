# Jev Fit Scorer

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chromium extension (plus a dependency-free Node CLI) that scores the job posting you have open against your saved resume with one TypeSafe Jev request — fit 0–4 shown out of 10 with confidence, the single strongest factor, and optionally how likely the employer sponsors US visas — with cached results and per-call time and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/akhil-neelam-ai/jev-fit-scorer) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/akhil-neelam-ai/jev-fit-scorer#readme) (unpacked extension; not on the Chrome Web Store). |
| Pricing and access | No fee; load unpacked. Requires your own TypeSafe API key (Jev billed by TypeSafe; README cites $0.042 per million input tokens). Checked 2026-10-08. |
| Jev evidence | [`scoring.js`](https://github.com/akhil-neelam-ai/jev-fit-scorer/blob/726d67d34df481d211a9230c6095deb9318ec4a4/scoring.js) builds the three questions and calls Jev; [`cli.js`](https://github.com/akhil-neelam-ai/jev-fit-scorer/blob/726d67d34df481d211a9230c6095deb9318ec4a4/cli.js) runs the same scoring from the terminal. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [akhil-neelam-ai](https://github.com/akhil-neelam-ai). Independently curated. |
| Format | Chromium MV3 extension + Node CLI |
| Platform and availability | Chrome and other Chromium browsers (Edge, Brave, Comet) on desktop; CLI on Node 18+. |
| Jev's role | Scores resume–job fit, picks the strongest factor and estimates visa sponsorship; the extension only displays and caches. |
| Requirements | A Chromium browser (developer-mode unpacked install) or Node 18+; a TypeSafe API key; your resume pasted as plain text. |
| License | [MIT](https://github.com/akhil-neelam-ai/jev-fit-scorer/blob/726d67d34df481d211a9230c6095deb9318ec4a4/LICENSE). |

## When to use

- Triage many job postings quickly instead of one 'Am I a fit?' click at a time.
- Score from the terminal or pipe a copied job description into the CLI.
- Mismatch: a fit score is a heuristic, not a hiring prediction.

## How it works

One request asks Jev a 0–4 `fit` score across five criteria (level, functional experience, background, stated requirements, adjacent experience), a `why` choice and an optional `visa` yes/no; stated requirements weigh more and Jev is told not to infer what the resume doesn't show.

## Get started

Load the extension (README *Install*) or use the CLI:

```sh
git clone https://github.com/akhil-neelam-ai/jev-fit-scorer.git && cd jev-fit-scorer
# chrome://extensions → Developer mode → Load unpacked → this folder
export TYPESAFE_API_KEY=...
node cli.js --resume resume.txt --job job.txt --company Stripe
```

One Jev request per scored job, billed to your TypeSafe key (cached repeats are free).

## Examples and demos

- README *How the score works* and *Score from the terminal*.

## Limits and data handling

Your resume and the job page text go to TypeSafe. Works on any job page, not only Lenny's Jobs. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 726d67d34df4](https://github.com/akhil-neelam-ai/jev-fit-scorer/tree/726d67d34df481d211a9230c6095deb9318ec4a4). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
