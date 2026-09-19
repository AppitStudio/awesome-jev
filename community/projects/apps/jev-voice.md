# Jev Voice

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

Hands-free macOS voice assistant: local whisper.cpp transcription, one TypeSafe Jev fan-out per command to select typed actions and arguments, then AppleScript/accessibility execution.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kevinbadi/jev-voice) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [jev-voice project homepage](https://github.com/kevinbadi/jev-voice) — source-run access; no separate product website. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-19**. Requires a TypeSafe key for routing. Local speech uses whisper.cpp (setup downloads models). Provider usage can incur charges; free-tier eligibility was not verified. |
| Jev evidence | Inspected [brain.py](https://github.com/kevinbadi/jev-voice/blob/cc697957bd9a67ee63e038b83361a26138706df0/jev_voice/brain.py) posting Choice/Noul questions to `TYPESAFE_URL` (default `https://api.typesafe.ai/v1/systemone`). Live voice and desktop actions were not tested. |
| Disclosure | Free source access does not include inference. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. |
| Maintainer | [kevinbadi](https://github.com/kevinbadi). |
| Format | Python voice application (`jev-voice` console script) with local mic/TTS and macOS automation. |
| Platform and availability | macOS, Apple Silicon–oriented setup (whisper.cpp Metal). Experimental **0.1.0** source-run prototype. No packaged App Store release was verified. |
| Jev's role | Selects action type and typed arguments (app, site, text candidate, shortcuts, scroll, and related gates) in one request. whisper.cpp handles STT; code executes via Accessibility/AppleScript. Jev does not generate free-form commands. |
| Requirements | Python **≥ 3.12**, `uv`/setup script dependencies, microphone, Accessibility and Input Monitoring permissions, `TYPESAFE_API_KEY`. Caps Lock remapping is optional via setup scripts. |
| License | [MIT](https://github.com/kevinbadi/jev-voice/blob/cc697957bd9a67ee63e038b83361a26138706df0/LICENSE). |

## When to use

Explore hands-free open/type/search/scroll/shortcut workflows where a single Jev request maps an utterance onto a closed action set. Prefer [macbrow](macbrow.md) if you need Gradium TTS, Chrome remote-debugging browser tasks, or an LLM tool-generation fallback. Prefer [Jev Voice Browser](../tools/jev-voice-browser.md) for Playwright page control rather than native macOS automation.

## How it works

Energy VAD feeds whisper.cpp; [Brain](https://github.com/kevinbadi/jev-voice/blob/cc697957bd9a67ee63e038b83361a26138706df0/jev_voice/brain.py) builds a multi-question System One payload (action Choice, addressed/compound Noul gates, app/site/engine/text Choices, and related argument questions). Application code maps selected answers to actions and runs them locally. `--dry-run` / `--text` exercise routing without the mic.

## Get started

Setup downloads tools and models; it does not require a live Jev call until you route a command.

```sh
git clone https://github.com/kevinbadi/jev-voice.git
cd jev-voice
git checkout cc697957bd9a67ee63e038b83361a26138706df0
cp .env.example .env   # add TYPESAFE_API_KEY
./scripts/setup.sh
jev --text "open chrome and go to youtube" --dry-run
```

Expected: a dry-run routing report without executing desktop actions (exact output depends on upstream). Live mic modes need permissions and incur TypeSafe usage for each command. This review did not run setup or dry-run on macOS.

## Examples and demos

Upstream README documents `jev`, `--hold`, `--always-on`, `--ptt`, and `--dry-run`. No automated unit test suite was found in the reviewed tree.

## Limits and data handling

Utterances and candidate strings are sent to TypeSafe when routing. Local audio stays on-device for STT. Accessibility automation can control the desktop—supervise early use. Confidence gates are operational, not measured accuracy. Distinct from [Jev Voice Browser](../tools/jev-voice-browser.md) and [macbrow](macbrow.md).

## Review and maintenance

Reviewed on **2026-09-19** at [commit cc69795](https://github.com/kevinbadi/jev-voice/tree/cc697957bd9a67ee63e038b83361a26138706df0): package **0.1.0**, MIT. AI-assisted source review of `brain.py`, `config.py`, `actions.py`, and README. No macOS execution, permission grant, or live TypeSafe calls were performed on the Linux review host.
