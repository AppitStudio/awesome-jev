# Resenha (free push-to-talk dictation for macOS with local Whisper and optional Jev corrections)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native push-to-talk dictation for Portuguese, English and Spanish: hold a shortcut, speak, and whisper.cpp transcribes on your Mac and types into the active field. Optionally, Jev judges only the transcript and local alternatives to pick contextual corrections; when it is unsure, the original text wins. A public unsigned Windows beta also exists.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luisroquette-labs/resenha) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://luisroquette-labs.github.io/resenha/) |
| Pricing and access | Free download and source (MIT); Jev corrections use your own provider key. Checked 2026-11-01. |
| Jev evidence | [`Sources/WhisperKey/ContextualCorrections.swift`](https://github.com/luisroquette-labs/resenha/blob/dc02d4130ee03a455ced115fe8ce28c566e2f57c/Sources/WhisperKey/ContextualCorrections.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/thedoomguy_ai/status/2116519306464747645)). |
| Maintainer | [luisroquette-labs](https://github.com/luisroquette-labs). Independently curated. |
| Format | Native macOS app (Swift); Windows beta EXE |
| Platform and availability | macOS 14+ on Apple Silicon; unsigned Windows beta. |
| Jev's role | Optional choice between the original transcript and local correction candidates. |
| Requirements | Apple Silicon Mac with macOS 14+ and Accessibility permission; optional TypeSafe or OpenRouter key for Jev corrections. |
| License | [MIT](https://github.com/luisroquette-labs/resenha/blob/dc02d4130ee03a455ced115fe8ce28c566e2f57c/LICENSE) |

## When to use

- Dictate into any app locally, with optional context-aware fixes for words Whisper confuses.
- Mismatch: Jev is optional and only sees text, never audio.

## How it works

Transcription runs locally with whisper.cpp. `Sources/WhisperKey/ContextualCorrections.swift` (model `typesafe/jev-1.14`) asks Jev to choose between the original transcript and local correction candidates; the Windows port does the same in `Windows/Resenha.Platform/JevContextualResolver.cs`. Integration evidence: [`Sources/WhisperKey/ContextualCorrections.swift`](https://github.com/luisroquette-labs/resenha/blob/dc02d4130ee03a455ced115fe8ce28c566e2f57c/Sources/WhisperKey/ContextualCorrections.swift).

## Get started

From the upstream README (not run on the review host):

```sh
# download from https://luisroquette-labs.github.io/resenha/ and move Resenha to Applications
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project site and download: [luisroquette-labs.github.io/resenha/](https://luisroquette-labs.github.io/resenha/)
- Mention on X: [x.com/thedoomguy_ai/status/2116519306464747645](https://x.com/thedoomguy_ai/status/2116519306464747645)

## Limits and data handling

Audio and transcription stay on the Mac; with Jev enabled, transcript text and candidates are sent to the configured provider. The Windows build is an unsigned beta. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit dc02d4130ee0](https://github.com/luisroquette-labs/resenha/tree/dc02d4130ee03a455ced115fe8ce28c566e2f57c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
