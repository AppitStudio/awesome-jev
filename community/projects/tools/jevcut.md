# jevcut

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Auto-clipper: code enumerates cut edges; TypeSafe Jev judges standalone clips for Shorts/Reels/TikTok (benchmarked on 38 videos).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VBS2004/jevcut) |
| Maintainer | [VBS2004](https://github.com/VBS2004). Independently curated. |
| Format | Python CLI auto-clipper for verbal long-form video. |
| Requirements | Python/uv; transcription provider; TypeSafe API key for Jev judgments; ffmpeg per upstream. |
| License | [MIT](https://github.com/VBS2004/jevcut/blob/562c0cbbd3907b2bc6fc8ed5d1644517e80b211c/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use for **podcast/talk/comedy** highlight clips where boundaries matter. Not for silent/visual-only moments (v1 transcript judge).

## How it works

Transcribes, enumerates candidate start/end edges in code, asks Jev only about clips those edges would make, filters ads/non-standalone segments, writes ranked mp4s.

## Get started

```sh
git clone https://github.com/VBS2004/jevcut.git
cd jevcut
git checkout 562c0cbbd3907b2bc6fc8ed5d1644517e80b211c
# uv run jevcut run talk.mp4 --model …; needs transcription + TypeSafe key
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 562c0cb](https://github.com/VBS2004/jevcut/tree/562c0cbbd3907b2bc6fc8ed5d1644517e80b211c). AI-assisted README and license inspection; install/live paths not executed.
