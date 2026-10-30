# Accurate and Useless (article and anonymized data from 5,300 Jev calls in a multi-agent coding pipeline)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Article, figures and anonymized data from a 16-day trial of Jev inside a multi-agent build pipeline for Claude Code, testing advisory checks, an on-demand tool for agents and binding gates. Jev answered 4,222 calls across five real builds plus 1,092 offline; the authors report that most label sets had a single class, so no check showed reliable judging and the hoped-for token savings were never measured. `recompute.mjs` rebuilds all 103 published numbers from the data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sash-ua/jev-experiments) |
| Maintainer | [sash-ua](https://github.com/sash-ua). Independently curated. |
| Format | Article + CSV data + Node.js recompute script |
| Requirements | Node.js 18+ to recompute; no API key (no new Jev calls are made). |
| License | [CC BY 4.0 (article, data) + MIT (code)](https://github.com/sash-ua/jev-experiments/blob/ab16ec4d41d665fd0250ebeb4c3ff7ace2ffc06f/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`data/field-calls.csv`](https://github.com/sash-ua/jev-experiments/blob/ab16ec4d41d665fd0250ebeb4c3ff7ace2ffc06f/data/field-calls.csv) at the pinned commit. |

## When to use

- Learn how to design label sets and baselines before judging whether a small judge model saves tokens.
- Mismatch: an experience report from one team's pipeline; the pipeline source is not published.

## How it works

`data/field-calls.csv` holds one row per Jev call in the five builds, with answers, labels and gate outcomes in sibling files; `recompute.mjs` checks every figure against the article. Integration evidence: [`data/field-calls.csv`](https://github.com/sash-ua/jev-experiments/blob/ab16ec4d41d665fd0250ebeb4c3ff7ace2ffc06f/data/field-calls.csv).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sash-ua/jev-experiments
cd jev-experiments
node recompute.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Article (DEV): [dev.to/sashua/accurate-and-useless-what-5300-calls-to-a-small-judge-model-taught-us-1i92](https://dev.to/sashua/accurate-and-useless-what-5300-calls-to-a-small-judge-model-taught-us-1i92)

## Limits and data handling

Data is an anonymized extract; full logs stay private. Article, figures and data are CC BY 4.0; code is MIT. Not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit ab16ec4d41d6](https://github.com/sash-ua/jev-experiments/tree/ab16ec4d41d665fd0250ebeb4c3ff7ace2ffc06f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
