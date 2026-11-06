# bianzhu-android (personal Android assistant fork with TypeSafe Jev as a judge provider)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Personal-maintained Android assistant based on jev-chat/jev-chat-jarvis: visible-text OCR, WeChat helpers, local contact memory and reply suggestions, with TypeSafe direct connect among several judge providers for decisions users confirm before send.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xlgbyyds/bianzhu-android) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/xlgbyyds/bianzhu-android#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-07. |
| Jev evidence | [`app/src/main/java/com/jev/probe/SettingsActivity.kt`](https://github.com/xlgbyyds/bianzhu-android/blob/58fa25ba36c6e8f29996f2147e719a46e1517f3a/app/src/main/java/com/jev/probe/SettingsActivity.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [xlgbyyds](https://github.com/xlgbyyds). Independently curated. |
| Format | Android app (Kotlin, MIT) |
| Platform and availability | Android (personal fork of jev-chat-jarvis). |
| Jev's role | Optional TypeSafe-direct judge provider among OpenRouter / Bocha Jev / Vercel / OpenCode Zen / custom endpoints for reply and relationship suggestions; messages are user-confirmed before send. |
| Requirements | Android build toolchain and a TypeSafe (or other listed provider) key for the judge lane. |
| License | [MIT](https://github.com/xlgbyyds/bianzhu-android/blob/58fa25ba36c6e8f29996f2147e719a46e1517f3a/LICENSE) |

## When to use

- Build a Chinese-first Android chat assistant with a TypeSafe judge.
- Keep send confirmation in the user's hands.
- Mismatch: personal fork; Chinese README; not an official TypeSafe app.

## How it works

`SettingsActivity.kt` exposes `PROVIDER_TYPESAFE` with a default TypeSafe judge base URL among other providers; judgment calls use the selected provider key. Integration evidence: [`app/src/main/java/com/jev/probe/SettingsActivity.kt`](https://github.com/xlgbyyds/bianzhu-android/blob/58fa25ba36c6e8f29996f2147e719a46e1517f3a/app/src/main/java/com/jev/probe/SettingsActivity.kt).

## Get started

Clone, open in Android Studio, set a TypeSafe key in settings, and build a debug APK.

```sh
git clone https://github.com/xlgbyyds/bianzhu-android.git && cd bianzhu-android
# Android Studio sync + run
# set TypeSafe key in in-app settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xlgbyyds/bianzhu-android/blob/58fa25ba36c6e8f29996f2147e719a46e1517f3a/README.md](https://github.com/xlgbyyds/bianzhu-android/blob/58fa25ba36c6e8f29996f2147e719a46e1517f3a/README.md)

## Limits and data handling

Visible chat text and suggestion context are sent to the configured judge provider on your key. The app does not auto-send messages.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 58fa25ba36c6](https://github.com/xlgbyyds/bianzhu-android/tree/58fa25ba36c6e8f29996f2147e719a46e1517f3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
