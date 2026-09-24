# JevGuide

[All projects](../README.md) · [Android apps](README.md#android-apps)

Android WeChat relationship-progress assistant: Accessibility or screenshot vision reads the chat, TypeSafe Jev scores intent/emotion/urgency/affinity (“攻略度”), then a chat model drafts three reply candidates on a persistent overlay—never sends for you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nisaka520/JevGuide) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product page](https://nisaka520.github.io/JevGuide/) — intro, APK, privacy. |
| Pricing and access | MIT source and [Release APK](https://github.com/Nisaka520/JevGuide/releases/latest); your TypeSafe key plus optional OpenAI-compatible chat/vision keys. No app purchase fee, checked **2026-09-24**. Provider usage billed separately. |
| Jev evidence | Inspected [`JevHttp.kt`](https://github.com/Nisaka520/JevGuide/blob/36c09f62bc684f091f7141c4b7bbf185f2edb037/app/src/main/java/io/github/nisaka520/jevguide/JevHttp.kt): POST `https://api.typesafe.ai/v1/systemone`. README documents eight Jev questions per analysis. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. APK/device/live Jev not run on the Linux review host. |
| Maintainer | [Nisaka520](https://github.com/Nisaka520). Independently curated. |
| Format | Native Android app (Accessibility overlay + optional vision path). |
| Platform and availability | Android; JDK 17 / SDK 35 source build or Release APK. Sister of JevBystander/JevIntent (same author). |
| Jev's role | Judges relationship signals and affinity; a separate chat model drafts replies. Jev is required for the judgment path. |
| Requirements | Android device; Accessibility (and optional screenshot) permissions; TypeSafe API key in settings; optional vision/chat endpoints. |
| License | [MIT](https://github.com/Nisaka520/JevGuide/blob/36c09f62bc684f091f7141c4b7bbf185f2edb037/LICENSE). |

## When to use

Use it for **on-device WeChat coaching** with a sticky affinity bar and draft replies. Prefer [JevBystander](jev-bystander.md) for judgment-only Toasts, or [Jev Chat Assistant](jev-chat-jarvis.md) for a different overlay stack.

## How it works

Screen text comes from the Accessibility tree or a vision OCR fallback (newer WeChat may return empty a11y trees). Local per-contact memory is merged into state; Jev answers typed questions; code updates the overlay and asks a chat model for three styled candidates. Nothing is auto-sent.

## Get started

```sh
git clone https://github.com/Nisaka520/JevGuide.git
cd JevGuide
git checkout 36c09f62bc684f091f7141c4b7bbf185f2edb037
# Build with Android Studio / Gradle (JDK 17, SDK 35), or install the Release APK
# Enable Accessibility; paste TypeSafe (+ optional chat/vision) keys in Settings
```

## Examples and demos

- Product page and README pipeline diagram.
- Unit tests under `app/src/test/...` (not executed on this review host).

## Limits and data handling

Chat excerpts and memory leave the device for TypeSafe (and optional vision/chat providers). Keys stay in app settings. Newer WeChat versions may force the paid vision path when a11y is empty. Not a medical or relationship-advice product.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 36c09f6](https://github.com/Nisaka520/JevGuide/tree/36c09f62bc684f091f7141c4b7bbf185f2edb037). AI-assisted README + `JevHttp.kt` inspection. No APK install or live TypeSafe spend.

Related: [JevBystander](jev-bystander.md), [JevIntent](jev-intent.md), [Jev Chat Assistant](jev-chat-jarvis.md).
