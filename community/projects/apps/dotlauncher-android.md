# DotLauncher (Android home app in a waybar/walker style where Jev finds apps by meaning and sorts them into categories)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Simple Android home app with a pixel-font, Omarchy-style bar and search: when no name matches, Jev picks installed apps by meaning ("music" finds music apps), and apps with no or too-broad categories are sorted into category pages by Jev once, with the answer kept on the device.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ptyhard/dot-launcher) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ptyhard/dot-launcher#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-13. |
| Jev evidence | [`app/src/main/java/jp/ptyhard/dotlauncher/JevSearch.kt`](https://github.com/ptyhard/dot-launcher/blob/c29e5732364dee8f205038a9d964040e9798ae88/app/src/main/java/jp/ptyhard/dotlauncher/JevSearch.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ptyhard](https://github.com/ptyhard). Independently curated. |
| Format | Android app built from source with Gradle (Kotlin, MIT; UI in Japanese) |
| Platform and availability | Android (tested by the author on Android 13 and 16); source build, no store release verified |
| Jev's role | Jev picks matching apps by meaning when name search finds nothing, and assigns categories to apps that declare none or only "Productivity". |
| Requirements | Android device, JDK 21 and the Android SDK to build, and an optional TypeSafe key entered in settings. |
| License | [MIT](https://github.com/ptyhard/dot-launcher/blob/c29e5732364dee8f205038a9d964040e9798ae88/LICENSE) |

## When to use

- Find apps on your phone by meaning rather than exact name.
- Mismatch: if you need an English UI or a store install; it is a Japanese-UI source build.

## How it works

`JevSearch.kt` posts to `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0`, warming the connection ahead of the first query; without a key the meaning search stays off and uncategorized apps go to "Other". The key stays on the device. Integration evidence: [`app/src/main/java/jp/ptyhard/dotlauncher/JevSearch.kt`](https://github.com/ptyhard/dot-launcher/blob/c29e5732364dee8f205038a9d964040e9798ae88/app/src/main/java/jp/ptyhard/dotlauncher/JevSearch.kt).

## Get started

Build the debug APK and install it with adb, then paste your key into settings by long-pressing an empty spot on home.

```sh
./gradlew assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with demo GIFs: [github.com/ptyhard/dot-launcher/blob/c29e5732364dee8f205038a9d964040e9798ae88/README.md](https://github.com/ptyhard/dot-launcher/blob/c29e5732364dee8f205038a9d964040e9798ae88/README.md)

## Limits and data handling

Search text and app names/labels go to TypeSafe on your key; category answers are cached on the device.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit c29e5732364d](https://github.com/ptyhard/dot-launcher/tree/c29e5732364dee8f205038a9d964040e9798ae88). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
