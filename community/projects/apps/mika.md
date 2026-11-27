# Mika by WangZan (on-device Android AI agent that operates apps and the web, with an optional Jev mode for intent and route decisions)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Android agent that opens apps, taps, types and scrolls on a separate background screen while you keep using the phone, with a built-in browser, schedules, memory and a Linux sandbox for files. There is no Mika server: you bring your own model key or sign in with a supported account. An optional Jev decision mode classifies each request as discussion, reading or action and picks saved routes for repeat tasks, falling back to the main model when unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wangzan101/Mika) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://github.com/wangzan101/Mika/releases/latest) |
| Pricing and access | Free Apache-2.0 app and source. You pay your own model provider; Jev calls are billed by TypeSafe or OpenRouter when the optional mode is on. Checked 2026-11-27. |
| Jev evidence | [`core/src/main/kotlin/com/wangzan101/mika/core/model/decision/SystemOneDecisionModel.kt`](https://github.com/wangzan101/Mika/blob/d0a515665fe27170f0e72372c221a9aa03b39788/core/src/main/kotlin/com/wangzan101/mika/core/model/decision/SystemOneDecisionModel.kt) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [WangZan](https://github.com/wangzan101) (wangzan101). Independently curated. |
| Format | Android app (Kotlin) |
| Platform and availability | Android phone (APK from GitHub Releases); phone control needs wireless-debugging pairing. |
| Jev's role | Optional router. When enabled under Settings › Models › Decision model · Jev, Jev classifies intent at the chat entry point and selects saved routes when experience replay is on; the main model still plans and calls tools, and Jev never operates the phone or replaces confirmation gates. |
| Requirements | Android phone, a main model key or supported account sign-in, and a TypeSafe or OpenRouter key for the optional Jev mode. |
| License | [Apache-2.0](https://github.com/wangzan101/Mika/blob/d0a515665fe27170f0e72372c221a9aa03b39788/LICENSE) |

## When to use

- Android users who want an agent to run multi-step phone and web tasks, with fast intent routing so simple chats skip full planning.
- Mismatch: a Jev-first app; Jev is an optional, off-by-default part of a general phone agent.

## How it works

`SystemOneDecisionModel.kt` posts text state and questions to a System One endpoint (TypeSafe `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0`, OpenRouter, or a custom HTTPS endpoint). Intent classification sends the current request and a little recent conversation; route selection sends the request, candidate templates and extracted parameters. Low probabilities, errors and timeouts fall back to the normal flow. Integration evidence: [`core/src/main/kotlin/com/wangzan101/mika/core/model/decision/SystemOneDecisionModel.kt`](https://github.com/wangzan101/Mika/blob/d0a515665fe27170f0e72372c221a9aa03b39788/core/src/main/kotlin/com/wangzan101/mika/core/model/decision/SystemOneDecisionModel.kt).

## Get started

Install the APK, connect a main model, then optionally enable Jev in Settings.

```sh
# APK: https://github.com/wangzan101/Mika/releases/latest
# Settings › Models › Decision model · Jev → TypeSafe, paste key, Save
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Models and Jev setup: [github.com/wangzan101/Mika/blob/main/docs/models.en.md](https://github.com/wangzan101/Mika/blob/main/docs/models.en.md)
- Setup guide: [github.com/wangzan101/Mika/blob/main/docs/setup-guide.en.md](https://github.com/wangzan101/Mika/blob/main/docs/setup-guide.en.md)

## Limits and data handling

Jev mode is off by default and does not send screenshots. The main model sees screen content while operating apps. The optional xAI sign-in reuses the public sign-in entry of xAI's command-line tool, which the author notes xAI did not set up for Mika and may restrict. Phone control requires wireless-debugging pairing.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit d0a515665fe2](https://github.com/wangzan101/Mika/tree/d0a515665fe27170f0e72372c221a9aa03b39788). Inspected the README, LICENSE, `docs/models.en.md` and `SystemOneDecisionModel.kt` at the pinned commit; the APK was not installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
