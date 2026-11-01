# Pairwise (experiment that compares Jev's drug-interaction answers from names alone with answers grounded in openFDA labels)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small Node.js experiment that probes what Jev knows: for 2 to 8 drugs it checks every pair twice, once from the drug names alone and once against retrieved openFDA interaction label text, and shows both answers side by side with links to DailyMed. A research probe, not a medical tool.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mpgtek/drug-interaction-checker) |
| Maintainer | [mpgtek](https://github.com/mpgtek). Independently curated. |
| Format | Node.js local web app, no dependencies |
| Requirements | Node.js 18+; a TypeSafe API key. |
| License | [MIT](https://github.com/mpgtek/drug-interaction-checker/blob/a7e4816c44734d636a676f3ec80355e688891ce4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/mpgtechsvc/status/2116758746387140773)). |
| Jev evidence | [`checker.mjs`](https://github.com/mpgtek/drug-interaction-checker/blob/a7e4816c44734d636a676f3ec80355e688891ce4/checker.mjs) at the pinned commit. |

## When to use

- Study how Jev's built-in knowledge compares with answers grounded in source text.
- Mismatch: not for clinical decisions.

## How it works

`checker.mjs` sends two `jev-latest` requests per drug pair: one with only the names and one with the openFDA label sections; `server.mjs` keeps the key on the server and serves the comparison UI. Integration evidence: [`checker.mjs`](https://github.com/mpgtek/drug-interaction-checker/blob/a7e4816c44734d636a676f3ec80355e688891ce4/checker.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
TYPESAFE_API_KEY=your_key_here npm start
# open http://localhost:5175
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Announcement on X: [x.com/mpgtechsvc/status/2116758746387140773](https://x.com/mpgtechsvc/status/2116758746387140773)

## Limits and data handling

Not medical advice; results are indirect evidence about model knowledge. Drug names and label excerpts are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit a7e4816c4473](https://github.com/mpgtek/drug-interaction-checker/tree/a7e4816c44734d636a676f3ec80355e688891ce4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
