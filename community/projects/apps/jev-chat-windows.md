# Jev Chat Windows

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows WeChat (4.x) side panel: local offline OCR reads the chat window, TypeSafe Jev (via OpenRouter Decisions) judges intent/emotion and ranks three fill-only reply candidates; send stays manual.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jev-chat/jev-chat-windows) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/jev-chat/jev-chat-windows#readme) — source build or Release zip; no separate hosted product. |
| Pricing and access | MIT source / Release zip has no app purchase fee, checked **2026-09-22**. Requires an OpenRouter API key for Jev Decisions (`typesafe/jev-1.13`) and a generative reply model (OpenRouter or DeepSeek). Provider usage can incur charges. |
| Jev evidence | Inspected [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/0e11956d947d89fbcab678767588ae87899ff46e/core/jev_client.py): posts typed questions to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.13`. Judgment kernel documented as adapted from the Android [Jev Chat Assistant](jev-chat-jarvis.md); capture is Windows Graphics Capture + RapidOCR instead of Accessibility. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, WeChat/Tencent, OpenRouter, DeepSeek, or TypeSafe. Listing is not an endorsement. Source inspected on Linux; Windows GUI, OCR, packing, and live OpenRouter calls were **not** run on the review host. Screenshot/OCR of chat leaves the host on live judgment. |
| Maintainer | [jev-chat](https://github.com/jev-chat) / [rezoch340](https://github.com/rezoch340). Independently curated; not an upstream submission. |
| Format | Python desktop app; Release zip (`jev-chat-windows.exe`) or source (`main.py` / `build.bat`). Reviewed tip **v0.1.6** Release available. |
| Platform and availability | Windows 10/11 with WeChat Windows 4.x. Early source/Release distribution—unsigned exe may trigger SmartScreen. |
| Jev's role | Judges conversation (intent, emotion, action signals) and ranks three drafted replies. Code owns WGC capture, offline OCR, UI, and fill-only paste into WeChat; the user must send. A separate generative model drafts candidates. |
| Requirements | Windows host; `OPENROUTER_API_KEY` (and optional `DEEPSEEK_API_KEY`); Screen / WeChat window visible. Source path needs Python deps per upstream `requirements.txt`. |
| License | [MIT](https://github.com/jev-chat/jev-chat-windows/blob/0e11956d947d89fbcab678767588ae87899ff46e/LICENSE). |

## When to use

Use it when you want a **Windows WeChat sidekick** that never auto-sends, with local OCR and Jev ranking. Prefer [Jev Chat Assistant](jev-chat-jarvis.md) for the Android Accessibility overlay, or [Crush Monitor](crush-monitor.md) for pasted WeChat-style logs on a local analyzer UI. Do not treat intent/risk labels as legal or relationship advice.

## How it works

The app captures the WeChat window, runs offline RapidOCR, and builds a per-session transcript. [`core/jev_client.py`](https://github.com/jev-chat/jev-chat-windows/blob/0e11956d947d89fbcab678767588ae87899ff46e/core/jev_client.py) calls OpenRouter Decisions with TypeSafe Jev questions; a separate model drafts three replies that Jev ranks. The UI shows judgment summary and candidates with **填入微信** / copy—send remains manual. Keys are stored in the user environment (per upstream README), not in project files.

## Get started

```sh
# Release path (Windows): download jev-chat-windows-v0.1.6.zip from GitHub Releases, extract, run jev-chat-windows.exe
# Source path (Windows):
git clone https://github.com/jev-chat/jev-chat-windows.git
cd jev-chat-windows
git checkout 0e11956d947d89fbcab678767588ae87899ff46e
# Follow upstream README for Python deps, then run main.py / build.bat
```

Live judgment sends OCR'd chat text to OpenRouter/TypeSafe and may incur charges. This listing did not run the Windows UI or live calls.

## Examples and demos

- Upstream README screenshots (`docs/ui_*.png`) and Release zip **v0.1.6**.
- Probe scripts under `probe/` for OCR/window experiments (Windows-oriented; not executed on the Linux review host).
- AST parse of `core/jev_client.py` succeeded on the review host.

## Limits and data handling

OCR'd chat content and drafted replies leave the host on live judgment. The tool is personal-use oriented per upstream privacy notes; it does not hook WeChat or read its database. Unsigned Release binaries require SmartScreen acknowledgment. Distinct from the Android [Jev Chat Assistant](jev-chat-jarvis.md) and from macOS `jev-chat/jev-chat-jarvis-mac` (not listed in this PR).

## Review and maintenance

Reviewed on **2026-09-22** at [commit 0e11956](https://github.com/jev-chat/jev-chat-windows/tree/0e11956d947d89fbcab678767588ae87899ff46e): MIT; Release tag **v0.1.6**. AI-assisted source review of README, `core/jev_client.py`, LICENSE. Offline: Python AST parse of `jev_client.py` OK. No Windows GUI, OCR, packaging, or live OpenRouter/TypeSafe on the review host.

Related: [Jev Chat Assistant](jev-chat-jarvis.md), [Crush Monitor](crush-monitor.md).
