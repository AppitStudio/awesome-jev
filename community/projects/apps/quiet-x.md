# Quiet X

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Open-source Chrome extension that silently hides X ads and posts by account country, language or topic; optional language/topic rules are judged by TypeSafe Jev on the rendered post text through a small local proxy that holds your key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arzumanabbasov/quiet-x) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/arzumanabbasov/quiet-x#readme); unpacked build on [GitHub Releases](https://github.com/arzumanabbasov/quiet-x/releases/tag/v1.2.2) (v1.2.2, first public release). |
| Pricing and access | Free MIT source/release; not verified on the Chrome Web Store. Ads and country filtering need no AI; topic/language filtering needs your own TypeSafe key in the proxy (usage billed by TypeSafe). Checked 2026-10-06. |
| Jev evidence | Inspected [`extension/src/ai/jev-client.ts`](https://github.com/arzumanabbasov/quiet-x/blob/9fa7fdafbd0243df5227411aa5e6f188180ddcdd/extension/src/ai/jev-client.ts) and [`server/jev.ts`](https://github.com/arzumanabbasov/quiet-x/blob/9fa7fdafbd0243df5227411aa5e6f188180ddcdd/server/jev.ts) (proxy forwarding typed questions to TypeSafe). |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [arzumanabbasov](https://github.com/arzumanabbasov). Independently curated. |
| Format | Manifest V3 Chrome extension + minimal Node proxy |
| Platform and availability | Chrome 116+ (load unpacked); Node.js 22+ for the proxy. Early release. |
| Jev's role | Optional: for posts from allowed countries, Jev answers whether the rendered text matches a blocked topic or language; code hides matches. Ads and country rules are deterministic. |
| Requirements | Chrome 116+, Node.js 22+; `TYPESAFE_API_KEY` and `PROXY_TOKEN` in the proxy's `.env` for AI filters. |
| License | [MIT](https://github.com/arzumanabbasov/quiet-x/blob/9fa7fdafbd0243df5227411aa5e6f188180ddcdd/LICENSE). |

## When to use

- Hide topics or languages you don't want on X without replacement cards or warnings.
- See a pattern for keeping a provider key out of a browser extension via a token-protected local proxy.
- Mismatch: country lookups depend on X internals and can break; unknown countries are hidden by default.

## How it works

The content script observes timeline posts, applies ad and country rules locally, and sends the rendered text of remaining posts to your proxy, which asks Jev typed questions with your TypeSafe key; posts that match are removed silently. No X API key is needed and no keys are bundled in the extension.

## Get started

Build, load unpacked, and start the proxy for AI filters:

```sh
git clone https://github.com/arzumanabbasov/quiet-x.git
cd quiet-x
npm ci && npm run build      # load extension/dist in chrome://extensions
cp .env.example .env         # TYPESAFE_API_KEY, PROXY_TOKEN
npm run start:proxy          # 127.0.0.1:8787
```

Topic/language filtering makes TypeSafe requests for visible posts; ads/country rules make none.

## Examples and demos

- v1.2.2 release with a launch video.
- `npm run check` fixture-based DOM/filter/cache/proxy tests.

## Limits and data handling

Early release; X endpoint changes can break country filtering. Post text is sent to your proxy and on to TypeSafe for AI rules. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 9fa7fdafbd02](https://github.com/arzumanabbasov/quiet-x/tree/9fa7fdafbd0243df5227411aa5e6f188180ddcdd). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
