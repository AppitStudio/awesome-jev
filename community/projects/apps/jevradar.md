# JevRadar (local-first Windows desktop radar for market sentiment and context, classified with Jev)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Tauri desktop app (Portuguese UI, bilingual setup) that combines public content from RSS, Reddit and optional X with Jev's typed classifications and real market series, to show shifts in attention and measure what happened after past signals. It does not recommend trades or execute orders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PedroReoli/JevRadar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/PedroReoli/JevRadar#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); Jev and data providers use your own keys. Checked 2026-11-02. |
| Jev evidence | [`src-tauri/src/infrastructure/jev/system_one.rs`](https://github.com/PedroReoli/JevRadar/blob/2f2eca7d2321fc6b7b9b0c94105050b2f6beae61/src-tauri/src/infrastructure/jev/system_one.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [PedroReoli](https://github.com/PedroReoli). Independently curated. |
| Format | Tauri (Rust + TypeScript) desktop app |
| Platform and availability | Windows (alpha); built from source. |
| Jev's role | Typed classification of each content item (asset, sentiment, relevance, hype). |
| Requirements | Windows (alpha); Node.js and Rust to build; a TypeSafe API key plus optional data-provider keys. |
| License | [Apache-2.0](https://github.com/PedroReoli/JevRadar/blob/2f2eca7d2321fc6b7b9b0c94105050b2f6beae61/LICENSE) |

## When to use

- Track how attention and sentiment around a watchlist change over time.
- Mismatch: alpha, Windows-first, Portuguese UI; not investment advice.

## How it works

`src-tauri/src/infrastructure/jev/system_one.rs` calls TypeSafe System One (`jev-latest`) to classify each item by asset, sentiment, relevance, type, factual claim, hype and context, validates the typed contract strictly, and shows daily token use in the app. Integration evidence: [`src-tauri/src/infrastructure/jev/system_one.rs`](https://github.com/PedroReoli/JevRadar/blob/2f2eca7d2321fc6b7b9b0c94105050b2f6beae61/src-tauri/src/infrastructure/jev/system_one.rs).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/PedroReoli/JevRadar#readme](https://github.com/PedroReoli/JevRadar#readme)

## Limits and data handling

Public posts and articles are sent to TypeSafe for classification; credentials stay in Windows Credential Manager. Not investment advice. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 2f2eca7d2321](https://github.com/PedroReoli/JevRadar/tree/2f2eca7d2321fc6b7b9b0c94105050b2f6beae61). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
