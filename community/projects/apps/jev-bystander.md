# JevBystander

[All projects](../README.md) · [Android apps](README.md#android-apps)

Android Accessibility WeChat reader: TypeSafe Jev judges intent, emotion, urgency, and reply stance, then shows exactly three Toasts—no reply generation, no send, ~861 KB APK with zero third-party runtime deps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nisaka520/JevBystander) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product page](https://nisaka520.github.io/JevBystander/) · [GitHub README](https://github.com/Nisaka520/JevBystander#readme) |
| Pricing and access | MIT source / debug-signed Release APK has no app purchase fee, checked **2026-09-23**. Requires TypeSafe API key + Accessibility permission. TypeSafe usage can incur charges. |
| Jev evidence | Inspected [`JevHttp.kt`](https://github.com/Nisaka520/JevBystander/blob/229b290c414060c80c07c345a8be00f6c0525cb0/app/src/main/java/io/github/nisaka520/jevbystander/JevHttp.kt): sole network exit `POST https://api.typesafe.ai/v1/systemone` with Bearer key. APK build, device install, and live calls were **not** run on the Linux review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, WeChat/Tencent, or TypeSafe. Listing is not an endorsement. Accessibility chat reading has privacy implications—review yourself. Sister of [JevIntent](https://github.com/Nisaka520/JevIntent); judgment-only (unlike reply-drafting [Jev Chat Assistant](jev-chat-jarvis.md)). |
| Maintainer | [Nisaka520](https://github.com/Nisaka520). |
| Format | Kotlin Android app (zero third-party deps; HttpURLConnection + hand-rolled JSON). |
| Platform and availability | Android 8.0+; [Release APK](https://github.com/Nisaka520/JevBystander/releases/latest) (debug-signed for self-use) or `./gradlew assembleDebug` (JDK 17, Android SDK 35). WeChat single-chat focus. |
| Jev's role | Judges intent/emotion/urgency/stance over on-screen digest; app code owns Accessibility read + three Toasts. Does not generate reply text or send. |
| Requirements | TypeSafe key; enable Accessibility service **旁观者 · 微信判读**. |
| License | [MIT](https://github.com/Nisaka520/JevBystander/blob/229b290c414060c80c07c345a8be00f6c0525cb0/LICENSE). |

## When to use

Use it for **Toast-only WeChat judgments** without LSPosed/FkWeChat. Prefer [JevIntent](https://github.com/Nisaka520/JevIntent) when you want hook-based long-press on the exact message, or [Jev Chat Assistant](jev-chat-jarvis.md) when you want ranked fill-only replies.

## How it works

Trigger via tile / Accessibility shortcut / notification. [`WeChatReader`](https://github.com/Nisaka520/JevBystander/tree/229b290c414060c80c07c345a8be00f6c0525cb0/app/src/main/java/io/github/nisaka520/jevbystander) builds a digest from the Accessibility tree; `JevHttp` posts to System One; `Toast3` shows three lines. Visible on-screen text only—no OCR/screenshot path in the reviewed revision.

## Get started

```sh
git clone https://github.com/Nisaka520/JevBystander.git
cd JevBystander
git checkout 229b290c414060c80c07c345a8be00f6c0525cb0
# Or install Release APK; then enable Accessibility and set TypeSafe key in-app
# ./gradlew assembleDebug / testDebugUnitTest — not run on this Linux host
```

## Examples and demos

- Product page and README sample Toast layout.
- Unit tests under `app/src/test` (including `LiveJevSmokeTest` — live not run here).

## Limits and data handling

On-screen chat text leaves the device on live TypeSafe calls. Debug-signed APKs are for personal installs. No device/live validation on this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 229b290](https://github.com/Nisaka520/JevBystander/tree/229b290c414060c80c07c345a8be00f6c0525cb0): MIT. AI-assisted review of README, LICENSE, `JevHttp.kt`. Gradle/APK/live not run.

Related: [JevIntent](https://github.com/Nisaka520/JevIntent), [Jev Chat Assistant](jev-chat-jarvis.md), [Crush Monitor](crush-monitor.md).
