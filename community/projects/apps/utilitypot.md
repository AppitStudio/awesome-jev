# UtilityPot

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free web utilities for messy data, shared text, diagrams and planning: browser-local CSV/JSON conversion, date cleanup and meeting-time finder, plus three bounded Jev tools for custom entity extraction, text-to-Mermaid flowcharts and finding the exact paragraphs on a webpage that answer a question.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tugrulguner/utilitypot) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://utilitypot.modepot.io/) |
| Pricing and access | Free hosted app, no signup (per the project README). Self-hosting needs your own TypeSafe key. Checked 2026-10-17. |
| Jev evidence | [`worker/index.js`](https://github.com/tugrulguner/utilitypot/blob/dae9459b7e543916ec0afaecee5e6fa84562c6ae/worker/index.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [tugrulguner](https://github.com/tugrulguner). Independently curated. |
| Format | Hosted web app (Astro + Cloudflare Worker), MIT source |
| Platform and availability | Web (hosted; self-hostable) |
| Jev's role | Jev answers bounded typed questions; code validates offsets and runs the operation. |
| Requirements | A browser for the hosted app; Node 22.19+ and your own TypeSafe key to self-host the AI utilities. |
| License | [MIT](https://github.com/tugrulguner/utilitypot/blob/dae9459b7e543916ec0afaecee5e6fa84562c6ae/LICENSE) |

## When to use

- Pull exact entity mentions or supporting paragraphs out of text without trusting a free-form AI answer.
- Turn up to eight listed steps into a reviewable Mermaid flowchart.
- Mismatch: AI utilities are tightly bounded (for example 120 source tokens for entities); not exhaustive NER or fact checking.

## How it works

The Worker posts typed questions to `https://api.typesafe.ai/v1/systemone` after you consent; answers become inspectable settings and exact offsets that deterministic code validates and executes, never generated code. Without a key the three AI utilities fail closed and the four local tools keep working. Integration evidence: [`worker/index.js`](https://github.com/tugrulguner/utilitypot/blob/dae9459b7e543916ec0afaecee5e6fa84562c6ae/worker/index.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tugrulguner/utilitypot.git && cd utilitypot
npm ci && npm run dev
# AI utilities: put TYPESAFE_API_KEY in a gitignored .dev.vars, then
npm run build && npx wrangler dev --local
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live app: [utilitypot.modepot.io/](https://utilitypot.modepot.io/)
- Privacy and limits: [utilitypot.modepot.io/privacy/](https://utilitypot.modepot.io/privacy/)

## Limits and data handling

Converters and calculators run in your browser; entity, diagram and webpage inputs go to TypeSafe through the hosted Worker after disclosed consent.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit dae9459b7e54](https://github.com/tugrulguner/utilitypot/tree/dae9459b7e543916ec0afaecee5e6fa84562c6ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
