# Xift

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Firefox add-on that collapses noise on your X timeline: TypeSafe Jev (via OpenRouter) scores each post for engagement bait, rage bait, low substance, and self-promotion, and posts over your thresholds fold to a one-line reason.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asaidaoui-netria/xift) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/asaidaoui-netria/xift#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you pay OpenRouter per post judged (README estimates about 3 cents per 1,000 posts) with a default $1/month spending limit. |
| Jev evidence | [`jev.js`](https://github.com/asaidaoui-netria/xift/blob/12ee297ceaf8da6078360267257ca9842ea1f939/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/abdou__dev/status/2111811203387314271)). |
| Maintainer | [asaidaoui-netria](https://github.com/asaidaoui-netria). Independently curated. |
| Format | Firefox add-on (WebExtension) |
| Platform and availability | Firefox 140+ (run with web-ext or self-sign; no addons.mozilla.org listing verified). |
| Jev's role | Jev answers four probability questions per post (text plus first photo); your thresholds, adjusted by Keep and Hide feedback, decide what collapses. |
| Requirements | Firefox 140+; an OpenRouter API key (a dedicated key with a small credit limit is recommended). |
| License | [MIT](https://github.com/asaidaoui-netria/xift/blob/12ee297ceaf8da6078360267257ca9842ea1f939/LICENSE) |

## When to use

- Quiet bait, rage, and promo posts on X without keyword filters.
- Want tunable thresholds and a spending cap on a BYOK key.
- Mismatch: Firefox only; not on the add-ons store, so install is developer-style.

## How it works

`jev.js` POSTs to OpenRouter's `/api/v1/systemone` with `typesafe/jev-1.13-20260917`, asking four yes/no-style questions per post. Scores are cached for 7 days; Keep and Hide feedback moves thresholds; an Always show list skips Jev for trusted authors. Integration evidence: [`jev.js`](https://github.com/asaidaoui-netria/xift/blob/12ee297ceaf8da6078360267257ca9842ea1f939/jev.js).

## Get started

From the upstream README: run `npx web-ext run` in the repo (or sign the add-on with your own AMO keys), allow x.com access, and paste your OpenRouter key.

```sh
git clone https://github.com/asaidaoui-netria/xift && cd xift
npx --yes web-ext@10.7.0 run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [www.netria.dev/articles/decision-model-x-feed/](https://www.netria.dev/articles/decision-model-x-feed/)
- jev.test.js

## Limits and data handling

Post text and the first photo go to OpenRouter and TypeSafe. GitHub reports the license as NOASSERTION, but LICENSE at the pinned commit is the MIT text. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 12ee297ceaf8](https://github.com/asaidaoui-netria/xift/tree/12ee297ceaf8da6078360267257ca9842ea1f939). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
