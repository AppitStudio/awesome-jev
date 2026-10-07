# pulp

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Personal macOS pipeline that turns Safari iCloud tabs into clean EPUBs for an e-ink reader (OPDS catalog, KOReader sync, optional reMarkable push); optional `--smart` triage asks TypeSafe Jev whether each tab the denylist kept is worth reading.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danemarguglio/pulp) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/danemarguglio/pulp#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT source; `--smart` triage needs your own TypeSafe key (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`src/pulp/triage.py`](https://github.com/danemarguglio/pulp/blob/42f2b1ff90ea7f9558c3a5a73e5a497c8b6c7c83/src/pulp/triage.py) sends one `jev-latest` request per remaining tab (worth-reading probability + page-type choice); README *`--smart` (TypeSafe / Jev)* documents it. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [danemarguglio](https://github.com/danemarguglio). Independently curated. |
| Format | Python CLI (`pulp run`) and always-on LaunchAgent server (`pulp serve`) with phone PWA |
| Platform and availability | macOS with Safari iCloud Tabs; any OPDS e-reader (built for Xteink X4 Pro / CrossPoint). |
| Jev's role | Optional: judges which leftover tabs are worth reading; the deterministic denylist, extraction and EPUB build are code. |
| Requirements | macOS, Python 3.12+ and uv; optional TypeSafe key at `~/.config/typesafe/key` (or `TYPESAFE_API_KEY`), `epubcheck`, `rmapi`. |
| License | [MIT](https://github.com/danemarguglio/pulp/blob/42f2b1ff90ea7f9558c3a5a73e5a497c8b6c7c83/LICENSE). |

## When to use

- Read articles opened on your phone later on an e-ink reader.
- Add Jev triage only for tabs the denylist did not skip (`pulp config smart=true`).
- Mismatch: personal project shared as-is (upstream); support not promised.

## How it works

`pull` reads Safari's `CloudTabs.db`, `triage` applies `denylist.toml` then (with `--smart`) Jev, `fetch` extracts article prose, `build` writes EPUBs, and the server exposes an OPDS catalog. Jev is only asked about URLs it has not judged before.

## Get started

Install and run once with smart triage (README):

```sh
git clone https://github.com/danemarguglio/pulp && cd pulp
uv sync
uv run pulp run --since 3d --smart
```

With `--smart`, each new tab is one Jev request billed to your TypeSafe key.

## Examples and demos

- README *What it does* and *Commands*.
- Companion firmware: [crosspoint-pulp](https://github.com/danemarguglio/crosspoint-pulp).

## Limits and data handling

Tab URLs and page text for triage go to TypeSafe only with `--smart`; articles are fetched from their sites. Reads Safari's local tab database. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 42f2b1ff90ea](https://github.com/danemarguglio/pulp/tree/42f2b1ff90ea7f9558c3a5a73e5a497c8b6c7c83). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
