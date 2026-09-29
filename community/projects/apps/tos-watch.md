# ToS Watch

[All projects](../README.md) · [Web apps](README.md#web-apps)

Email alerts when a company’s data practices change: Open Terms Archive history, TypeSafe Jev classification, static site, and Cloudflare Worker

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/watthem/tos-watch) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [tos.watch](https://tos.watch) |
| Pricing and access | Free Apache-2.0 source and public site. Running classifiers/workers yourself needs TypeSafe (and Cloudflare) credentials as documented. Checked 2026-09-29. |
| Jev evidence | [Upstream README](https://github.com/watthem/tos-watch/blob/67f0f96609583bb374e2a094d024a96da913f86d/README.md): Jev classifies material changes in Terms of Service / privacy diffs in the alert pipeline. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Worker/Jev not run on the review host. |
| Maintainer | [watthem](https://github.com/watthem). Independently curated. |
| Format | Python · classifier + static site + Cloudflare Worker (Apache-2.0). |
| Platform and availability | Public site [tos.watch](https://tos.watch); self-host via repo. |
| Jev's role | Jev judges whether archived ToS/privacy diffs reflect material data-practice changes; code owns fetch, email, and site. |
| Requirements | Python; TypeSafe API key for classification; Cloudflare for Worker path per upstream. |
| License | [Apache-2.0](https://github.com/watthem/tos-watch/blob/67f0f96609583bb374e2a094d024a96da913f86d/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when you want change alerts on privacy/ToS documents with a typed classifier rather than keyword-only diffs.

## How it works

Open Terms Archive history feeds a Jev classifier; notable changes become email alerts and site updates via a Cloudflare Worker.

## Get started

```sh
git clone https://github.com/watthem/tos-watch.git
cd tos-watch
git checkout 67f0f96609583bb374e2a094d024a96da913f86d
# follow upstream README for classifier/worker setup
```

## Examples and demos

Public site [tos.watch](https://tos.watch). No live classification was run on the review host.

## Limits and data handling

Live TypeSafe/Cloudflare paths not executed on the review host. Treat alert quality as author-reported unless reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 67f0f96](https://github.com/watthem/tos-watch/tree/67f0f96609583bb374e2a094d024a96da913f86d). AI-assisted README + LICENSE inspection; live paths not executed.
