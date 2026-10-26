# Jev ToS Checker (Chrome extension that flags terms-of-service clauses that may work against you)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that, on request, splits the terms of service or privacy policy on the current page into clauses, has Jev check each against five risk types, and lists the flagged clauses with their original text, scrolling to each on the page; works on any site and in any language; English and Japanese UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shohei81/jev-tos-checker) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://shohei81.github.io/jev-tos-checker/) |
| Pricing and access | Open source (MIT); free from GitHub Releases (v0.3.1). Jev calls are billed to your TypeSafe key, or handled by a server you are given. Checked 2026-10-26. |
| Jev evidence | [`core/jev.ts`](https://github.com/shohei81/jev-tos-checker/blob/ad1c84fbba744d4740644898c7044205e4989f9f/core/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [shohei81](https://github.com/shohei81). Independently curated. |
| Format | Chrome extension (TypeScript) |
| Platform and availability | Chrome (installed from a downloaded release folder; not on the Chrome Web Store at review time). |
| Jev's role | Clause judge: each clause is asked five typed risk questions, and the flagged ones are shown. |
| Requirements | Chrome; your own TypeSafe API key, or the URL of an analysis server someone runs for you. |
| License | [MIT](https://github.com/shohei81/jev-tos-checker/blob/ad1c84fbba744d4740644898c7044205e4989f9f/LICENSE) |

## When to use

- Spot clauses worth reading before you accept a service's terms.
- Check terms in languages you do not read well.
- Mismatch: flags possible risks; not legal advice. Distinct from the separately listed ToS Decipher and ToS Watch.

## How it works

`core/jev.ts` posts each clause with the risk questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); the optional analysis server (a Cloudflare Worker in the repo) does the same with its own key. Integration evidence: [`core/jev.ts`](https://github.com/shohei81/jev-tos-checker/blob/ad1c84fbba744d4740644898c7044205e4989f9f/core/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# download the release, unzip, chrome://extensions → Load unpacked
# then choose "Use my own API key" and paste your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Website: [shohei81.github.io/jev-tos-checker/](https://shohei81.github.io/jev-tos-checker/)
- Releases: [github.com/shohei81/jev-tos-checker/releases](https://github.com/shohei81/jev-tos-checker/releases)

## Limits and data handling

Clause text from the page goes to TypeSafe, or to the analysis server you configure; the page is read only when you click Analyze.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit ad1c84fbba74](https://github.com/shohei81/jev-tos-checker/tree/ad1c84fbba744d4740644898c7044205e4989f9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
