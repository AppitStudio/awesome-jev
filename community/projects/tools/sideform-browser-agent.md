# @sideform/browser-agent

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Goal-driven browser agent library in TypeScript (controller, step policy, browse_task loop) whose step policy uses a System One decision client such as TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dan-rozhkov/browser-agent) |
| Maintainer | [dan-rozhkov](https://github.com/dan-rozhkov). Independently curated. |
| Format | TypeScript library (npm package layout) |
| Requirements | Node.js; browser target per adapters; TypeSafe key; OpenRouter key for text models. |
| License | [MIT](https://github.com/dan-rozhkov/browser-agent/blob/22e462c894f1586cc0e361e1e1d0b5d40697f9ed/LICENSE) |
| Jev evidence | [`src/policy/decide.ts`](https://github.com/dan-rozhkov/browser-agent/blob/22e462c894f1586cc0e361e1e1d0b5d40697f9ed/src/policy/decide.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Embed a snapshot→decide→act browser loop in your own app.
- Mismatch: text-only Jev policy (no screenshots); extracted from another product's stack.

## How it works

The controller snapshots a tab, the policy asks the decision client to pick the next step, and the loop acts until done, blocked or out of budget, returning a transcript. (Summarized from the upstream [README](https://github.com/dan-rozhkov/browser-agent/blob/22e462c894f1586cc0e361e1e1d0b5d40697f9ed/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `TYPESAFE_API_KEY=... OPENROUTER_API_KEY=... npm run example -- "open example.com and read the heading"`.

## Limits and data handling

Page snapshots go to TypeSafe; planning text to OpenRouter. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 22e462c894f1](https://github.com/dan-rozhkov/browser-agent/tree/22e462c894f1586cc0e361e1e1d0b5d40697f9ed). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
