# Tab (Mac next-action autocomplete)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Hackathon proof of concept that predicts your next action on a Mac and shows it as a gray ghost (a highlighted button or gray text); press Tab to do it. Jev picks among code-proposed candidate actions, and x402 paywalls become testnet payments with an amount check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alaramartin/paradigmhacks) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/alaramartin/paradigmhacks#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source; no license file on the reviewed commit (all rights reserved by default). Testnet payments only. Checked 2026-10-16. |
| Jev evidence | [`brain/src/model.ts`](https://github.com/alaramartin/paradigmhacks/blob/f459a79c51440f32a579cf40fd292dd0fcb98226/brain/src/model.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/alara_martin_/status/2110875781819928838)). |
| Maintainer | [alaramartin](https://github.com/alaramartin). Independently curated. |
| Format | macOS Swift shell + TypeScript hub/brain + Chrome over CDP (source only) |
| Platform and availability | macOS (source build; work in progress) |
| Jev's role | Jev picks the next action from code-proposed candidates, with a calibrated confidence. |
| Requirements | macOS, Node.js/TypeScript toolchain, Xcode for the Swift shell, Chrome with a debug profile, a TypeSafe API key; testnet USDC on Base Sepolia for the payment demo. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See how Jev can choose the next UI step from a short list of candidates fast enough for an autocomplete-style UX.
- Study an intent check that blocks a payment when the requested amount does not match the page.
- Mismatch: hackathon proof of concept (Paradigm Frontiers 2026); testnet only; no license file, so the code is source-available, not open source.

## How it works

Code proposes candidate actions for the current screen; `JevDecider` posts them to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and takes the pick with its confidence, caching confident answers per screen and falling back to the cache when Jev is slow or fails. A repeat-what-you-did rule handles patterns with no model call. Integration evidence: [`brain/src/model.ts`](https://github.com/alaramartin/paradigmhacks/blob/f459a79c51440f32a579cf40fd292dd0fcb98226/brain/src/model.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/alaramartin/paradigmhacks.git && cd paradigmhacks
# follow PLAN.md / STATUS.md to start the hub (ws://127.0.0.1:7800), Chrome on CDP 9222 and the Swift shell
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video in the author's X post.
- Build plan and protocol: `PLAN.md`; current state: `STATUS.md`.

## Limits and data handling

Screen and candidate-action descriptions go to TypeSafe on your key; payments use testnet funds only. Never commit keys.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit f459a79c5144](https://github.com/alaramartin/paradigmhacks/tree/f459a79c51440f32a579cf40fd292dd0fcb98226). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
