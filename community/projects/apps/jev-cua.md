# Jev Voice (CUA)

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

Native macOS floating bar for continuous voice and text commands. Jev selects the next Accessibility action from the live UI; Swift runs an observe–act–verify loop with no generative LLM planner.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ronadin2002/jev-cua) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [jev-cua project homepage](https://github.com/ronadin2002/jev-cua) — source-build app branded **Jev Voice**; no separate product site. |
| Pricing and access | Public GitHub source has **no app purchase fee**, checked **2026-09-23**. Build with `bash build.sh` on Apple silicon macOS 14+. Requires your own **OpenRouter** (`sk-or-…`) or **TypeSafe** (`apikey_…`) key in Settings (Keychain). Provider usage can incur charges; free-tier eligibility was not verified. |
| Jev evidence | Inspected [`Sources/Core.swift`](https://github.com/ronadin2002/jev-cua/blob/098e9348fbfc7afae61575960c15cdaaae960b0b/Sources/Core.swift) `JevProvider` / `JevClient`: OpenRouter posts to `/api/alpha/decisions` with `~typesafe/jev-latest`; TypeSafe posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`. Architecture: [docs/architecture.md](https://github.com/ronadin2002/jev-cua/blob/098e9348fbfc7afae61575960c15cdaaae960b0b/docs/architecture.md). Live voice and desktop control were not tested on the Linux review host. |
| Disclosure | Public source without a published open-source license (GitHub license null; no `LICENSE`/`COPYING` in the reviewed tree)—treat as **all rights reserved** / source-available, not Open source. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not an endorsement. |
| Maintainer | [ronadin2002](https://github.com/ronadin2002) (Ron Adin / [@adin_ron](https://x.com/adin_ron)). |
| Format | Native Swift macOS application (`Jev Voice.app`) with on-device speech recognition and Accessibility automation. |
| Platform and availability | **Apple silicon**, **macOS 14+**. Experimental source-build; GitHub Actions macOS build/self-test badge. No App Store package was verified. |
| Jev's role | Chooses one next atomic UI action (and related parameter choices such as typing text) from a live catalogue discovered via Accessibility. Native speech handles STT; Swift executes and re-observes. **No LLM planner** generates free-form commands or prose. Jev use is required for computer control. |
| Requirements | Apple silicon Mac, macOS 14+, Xcode command-line tools, Accessibility + Microphone + Speech Recognition permissions, OpenRouter or TypeSafe API key. |
| License | **Unlicensed public source** at review tip—no `LICENSE`/`COPYING` file and null GitHub license field. Default copyright / all-rights-reserved unless the author adds terms. |

## When to use

Use this when you want a **persistent floating bar** and a **multi-step observe–act–verify loop** over live macOS controls, driven by continuous voice or typed commands.

Prefer [Jev Voice](jev-voice.md) (`kevinbadi/jev-voice`) for a Python / whisper.cpp prototype that maps each utterance to a closed typed-action set in one fan-out. Prefer [Cua jev-use](../tools/cua-jev-use.md) for a Cua Driver browser-form integration recipe, not a native floating-bar app. Prefer [macbrow](macbrow.md) when you need Gradium TTS plus an LLM tool-generation path.

## How it works

On-device speech (or typed Return) supplies the original request. The app discovers installed apps and the current Accessibility tree, groups large catalogues under Jev’s choice limit, and asks Jev for the next action. Swift executes via Accessibility / keyboard / pointer APIs, then re-observes until Jev selects completion; a separate Jev check compares the screen to the full request. See [architecture.md](https://github.com/ronadin2002/jev-cua/blob/098e9348fbfc7afae61575960c15cdaaae960b0b/docs/architecture.md).

## Get started

```sh
git clone https://github.com/ronadin2002/jev-cua.git
cd jev-cua
git checkout 098e9348fbfc7afae61575960c15cdaaae960b0b
# On Apple silicon macOS 14+ with Xcode CLT:
bash build.sh
open 'dist/Jev Voice.app'
```

In **Settings → General**, paste an OpenRouter or TypeSafe key (provider is detected from the key prefix). Grant Accessibility, Microphone, and Speech Recognition. Upstream documents credential-free `--self-test` / `--activity-test` after build. This review did **not** run `build.sh` or live control on the Linux host.

## Examples and demos

- README demo GIF / [MP4](https://github.com/ronadin2002/jev-cua/raw/098e9348fbfc7afae61575960c15cdaaae960b0b/assets/demo.mp4) (Chrome, search, Calculator, Photo Booth)—a recording, not a performance benchmark.
- Menu-bar **Settings & diagnostics → Jev activity** for request/option/error traces.

## Limits and data handling

Speech stays on-device. **Commands, relevant screen text, and action options** go to OpenRouter or TypeSafe for Jev decisions. Keys stay in Keychain. Secure fields are excluded. Missing or stale Accessibility trees can fail; completion checks can be wrong; Jev does not read screenshots or invent prose. Supervise early Accessibility use. Distinct from [Jev Voice](jev-voice.md) and [Cua jev-use](../tools/cua-jev-use.md).

## Review and maintenance

Reviewed on **2026-09-23** at [commit 098e934](https://github.com/ronadin2002/jev-cua/tree/098e9348fbfc7afae61575960c15cdaaae960b0b) (merge of direct TypeSafe API support). AI-assisted source review of README, `Sources/Core.swift` (`JevProvider`/`JevClient`), architecture docs, and tree license scan (no LICENSE). No macOS build, permission grant, or live provider calls were performed on the Linux review host. Discovered via [X](https://x.com/adin_ron/status/2102433115918725337).
