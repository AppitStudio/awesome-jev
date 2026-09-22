# JevIntent

[All projects](../README.md) · [Android apps](README.md#android-apps)

FkWeChat / LSPosed WeChat plugin: long-press a message → TypeSafe Jev judges intent, emotion, urgency, and reply stance locally as overlays—no generated reply text and no send.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nisaka520/JevIntent) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Nisaka520/JevIntent#readme) — plugin files for FkWeChat; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-23**. Requires a TypeSafe API key (`api_key=apikey_…`) and a working FkWeChat/LSPosed WeChat host. TypeSafe usage can incur charges. |
| Jev evidence | Inspected [`main.java`](https://github.com/Nisaka520/JevIntent/blob/0023ee2fb92acad8b5bf6f4c524acaed95695a7c/main.java): default endpoint `https://api.typesafe.ai/v1/systemone`, model `jev-latest`; typed Choice questions for intent/emotion/urgency/stance. Device install and live calls were **not** run on the Linux review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, WeChat/Tencent, FkWeChat/LSPosed, or TypeSafe. Listing is not an endorsement. Hooking WeChat may violate platform ToS—review privacy and compliance yourself. Sister of [JevBystander](https://github.com/Nisaka520/JevBystander); distinct from reply-generating [Jev Chat Assistant](jev-chat-jarvis.md). |
| Maintainer | [Nisaka520](https://github.com/Nisaka520). |
| Format | FkWeChat plugin (`main.java` + `info.prop` + local `config.properties`). |
| Platform and availability | Android WeChat with FkWeChat plugin support enabled. Source-only install path documented in README. |
| Jev's role | Judges intent, emotion distribution, urgency, and suggested reply stance; plugin code owns UI/Toasts and never generates reply text or sends messages. |
| Requirements | FkWeChat + TypeSafe key; optional per-chat relationship preset. |
| License | [MIT](https://github.com/Nisaka520/JevIntent/blob/0023ee2fb92acad8b5bf6f4c524acaed95695a7c/LICENSE). |

## When to use

Use it for **judgment-only WeChat overlays** when you already run FkWeChat/LSPosed and do not want reply drafting. Prefer [JevBystander](https://github.com/Nisaka520/JevBystander) for Accessibility-only Toast judgments without hooks, or [Jev Chat Assistant](jev-chat-jarvis.md) when you want ranked fill-only reply candidates.

## How it works

Long-press a text message → menu **意图**. The plugin POSTs structured state to TypeSafe System One and shows fixed overlay lines. Relationship can be cycled per chat. Message text leaves the device on live analysis.

## Get started

```sh
git clone https://github.com/Nisaka520/JevIntent.git
cd JevIntent
git checkout 0023ee2fb92acad8b5bf6f4c524acaed95695a7c
# Copy main.java + info.prop into FkWeChat Plugin/JevIntent/; set api_key in config.properties
# Reload plugin / restart WeChat — device steps not run here
```

## Examples and demos

- README timing notes (v1.9 prefetch) and option taxonomies.
- `test/` helpers for quote/settings/speed (not executed on this host).

## Limits and data handling

Chat text is sent to TypeSafe under your key. Hook-based WeChat access carries ToS and security risk. No live TypeSafe/device validation on this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 0023ee2](https://github.com/Nisaka520/JevIntent/tree/0023ee2fb92acad8b5bf6f4c524acaed95695a7c): MIT. AI-assisted review of README, LICENSE, `main.java` endpoint/defaults. Device/live not run.

Related: [JevBystander](https://github.com/Nisaka520/JevBystander), [Jev Chat Assistant](jev-chat-jarvis.md), [Crush Monitor](crush-monitor.md).
