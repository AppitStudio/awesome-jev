# TabTidy

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome MV3 extension that filters tabs locally (active, pinned, audible, downloading stay), then sends one Jev request with a KEEP / CLOSE / UNCERTAIN choice question per remaining tab; it closes only what you confirm (one-click undo through Chrome sessions) and turns your corrections into domain rules that override Jev next time.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/123456342g-lang/tabtidy) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/123456342g-lang/tabtidy#readme) (unpacked extension; not on the Chrome Web Store). |
| Pricing and access | No fee; load the unpacked extension. Jev judgement needs your own TypeSafe API key (billed by TypeSafe); without a key it runs local rules only. Checked 2026-10-08. |
| Jev evidence | [`src/lib/jev-client.js`](https://github.com/123456342g-lang/tabtidy/blob/20b080efa63950a75080c1eb6e4e8ff1f89f16d1/src/lib/jev-client.js) posts to `https://api.typesafe.ai/v1/systemone`; [`src/lib/jev.js`](https://github.com/123456342g-lang/tabtidy/blob/20b080efa63950a75080c1eb6e4e8ff1f89f16d1/src/lib/jev.js) builds the per-tab questions and maps answers. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [123456342g-lang](https://github.com/123456342g-lang). Independently curated. |
| Format | Chrome MV3 extension (load unpacked; Chrome 121+) |
| Platform and availability | Google Chrome 121+ on desktop (developer-mode unpacked install). |
| Jev's role | Judges, in one batch, whether each candidate tab is still worth keeping; local filters, thresholds and your remembered rules decide first. |
| Requirements | Chrome 121+; a TypeSafe API key entered in the popup after the privacy consent. |
| License | [MIT](https://github.com/123456342g-lang/tabtidy/blob/20b080efa63950a75080c1eb6e4e8ff1f89f16d1/LICENSE). |

## When to use

- Clear a window full of stale tabs without judging each one yourself.
- Teach the extension your own keep/close taste through corrections.
- Mismatch: personal rules can't be exported yet; removing the extension may clear them.

## How it works

The extension snapshots tab metadata (domain, title, age, last access, group, duplicates), keeps protected tabs locally, assembles one state with tab relationships and your rules, and sends a single typed request. Low-confidence answers are downgraded to UNCERTAIN; closing goes through `chrome.sessions` so it can be undone.

## Get started

Load the unpacked extension (README *Install*), then enter your key in the popup:

```sh
git clone https://github.com/123456342g-lang/tabtidy.git
# chrome://extensions → Developer mode → Load unpacked → pick the tabtidy folder
npm test   # optional: unit + scenario tests with a fake Jev
```

Each tidy is one Jev request billed to your TypeSafe key.

## Examples and demos

- README *What it does* and the 20-tab scenario test (`npm run test:scenario`).

## Limits and data handling

Tab titles, domains and your rule sentences go to TypeSafe (the popup shows what will be sent). The client also supports an optional third-party gateway URL (jevai.org) if you configure one; the default is the official TypeSafe endpoint. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 20b080efa639](https://github.com/123456342g-lang/tabtidy/tree/20b080efa63950a75080c1eb6e4e8ff1f89f16d1). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
