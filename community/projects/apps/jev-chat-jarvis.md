# Jev Chat Assistant

[All projects](../README.md) · [Android apps](README.md#android-apps)

Non-invasive Android overlay that reads on-screen chat via Accessibility, uses TypeSafe Jev (OpenRouter Decisions) for intent/danger/action judgments and reply ranking, and fills—but never sends—candidate replies. WeChat is the first proven surface.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Finderchangchang/jev-chat-JARVIS) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Finderchangchang/jev-chat-JARVIS#readme) — source-built Android APK; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Requires an OpenRouter API key for Jev Decisions and a generative reply model. OpenRouter/TypeSafe usage can incur charges. |
| Jev evidence | Inspected [`JevClient.kt`](https://github.com/Finderchangchang/jev-chat-JARVIS/blob/6d36bcd9a45fe00a7dcc01c452f2eae4cca95b92/app/src/main/java/com/jev/probe/jev/JevClient.kt): posts typed questions to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13` (seven judgment questions plus candidate ranking). Generative drafting uses a separate chat-completions model (default DeepSeek). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, WeChat/Tencent, Feishu/Lark, OpenRouter, or TypeSafe. Listing is not an endorsement. Source inspected; Android SDK build, device install, Accessibility enablement, and live OpenRouter calls were **not** run on the Linux review host. Accessibility disguise for WeChat node reading is documented upstream—review platform ToS and privacy implications yourself. |
| Maintainer | [Finderchangchang](https://github.com/Finderchangchang). |
| Format | Kotlin Android app (Gradle); debug APK via `./gradlew assembleDebug`. |
| Platform and availability | Android (WeChat 8.0.78 reported working); Feishu/Lark and other IM surfaces described as in progress. Early source distribution—no Play Store listing reviewed here. |
| Jev's role | Judges on-screen conversation (intent, danger score, needs, whether to reply, best action, tension/literal signals) and ranks three drafted replies. Code owns capture, overlay UI, and fill-only paste; send stays manual. A separate generative model drafts candidates. |
| Requirements | JDK 17, Android SDK (platform/build-tools 35), OpenRouter key, Accessibility + overlay + OEM background permissions. |
| License | [MIT](https://github.com/Finderchangchang/jev-chat-JARVIS/blob/6d36bcd9a45fe00a7dcc01c452f2eae4cca95b92/LICENSE). |

## When to use

Use it when you want a side-panel judgment layer over an existing mobile chat app without integrating that app’s APIs, and you accept Accessibility capture plus BYOK inference. Prefer [Crush Monitor](crush-monitor.md) for pasted WeChat-style logs on a local desktop UI, or ordinary manual replies when you do not want chat text leaving the device. Do not treat danger/intent labels as legal, safety, or relationship advice.

## How it works

An Accessibility service reads visible chat bubbles, builds a snapshot, and calls OpenRouter Decisions with TypeSafe Jev questions in one fan-out. A generative model drafts three replies; Jev ranks them. A translucent overlay shows judgments and ranked candidates; **Fill** / clipboard paste writes into the input box only—the user must tap send. Keys stay in app-private storage per upstream docs. Screenshots of the overlay and settings pages are in the upstream README.

## Get started

```sh
git clone https://github.com/Finderchangchang/jev-chat-JARVIS.git
cd jev-chat-JARVIS
git checkout 6d36bcd9a45fe00a7dcc01c452f2eae4cca95b92
# Requires JDK 17 + Android SDK (sdk.dir in local.properties)
./gradlew assembleDebug
# Install app/build/outputs/apk/debug/app-debug.apk, set OpenRouter key in Settings,
# enable Accessibility / overlay / OEM autostart as documented upstream.
```

Live analysis sends on-screen chat text and drafted replies to OpenRouter (Jev + generative model) and can incur charges. This listing did not build or install the APK.

## Examples and demos

- Upstream overlay and settings screenshots under [`docs/images/`](https://github.com/Finderchangchang/jev-chat-JARVIS/tree/6d36bcd9a45fe00a7dcc01c452f2eae4cca95b92/docs/images).
- Settings connectivity test path in `SettingsActivity` (live OpenRouter).
- No separate offline fixture suite was found in the reviewed tree.

## Limits and data handling

Chat text and relationship prompts leave the device on live analysis. Group chat “other party” modelling is limited. OEM background kills (e.g. HyperOS) can interrupt capture. Upstream notes Jev’s primary training language is English while chat may be Chinese. Accessibility service class-name disguise for WeChat is an upstream implementation detail—evaluate ToS/privacy risk before use. Fills never auto-send; transfer/red-packet UI is intentionally untouched per README.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 6d36bcd](https://github.com/Finderchangchang/jev-chat-JARVIS/tree/6d36bcd9a45fe00a7dcc01c452f2eae4cca95b92): MIT. AI-assisted source review of README, LICENSE, `JevClient.kt`, capture/overlay activities. Android Gradle build, device install, and live OpenRouter calls were not run.

Related: [Crush Monitor](crush-monitor.md), [jev-android](../tools/jev-android.md) (developer UI-agent SDK—not this end-user overlay).
