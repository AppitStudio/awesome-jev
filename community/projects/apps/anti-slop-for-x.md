# Anti Slop for X (Chrome extension that folds AI-bait and bot replies on X, scored by Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension for x.com that pre-screens replies with local keywords, then optionally sends a post and its parent to a decision model through your own proxy worker. Jev answers whether it reads like AI engagement bait, which kind of bait it is and how strongly; replies over the threshold are folded with the score and reason shown, and mute or block only happens when you click. Inspired by slop-filter (MIT) but written independently. README in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Caph-dev/anti-slop-for-x) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Caph-dev/anti-slop-for-x#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you run the proxy and bring your own TypeSafe key. Checked 2026-10-30. |
| Jev evidence | [`extension/lib/adapters/jev.ts`](https://github.com/Caph-dev/anti-slop-for-x/blob/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28/extension/lib/adapters/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Caph-dev](https://github.com/Caph-dev). Independently curated. |
| Format | Chrome MV3 extension (WXT, TypeScript) + small proxy worker |
| Platform and availability | Desktop Chrome; build and load unpacked (no Chrome Web Store listing verified). |
| Jev's role | Scores each reply for AI engagement bait so the extension can fold it. |
| Requirements | Node.js to build; a local Node proxy or Cloudflare Worker you run, holding a TypeSafe key. |
| License | [MIT](https://github.com/Caph-dev/anti-slop-for-x/blob/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28/LICENSE) |

## When to use

- Hide low-effort AI and bot replies on X without auto-blocking anyone.
- Mismatch: not on the Chrome Web Store; the Cloudflare Worker deployment is still a scaffold.

## How it works

`adapters/jev.ts` builds the state (post and parent text) with noul, choice and score questions for `jev-latest`; the worker only adds authorization and forwards to `/systemone`. Integration evidence: [`extension/lib/adapters/jev.ts`](https://github.com/Caph-dev/anti-slop-for-x/blob/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28/extension/lib/adapters/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd anti-slop-for-x
npm install
npm run build
# chrome://extensions -> Developer mode -> Load unpacked -> extension/.output/chrome-mv3
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy policy draft and architecture: [github.com/Caph-dev/anti-slop-for-x/tree/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28/docs](https://github.com/Caph-dev/anti-slop-for-x/tree/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28/docs)

## Limits and data handling

Post and parent text of screened replies go through your proxy to TypeSafe. New project; privacy policy is a draft. Not affiliated with X or TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 3141a39aa861](https://github.com/Caph-dev/anti-slop-for-x/tree/3141a39aa8616b3cde50b2fa3a3426aa2e2b5e28). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
