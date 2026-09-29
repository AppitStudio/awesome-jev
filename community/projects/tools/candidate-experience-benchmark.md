# Candidate Experience Feedback Benchmark

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Benchmark comparing TypeSafe Jev vs LLMs on 60 synthetic candidate-experience reviews across four typed classification tasks

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adambkovacs/candidate-experience-benchmark) |
| Maintainer | [adambkovacs](https://github.com/adambkovacs). Independently curated. |
| Format | HTML/JS · reproducible evidence packs + public explorer (MIT). |
| Requirements | Browse published results offline; regenerating runs needs provider keys per upstream docs. |
| License | [MIT](https://github.com/adambkovacs/candidate-experience-benchmark/blob/bcfbb8f6c0cee20dd5264595599f759f2ffcaf1b/LICENSE). Provider usage may incur charges when regenerating. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Development findings on synthetic reviews — not a held-out leaderboard. Live re-runs not executed on the review host. |

## When to use

Use when comparing System One vs general LLMs on HR-feedback style classifications with saved costs/tokens and prompt variants.

## How it works

Sixty fictional reviews; four judgments (sentiment, follow-up, serious concern, testimonial potential). Published explorer and reports include Jev and many LLM configurations.

## Get started

```sh
git clone https://github.com/adambkovacs/candidate-experience-benchmark.git
cd candidate-experience-benchmark
git checkout bcfbb8f6c0cee20dd5264595599f759f2ffcaf1b
# explore: https://adambkovacs.github.io/candidate-experience-benchmark/
```

## Examples and demos

[Public explorer](https://adambkovacs.github.io/candidate-experience-benchmark/) and `results/comparison/REPORT.md`. No live re-run on the review host.

## Limits and data handling

References were AI-assisted; no independent human adjudication claimed. Scores are development observations on the same 60 reviews.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit bcfbb8f](https://github.com/adambkovacs/candidate-experience-benchmark/tree/bcfbb8f6c0cee20dd5264595599f759f2ffcaf1b). AI-assisted README + LICENSE inspection; live regeneration not executed.
