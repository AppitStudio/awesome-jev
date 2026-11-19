# S1Bench Decision Model Atlas by Jake Cuth (live benchmark of open and hosted decision models against Jev 1.13.0)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Public, read-only leaderboard that scores open and hosted decision models against published Jev 1.13.0 results. Every candidate runs the same six public suites (vitaminc-dev, massive-en-US, boolq, helpsteer2, aegis2 and paws) with identical prompts, and the page reports macro accuracy, the difference from Jev with a paired McNemar test (p < 0.05), speed, calibration (ECE), cost per 1,000 calls and parameter count. It adds a vision subset (496 image and video questions), a Pareto view of size against accuracy, a "decision finder" by constraint (free, local up to 5B, fastest, best value, best calibrated) and CSV export. The author runs the models on his own DGX machine.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://bench.jakecuth.com) |
| Maintainer | Jake Cuth ([@ItsCuthulhu](https://x.com/ItsCuthulhu), [jakecuth.com](https://www.jakecuth.com)). Independently curated. |
| Format | Hosted interactive web page (read-only results). |
| Requirements | A web browser. |
| License | No license stated; no public repository found for the site or its run files. |
| Disclosure | Independent benchmark, not run by TypeSafe. Jev figures are the published Jev 1.13.0 numbers the author compares against, not fresh Jev runs on this site; other results are author-reported and were not reproduced. AI-assisted catalog review; no affiliation with the author. Listing is not an endorsement. Discovered via X ([post](https://x.com/ItsCuthulhu/status/2123526099422335185)). |
| Jev evidence | [bench.jakecuth.com](https://bench.jakecuth.com/) methodology section: Δ Jev compares each model's macro accuracy with published Jev 1.13.0 (76.8%) on shared items. Page fetched 2026-11-20. |

## When to use

- Compare a local or cheaper decision model with Jev before switching a classifier, with significance testing rather than a single accuracy number.
- Mismatch: evaluating your own task; these are six public suites, and results on your data can differ.

## How it works

Each candidate model answers the same prompts on the six public suites. The page compares its correct and incorrect items with the published Jev 1.13.0 results using a paired McNemar test and marks it as beating, tied with or trailing Jev. By default a "Clean only" filter hides models with documented overlap between their training data and the evaluation sources. Speed, calibration error and cost per 1,000 calls are shown next to accuracy.

## Get started

Open [bench.jakecuth.com](https://bench.jakecuth.com/), pick a constraint in the decision finder, or click any model in the leaderboard for its per-suite diagnostics. Use **Export CSV** to take the table with you.

## Examples and demos

- [Author's X thread](https://x.com/ItsCuthulhu/status/2123526099422335185) introducing the atlas, with chart walkthroughs.
- [Live atlas](https://bench.jakecuth.com/).

## Limits and data handling

Results are live and change as runs finish; some models may be partly evaluated. The page says the suggestion form stores your message, optional name or contact and IP address for abuse triage. No license is stated for the data, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) with AI assistance. Primary sources: [bench.jakecuth.com](https://bench.jakecuth.com/) (fetched 2026-11-20) and the author's [X thread](https://x.com/ItsCuthulhu/status/2123526099422335185) (2026-11-19). Catalog de-dupe found no existing listing for this site.
