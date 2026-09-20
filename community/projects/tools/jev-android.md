# jev-android

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Kotlin Android UI-agent SDK: builds a dynamic action table from the accessibility tree; **TypeSafe Jev** (or optional DeepSeek) selects the next operation/targets; an accessibility service executes clicks, text replace, scroll, back, and allowed app launches. Distinct from [Mobile Jev](mobile-jev.md) (Mobilerun JS agent/studio).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dougsong/jev-android) |
| Maintainer | [dougsong](https://github.com/dougsong). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Kotlin multi-module Gradle project **0.2.0** (`core`, `sdk`, `sample`); local Maven publication only (not on Maven Central). |
| Requirements | Android SDK / Gradle build; TypeSafe key for Jev **or** DeepSeek key for the alternate provider. Sample includes a local fixture screen. API still unstable per upstream. |
| License | [MIT](https://github.com/dougsong/jev-android/blob/cbb26de39e2ac05f2b6065a28a606ab4dcb398a2/LICENSE). Provider inference costs are separate. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and upstream VALIDATION.md inspected; Android SDK builds and live provider calls were not run on the review host. |

## When to use

Use it when you want an **in-process Android SDK** that lets Jev choose among observed controls with host-supplied exact `textValues`, package allowlists, and stale-screen guards. Prefer [Mobile Jev](mobile-jev.md) for a Mobilerun-based agent/studio workflow.

## How it works

[`sdk/.../JevProvider.kt`](https://github.com/dougsong/jev-android/blob/cbb26de39e2ac05f2b6065a28a606ab4dcb398a2/sdk/src/main/kotlin/io/github/jevandroid/JevProvider.kt) posts multi-question Choice payloads to `https://api.typesafe.ai/v1/systemone` (`jev-latest` default). Protocol parsing and decision rules live in the same module for fixture tests without network. DeepSeek is an optional alternate `DecisionProvider`. Accessibility runtime executes accepted actions only after fingerprint checks.

## Get started

```sh
git clone https://github.com/dougsong/jev-android.git
cd jev-android
git checkout cbb26de39e2ac05f2b6065a28a606ab4dcb398a2
# Follow upstream README for Gradle/Android SDK setup and sample install.
# Upstream VALIDATION.md reports offline unit tests and local Maven publish for 0.2.0.
```

Set a TypeSafe or DeepSeek API key only for live decisions. Live UI state leaves the device toward the selected provider; this listing did not run Gradle or live calls.

## Examples and demos

- Upstream [VALIDATION.md](https://github.com/dougsong/jev-android/blob/cbb26de39e2ac05f2b6065a28a606ab4dcb398a2/VALIDATION.md): **55 offline unit tests** reported passed for 0.2.0 (not re-run here); prior device baseline on API 33 with a deterministic provider (not live Jev).
- Sample app with provider picker and fixture activity.

## Limits and data handling

Accessibility labels/values are untrusted data in prompts. Keys must not be logged by the SDK paths inspected. Not published to Maven Central. Device coverage and live model quality are unverified here. HyperOS/third-party permission quirks are out of scope for this listing.

## Review and maintenance

Reviewed on **2026-09-20** at [commit cbb26de](https://github.com/dougsong/jev-android/tree/cbb26de39e2ac05f2b6065a28a606ab4dcb398a2): **0.2.0**, MIT. AI-assisted source review of README, LICENSE, `JevProvider.kt`, module layout, and VALIDATION.md. No Android SDK on the review host; no live TypeSafe/DeepSeek calls.

Related: [Mobile Jev](mobile-jev.md), [jev-macos-loop](jev-macos-loop.md), [Cua jev-use](cua-jev-use.md).
