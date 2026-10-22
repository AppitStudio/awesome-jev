# Jev Talking Head Workflow (talking-head video production skills)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Reusable workflow of agent skills for Chinese talking-head videos, from script to rough cut, B-roll, subtitles, mixing and QA, where Jev is the structured review layer comparing takes, flagging fragments and repetition and suggesting layouts, while humans confirm every edit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow) |
| Maintainer | [HaoyuJiangdasak](https://github.com/HaoyuJiangdasak). Independently curated. |
| Format | Agent skills for Codex and Claude Code (Python scripts) |
| Requirements | Codex or Claude Code; Whisper and the video tools named in the skills; a TypeSafe or OpenRouter key for Jev review. |
| License | [MIT](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow/blob/e71b17d7407aa983e68fbaad44d82c5b81564a6c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jev-video-review/scripts/jev_video_review.py`](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow/blob/e71b17d7407aa983e68fbaad44d82c5b81564a6c/skills/jev-video-review/scripts/jev_video_review.py) at the pinned commit. |

## When to use

- Compare several recorded takes and pick the cleanest one with probabilities.
- Get a second opinion on openings and repetition before rendering.
- Mismatch: docs are in Chinese; Jev never edits the timeline itself.

## How it works

`skills/jev-video-review/scripts/jev_video_review.py` runs take, motion and script reviews against TypeSafe (`jev-1.14.0`) or OpenRouter (`typesafe/jev-1.14`); low-confidence results go back to a human for listening, frame checks or QA. Integration evidence: [`skills/jev-video-review/scripts/jev_video_review.py`](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow/blob/e71b17d7407aa983e68fbaad44d82c5b81564a6c/skills/jev-video-review/scripts/jev_video_review.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/HaoyuJiangdasak/jev-talking-head-workflow.git
# copy the skills/ folders into your Codex or Claude Code skills directory per the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skills overview in the README: [github.com/HaoyuJiangdasak/jev-talking-head-workflow#readme](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow#readme)

## Limits and data handling

Transcript and script text are sent to TypeSafe or OpenRouter for review. Some ChatCut-internal skills are not included for licensing reasons, per the README.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit e71b17d7407a](https://github.com/HaoyuJiangdasak/jev-talking-head-workflow/tree/e71b17d7407aa983e68fbaad44d82c5b81564a6c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
