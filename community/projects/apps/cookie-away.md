# Cookie Away (Chrome extension that rejects cookie banners for you, with optional Jev help on banners it can't read)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Free Chrome extension that rejects cookie banners, including ones that hide Reject behind a settings screen: it knows 27 consent platforms, reads other banners in about 20 languages, and checks the banner is gone after each click. For banners it still can't read, it can ask Jev which button is which; that is off by default and uses your own key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/upstrategylab/cookie-away) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://www.cookieaway.com) |
| Pricing and access | Free extension under MIT; the optional Jev feature is billed to your own TypeSafe key. Checked 2026-11-03. |
| Jev evidence | [`background/service_worker.js`](https://github.com/upstrategylab/cookie-away/blob/f6c10320cdc8aeb98cd1244434cfc54595dcbd0a/background/service_worker.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [upstrategylab](https://github.com/upstrategylab). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Chrome, Edge, Brave, Arc (load unpacked; Chrome Web Store in review). |
| Jev's role | Picks the reject button on banners the heuristics can't read (optional). |
| Requirements | Chrome or another Chromium browser; your own TypeSafe API key only for the optional Jev feature. |
| License | [MIT](https://github.com/upstrategylab/cookie-away/blob/f6c10320cdc8aeb98cd1244434cfc54595dcbd0a/LICENSE) |

## When to use

- Say no to cookie tracking without clicking through settings screens.
- Mismatch: Jev is an optional fallback; most banners are handled without it.

## How it works

`background/service_worker.js` sends the hostname, banner text and button labels to `https://api.typesafe.ai/v1/systemone` as a choice question when heuristics fail, accepts answers above 0.6, caches them and allows at most 3 calls per site per day. Integration evidence: [`background/service_worker.js`](https://github.com/upstrategylab/cookie-away/blob/f6c10320cdc8aeb98cd1244434cfc54595dcbd0a/background/service_worker.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/upstrategylab/cookie-away.git
# chrome://extensions > Developer mode > Load unpacked > pick the folder
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Published benchmark against Consent-O-Matic: [www.cookieaway.com/benchmarks](https://www.cookieaway.com/benchmarks)

## Limits and data handling

With Jev on, the site's hostname, banner text and button labels go to TypeSafe on your key; otherwise nothing leaves the browser. Chrome Web Store listing in review. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit f6c10320cdc8](https://github.com/upstrategylab/cookie-away/tree/f6c10320cdc8aeb98cd1244434cfc54595dcbd0a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
