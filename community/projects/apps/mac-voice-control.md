# Mac Voice Control

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Hands-free macOS control by voice: Deepgram or local Whisper speech-to-text, typed action routing by Jev (`typesafe/jev` through Command Code's provider API) or an LLM over a closed action set, and AppleScript/Accessibility execution; open apps, drive browser tabs and dictate code into IntelliJ or VS Code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nagesh-bhosle/mac-voice-control) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nagesh-bhosle/mac-voice-control#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the MIT source build. Jev routing uses a **Command Code** provider key (third-party relay for `typesafe/jev`); Deepgram STT is optional (local Whisper is free). Each provider bills separately. Checked 2026-10-07. |
| Jev evidence | [`src/mac_voice/brain/jev_router.py`](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/src/mac_voice/brain/jev_router.py) builds typed questions over the closed action catalog in [`candidates.py`](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/src/mac_voice/brain/candidates.py) and calls Command Code's `/provider/v1/systemone` with model `typesafe/jev`; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [nagesh-bhosle](https://github.com/nagesh-bhosle). Independently curated. |
| Format | Python CLI/daemon (`mac_voice`, uv) with wake word |
| Platform and availability | macOS (Apple Silicon preferred) for live mic and execution; Linux supports routing tests and `--dry-run` only. Source build only. |
| Jev's role | With `--use-jev`, Jev picks the action and slots from a closed catalog for each utterance; a local heuristic or Command Code LLM can route instead. Code validates the action and executes it via AppleScript/Accessibility — model output is never run as shell. |
| Requirements | macOS with Microphone, Accessibility and Automation permissions; Python 3.12+, uv; Homebrew ffmpeg/whisper-cpp via `scripts/setup.sh`; `COMMAND_CODE_API_KEY` for Jev/LLM routing; optional `DEEPGRAM_API_KEY`. |
| License | [MIT](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/LICENSE). |

## When to use

- Open apps, switch browser tabs or dictate code on a Mac without touching the keyboard.
- Try routing safely with `--dry-run`, which prints the plan without executing.
- Mismatch: Jev is reached through Command Code, not TypeSafe directly; macOS permissions grant broad control.

## How it works

Audio is transcribed by Deepgram or local Whisper ([`src/mac_voice/stt/`](https://github.com/nagesh-bhosle/mac-voice-control/tree/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/src/mac_voice/stt)); [`jev_router.py`](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/src/mac_voice/brain/jev_router.py) asks Jev to choose among closed actions; [`exec/dispatcher.py`](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/src/mac_voice/exec/dispatcher.py) rejects unknown actions and runs the rest through AppleScript and Accessibility. The only shell path is a fixed `screencapture` call.

## Get started

Setup and a dry run:

```sh
git clone https://github.com/nagesh-bhosle/mac-voice-control.git && cd mac-voice-control
cp .env.example .env    # add COMMAND_CODE_API_KEY (and DEEPGRAM_API_KEY if used)
./scripts/setup.sh
uv run python -m mac_voice --text "open chrome and open facebook in a tab" --dry-run
```

Jev/LLM routing is billed via your Command Code key; Deepgram transcription is billed by Deepgram; Whisper runs locally.

## Examples and demos

- Utterance examples: [`docs/examples.md`](https://github.com/nagesh-bhosle/mac-voice-control/blob/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f/docs/examples.md).
- README *Voice coding* and *Safety: closed actions*.

## Limits and data handling

Utterance text goes to Command Code (relaying to Jev) and, if enabled, audio to Deepgram. Third-party relay — not TypeSafe's own API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit d9e11fd4c4f4](https://github.com/nagesh-bhosle/mac-voice-control/tree/d9e11fd4c4f4f05d73bd768e6d571fb950a5ae9f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
