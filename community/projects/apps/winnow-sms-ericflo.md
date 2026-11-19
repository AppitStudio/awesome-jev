# Winnow by Eric Florenzano (Android SMS app that classifies every text before it can buzz your phone, Jev first)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Full SMS/MMS app for Android that replaces Google Messages as your default and decides, for each incoming text, whether it deserves your attention: personal and transactional notify, marketing arrives silently, political and spam go to Filtered with no notification, and nothing is deleted. Decisions come from rules on the phone, an on-phone model you train with one-tap labels, and an optional classifier service: Jev by TypeSafe or OpenRouter, any System One server, or any OpenAI-compatible model. Each filtered conversation says what decided it and why.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ericflo/winnow) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ericflo/winnow#readme) (source-built; no separate product site verified). |
| Pricing and access | Free APK and MIT source; the optional Jev service is billed to your own TypeSafe or OpenRouter key (the author estimates about $0.0001 a text). Checked 2026-11-19. |
| Jev evidence | [`classifier/src/main/kotlin/com/ericflo/winnow/classifier/providers/SystemOneProvider.kt`](https://github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/classifier/src/main/kotlin/com/ericflo/winnow/classifier/providers/SystemOneProvider.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ericflo](https://github.com/ericflo). Independently curated. |
| Format | Android app (Kotlin) |
| Platform and availability | Android 12 or later; APK from GitHub Releases (v0.1.73 on 2026-11-06), not on Google Play. SMS/MMS only, no RCS. |
| Jev's role | Optional classifier service: answers a typed choice over five categories for texts the on-phone rules and model leave undecided, after redaction. |
| Requirements | Android 12+; set as default SMS app with RCS off in Google Messages. A TypeSafe or OpenRouter key only if you enable the Jev service. |
| License | [MIT](https://github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/LICENSE) |

## When to use

- Keep spam, scams and political blasts from buzzing your phone while seeing why each text was filtered.
- Mismatch: RCS chats or iPhone; it is an SMS/MMS-only Android app installed outside Google Play.

## How it works

`SystemOneProvider.kt` sends redacted text (digits, emails and links masked) to `https://api.typesafe.ai/v1/systemone` (or OpenRouter's decisions endpoint) as a multiple-choice question with probabilities; contacts, people you have texted and verification codes never leave the phone. Integration evidence: [`classifier/src/main/kotlin/com/ericflo/winnow/classifier/providers/SystemOneProvider.kt`](https://github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/classifier/src/main/kotlin/com/ericflo/winnow/classifier/providers/SystemOneProvider.kt).

## Get started

Install the APK from the latest release and set Winnow as the default SMS app; add a Jev key in settings only if you want the service.

```sh
# Install: download winnow-X.Y.Z.apk from https://github.com/ericflo/winnow/releases
# Build from source (JDK 17+, Android SDK API 37):
git clone https://github.com/ericflo/winnow && cd winnow
./gradlew :app:assembleDebug
adb install -r app/build/outputs/apk/debug/app-debug.apk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/README.md](https://github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/README.md)
- Architecture: [github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/docs/ARCHITECTURE.md](https://github.com/ericflo/winnow/blob/755b226c370bd264f7c64f5a0454ffc43008d0ee/docs/ARCHITECTURE.md)
- Releases: [github.com/ericflo/winnow/releases](https://github.com/ericflo/winnow/releases)

## Limits and data handling

With the service on, redacted text of undecided messages goes to TypeSafe or OpenRouter, and the README limits optional backlog labelling by a service to zero-retention providers; the sender's number is shared only if you enable it. On-phone-only mode keeps everything local. Accuracy figures in the README are the author's cross-validation on hand-written texts.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 755b226c370b](https://github.com/ericflo/winnow/tree/755b226c370bd264f7c64f5a0454ffc43008d0ee). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
