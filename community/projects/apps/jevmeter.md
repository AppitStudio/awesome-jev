# Jevmeter

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

A command-line video editor that overlays Jev sentence judgments and assembles clips with captions, gauges and speaker summaries.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChetasLua/jevmeter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/ChetasLua/jevmeter#readme) |
| Pricing and access | [Manual installation](https://github.com/ChetasLua/jevmeter#-command-line-for-power-users) has no app purchase fee. A TypeSafe account/key and paid inference may be required; reviewed 2026-09-19. |
| Jev evidence | [Scoring implementation](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/jevmeter/score.py) sends one request per sentence with preset Noul questions. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. Source inspected; end-to-end operation was not tested. |
| Maintainer | [Chetas Lua](https://github.com/ChetasLua) |
| Format | Python CLI with interactive wizard, video renderer and JSON presets; version 0.1.0 |
| Platform and availability | Source build; macOS/Linux installer, manual Windows instructions. Apple Silicon uses mlx-whisper; other systems can use faster-whisper. |
| Jev's role | Scores rhetorical properties of transcript sentences; local code averages scores, chooses highlight intervals and renders the edit. |
| Requirements | Python 3.9+, Whisper backend/model, FFmpeg support through imageio-ffmpeg, TypeSafe key, footage and optional speaker-labeled transcript. |
| License | [MIT](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/LICENSE); third-party demonstration footage has separate rights. |

## When to use

Use it to experiment with annotated debate, interview, podcast or presentation footage,
or to build custom question presets for a video-analysis workflow. Its labels describe
model judgments about wording in limited context. They do not establish truth, deception,
speaker reliability or a fair comparison between people.

## How it works

[Transcription](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/jevmeter/transcribe.py)
runs Whisper locally, downloading model weights when needed. An optional `NAME: text`
transcript supplies speaker labels and text, aligned to audio timestamps; otherwise
speech belongs to one speaker.

Each scoring request goes to TypeSafe `/v1/systemone` with `jev-latest` by default.
The state includes the sentence, speaker, recent context turn, up to 25 earlier statements
and a bounded answer-so-far. Presets supply independent Noul questions and criteria.
Application code averages configured questions into an index and computes flag thresholds.
Pillow and FFmpeg produce video frames, captions, effects and the soundtrack.

## Get started

Follow the [upstream manual setup](https://github.com/ChetasLua/jevmeter#-command-line-for-power-users).
For a CPU-based installation on macOS/Linux:

```sh
git clone https://github.com/ChetasLua/jevmeter.git
cd jevmeter
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[cpu]'
```

On Apple Silicon, use `.[mlx]` instead. Set `TYPESAFE_API_KEY` privately in your environment
or use `jevmeter setup`, which checks the key through a live request and stores it in
user configuration. `jevmeter doctor` also checks a configured key online.

The following is a **live scoring and rendering command**, not an offline demonstration.
It sends transcript context to TypeSafe and may make multiple billable requests:

```sh
jevmeter run pitch.mp4 --preset sales_pitch --speakers Founder \
  --mode full --start 60 --end 120
```

The expected artifact is `pitch.jevmeter.mp4` with a work/cache directory beside it.
Use your own suitable video. The interactive `jevmeter` wizard offers the same workflow;
`--score-only` skips rendering but still performs provider scoring.

## Examples and demos

- [Fictional debate materials](https://github.com/ChetasLua/jevmeter/tree/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/examples) include a transcript, recorded summary and a macOS text-to-speech video generator. The subsequent scoring command still calls Jev.
- [Preset definitions](https://github.com/ChetasLua/jevmeter/tree/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/jevmeter/presets) cover debate, earnings-call, podcast and sales-pitch rhetoric.
- [Upstream evaluation report](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/eval/RESULTS.md) documents an author-reported labeled sentence evaluation. Its results were not reproduced and do not establish accuracy on real videos.

## Limits and data handling

Provider answers are indexed directly as `noul` values without comprehensive type,
range or completeness validation. Missing answer keys can fail downstream planning.
There is no uncertainty/abstention path before scores become overlays and averages.
Requests retry up to six times; authentication failures stop the run. Other exhausted
failures are logged and omitted from the scored timeline, potentially changing coverage.

Transcripts, scores, summaries and edit plans persist in the local work directory.
Score-cache invalidation includes model and questions, but not all source/context changes;
use a fresh work directory when replacing footage or transcripts. Audio and rendering are
local; text context reaches TypeSafe. Optional URL inputs use yt-dlp and contact the source
site. Model downloads and dependencies require network access.

The reported cost counter uses a configurable fixed price, not verified billing.
Speaker attribution, sentence timing and short-context rhetorical judgments can be wrong.
Highlights emphasize high scores by design. Inspect the full transcript, output and
coverage before sharing; do not reuse upstream performance or political comparisons as
independently verified findings.

## Review and maintenance

Reviewed **2026-09-19** at
[`cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a`](https://github.com/ChetasLua/jevmeter/tree/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a).
Inspected README, license, package metadata, installer, CLI, key handling, transcription,
scoring, timeline planning, debate preset and evaluation runner/report. No conventional
unit-test suite was found in the inspected tree. No installation, transcription,
rendering, evaluation or live request was run; the published demo and metrics are upstream reports.
