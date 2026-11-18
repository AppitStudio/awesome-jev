# SmartRSSReader by Dylan Festa (desktop RSS reader that ranks new journal papers against your criteria with Jev)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Local desktop app (Tauri v2) for scientific feeds: pick the RSS feeds of the journals and preprint servers you follow, define any number of positive and negative criteria, and Jev scores each new paper's title and abstract against them for a combined relevance ranking. Papers already scored are remembered, so you never pay twice, and changing a criterion's weight re-ranks the feed offline. Pre-built installers for Windows, macOS and Linux. Alpha.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dylanfesta/RSS-Sci-Jev-Reader) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/releases/latest) |
| Pricing and access | Free download and CC0 source; Jev calls are billed to your own OpenRouter key. Checked 2026-11-18. |
| Jev evidence | [`src-tauri/src/jev_client.rs`](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/blob/6be9652eec6d953deb85a5d1dc673228874e6d92/src-tauri/src/jev_client.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [dylanfesta](https://github.com/dylanfesta). Independently curated. |
| Format | Tauri v2 desktop app (Rust and JavaScript) (CC0-1.0) |
| Platform and availability | Windows, macOS (Apple Silicon and Intel) and Linux; unsigned alpha builds |
| Jev's role | Answers yes/no and rubric questions for each paper against each of your criteria; the app combines the probabilities into a ranking. |
| Requirements | An OpenRouter key with access to Jev (default `typesafe/jev-1.14`); the author recommends a key with a spending cap. |
| License | [CC0-1.0](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/blob/6be9652eec6d953deb85a5d1dc673228874e6d92/LICENSE) |

## When to use

- Turn a dozen journal feeds into one ranked reading list for your topics.
- Mismatch: production-grade software; the author labels it untested alpha.

## How it works

`src-tauri/src/jev_client.rs` posts each paper and criteria to OpenRouter's decisions endpoint (`/api/alpha/decisions`) with `typesafe/jev-1.14` by default; `src-tauri/src/database.rs` caches scores locally. Integration evidence: [`src-tauri/src/jev_client.rs`](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/blob/6be9652eec6d953deb85a5d1dc673228874e6d92/src-tauri/src/jev_client.rs).

## Get started

Download the installer for your OS from the latest release, add your OpenRouter key, then add feeds and criteria.

```sh
# pre-built installers: https://github.com/dylanfesta/RSS-Sci-Jev-Reader/releases/latest
# or build from source (Rust + Node.js):
git clone https://github.com/dylanfesta/RSS-Sci-Jev-Reader && cd RSS-Sci-Jev-Reader
npm install && npm run tauri build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/dylanfesta/RSS-Sci-Jev-Reader/releases](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/releases)
- README: [github.com/dylanfesta/RSS-Sci-Jev-Reader/blob/6be9652eec6d953deb85a5d1dc673228874e6d92/README.md](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/blob/6be9652eec6d953deb85a5d1dc673228874e6d92/README.md)

## Limits and data handling

Paper titles and abstracts (public feed content) and your criteria go to OpenRouter/TypeSafe. Binaries are not code-signed. The author's cost figure (~5 cents across all feeds) is not verified here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 6be9652eec6d](https://github.com/dylanfesta/RSS-Sci-Jev-Reader/tree/6be9652eec6d953deb85a5d1dc673228874e6d92). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
