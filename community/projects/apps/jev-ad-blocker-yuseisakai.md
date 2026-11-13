# Jev-Ad blocker by yuseisakai (Chrome extension that has Jev judge ad candidates on a page and removes them reversibly)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that collects ad candidates on each page, asks Jev whether each is an ad, and removes the ones above an adjustable threshold (default 80%), with undo for the last or all removals and no URL history kept.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yuseisakai/jev-adblock) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/yuseisakai/jev-adblock#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-13. |
| Jev evidence | [`src/core.js`](https://github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/src/core.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [yuseisakai](https://github.com/yuseisakai). Independently curated. |
| Format | Chrome MV3 extension loaded in developer mode (JavaScript, MIT; UI and docs in Japanese) |
| Platform and availability | Chrome desktop (load unpacked); no Chrome Web Store listing |
| Jev's role | Jev decides whether each collected page element is an ad; the extension removes those above your threshold. |
| Requirements | Chrome on desktop and your own TypeSafe key, or a Cloudflare AI Gateway you configure. |
| License | [MIT](https://github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/LICENSE) |

## When to use

- Hide display ads with a model judgment instead of filter lists.
- Mismatch: network-level blocking or YouTube video ads; it removes visible elements only.

## How it works

`src/core.js` sends candidates to `https://api.typesafe.ai/v1/systemone` with `jev-latest` in direct mode, or through your own Cloudflare AI Gateway account with model `typesafe/jev`. It removes elements after they render, so it does not block requests, tracking or video ads. Integration evidence: [`src/core.js`](https://github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/src/core.js).

## Get started

Download the ZIP from the repository or a release, load it unpacked in Chrome's developer mode, and enter your key in the options page.

```sh
# chrome://extensions → Developer mode → Load unpacked → select the folder
# then open the extension options and paste your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/README.md](https://github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/README.md)
- Privacy notes: [github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/PRIVACY.md](https://github.com/yuseisakai/jev-adblock/blob/720b423860066a4d184ffa83311afb8a8ee64a49/PRIVACY.md)

## Limits and data handling

Ad-candidate snippets from pages you visit go to TypeSafe (or your Cloudflare gateway) on your key when auto-judging is on.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 720b42386006](https://github.com/yuseisakai/jev-adblock/tree/720b423860066a4d184ffa83311afb8a8ee64a49). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
