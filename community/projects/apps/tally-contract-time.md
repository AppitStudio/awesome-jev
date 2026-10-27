# Tally (automatic time, income and evidence tracking for hourly contract work)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Menu bar app for hourly contractors that records which app, window and tab you are in every few seconds, assigns time to projects by your rules, seals intervals into a hash-chained ledger and bills only explicit client sessions; optionally Jev assigns unmatched windows to projects (at 80% confidence or more) and to activity categories.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0Calories/tally) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/0Calories/tally#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Optional Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. |
| Jev evidence | [`src-tauri/src/jev.rs`](https://github.com/0Calories/tally/blob/710598f8ea5a5bca40eaf3b6f4b1753f9a7e14c1/src-tauri/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [0Calories](https://github.com/0Calories). Independently curated. |
| Format | macOS menu bar app (Tauri 2, Rust and React) |
| Platform and availability | macOS; build from source (self-signed release builds). |
| Jev's role | Optional classifier: windows no rule matches go to Jev once per window for a project or category; Jev never puts time on a client. |
| Requirements | macOS, Rust, Node.js and pnpm to build; a TypeSafe API key (stored in the Keychain) only for the optional Jev features. |
| License | [MIT](https://github.com/0Calories/tally/blob/710598f8ea5a5bca40eaf3b6f4b1753f9a7e14c1/LICENSE) |

## When to use

- Track contract hours without starting timers, with evidence you can show a client.
- Let a decision model sort the leftover windows your rules miss.
- Mismatch: macOS only and build-from-source; client time is never assigned automatically.

## How it works

`src-tauri/src/jev.rs` posts the window's app, title and site with the project and category options to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); answers below the confidence threshold leave the window unassigned. Integration evidence: [`src-tauri/src/jev.rs`](https://github.com/0Calories/tally/blob/710598f8ea5a5bca40eaf3b6f4b1753f9a7e14c1/src-tauri/src/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/0Calories/tally && cd tally
pnpm install
scripts/release.sh   # see the README for signing and install steps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/0Calories/tally#readme](https://github.com/0Calories/tally#readme)

## Limits and data handling

With Jev on, non-client window titles, app names and sites go to TypeSafe; client time and calendar data are handled only on the Mac. Screenshots and the ledger stay local.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 710598f8ea5a](https://github.com/0Calories/tally/tree/710598f8ea5a5bca40eaf3b6f4b1753f9a7e14c1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
