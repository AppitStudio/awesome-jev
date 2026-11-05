# YapCut (local talking-head video editor that cuts, titles, zooms, captions and grades a take, with an optional Jev frame check)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac app and Claude Code plugin that turns a raw talking-head video into cut, titled, zoomed and captioned vertical Reel versions, each graded with a list of failed checks. The edit runs on your Mac with the Claude Code or Codex CLI you already use. An optional TypeSafe frame check sends frames at 2 fps to Jev with yes/no questions and face and problem boxes (text over the face, cut-off text, broken frames), grouped into issues with a fix each.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royherma/yapcut) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://tools.techguyverlabs.org/t/yapcut) |
| Pricing and access | Free source build (MIT). It uses the Claude Code or Codex plan you already have; the optional TypeSafe frame check is billed to your own key (about $0.042 per million input tokens per the source). Checked 2026-11-05. |
| Jev evidence | [`lib/jev.mjs`](https://github.com/royherma/yapcut/blob/e70f586fff2064d5365a9160b9a9f61218cacb80/lib/jev.mjs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [royherma](https://github.com/royherma). Independently curated. |
| Format | Local web studio and CLI (Node.js, Python and ffmpeg; MIT) plus Claude Code plugin |
| Platform and availability | macOS on Apple silicon (local web studio at localhost:4901; Claude Code plugin) |
| Jev's role | Optional frame check that answers yes/no questions and returns face and problem boxes for each frame of an edited video, so layout issues become fixable checks. |
| Requirements | Mac with Apple silicon, Homebrew (`node`, `uv`, `ffmpeg@7`), Google Chrome, and Claude Code or Codex; `TYPESAFE_API_KEY` only for the optional frame check. |
| License | [MIT](https://github.com/royherma/yapcut/blob/e70f586fff2064d5365a9160b9a9f61218cacb80/LICENSE) |

## When to use

- Check an edited Reel for captions over the speaker's face, cut-off text and broken frames with a pixel-aware decision model.
- Edit a talking-head take locally with versions from Clean to Heavy and an Improve this loop that keeps only changes that raise the grade.
- Mismatch: Jev is an optional paid add-on that is off unless you set a key; the README says nothing leaves your Mac except your AI CLI's prompts unless you set it.

## How it works

`lib/jev.mjs` posts each frame to `https://api.typesafe.ai/v1/systemone` with model `jev-1.14.0`, noul questions per issue kind plus `box` questions for the face and the worst overlay, caches answers by frame hash so re-checks only pay for changed frames, and tracks token cost at $0.042 per million. Integration evidence: [`lib/jev.mjs`](https://github.com/royherma/yapcut/blob/e70f586fff2064d5365a9160b9a9f61218cacb80/lib/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
brew install node uv ffmpeg@7
git clone https://github.com/royherma/yapcut.git && cd yapcut
scripts/install.sh
yapcut preview   # then open http://localhost:4901
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (features, grading, install, add-ons): [github.com/royherma/yapcut/blob/e70f586fff2064d5365a9160b9a9f61218cacb80/README.md](https://github.com/royherma/yapcut/blob/e70f586fff2064d5365a9160b9a9f61218cacb80/README.md)
- Tool page: [tools.techguyverlabs.org/t/yapcut](https://tools.techguyverlabs.org/t/yapcut)

## Limits and data handling

With TYPESAFE_API_KEY set, video frames go to TypeSafe on your key; image input is experimental at TypeSafe. The first take downloads several GB of speech and word-timing models. The repository was created on 2026-11-05.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit e70f586fff20](https://github.com/royherma/yapcut/tree/e70f586fff2064d5365a9160b9a9f61218cacb80). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
