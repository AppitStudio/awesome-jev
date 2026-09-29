# Capture (sgaabdu4)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Private Mac voice diary: local Parakeet transcription, TypeSafe Jev sorting into typed buckets, then Notion library after you approve

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sgaabdu4/capture) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/sgaabdu4/capture#readme) |
| Pricing and access | Free source build; no app purchase fee. TypeSafe key for Jev sorting; Notion OAuth for library. Checked 2026-09-29. |
| Jev evidence | [Upstream README](https://github.com/sgaabdu4/capture/blob/c41d779147968e26fdc5423f717298dd006675db/README.md): speech stays local; Jev splits utterances into notes/tasks/reminders; titles/bodies come from your words. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. macOS build/live Jev not run on the Linux review host. |
| Maintainer | [sgaabdu4](https://github.com/sgaabdu4). Independently curated. |
| Format | Dart/Flutter · macOS (and iPhone transcription path) app (MIT). |
| Platform and availability | macOS source build; shortcut to record → review → Notion. |
| Jev's role | Jev sorts transcribed speech into typed groups; you approve before Notion/reminders. Audio is not sent to AI services. |
| Requirements | macOS; TypeSafe API key; Notion; local Parakeet transcription per upstream docs. |
| License | [MIT](https://github.com/sgaabdu4/capture/blob/c41d779147968e26fdc5423f717298dd006675db/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when you want a private voice inbox that classifies thoughts without rewriting them.

## How it works

`⌃⌥` to speak → local transcription → Jev sorting → review → Notion + Mac reminders. Auto-save is optional.

## Get started

```sh
git clone https://github.com/sgaabdu4/capture.git
cd capture
git checkout c41d779147968e26fdc5423f717298dd006675db
# follow upstream README for Flutter/macOS build and Notion/TypeSafe setup
```

## Examples and demos

Upstream README screenshots and attached demo video. No live capture was run on the review host.

## Limits and data handling

Audio stays on-device for transcription; Jev receives text for sorting; Notion receives only approved items. Live paths not executed on the review host.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit c41d779](https://github.com/sgaabdu4/capture/tree/c41d779147968e26fdc5423f717298dd006675db). AI-assisted README + LICENSE inspection; macOS build/live paths not executed.
