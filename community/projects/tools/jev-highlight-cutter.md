# Jev Highlight Cutter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex agent skill and stdlib Python CLI (Chinese docs) that cuts long interviews, podcasts and streams into an evidence-backed highlight reel of a target length: transcript windows are scored by Jev against your preferences, selections are traceable, and FFmpeg makes a local rough cut.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gnipbao/jev-highlight-cutter) |
| Maintainer | [gnipbao](https://github.com/gnipbao). Independently curated. |
| Format | Agent skill (`SKILL.md`) + Python CLI `scripts/highlight.py` (no pip install) |
| Requirements | Python 3.10+, FFmpeg/ffprobe, Git; `TYPESAFE_API_KEY` for scoring; subtitles (SRT/VTT/Whisper JSON) or optional local transcription. |
| License | [MIT](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Cut long talk-format video to a time budget while keeping original audio and timestamps.
- Inspect the exact text requests before sending (`transfer-preview.json`) and re-score after preference changes.
- Mismatch: outputs a rough cut only — no subtitles, dubbing, music or editor project export.

## How it works

[`scripts/highlight.py`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/scripts/highlight.py) indexes the transcript, builds candidate windows and prepares requests; [`scripts/jev.py`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/scripts/jev.py) scores information value, hook, completeness, emotion and taste fit with caching and retries; [`scripts/planner.py`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/scripts/planner.py) picks non-overlapping segments within budget and [`scripts/media.py`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/scripts/media.py) renders clips and the reel with FFmpeg. Rubrics live in [`references/rubrics.md`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/references/rubrics.md).

## Get started

Manual CLI flow (from the README):

```sh
SKILL="$HOME/.codex/skills/jev-highlight-cutter"   # or a clone of gnipbao/jev-highlight-cutter
RUN="$HOME/jev-runs/interview-001"
python3 "$SKILL/scripts/highlight.py" doctor
python3 "$SKILL/scripts/highlight.py" init --run "$RUN" --genre interview --target 8m --duration-mode target
python3 "$SKILL/scripts/highlight.py" index --run "$RUN" --video /data/interview.mp4 --transcript /data/interview.srt
python3 "$SKILL/scripts/highlight.py" score --run "$RUN" --prepare   # review transfer-preview.json before sending
```

Scoring requests are billed to your TypeSafe key; video processing stays local.

## Examples and demos

- Jev API setup, privacy and cost notes: [`docs/jev-api.md`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/docs/jev-api.md).
- Full command reference: [`references/commands.md`](https://github.com/gnipbao/jev-highlight-cutter/blob/b7b84fc588ec75af8888035376ec48f9f4b79941/references/commands.md).

## Limits and data handling

Only transcript text is sent to TypeSafe; video stays local (upstream). Docs are in Chinese. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b7b84fc588ec](https://github.com/gnipbao/jev-highlight-cutter/tree/b7b84fc588ec75af8888035376ec48f9f4b79941). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
