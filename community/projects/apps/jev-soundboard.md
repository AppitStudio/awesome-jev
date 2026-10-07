# Jev Soundboard

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Live AI soundboard that listens to a call (FaceTime, Zoom, Meet, Discord or a stream), transcribes it and lets TypeSafe Jev decide whether to react and which clip to play within about a second; 15 built-in synthesized sounds, local control panel and an optional Discord bot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kiggsworthy/jev-soundboard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Kiggsworthy/jev-soundboard#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the MIT source build. Requires your own TypeSafe key (Jev) and OpenAI key (speech-to-text); upstream estimates about $0.30–0.40 per hour of constant talk (prices as of October 2026). Checked 2026-10-07. |
| Jev evidence | [`jevboard/jev.py`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/jevboard/jev.py) sends one request per new speech slice to `api.typesafe.ai/v1/systemone` with a `react_now` Noul and a `clip` Choice; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Kiggsworthy](https://github.com/Kiggsworthy). Independently curated. |
| Format | Python CLI app (`jevboard`, uv) with local web control panel and optional Discord bot |
| Platform and availability | Self-run on macOS (loopback audio via a virtual device, ffmpeg) or as a Discord bot; source build only. |
| Jev's role | Jev reads the rolling ~25 s transcript and answers two questions per slice — should a reaction land right now, and which clip (or none). Code applies the trigger level, minimum gap and no-repeat rules; OpenAI does the transcription. |
| Requirements | uv, ffmpeg, a virtual audio device for call routing (see upstream audio setup), `TYPESAFE_API_KEY` and `OPENAI_API_KEY`; Discord bot token for the Discord transport. |
| License | [MIT](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/LICENSE). |

## When to use

- Add reactive sound effects to a call or stream without pressing buttons.
- Try `jevboard try "..."` to see which clip Jev picks for a line before wiring up audio.
- Mismatch: it listens to everyone on the call — tell participants (the Discord bot announces itself).

## How it works

A slicer cuts call audio every 1.2 s, skips silence and streams speech to OpenAI Realtime transcription ([`jevboard/transcribe.py`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/jevboard/transcribe.py)). Each new slice triggers one Jev call ([`jevboard/jev.py`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/jevboard/jev.py)) with the rolling transcript; recently played clips are removed from the Choice. [`jevboard/sidekick.py`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/jevboard/sidekick.py) applies the rules and the mixer plays the clip back into the call through the chosen transport.

## Get started

Quickstart from the README:

```sh
git clone https://github.com/Kiggsworthy/jev-soundboard.git && cd jev-soundboard
uv sync
cp .env.example .env            # add TYPESAFE_API_KEY and OPENAI_API_KEY
uv run jevboard effects --play all
uv run jevboard try "he said he'd win and then fell off the map"
```

Jev decisions and OpenAI transcription are billed to your keys; the panel shows both meters live.

## Examples and demos

- Audio routing guides: [`docs/AUDIO-SETUP.md`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/docs/AUDIO-SETUP.md) and [`docs/DISCORD.md`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/docs/DISCORD.md).
- Build your own clip library: [`docs/BUILD-YOUR-CLIP-LIBRARY.md`](https://github.com/Kiggsworthy/jev-soundboard/blob/e3f110f2bca20843025f9c03c0592b852b29e304/docs/BUILD-YOUR-CLIP-LIBRARY.md).

## Limits and data handling

Audio streams to OpenAI and transcript text to TypeSafe; upstream states nothing is recorded to disk and transcripts stay in a ~25 s in-memory window. The control panel binds to localhost with a random token. Cost figures are upstream estimates. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit e3f110f2bca2](https://github.com/Kiggsworthy/jev-soundboard/tree/e3f110f2bca20843025f9c03c0592b852b29e304). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
