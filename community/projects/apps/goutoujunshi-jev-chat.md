# Goutoujunshi Jev Chat

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

WeChat companion (macOS source preview + Windows preview ZIP): screen-read the chat, analyze with optional TypeSafe Jev strategy judgment, and draft ranked replies—you always send manually.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/shengjidaguai-china/goutoujunshi-jev-chat](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat) |
| Pricing and access | MIT source/preview builds from GitHub Releases (Mac source ZIP; Windows exe ZIP). No app purchase fee. DeepSeek (or OpenAI-compatible) for drafts; optional TypeSafe Jev key for strategy. Checked 2026-09-25. |
| Jev evidence | [README_EN.md](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/blob/7e32ecc22ebbec79922a077a3f50de3935d92f2c/README_EN.md) documents optional TypeSafe Jev as a strategy layer before the reply model; separate Keychain entries for DeepSeek vs Jev. |
| Disclosure | Open source MIT preview builds. Provider costs separate (BYOK). Windows device validation still pending upstream. Independently curated; no affiliation. Listing is not an endorsement. GUI/OCR/live Jev not run on the Linux review host. |
| Maintainer | [shengjidaguai-china](https://github.com/shengjidaguai-china). Independently curated. |
| Format | Application (desktop overlay beside WeChat). |
| Platform and availability | macOS source preview (Python 3.12 + uv); Windows 10/11 WeChat 4.x preview exe. No signed `.app` / no APK yet. |
| Jev's role | Optional strategy judgment before draft generation; OCR and reply text use other local/cloud components. |
| Requirements | WeChat for Mac or Windows 4.x; Screen Recording/Accessibility (Mac); DeepSeek key; optional `TypeSafe Jev` key. |
| License | [MIT](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/blob/7e32ecc22ebbec79922a077a3f50de3935d92f2c/LICENSE). |

## When to use

Use as a **WeChat sidekick** that suggests intent analysis and reply drafts without auto-send. Prefer thinner classifiers if you only need labels without drafting.

## How it works

Local OCR (Apple Vision by default) reads the visible chat; optional DeepSeek vision can replace OCR. An optional Jev strategy step runs before a chat model drafts candidates; fill/copy never presses Send.

## Get started

```sh
# Prefer Releases artifacts; or:
git clone https://github.com/shengjidaguai-china/goutoujunshi-jev-chat.git
cd goutoujunshi-jev-chat
git checkout 7e32ecc22ebbec79922a077a3f50de3935d92f2c
# Follow README_EN.md Mac/Windows preview steps
```

## Examples and demos

- Screenshots and offline demo scripts in the README / documentation folder.
- Releases: Mac source ZIP and Windows preview ZIP.

## Limits and data handling

Screenshots or recognized text may go to DeepSeek when that path is enabled; Jev receives strategy questions when configured. Confidence percentages in the UI are not calibrated outcome probabilities.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 7e32ecc](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/tree/7e32ecc22ebbec79922a077a3f50de3935d92f2c). AI-assisted README_EN/LICENSE inspection; desktop WeChat flows not run on the review host.

Related: [Jev Chat Windows](jev-chat-windows.md), [Crush Monitor with Jev](crush-monitor-with-jev.md).
