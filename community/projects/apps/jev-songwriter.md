# Jev Songwriter

[All projects](../README.md) · [Apps](README.md) · [Web apps](README.md#web-apps)

Composable song lab where code enumerates legal musical options and TypeSafe Jev picks mode, tempo, form, chords, and notes—one typed Choice per decision—with replayable HTML demos of every call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/beingcognitive/jev-songwriter) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [jev-songwriter.chardonn.ai](https://jev-songwriter.chardonn.ai) — hosted demos also on [Cloudflare Pages](https://jev-songwriter.pages.dev) and [GitHub Pages](https://beingcognitive.github.io/jev-songwriter/). |
| Pricing and access | No app purchase fee for the MIT source or static demo replays reviewed **2026-09-22**. Live `compose` needs `TYPESAFE_API_KEY` (or `.dev.vars`); without a key a seeded mock runs offline. Provider usage can incur charges for live compose. |
| Jev evidence | [`lib/jev.js`](https://github.com/beingcognitive/jev-songwriter/blob/d02d1947116d871a55148185d26829f12f29a5f9/lib/jev.js) posts to `https://api.typesafe.ai/v1/systemone` when a key is set; mock/fake backends for offline and tests. |
| Disclosure | Independently curated; no affiliation. Listing is not endorsement. AI-assisted catalog review. Offline `npm test` **32 pass** after creating `out/` on the review host. Live compose/TypeSafe not run. Hosted demos not re-measured for latency/cost claims. |
| Maintainer | [beingcognitive](https://github.com/beingcognitive) / Kyung-Hoon Kim. Independently curated; not an upstream submission. |
| Format | Node.js compose CLI plus static demo/replay pages (no npm dependencies). |
| Platform and availability | Node **22.15+**; browser for demos. Early source + public demo sites. |
| Jev's role | Chooses among code-built musical options (mode/tempo/form/chords/notes); never writes free text or invents illegal pitches. Code enforces meter, key, and cadences. |
| Requirements and costs | Optional TypeSafe key for live compose; mock without. Static replays need no key. |
| License | [MIT](https://github.com/beingcognitive/jev-songwriter/blob/d02d1947116d871a55148185d26829f12f29a5f9/LICENSE). |

## When to use

Use it to **see System One pick a song decision-by-decision** with probabilities beside the score. Prefer games like [Jev Chess](jevchess.md) for board play, or music controllers like [Live Jev](live-jev.md) for DAW actions. Do not treat outputs as professional compositions or measured musical quality.

## How it works

Setup/chord/note stages call [`ask`](https://github.com/beingcognitive/jev-songwriter/blob/d02d1947116d871a55148185d26829f12f29a5f9/lib/jev.js) with typed Choice questions. Code lists legal options and theory facts; Jev returns a choice and probabilities; traces feed HTML replay pages. Without `TYPESAFE_API_KEY`, a seeded mock substitutes so demos and tests stay offline.

## Get started

```sh
git clone https://github.com/beingcognitive/jev-songwriter.git
cd jev-songwriter
git checkout d02d1947116d871a55148185d26829f12f29a5f9
mkdir -p out
npm test
# Live compose (charges): export TYPESAFE_API_KEY=... && npm run compose -- --mood "wistful, late night"
```

Live compose sends mood/state and option lists to TypeSafe. This listing did not run live compose.

## Examples and demos

- Offline `npm test` — **32 pass** (create `out/` first if missing).
- Hosted replays: [river](https://beingcognitive.github.io/jev-songwriter/demos/demo-river.html?replay=1) and siblings linked from the README (HTTP reachability not re-checked this pass beyond prior discovery).
- Source demos under `docs/demos/`.

## Limits and data handling

Mock mode makes no network calls. Live compose sends decision payloads to TypeSafe. Upstream cost/latency figures are author-reported. Experimental / for-fun project.

## Review and maintenance

Reviewed on **2026-09-22** at [commit d02d194](https://github.com/beingcognitive/jev-songwriter/tree/d02d1947116d871a55148185d26829f12f29a5f9): MIT. AI-assisted source review of README, LICENSE, `lib/jev.js`, and `test.mjs`. Offline `npm test` **32 pass**. No live TypeSafe spend.

Related: [Jev Chess](jevchess.md), [Live Jev](live-jev.md), [discoprint](../tools/discoprint.md).
