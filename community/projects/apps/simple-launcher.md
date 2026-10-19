# Simple Launcher

[All projects](../README.md) · [Android apps](README.md#android-apps)

Minimal Android home app styled after Omarchy's waybar and walker: status bar, next event, notifications, recent apps, and a fuzzy app search where Jev picks the app by meaning when nothing matches by name.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/polidog/simple-launcher) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/polidog/simple-launcher#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-19. |
| Jev evidence | [`app/build.gradle.kts`](https://github.com/polidog/simple-launcher/blob/512d97e9d3c1493fec9ddfd6ba3d846e1825b576/app/build.gradle.kts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [polidog](https://github.com/polidog). Independently curated. |
| Format | Android app (Kotlin, Gradle) |
| Platform and availability | Android (build from source and sideload; tested on Pixel 4a, Android 13; no Play Store listing verified). |
| Jev's role | Semantic fallback in search: when no prefix or word-start match exists, Jev chooses the app that fits the query (for example "music" finds the music app). |
| Requirements | JDK 21, Android SDK, adb; optional `TYPESAFE_API_KEY` in `local.properties` (baked into the APK). |
| License | [MIT](https://github.com/polidog/simple-launcher/blob/512d97e9d3c1493fec9ddfd6ba3d846e1825b576/LICENSE) |

## When to use

- Want a keyboard-first, minimal Android launcher.
- Want search to find apps by meaning, not only by name.
- Mismatch: the API key is compiled into the APK, so use it only on your own device.

## How it works

Search filters installed apps by prefix, word start, substring and subsequence. When the first two find nothing, the app asks Jev to choose among installed apps and inserts the pick with a marker. `app/build.gradle.kts` reads `TYPESAFE_API_KEY` into `BuildConfig`; without it the Jev feature is hidden. Integration evidence: [`app/build.gradle.kts`](https://github.com/polidog/simple-launcher/blob/512d97e9d3c1493fec9ddfd6ba3d846e1825b576/app/build.gradle.kts).

## Get started

From the upstream README: build with JDK 21, install with adb, and set it as the home activity.

```sh
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README demo mode (`--ez demo true`)

## Limits and data handling

Search text and app names go to TypeSafe when the Jev fallback runs. Japanese-language README.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 512d97e9d3c1](https://github.com/polidog/simple-launcher/tree/512d97e9d3c1493fec9ddfd6ba3d846e1825b576). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
