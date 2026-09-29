# jevbar

[All projects](../README.md) · [Web apps](README.md#web-apps)

Plain-language query box that uses TypeSafe Jev to compose screens (forms, confirmations, rankings, dashboards) from declared parts

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marshallsfolly/jevbar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/marshallsfolly/jevbar#readme) |
| Pricing and access | Free MIT source. Without a TypeSafe key, exact wording still applies; live intent/screen choice needs a key. Checked 2026-09-29. |
| Jev evidence | [Upstream README](https://github.com/marshallsfolly/jevbar/blob/bf1588ad7de73f232041177ffdbf57caacb5d930/README.md): one Jev call (~110–290 ms in the demo) picks parts/layout; exact phrases (dates, IDs) are settled by code first. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live demo/Jev not run on the review host. |
| Maintainer | [marshallsfolly](https://github.com/marshallsfolly). Independently curated. |
| Format | TypeScript · core library + optional React components (MIT; zero runtime deps in core). |
| Platform and availability | Web/React demo in-repo; keyboard and mobile-friendly input patterns documented. |
| Jev's role | Jev chooses which declared UI parts and layout answer the request; code forbids invented field values. |
| Requirements | TypeScript/Node per upstream; optional `TYPESAFE_API_KEY` for model-backed composition. |
| License | [MIT](https://github.com/marshallsfolly/jevbar/blob/bf1588ad7de73f232041177ffdbf57caacb5d930/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when a single NL input should assemble typed UI screens from your own part catalog instead of free-form LLM JSON.

## How it works

Twelve part types (form, confirmation, ranking, …). Jev scores and orders parts; trace marks each field as word-settled or model-chosen.

## Get started

```sh
git clone https://github.com/marshallsfolly/jevbar.git
cd jevbar
git checkout bf1588ad7de73f232041177ffdbf57caacb5d930
# follow upstream README for demo / package use
```

## Examples and demos

README hero GIF/MP4 of five live requests. No live Jev call on the review host.

## Limits and data handling

Without a key, only exact wording applies. Live TypeSafe paths not executed on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit bf1588a](https://github.com/marshallsfolly/jevbar/tree/bf1588ad7de73f232041177ffdbf57caacb5d930). AI-assisted README + LICENSE inspection; install/live paths not executed.
