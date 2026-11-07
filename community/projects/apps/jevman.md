# jevman (Pac-Man driven by TypeSafe Jev and other System One models)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser Pac-Man where ghosts and Pac-Man choose moves with System One decision models; TypeSafe Jev is the default path (typesafe/jev-1.13.0 via api.typesafe.ai) and Opper-served models are also supported, with a live demo and recorded replays.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joch/jevman) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://jevman.chadda.se) |
| Pricing and access | Free source build / free hosted demo; you supply TypeSafe or Opper keys for live decisions. Checked 2026-11-07. |
| Jev evidence | [`server/jev.ts`](https://github.com/joch/jevman/blob/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [joch](https://github.com/joch). Independently curated. |
| Format | TypeScript web game + Deno/Node server (AGPL-3.0) |
| Platform and availability | Web (hosted demo at jevman.chadda.se; or self-host). |
| Jev's role | Core: each actor move is a System One Choice; TypeSafe Jev is the default provider path. |
| Requirements | A modern browser for the demo, or Node/Deno to self-host; a TypeSafe or Opper API key for live decisions. |
| License | [AGPL-3.0](https://github.com/joch/jevman/blob/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc/LICENSE) |

## When to use

- Watch or play Pac-Man steered by typed System One choices.
- Compare TypeSafe Jev against other decision models on the same maze.
- Mismatch: real-time game costs accumulate; use a spending-capped key.

## How it works

`server/jev.ts` posts Choice questions to `https://api.typesafe.ai/v1/systemone` when `TYPESAFE_API_KEY` is set (default model `jev-1.13.0`), or to Opper's compatible path otherwise; answers drive actor moves. Integration evidence: [`server/jev.ts`](https://github.com/joch/jevman/blob/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc/server/jev.ts).

## Get started

Open the hosted demo or clone and run per README with a TypeSafe or Opper key.

```sh
git clone https://github.com/joch/jevman.git && cd jevman
export TYPESAFE_API_KEY=...
# follow README to run locally
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo: [jevman.chadda.se](https://jevman.chadda.se)
- README: [github.com/joch/jevman/blob/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc/README.md](https://github.com/joch/jevman/blob/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc/README.md)

## Limits and data handling

Game state and questions go to TypeSafe or Opper on your key. AGPL-3.0 applies to the source.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 27be2b8dc293](https://github.com/joch/jevman/tree/27be2b8dc2934c31383c9fb7c6ac0c2ba40bbebc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
