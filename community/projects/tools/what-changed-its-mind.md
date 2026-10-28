# What Changed Its Mind? (does more evidence improve Jev's election forecasts, or only make them more certain?)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open research essay on competitive 2026 US midterm races: explore a map, add evidence, inspect the exact Jev requests and compare precomputed changes when candidate or source order changes. The first frozen release has three Senate races and 23 valid forecasts; the author stresses it is an experiment, not a calibrated election forecast.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prashaantr/what-changed-its-mind) |
| Maintainer | [prashaantr](https://github.com/prashaantr). Independently curated. |
| Format | Python pipeline and web app (site on GitHub Pages) |
| Requirements | Python 3.12+ with uv and Node 24+; a TypeSafe API key only to collect new forecasts. |
| License | [MIT](https://github.com/prashaantr/what-changed-its-mind/blob/fdc1f1eb262828744e40ab09506f568df54f2a7e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/jev_elections/jev.py`](https://github.com/prashaantr/what-changed-its-mind/blob/fdc1f1eb262828744e40ab09506f568df54f2a7e/pipeline/jev_elections/jev.py) at the pinned commit. |

## When to use

- Study order effects and evidence sensitivity in a decision model.
- Mismatch: small sample; not a forecast.

## How it works

`pipeline/jev_elections/jev.py` posts each race's evidence to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.14.0` and stores every request and answer. Integration evidence: [`pipeline/jev_elections/jev.py`](https://github.com/prashaantr/what-changed-its-mind/blob/fdc1f1eb262828744e40ab09506f568df54f2a7e/pipeline/jev_elections/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/prashaantr/what-changed-its-mind && cd what-changed-its-mind
uv sync --locked --extra dev
npm --prefix apps/web ci && npm --prefix apps/web run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site: [prashaantr.github.io/what-changed-its-mind/](https://prashaantr.github.io/what-changed-its-mind/)
- Initial report: [github.com/prashaantr/what-changed-its-mind/blob/codex/what-changed-its-mind/docs/INITIAL_REPORT.md](https://github.com/prashaantr/what-changed-its-mind/blob/codex/what-changed-its-mind/docs/INITIAL_REPORT.md)

## Limits and data handling

Public race material goes to TypeSafe during collection. Stored results replay without a key.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit fdc1f1eb2628](https://github.com/prashaantr/what-changed-its-mind/tree/fdc1f1eb262828744e40ab09506f568df54f2a7e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
