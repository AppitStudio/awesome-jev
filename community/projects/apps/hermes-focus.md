# Hermes Focus (Mac app that keeps you on task in 25-minute blocks, judged by Jev on your own keys)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac focus app: type what you are about to do, start a 25-minute block, and the app reads the front window once a second and asks Jev whether you are on task; a nudge appears only after about twenty seconds of confident drift, with one "I'm on task" button to correct it. Each block ends with a score out of 1,000 weighed against a rubric for your goal. No server or account.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/philiprmocanu-cell/hermes-focus) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/philiprmocanu-cell/hermes-focus#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. TypeSafe usage is billed to your key; the author estimates one to three dollars per full day of blocks. Checked 2026-10-29. |
| Jev evidence | [`Sources/FocusCore/Clients/TypeSafeClient.swift`](https://github.com/philiprmocanu-cell/hermes-focus/blob/99f618583c4afd953a0cbfb53464f810d6ab1650/Sources/FocusCore/Clients/TypeSafeClient.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [philiprmocanu-cell](https://github.com/philiprmocanu-cell). Independently curated. |
| Format | Native macOS app (Swift) |
| Platform and availability | macOS 14+ on Apple silicon; build from source with `install.sh` (no notarized release verified). |
| Jev's role | Per-second judgment of whether the current screen matches the block's goal and rubric. |
| Requirements | A Mac with Apple silicon, Xcode command line tools, a TypeSafe API key; optionally an Anthropic key for rubrics and advice. |
| License | [MIT](https://github.com/philiprmocanu-cell/hermes-focus/blob/99f618583c4afd953a0cbfb53464f810d6ab1650/LICENSE) |

## When to use

- Get honest feedback on focus during deep-work blocks.
- Mismatch: screen text and screenshots leave your Mac for judging.

## How it works

`Sources/FocusCore/Clients/TypeSafeClient.swift` posts the window state to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), and `Sources/FocusCore/Judge/Judge.swift` turns the answers into drift and milestone signals. Integration evidence: [`Sources/FocusCore/Clients/TypeSafeClient.swift`](https://github.com/philiprmocanu-cell/hermes-focus/blob/99f618583c4afd953a0cbfb53464f810d6ab1650/Sources/FocusCore/Clients/TypeSafeClient.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/philiprmocanu-cell/hermes-focus && cd hermes-focus
./install.sh --launch   # then choose "Run on my own keys" and paste a TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/philiprmocanu-cell/hermes-focus#readme](https://github.com/philiprmocanu-cell/hermes-focus#readme)

## Limits and data handling

Front-window text, page addresses and small screenshots go to TypeSafe (and to Anthropic when that key is set); history stays in Application Support.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 99f618583c4a](https://github.com/philiprmocanu-cell/hermes-focus/tree/99f618583c4afd953a0cbfb53464f810d6ab1650). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
