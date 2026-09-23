# Shapeshift

[All projects](../README.md) · [Web apps](README.md#web-apps)

One text box that morphs into the right UI (event, checklist, timer, split, convert, …) as you type: TypeSafe Jev classifies intent; deterministic parsers fill values. Offline keyword classifier by default; live demo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anishfn/shapeshift) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [shapeshiftui.vercel.app](https://shapeshiftui.vercel.app) |
| Pricing and access | Hosted demo appears free (limits unchecked). Source-build with Bun; optional `TYPESAFE_API_KEY` for online Jev (`jev-1.13.0` default). No app purchase fee; TypeSafe usage is separate. Reviewed 2026-09-23. |
| Jev evidence | [`src/lib/jev/questions.ts`](https://github.com/anishfn/shapeshift/blob/71a68394efb79ee9ef836bdba111cf19522aab66/src/lib/jev/questions.ts) and server `/api/intent` fan out typed questions (card type + signals); [`src/lib/jev/mock.ts`](https://github.com/anishfn/shapeshift/blob/71a68394efb79ee9ef836bdba111cf19522aab66/src/lib/jev/mock.ts) offline path. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, package, jev paths). Hosted demo and live TypeSafe calls were **not** run on the review host. |
| Maintainer | [anishfn](https://github.com/anishfn). |
| Format | Next.js / Bun web app **shapeshift 0.1.0** (`@typesafe-ai/sdk`). |
| Platform and availability | Web (local `bun dev` or [hosted demo](https://shapeshiftui.vercel.app)). |
| Jev's role | Classifies which card type and boolean signals; parsers/math stay in code. Offline mock when no key. |
| Requirements | Bun 1.2+ for local; optional `TYPESAFE_API_KEY` (server-only). |
| License | [MIT](https://github.com/anishfn/shapeshift/blob/71a68394efb79ee9ef836bdba111cf19522aab66/LICENSE). |

## When to use

Use it when you want a single input that becomes structured UI from natural language, with calm confidence gating. Prefer [Apparite (jev2ui)](jev2ui.md) for IA/anatomy mock labs rather than personal productivity cards.

## How it works

Debounced keystrokes hit `/api/intent`, which asks Jev many typed questions in parallel (or the offline classifier). A state machine commits a card only after hysteresis; parsers extract dates, amounts, and units. Cards persist in `localStorage`.

## Get started

```sh
git clone https://github.com/anishfn/shapeshift.git
cd shapeshift
git checkout 71a68394efb79ee9ef836bdba111cf19522aab66
bun install && bun dev
# Open http://localhost:3000 — offline by default
# Optional: cp .env.example .env.local and set TYPESAFE_API_KEY
```

## Examples and demos

- Live site: [shapeshiftui.vercel.app](https://shapeshiftui.vercel.app)
- `docs/demo.gif` / `docs/demo.mp4`; `?demo=1&loop=1` scripted demo; `?debug=1` shows probabilities.

## Limits and data handling

With a key, typed text goes to TypeSafe via the server route; the key never reaches the browser. Without a key, classification stays local. This listing did not call live Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 71a6839](https://github.com/anishfn/shapeshift/tree/71a68394efb79ee9ef836bdba111cf19522aab66) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, package metadata, and jev modules. No live TypeSafe spend.

Related: [Apparite (jev2ui)](jev2ui.md), [Polymorph](polymorph.md).
