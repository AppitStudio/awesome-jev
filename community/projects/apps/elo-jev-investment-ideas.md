# Elo Jev 4 Investment Ideas

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local tournament app that ranks investment ideas for further research: TypeSafe Jev judges pairwise matchups per weighted criterion and an Elo leaderboard emerges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DidierRLopes/elo-jev-4-investment-ideas) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/DidierRLopes/elo-jev-4-investment-ideas#readme](https://github.com/DidierRLopes/elo-jev-4-investment-ideas#readme) |
| Pricing and access | Free MIT source; judging calls billed to your TypeSafe key. |
| Jev evidence | [`judge.mjs`](https://github.com/DidierRLopes/elo-jev-4-investment-ideas/blob/9df9048e91bf785c77e95bb381a77880bcc53642/judge.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [DidierRLopes](https://github.com/DidierRLopes). Independently curated. |
| Format | Local web app (JavaScript) |
| Platform and availability | Web (local Node server) |
| Jev's role | Jev compares two ideas at a time on each criterion prompt; the app turns outcomes into Elo ratings. |
| Requirements | Node.js; TypeSafe key. |
| License | [MIT](https://github.com/DidierRLopes/elo-jev-4-investment-ideas/blob/9df9048e91bf785c77e95bb381a77880bcc53642/LICENSE) |

## When to use

- Prioritize a pile of research ideas with an editable rubric instead of one-shot scoring.
- Mismatch: Research triage only, not investment advice; screenshots use a mocked judge.

## How it works

You select ideas and edit criteria and weights; the server runs pairwise matches through Jev and updates Elo ratings live. (Summarized from the upstream [README](https://github.com/DidierRLopes/elo-jev-4-investment-ideas/blob/9df9048e91bf785c77e95bb381a77880bcc53642/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install, set your key in `.env`, start the server, and open the Setup page.

## Limits and data handling

Idea text and criteria go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 9df9048e91bf](https://github.com/DidierRLopes/elo-jev-4-investment-ideas/tree/9df9048e91bf785c77e95bb381a77880bcc53642). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
