# GraphPaper by Aron Bijl (local-first Windows writing studio with source graphs and an optional Jev decision studio)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Writing studio for nonfiction, fiction, polemic and scientific manuscripts: upload sources, explore them as a knowledge graph, pick an angle, outline and draft in a saved author voice, then review and export to PDF or Word with citations. An optional Jev connection guides source selection, graph exploration, edit checks and research triage, shows its questions and distributions, and lets you save corrections and train a local preference ranker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AronAxe/GraphPaper) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/AronAxe/GraphPaper#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download (Windows x64 ZIP on GitHub Releases) and MIT source; writing needs your own ChatGPT/Codex sign-in or provider keys, and Jev an OpenRouter or TypeSafe key. Checked 2026-11-28. |
| Jev evidence | [`graphpaper/system_one.py`](https://github.com/AronAxe/GraphPaper/blob/37b4a568c4326ca610e4a434408fd6f61bb8fcbf/graphpaper/system_one.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Aron Bijl](https://github.com/AronAxe). Independently curated. |
| Format | Windows desktop app + Python source |
| Platform and availability | Windows x64 desktop app (release ZIP, needs Edge WebView2); Python 3.11+ source edition. |
| Jev's role | Optional: Jev answers typed questions for source selection, graph candidates, evidence gaps, intent repair and edit checks; GraphPaper shows each distribution and the action taken. |
| Requirements | Windows x64 with WebView2 (or Python 3.11+); a writing model connection; an OpenRouter or TypeSafe key for Jev. |
| License | [MIT](https://github.com/AronAxe/GraphPaper/blob/37b4a568c4326ca610e4a434408fd6f61bb8fcbf/LICENSE) |

## When to use

- Writers who want sources, graph and draft in one local app with inspectable decision support.
- Mismatch: macOS or Linux desktop users; the packaged build is Windows-only.

## How it works

`graphpaper/system_one.py` builds the Jev requests (`jev-latest` by default) and sends them to `https://api.typesafe.ai/v1/systemone` or OpenRouter's decisions endpoint (`~typesafe/jev-latest`); `graphpaper/jev_budget.py` caps request size and spend. Integration evidence: [`graphpaper/system_one.py`](https://github.com/AronAxe/GraphPaper/blob/37b4a568c4326ca610e4a434408fd6f61bb8fcbf/graphpaper/system_one.py).

## Get started

Download the Windows ZIP from Releases, extract the whole folder and run `GraphPaper.exe`, or run the source edition.

```sh
# Windows build: download GraphPaper-v0.8.1-Windows-x64.zip from GitHub Releases,
# extract the complete folder and run GraphPaper.exe
# Source edition (Python 3.11+ with Tcl/Tk):
git clone https://github.com/AronAxe/GraphPaper
# then double-click "Open GraphPaper.vbs" (first run installs dependencies)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/AronAxe/GraphPaper/releases/latest](https://github.com/AronAxe/GraphPaper/releases/latest)
- System One docs: [github.com/AronAxe/GraphPaper/blob/main/docs/SYSTEM-ONE.md](https://github.com/AronAxe/GraphPaper/blob/main/docs/SYSTEM-ONE.md)

## Limits and data handling

Cloud generation sends project material to the providers you authorize, and Jev requests go to OpenRouter or TypeSafe. The release binary was not downloaded or run on the review host.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 37b4a568c432](https://github.com/AronAxe/GraphPaper/tree/37b4a568c4326ca610e4a434408fd6f61bb8fcbf). Inspected the README, LICENSE, Getting started guide, `graphpaper/system_one.py` and `graphpaper/jev_budget.py` at the pinned commit and confirmed the v0.8.1 release assets; nothing was downloaded or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
