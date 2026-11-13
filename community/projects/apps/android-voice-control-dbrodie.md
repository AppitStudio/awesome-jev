# Android Voice Control by dbrodie (say a task and GPT-Live hands it to an on-device loop where Jev picks each tap, type or swipe)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Floating mic bubble over every app: you say a task such as "open settings and turn on Bluetooth", GPT-Live turns it into a crisp instruction, and the phone runs a screenshot → decide → act loop through an accessibility service, asking Jev which tap, typing or swipe comes next until the task is done. Based on System One Computer Use by brainstormity.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dbrodie/android-voice-control) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/dbrodie/android-voice-control#readme) (source-built; no separate product site verified). |
| Pricing and access | Free APK and source; TypeSafe usage on your key, plus a ChatGPT Plus/Pro plan or OpenAI API usage for voice. Checked 2026-11-13. |
| Jev evidence | [`app/src/main/java/com/brainstormity/voicecontrol/agent/JevClient.kt`](https://github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/app/src/main/java/com/brainstormity/voicecontrol/agent/JevClient.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [dbrodie](https://github.com/dbrodie). Independently curated. |
| Format | Android app (Kotlin, MIT; APK on GitHub Releases) |
| Platform and availability | Android 11+ (arm64 APK v0.1.1 on GitHub Releases, published 2026-11-13); no Play Store listing verified |
| Jev's role | Jev chooses the next tap, typing or swipe from each screenshot until the spoken task is done. |
| Requirements | Android 11+, a TypeSafe key, and a ChatGPT Plus/Pro sign-in or an OpenAI API key for the voice side. |
| License | [MIT](https://github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/LICENSE) |

## When to use

- Hands-free phone control for simple settings and app tasks.
- Mismatch: banking or other sensitive apps; screenshots of the current screen go to TypeSafe.

## How it works

`JevClient.kt` posts each step to `https://api.typesafe.ai/v1/systemone` (model `jev-1.14.0` in the tests); the key is stored encrypted with Android Keystore and only sent to api.typesafe.ai per the app's privacy note. The README estimates about $0.0002 per step. Integration evidence: [`app/src/main/java/com/brainstormity/voicecontrol/agent/JevClient.kt`](https://github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/app/src/main/java/com/brainstormity/voicecontrol/agent/JevClient.kt).

## Get started

Install the release APK, grant overlay, accessibility, microphone and notification permissions, sign in for voice and paste your TypeSafe key.

```sh
adb install voice-control-0.1.1-arm64-v8a-release.apk   # from GitHub Releases
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/README.md](https://github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/README.md)
- Releases: [github.com/dbrodie/android-voice-control/releases](https://github.com/dbrodie/android-voice-control/releases)
- Architecture: [github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/ARCHITECTURE.md](https://github.com/dbrodie/android-voice-control/blob/b32dc23441f07082589620e2effa8634611e9036/ARCHITECTURE.md)

## Limits and data handling

Screenshots of the current screen go to TypeSafe on your key at each step; voice goes to OpenAI.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit b32dc23441f0](https://github.com/dbrodie/android-voice-control/tree/b32dc23441f07082589620e2effa8634611e9036). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
