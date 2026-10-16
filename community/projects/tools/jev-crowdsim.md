# jev-crowdsim

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Test a message across an explicit grid of audience traits: Jev returns finite reactions (engage, trust, convert, main objection) for each declared combination, and code computes main effects and Wilson intervals instead of one average.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-crowdsim) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js CLI and library |
| Requirements | Node.js 22+, a TypeSafe API key for live runs (a `--fake` fixture mode needs none). |
| License | [MIT](https://github.com/gbesse/jev-crowdsim/blob/ec9c79e006be51cfe70bd8f2cb7c0b85d409cabf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-client.mjs`](https://github.com/gbesse/jev-crowdsim/blob/ec9c79e006be51cfe70bd8f2cb7c0b85d409cabf/src/jev-client.mjs) at the pinned commit. |

## When to use

- Compare two versions of landing-page or email copy across the same trait grid within a call budget.
- Mismatch: directional triage over a simplified declared model, not user research or a claim about a real population.

## How it works

Each respondent is one trait dictionary; its request asks `would_engage`, `trust`, `would_convert` and one `objection` choice from your list, pinned to `jev-1.13.0`. Up to 64 combinations run as a full factorial, larger spaces use a seeded balanced sample, and `--budget` caps paid calls. Integration evidence: [`src/jev-client.mjs`](https://github.com/gbesse/jev-crowdsim/blob/ec9c79e006be51cfe70bd8f2cb7c0b85d409cabf/src/jev-client.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbesse/jev-crowdsim.git && cd jev-crowdsim
npm run demo
export TYPESAFE_API_KEY=...
node bin/jev-crowdsim.mjs compare a.txt b.txt --design design.json --budget 200
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Experimental design guide: `docs/designs.md`.
- Shareable demo report: `npm run demo:report`.

## Limits and data handling

Your message text and trait levels go to TypeSafe on your key; reports are written locally.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit ec9c79e006be](https://github.com/gbesse/jev-crowdsim/tree/ec9c79e006be51cfe70bd8f2cb7c0b85d409cabf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
