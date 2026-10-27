# The right model for each step (experiment: Jev picks the skill, Claude fetches it)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small experiment on 53 Hebrew questions from the mekomIL skill catalog: Jev makes three short decisions (is a skill needed, which category, which skill) before Claude Sonnet 5.5 fetches it, compared with Claude doing it alone; the author reports median time to the right skill falling from 5.1 s to 1.5 s, with a bilingual results page.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ilanvys/jev-mekomil-study) |
| Maintainer | [ilanvys](https://github.com/ilanvys). Independently curated. |
| Format | Python experiment with results page |
| Requirements | Python 3; a TypeSafe API key and an Anthropic key to rerun. |
| License | [MIT](https://github.com/ilanvys/jev-mekomil-study/blob/0944bd09f7eca82e23acb0233821133b2776056c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.py`](https://github.com/ilanvys/jev-mekomil-study/blob/0944bd09f7eca82e23acb0233821133b2776056c/run.py) at the pinned commit. |

## When to use

- See how splitting a skill-selection step off to a decision model affects latency.
- Reuse the two-route setup for your own skill catalog.
- Mismatch: one catalog and language; timings are the author's.

## How it works

`run.py` posts each question to `https://api.typesafe.ai/v1/systemone` with `jev-1.13.0` for the three routing decisions, then passes a note naming the skill to Claude. Integration evidence: [`run.py`](https://github.com/ilanvys/jev-mekomil-study/blob/0944bd09f7eca82e23acb0233821133b2776056c/run.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ilanvys/jev-mekomil-study && cd jev-mekomil-study
# set TYPESAFE_API_KEY and your Anthropic key, then run run.py as in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results page (Hebrew and English): [ilanvys.github.io/jev-mekomil-study/](https://ilanvys.github.io/jev-mekomil-study/)
- README: [github.com/ilanvys/jev-mekomil-study#readme](https://github.com/ilanvys/jev-mekomil-study#readme)

## Limits and data handling

Questions go to TypeSafe and Anthropic when rerun. Results are the author's. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 0944bd09f7ec](https://github.com/ilanvys/jev-mekomil-study/tree/0944bd09f7eca82e23acb0233821133b2776056c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
