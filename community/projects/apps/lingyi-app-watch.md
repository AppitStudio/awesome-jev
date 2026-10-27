# LingYi App Watch (local macOS app-update dashboard, with optional Jev upgrade-risk ratings)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local-first macOS update dashboard that gathers pending updates from Homebrew, the Mac App Store, GitHub Releases, Sparkle appcasts and other sources, flags third-party sources and lets you mark apps as do-not-upgrade or to-verify; with a TypeSafe key, each pending update also gets a Jev risk level, confidence and reason. Chinese-language UI and docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jascenn/lingyi-app-watch) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://watch.lingyi.tools) |
| Pricing and access | Open source (MIT); free. Optional Jev calls are billed to your own TypeSafe key. Checked 2026-10-28. |
| Jev evidence | [`src/core/jev.ts`](https://github.com/Jascenn/lingyi-app-watch/blob/0ef65b8330d2040c6bcd7e8047f2274424e071a4/src/core/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Jascenn](https://github.com/Jascenn). Independently curated. |
| Format | Local web dashboard and CLI (TypeScript) |
| Platform and availability | macOS; run from source (Node.js) at 127.0.0.1:4123. |
| Jev's role | Optional upgrade-risk rating for each pending update, with a confidence and reason. |
| Requirements | macOS and Node.js; a TypeSafe API key only for the AI risk assessment. |
| License | [MIT](https://github.com/Jascenn/lingyi-app-watch/blob/0ef65b8330d2040c6bcd7e8047f2274424e071a4/LICENSE) |

## When to use

- Decide which Mac app updates to apply first, and which to hold.
- Mismatch: Chinese UI; the AI rating is optional.

## How it works

`src/core/jev.ts` posts each pending update to `https://api.typesafe.ai/v1/systemone` (override with `TYPESAFE_ENDPOINT`) using the key from the environment or the in-app AI settings. Integration evidence: [`src/core/jev.ts`](https://github.com/Jascenn/lingyi-app-watch/blob/0ef65b8330d2040c6bcd7e8047f2274424e071a4/src/core/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Jascenn/lingyi-app-watch.git && cd lingyi-app-watch
npm install
npm run dev   # opens http://127.0.0.1:4123
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Website: [watch.lingyi.tools](https://watch.lingyi.tools)
- README (Chinese): [github.com/Jascenn/lingyi-app-watch#readme](https://github.com/Jascenn/lingyi-app-watch#readme)

## Limits and data handling

App names, versions and source details go to TypeSafe only when the AI rating is on. Everything else stays on the Mac.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 0ef65b8330d2](https://github.com/Jascenn/lingyi-app-watch/tree/0ef65b8330d2040c6bcd7e8047f2274424e071a4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
