# Notiq

[All projects](../README.md) · [Android apps](README.md#android-apps)

Native Android notification filter: natural-language rules plus TypeSafe Jev (or self-hosted FastJev) Choice keep/filter/uncertain—high-threshold filtering only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chengyongru/notiq) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/chengyongru/notiq#readme) — source-built Android app; no separate store listing verified. |
| Pricing and access | Public source has **no LICENSE file** at tip—not Open source. Build with JDK/Android SDK; TypeSafe or self-hosted FastJev endpoint + key. No app purchase fee observed **2026-09-24**. |
| Jev evidence | Inspected [`DecisionClient.kt`](https://github.com/chengyongru/notiq/blob/c44a262056a4d932f588a0d4ec41337cbffea42f/app/src/main/java/dev/notiq/network/DecisionClient.kt): POST `{base}/v1/systemone` with Choice `keep`/`filter`/`uncertain` over app/title/body + user rule; HTTPS required for `jev` provider; threshold ∈ 0.90–1.0. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. No LICENSE; APK/device/live calls not run on Linux review host. |
| Maintainer | [chengyongru](https://github.com/chengyongru). Independently curated. |
| Format | Kotlin Android app (Gradle). |
| Platform and availability | Source build (Android); Notification Access permission required. |
| Jev's role | Per-notification keep/filter judgment; code applies threshold. FastJev self-host supported as alternate endpoint. |
| Requirements | JDK + Android SDK; TypeSafe API key or FastJev URL; Notification Listener access. |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. |

## When to use

Use it for **rule-shaped Android notification quieting** with calibrated filter confidence. Prefer OS Do Not Disturb when you only need schedule-based muting.

## How it works

Notification Access feeds app/title/body into `DecisionClient`. The user rule is embedded in Choice instructions; uncertain/low-probability results keep the notification. Keys and endpoints are configured in-app; redirects and cleartext (except localhost) are rejected.

## Get started

```sh
git clone https://github.com/chengyongru/notiq.git
cd notiq
git checkout c44a262056a4d932f588a0d4ec41337cbffea42f
# Android Studio / Gradle assemble; grant Notification Access; configure Jev endpoint + key
```

See upstream README (EN/ZH) and `docs/verification.md`.

## Examples and demos

- README banners and verification docs.
- Unit test `DecisionClientTest.kt` (not executed here).

## Limits and data handling

Notification text leaves the device on live Jev/FastJev calls. High default thresholds reduce false filters but can miss spam. No OSS license file.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit c44a262](https://github.com/chengyongru/notiq/tree/c44a262056a4d932f588a0d4ec41337cbffea42f). AI-assisted README + `DecisionClient.kt` inspection. No device install or live spend.

Related: [Tab Bouncer](tab-bouncer.md), [Jev Content Guard](jev-content-guard.md).
