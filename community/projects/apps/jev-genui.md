# Jev/ui (jev-genui)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Generative UI sandbox: TypeSafe Jev walks a UI grammar via typed Choice questions; a React interpreter renders live shadcn components.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/claudfuen/jev-genui) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/claudfuen/jev-genui#readme) — local Next.js sandbox; no separate commercial site. |
| Pricing and access | Public source has no app purchase fee, checked **2026-09-24**. Live compose needs `AI_GATEWAY_API_KEY` (Vercel AI Gateway). Provider usage is billed separately. **No LICENSE file** at tip—not open source. |
| Jev evidence | Inspected [`lib/genui/engine.ts`](https://github.com/claudfuen/jev-genui/blob/a4e59d816415839d5284ded71e959d3a1d730d84/lib/genui/engine.ts): `experimental_evaluate` with model `typesafe-ai/jev` over grammar Choice shards; [`app/api/compose/route.ts`](https://github.com/claudfuen/jev-genui/blob/a4e59d816415839d5284ded71e959d3a1d730d84/app/api/compose/route.ts) streams compose events. Live compose **not** run. |
| Disclosure | Source available without a declared open-source license. AI-assisted, independently curated; no commercial relationship declared. Listing is not an endorsement. |
| Maintainer | [claudfuen](https://github.com/claudfuen). |
| Format | Next.js / React / Bun (`jev-genui` 0.0.1). |
| Platform and availability | Source build: `bun install` then `AI_GATEWAY_API_KEY=… bun dev`. Experimental demo quality. |
| Jev's role | Answers parallel Choice questions that fill a page→section→tile grammar; application code maps the tree onto shadcn/ui. Jev does not emit JSX. |
| Requirements | Bun; `AI_GATEWAY_API_KEY` for live compose (OIDC on Vercel). |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. |

## When to use

Use it to study “Jev decides structure, code renders UI” with a visible Decisions panel. Prefer production design systems when you need shipped product chrome.

## How it works

Compose rounds batch Choice questions against the request and tree so far. The interpreter maps answers onto components; probabilities and runners-up stay visible.

## Get started

```sh
git clone https://github.com/claudfuen/jev-genui.git
cd jev-genui
git checkout a4e59d816415839d5284ded71e959d3a1d730d84
bun install
AI_GATEWAY_API_KEY=... bun dev
# or: AI_GATEWAY_API_KEY=... bun scripts/try.ts "sales dashboard for a coffee shop"
```

## Examples and demos

- README grammar walkthrough and Decisions panel description.
- Terminal `scripts/try.ts` path without the UI.

## Limits and data handling

Query text goes to Vercel AI Gateway / TypeSafe Jev when live. No LICENSE file. Rate limit and cache exist in the compose route; quality of composed UIs was not measured here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit a4e59d8](https://github.com/claudfuen/jev-genui/tree/a4e59d816415839d5284ded71e959d3a1d730d84). AI-assisted source review of README, `engine.ts`, compose route. No live Gateway spend.

Related: [Apparite (jev2ui)](jev2ui.md), [Shapeshift](shapeshift.md).
