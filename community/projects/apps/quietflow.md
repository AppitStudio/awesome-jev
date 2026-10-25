# QuietFlow (Android notification attention manager with opt-in Jev classification)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Android proof of concept that listens to notifications and sorts them into five attention classes, from action required to hide; local safety rules protect OTP, security, finance, calls and system notifications, Jev classifies the rest when you opt in, and observation mode (never dismissing anything) is the default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KoheiTakada/QuietFlow) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/KoheiTakada/QuietFlow#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls are billed to your TypeSafe key. Checked 2026-10-26. |
| Jev evidence | [`app/src/main/java/dev/quietflow/JevClassifier.java`](https://github.com/KoheiTakada/QuietFlow/blob/edab949e05809acf32778fae2ecfb295a138f8f8/app/src/main/java/dev/quietflow/JevClassifier.java) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [KoheiTakada](https://github.com/KoheiTakada). Independently curated. |
| Format | Android app (Java, platform UI only) |
| Platform and availability | Android 10+, built from source or from the CI debug APK artifact; not on Google Play. |
| Jev's role | Optional but central: with a key and explicit permission, Jev picks one of the five classes for redacted notification text, with confidence; high-confidence results drive active-mode actions. |
| Requirements | Android 10+ device (tuned for Pixel); Android Studio or Gradle to build; your own TypeSafe API key for Jev. |
| License | [MIT](https://github.com/KoheiTakada/QuietFlow/blob/edab949e05809acf32778fae2ecfb295a138f8f8/LICENSE) |

## When to use

- Quiet low-value notifications without missing ones that need action.
- Watch the classifier in observation mode before letting it act.
- Mismatch: MVP; README is partly Japanese and redaction is not a full privacy guarantee.

## How it works

`JevClassifier.java` posts redacted notification text with one Choice question to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); protected, low-confidence or failed cases are never dismissed. Integration evidence: [`app/src/main/java/dev/quietflow/JevClassifier.java`](https://github.com/KoheiTakada/QuietFlow/blob/edab949e05809acf32778fae2ecfb295a138f8f8/app/src/main/java/dev/quietflow/JevClassifier.java).

## Get started

From the upstream README (not run on the review host):

```sh
gradle :app:assembleDebug
# install app/build/outputs/apk/debug/app-debug.apk, grant notification access,
# then enter a TypeSafe key and allow cloud classification in the app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KoheiTakada/QuietFlow#readme](https://github.com/KoheiTakada/QuietFlow#readme)

## Limits and data handling

Redacted notification content (digits, phone numbers and emails removed) goes to TypeSafe only after you enable it. The key is encrypted with Android Keystore and local history is capped at 1,000 events.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit edab949e0580](https://github.com/KoheiTakada/QuietFlow/tree/edab949e05809acf32778fae2ecfb295a138f8f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
