# Please.exe

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Private tone coach for Claude and ChatGPT prompts: a local tone meter with suggested edits, plus an optional, explicitly confirmed TypeSafe Jev second opinion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hyper186/please-exe) |
| Tags | `Open source` · `Free` |
| Product homepage | [hyper186.github.io/please-exe/](https://hyper186.github.io/please-exe/) |
| Pricing and access | Free; local mode needs no key. Jev second opinions use your own TypeSafe key (see docs/JEV-SETUP.md). |
| Jev evidence | [`src/server/jev.ts`](https://github.com/hyper186/please-exe/blob/4ce1facddfa9ed457956ecf936599ae45cf5acc1/src/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [hyper186](https://github.com/hyper186). Independently curated. |
| Format | Browser extension (TypeScript) |
| Platform and availability | Chrome extension (beta release zip) · web playground |
| Jev's role | Optional: after you confirm, Jev gives a second opinion on a draft's tone in a separate extension tab; local rules do the default rating. |
| Requirements | Chrome; optional TypeSafe key for Jev mode. |
| License | [MIT](https://github.com/hyper186/please-exe/blob/4ce1facddfa9ed457956ecf936599ae45cf5acc1/LICENSE) |

## When to use

- Catch harsh phrasing before sending a prompt, without telemetry or auto-rewrites.
- Mismatch: Jev is optional; English-first rules.

## How it works

Local rules rate the current message green/amber/red and suggest edits; with Jev enabled and confirmed, the draft is sent for a typed tone judgment shown separately. (Summarized from the upstream [README](https://github.com/hyper186/please-exe/blob/4ce1facddfa9ed457956ecf936599ae45cf5acc1/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): download the beta zip from Releases and load it, or try the web playground.

## Limits and data handling

Only confirmed Jev requests leave the browser. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 4ce1facddfa9](https://github.com/hyper186/please-exe/tree/4ce1facddfa9ed457956ecf936599ae45cf5acc1). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
