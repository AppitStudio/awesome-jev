# Tacet

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Marketing decision layer that can choose to send nothing: code applies consent and frequency caps, Jev picks the next best action or budget move among what is allowed, and anything under 60% confidence goes to a person. Compares raw CRM records with compact jev-state input.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suranjaychandra/jev-decision-layer) |
| Maintainer | [suranjaychandra](https://github.com/suranjaychandra). Independently curated. |
| Format | TypeScript benchmark and dashboard (npm scripts; static dashboard on GitHub Pages) |
| Requirements | Node.js; a TypeSafe API key for live runs (tests and `--dry` runs need none). |
| License | [MIT](https://github.com/suranjaychandra/jev-decision-layer/blob/5c8e5093e04dddff9b780a4533ac4a05d3c92509/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/nba/run.ts`](https://github.com/suranjaychandra/jev-decision-layer/blob/5c8e5093e04dddff9b780a4533ac4a05d3c92509/src/nba/run.ts) at the pinned commit. |

## When to use

- Prototype next-best-action or ad budget steering where waiting is a valid, often correct, answer.
- Measure how much a cleaned-up state format changes accuracy, review rate and tokens on the same rules and model.
- Mismatch: synthetic seeded customers and ads; the results measure this design end to end, not Uplane's system.

## How it works

Hard limits stay in code: actions blocked by consent or caps are removed before Jev sees the question. `src/nba/run.ts` asks Jev through the TypeSafe SDK, once with the raw record and once with jev-state facts, using `pick()` from jev-state; low-confidence choices go to review. The author reports 80.6% to 95.6% accuracy on the next-best-action test set. Integration evidence: [`src/nba/run.ts`](https://github.com/suranjaychandra/jev-decision-layer/blob/5c8e5093e04dddff9b780a4533ac4a05d3c92509/src/nba/run.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm test                     # no network, no API key
npm run nba -- --dry         # print what would be sent
npm run nba -- --limit 5     # 10 live Jev calls with TYPESAFE_API_KEY in .env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Dashboard replaying saved answers: [suranjaychandra.github.io/jev-decision-layer/](https://suranjaychandra.github.io/jev-decision-layer/)
- Built on [github.com/suranjaychandra/jev-state](https://github.com/suranjaychandra/jev-state).

## Limits and data handling

Synthetic customer records go to TypeSafe on your key in live runs. Accuracy figures are the author's own runs on `jev-1.13.0`.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 5c8e5093e04d](https://github.com/suranjaychandra/jev-decision-layer/tree/5c8e5093e04dddff9b780a4533ac4a05d3c92509). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
