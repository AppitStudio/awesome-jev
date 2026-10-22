# 快学 CoursePilot (course video workbench with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first desktop workbench for online course videos (Chinese UI) that produces subtitles, notes, mind maps, slide OCR, quizzes and spaced review; this fork adds Jev judgments on the transcript, which the author uses to speed up filler and slow down key parts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/litany-lty/CoursePilot) |
| Maintainer | [litany-lty](https://github.com/litany-lty). Independently curated. |
| Format | Desktop app (Tauri, Rust and React) |
| Requirements | Build from source per the README; a Jev API key saved in the app's settings for the Jev features. |
| License | [MIT](https://github.com/litany-lty/CoursePilot/blob/c82efcb671d1f22718de8ca91b1bf52425488a58/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/elidlicom/status/2113121463721181432)). |
| Jev evidence | [`course-ai/src-tauri/src/llm/jev.rs`](https://github.com/litany-lty/CoursePilot/blob/c82efcb671d1f22718de8ca91b1bf52425488a58/course-ai/src-tauri/src/llm/jev.rs) at the pinned commit. |

## When to use

- Study long course recordings with notes, quizzes and review in one place.
- Let Jev mark which transcript parts matter so playback can adapt.
- Mismatch: a derivative of wansui976/CoursePilot; docs are mainly in Chinese.

## How it works

`course-ai/src-tauri/src/llm/jev.rs` sends transcript segments to `POST {base}/v1/systemone` (`jev-latest` by default) for structured judgments without generating text; the key is stored in the app's own database. Integration evidence: [`course-ai/src-tauri/src/llm/jev.rs`](https://github.com/litany-lty/CoursePilot/blob/c82efcb671d1f22718de8ca91b1bf52425488a58/course-ai/src-tauri/src/llm/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/litany-lty/CoursePilot.git
# follow the build steps in the README (Tauri desktop app)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/litany-lty/CoursePilot/blob/main/README_en.md](https://github.com/litany-lty/CoursePilot/blob/main/README_en.md)
- Upstream project: [github.com/wansui976/CoursePilot](https://github.com/wansui976/CoursePilot)

## Limits and data handling

Transcript text is sent to TypeSafe when Jev is configured; other AI features use the providers you set. Fork of an MIT project with attribution in NOTICE.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit c82efcb671d1](https://github.com/litany-lty/CoursePilot/tree/c82efcb671d1f22718de8ca91b1bf52425488a58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
