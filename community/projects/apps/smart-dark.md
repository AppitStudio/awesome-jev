# Smart Dark (adaptive dark mode with optional Jev screenshot checks)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that darkens websites by using a site's own dark theme when it has one and otherwise rewriting its colours while keeping layout, hover states and brand colours; optional Jev screenshot checks decide whether a page should stay dark or return to its original look.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ThrownLemon/smart-dark) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/ThrownLemon/smart-dark#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to load from a release or source. Jev checks use your own TypeSafe key and are capped at 30 image checks per UTC day. Checked 2026-10-23. |
| Jev evidence | [`src/jev.js`](https://github.com/ThrownLemon/smart-dark/blob/2bbedf42f165fa745dda75e59b84ad905418a10f/src/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ThrownLemon](https://github.com/ThrownLemon). Independently curated. |
| Format | Chrome extension (Manifest V3, JavaScript) |
| Platform and availability | Chrome desktop, loaded unpacked from a release zip or source build; not on the Chrome Web Store. |
| Jev's role | Optional: Jev looks at a screenshot of the darkened page and decides whether to keep the dark theme or restore the original. |
| Requirements | Chrome or another Chromium browser (load unpacked); optional TypeSafe API key for Jev checks. |
| License | [MIT](https://github.com/ThrownLemon/smart-dark/blob/2bbedf42f165fa745dda75e59b84ad905418a10f/LICENSE) |

## When to use

- Get dark mode that respects a site's own theme instead of inverting everything.
- Let Jev catch pages where the rewrite looks wrong.
- Mismatch: beta; live Jev visual accuracy is not verified by the author.

## How it works

`src/jev.js` sends a JPEG of the visible page and a few original-colour measurements to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and the image asset structure; automatic checks are a separate opt-in for ambiguous pages. Integration evidence: [`src/jev.js`](https://github.com/ThrownLemon/smart-dark/blob/2bbedf42f165fa745dda75e59b84ad905418a10f/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Install steps and before and after gallery in the README: [github.com/ThrownLemon/smart-dark#readme](https://github.com/ThrownLemon/smart-dark#readme)

## Limits and data handling

Screenshots can contain private content and are not redacted; the extension pauses when it sees password, payment or one-time-code inputs, but review the README's privacy notes before enabling. A copy of the repository also exists at travisw84/smart-dark.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 2bbedf42f165](https://github.com/ThrownLemon/smart-dark/tree/2bbedf42f165fa745dda75e59b84ad905418a10f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
