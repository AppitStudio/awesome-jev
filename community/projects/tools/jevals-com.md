# Jevals.com

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hosted independent benchmark boards: TypeSafe Jev (`typesafe-ai/jev` via Vercel AI Gateway) vs six LLMs on PubMedQA (Noul), Banking77 (Choice), and HelpSteer2 (Score)—accuracy, calibration, coverage@threshold, cost, and latency. Distinct from the local [jevals](jevals.md) workbench (dayhaysoos).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jevals.com/) |
| Maintainer | [Jevals](https://github.com/Jevals) (community issue [#372](https://github.com/AppitStudio/awesome-jev/issues/372)). Independently curated listing of a maintainer-submitted resource; not a TypeSafe endorsement. |
| Format | Hosted release boards + methodology pages; open data at [Jevals/jevals-data](https://github.com/Jevals/jevals-data) (CC BY 4.0). Harness code is private. |
| Requirements | Browser only to read boards. No account required for the public site (checked 2026-09-23). Recomputing numbers needs the published data repo—not the private harness. |
| License | Site: free to read (no paid tier stated). Data: [CC BY 4.0](https://github.com/Jevals/jevals-data). Harness: closed / not published. |
| Disclosure | AI-assisted catalog review of the public site, issue #372, and jevals-data metadata. Implementation of the private harness was **not** inspected. Metrics and methodology are vendor/maintainer-reported; this listing did not re-run the suite. Listing is not an endorsement. |

## When to use

Use it to inspect how hosted Jev confidence trades off against accuracy/cost/latency on labelled decision tasks vs adapter-prompted LLMs. Prefer [jevals](jevals.md) when you want to author and run local Noul/Choice/Score cases yourself.

## How it works

Per maintainer description: same typed questions graded against human labels (300 items × 5 runs). Boards report accuracy, calibration error, coverage and accuracy at confidence thresholds, cost per 1k decisions, and p95 latency. Per-decision logs and suite files ship in jevals-data so numbers can be recomputed without the harness.

## Get started

1. Open [jevals.com](https://jevals.com/) and the [methodology](https://jevals.com/methodology/) pages.
2. Optional: browse [Jevals/jevals-data](https://github.com/Jevals/jevals-data) for CC BY 4.0 boards and logs.

## Examples and demos

- Public boards on the homepage (Noul/Choice/Score).
- Atom feed linked from the site for releases.
- Issue #372 details pinning by release date (e.g. 2026-09-18) when Gateway omits a version string.

## Limits and data handling

One published release slice, three English tasks; harness not reproducible as-is. Visiting the site may involve analytics (Google tags observed in HTML). This listing did not verify every board cell against the data repo.

## Review and maintenance

Reviewed on **2026-09-23**: site HTTP 200; issue #372; jevals-data CC BY 4.0. AI-assisted public-artifact review only.

Related: [jevals](jevals.md), [agent-evals](agent-evals.md), [chinese-workflow-decision-bench](chinese-workflow-decision-bench.md).
