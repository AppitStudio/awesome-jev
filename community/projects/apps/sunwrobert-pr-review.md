# PR Review (sunwrobert)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Keyboard-first macOS app for reviewing and merging GitHub pull requests through your `gh` login, with optional Jev readiness scores, smart search and grouping of related PRs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sunwrobert/pr-review) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/sunwrobert/pr-review#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-16. |
| Jev evidence | [`src-tauri/src/lib.rs`](https://github.com/sunwrobert/pr-review/blob/127a1ff45b0368bcf47ca28ea63cc23a2ff34493/src-tauri/src/lib.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [sunwrobert](https://github.com/sunwrobert). Independently curated. |
| Format | macOS app (Tauri, Rust + TypeScript); signed self-updating releases or source build |
| Platform and availability | macOS (universal build) |
| Jev's role | Optional: Jev adds readiness scoring, topic search and grouping on top of GitHub facts. |
| Requirements | macOS, `gh` authenticated; Bun, Rust and Xcode Command Line Tools to build; `OPENROUTER_API_KEY` for the Jev features. |
| License | [MIT](https://github.com/sunwrobert/pr-review/blob/127a1ff45b0368bcf47ca28ea63cc23a2ff34493/LICENSE) |

## When to use

- Work a review queue sorted by readiness, where Jev adds what GitHub facts can't see (description and review timeline).
- Search PRs by topic (frontend, billing) even when the word isn't in them.
- Mismatch: Jev is optional and reached through OpenRouter's System One route; the app is not Apple-notarized.

## How it works

The Rust backend runs validated `gh` commands for GitHub data and, when `OPENROUTER_API_KEY` is set, posts typed questions to `https://openrouter.ai/api/v1/systemone`; GitHub facts carry most of the 0-100 readiness score and Jev's answers fill in the rest. Integration evidence: [`src-tauri/src/lib.rs`](https://github.com/sunwrobert/pr-review/blob/127a1ff45b0368bcf47ca28ea63cc23a2ff34493/src-tauri/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
gh repo clone sunwrobert/pr-review /tmp/pr-review-src -- -q && bash /tmp/pr-review-src/scripts/install.sh
# optional: export OPENROUTER_API_KEY=... for readiness, smart search and groups
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Feature list and keyboard shortcuts in the README (`?` in the app lists all).

## Limits and data handling

PR descriptions and review timelines go to OpenRouter on your key when Jev features are on; GitHub access stays in your `gh` login and the app never stores a token.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 127a1ff45b03](https://github.com/sunwrobert/pr-review/tree/127a1ff45b0368bcf47ca28ea63cc23a2ff34493). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
