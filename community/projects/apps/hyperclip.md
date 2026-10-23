# Hyperclip (macOS video clipper with Jev clip scoring)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native SwiftUI app that turns long videos into short captioned clips on your Mac: it downloads with yt-dlp, transcribes on device, finds clips with built-in scoring, a Jev-compatible decision model or an LLM, frames the speaker and burns in word-by-word captions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexisbcz/hyperclip) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/alexisbcz/hyperclip#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to build. Jev calls use your own TypeSafe key; self-hosted Jev-compatible servers and LLMs are alternatives; optional publishing uses Zernio. Checked 2026-10-23. |
| Jev evidence | [`Hyperclip/Core/Finder.swift`](https://github.com/alexisbcz/hyperclip/blob/f5ee98094f668b8022eb84af4ab1dda4f45bee52/Hyperclip/Core/Finder.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [alexisbcz](https://github.com/alexisbcz). Independently curated. |
| Format | macOS app (SwiftUI), built from source |
| Platform and availability | macOS 26+ on Apple silicon; built from source by the install script. |
| Jev's role | Optional: after built-in scoring shortlists spans, Jev answers typed questions about each candidate clip (hook strength, whether it stands alone, payoff) to rank them. |
| Requirements | Apple silicon Mac with macOS 26+ and Xcode; yt-dlp, FFmpeg and whisper.cpp (installed by the script with Homebrew or from inside the app); a TypeSafe key for the TypeSafe Jev preset. |
| License | [MIT](https://github.com/alexisbcz/hyperclip/blob/f5ee98094f668b8022eb84af4ab1dda4f45bee52/LICENSE) |

## When to use

- Cut talks, podcasts and streams into short clips locally.
- Rank candidate clips with typed questions instead of a full LLM read.
- Mismatch: needs a recent Apple silicon Mac and Xcode to build.

## How it works

`Hyperclip/Core/Finder.swift` offers a TypeSafe Jev preset (`https://api.typesafe.ai`, `/v1/systemone`, `jev-latest`) next to self-hosted Laya, Von or Kev servers, AnyJev and custom endpoints for the decision-model clip finder. Integration evidence: [`Hyperclip/Core/Finder.swift`](https://github.com/alexisbcz/hyperclip/blob/f5ee98094f668b8022eb84af4ab1dda4f45bee52/Hyperclip/Core/Finder.swift).

## Get started

From the upstream README (review the script before running; not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/alexisbcz/hyperclip/main/install.sh | bash
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshot and features in the README: [github.com/alexisbcz/hyperclip#readme](https://github.com/alexisbcz/hyperclip#readme)

## Limits and data handling

With the TypeSafe preset, transcript excerpts of candidate clips go to TypeSafe. The app can read browser cookies to download restricted videos; review that before enabling.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit f5ee98094f66](https://github.com/alexisbcz/hyperclip/tree/f5ee98094f668b8022eb84af4ab1dda4f45bee52). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
