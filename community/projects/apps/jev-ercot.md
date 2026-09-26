# jev-ercot

[All projects](../README.md) · [Web apps](README.md#web-apps)

Texas Power-to-Choose shopper: Jev classifies EFL text; code computes plan costs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cdubiel08/jev-ercot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/cdubiel08/jev-ercot#readme) |
| Pricing and access | MIT source build; bring your own TypeSafe key for live classify/rebuild. No app purchase fee; TypeSafe usage separate. Checked **2026-09-27**. |
| Jev evidence | Pipeline modules under [`web/src/pipeline/`](https://github.com/cdubiel08/jev-ercot/tree/b1c0563077578835d3623811221e6a792c6ad64b/web/src/pipeline) and classify scripts; README describes batched System One questions over EFL text. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live classify/provider paths not run on the review host. |
| Maintainer | [cdubiel08](https://github.com/cdubiel08). Independently curated. |
| Format | Next.js app + Bun/TypeScript classification pipeline. |
| Platform and availability | Source-built Next.js web app; static classified corpus committed under `web/src/data/`. |
| Jev's role | Classifies Electricity Facts Label spans and sentence families; application code owns cost math and ranking. |
| Requirements | Node/Bun for web; TypeSafe key only for live classify page or rebuild pipeline. |
| License | [MIT](https://github.com/cdubiel08/jev-ercot/blob/b1c0563077578835d3623811221e6a792c6ad64b/LICENSE). |

## When to use

Use to explore Texas competitive electric plans with inspectable Jev judgments. Not a brokerage or enrollment service.

## How it works

Regex candidates + batched Jev Choice/Noul/Score over EFL text; code turns picks into numbers and verifies against EFL price tables.

## Get started

```sh
git clone https://github.com/cdubiel08/jev-ercot.git
cd jev-ercot/web
git checkout b1c0563077578835d3623811221e6a792c6ad64b
npm install
npm run build
```

Pin revision `b1c0563077578835d3623811221e6a792c6ad64b` when reproducing this review.

## Examples and demos

Committed `plans.json` corpus powers the static shopper UI. Live `/classify` needs a server TypeSafe key.

## Limits and data handling

Corpus is as of the committed export date. Live classify sends pasted EFL text to TypeSafe. Full document fetch/rebuild needs extra tooling.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit b1c0563](https://github.com/cdubiel08/jev-ercot/tree/b1c0563077578835d3623811221e6a792c6ad64b). AI-assisted README and LICENSE inspection; live paths not executed.
