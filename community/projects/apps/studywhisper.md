# StudyWhisper (Windows study assistant that listens only when you switch monitoring on and uses Jev to decide which transcribed speech is a real study question)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows 10/11 tray app (README in Portuguese) that listens on a pausable microphone or system source, filters silence locally with Silero VAD, transcribes through OpenRouter, and sends only the transcribed text to a Jev classifier. Clear study questions get a short text answer from a model you choose; comments and interjections are ignored, and incomplete speech waits up to 12 seconds. Monitoring always starts off.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rnahumaf/StudyWhisper) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/rnahumaf/StudyWhisper#readme) (source-built; no separate product site verified). |
| Pricing and access | Free and open source (MIT) with no subscription or included balance; transcription, Jev, answer and search calls are billed to your own OpenRouter key. Checked 2026-11-05. |
| Jev evidence | [`src/StudyWhisper.Core/Settings.cs`](https://github.com/rnahumaf/StudyWhisper/blob/7f4b0974a7553fa3036ff22947267ab94741aa3a/src/StudyWhisper.Core/Settings.cs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [rnahumaf](https://github.com/rnahumaf). Independently curated. |
| Format | Windows desktop app (.NET, per-user installer, MIT) |
| Platform and availability | Windows 10/11 x64 (per-user installer from GitHub Releases) |
| Jev's role | Text classifier that decides which transcribed speech is a clear study question to answer and which comments to ignore. |
| Requirements | Windows 10/11 x64, a recording device, internet, your own OpenRouter key, and the Microsoft Visual C++ v14 Redistributable for the local ONNX filter; the installer includes .NET. |
| License | [MIT](https://github.com/rnahumaf/StudyWhisper/blob/7f4b0974a7553fa3036ff22947267ab94741aa3a/LICENSE) |

## When to use

- Get text-only answers to spoken study questions without answering every comment in the room.
- Choose your own transcription, Jev and answer models through OpenRouter and see per-call costs.
- Mismatch: accuracy of the question filter for real Portuguese speech depends on the route you choose, and the README states it does not identify TV or speakers.

## How it works

`Settings.cs` makes Jev (default `typesafe/jev-1.14`, with 1.13 selectable) the classifier that decides whether transcribed text is a question that should be answered; only the transcribed text and, if memory is on, the last ten question and answer pairs reach Jev. Integration evidence: [`src/StudyWhisper.Core/Settings.cs`](https://github.com/rnahumaf/StudyWhisper/blob/7f4b0974a7553fa3036ff22947267ab94741aa3a/src/StudyWhisper.Core/Settings.cs).

## Get started

From the upstream README (not run on the review host):

```sh
# download StudyWhisper-0.1.7-Setup-x64.exe from the project's Releases page and run it
# then paste your OpenRouter key in Settings and choose transcription, JEV and answer models
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (listening, privacy, costs, versions): [github.com/rnahumaf/StudyWhisper/blob/7f4b0974a7553fa3036ff22947267ab94741aa3a/README.md](https://github.com/rnahumaf/StudyWhisper/blob/7f4b0974a7553fa3036ff22947267ab94741aa3a/README.md)
- Releases: [github.com/rnahumaf/StudyWhisper/releases](https://github.com/rnahumaf/StudyWhisper/releases)

## Limits and data handling

Approved audio goes to speech-to-text through OpenRouter, transcripts and context go to Jev and the answer model, and optional web search sends a model-written query to a search service; all billed to your OpenRouter key with no built-in spending cap. The installer is not digitally signed. Several newer versions described in the README are local and unpublished.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 7f4b0974a755](https://github.com/rnahumaf/StudyWhisper/tree/7f4b0974a7553fa3036ff22947267ab94741aa3a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
