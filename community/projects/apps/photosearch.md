# photosearch by Mumit Khan (search your Apple Photos library by description on your Mac, with optional Jev smart-search filters)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local search for your Apple Photos library: describe a picture, find look-alikes, browse a map or a galaxy of the library, and tidy duplicates into albums, all with an open embedding model on your Mac. With a TypeSafe key, Jev reads the smart search box into filters (photo or video, season, dates, no people) and checks the first results from text descriptions; without one, keyword rules do the same job.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mumit/photosearch) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/mumit/photosearch#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source and PyPI package (0.3.0). Jev features are optional and use your own TypeSafe key; search itself runs locally with no key. Checked 2026-11-27. |
| Jev evidence | [`src/photosearch/smartbox.py`](https://github.com/mumit/photosearch/blob/f1f32f134b3d6f12480de81a2830dc6977e46665/src/photosearch/smartbox.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/MumitKhan/status/2126010038011707616)). |
| Maintainer | [Mumit Khan](https://github.com/mumit) (mumit). Independently curated. |
| Format | Python package (PyPI) with local web UI and MCP server |
| Platform and availability | macOS (Apple Silicon recommended), installed as a Python tool with uv; web UI on localhost and an MCP server for agents. |
| Jev's role | Optional. `smartbox.py` asks Jev typed `choice` and `noul` questions to turn your words into filters, and `checks.py` asks which of the first 40 results fit, using text descriptions only; photos, names and places are never sent. With no key or no answer, local keyword rules take over. |
| Requirements | A Mac with the Photos app, about 3 GB of disk for software and the model, uv; optional ffmpeg for video, optional TypeSafe key for the Jev steps. |
| License | [MIT](https://github.com/mumit/photosearch/blob/f1f32f134b3d6f12480de81a2830dc6977e46665/LICENSE) |

## When to use

- Mac users who want private, local search over a large Apple Photos library, including iCloud libraries with Optimize Mac Storage.
- Mismatch: a Jev showcase; Jev is an optional helper, and the author's own tests found keyword rules nearly as accurate (196 vs 198 of 200).

## How it works

`smartbox.py` posts the search text (names replaced by "someone") to `https://api.typesafe.ai/v1/systemone` with five typed questions and applies the author's cut-offs; `checks.py` sends word descriptions of the first results and reorders them by Jev's answers. Embedding search uses Google's open EmbeddingGemma 2 on the Mac. Integration evidence: [`src/photosearch/smartbox.py`](https://github.com/mumit/photosearch/blob/f1f32f134b3d6f12480de81a2830dc6977e46665/src/photosearch/smartbox.py).

## Get started

Install uv, then the package, and index your library; add a TypeSafe key in `.env` only if you want the Jev steps.

```sh
brew install uv
uv tool install photosearch
photosearch index      # index the Photos library
photosearch serve      # local web UI
# optional: TYPESAFE_API_KEY=... in the photosearch .env for Jev smart search
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Findings and experiment notes: [github.com/mumit/photosearch/blob/main/FINDINGS.md](https://github.com/mumit/photosearch/blob/main/FINDINGS.md)
- PyPI: [pypi.org/project/photosearch/](https://pypi.org/project/photosearch/)

## Limits and data handling

A learning project, not a product, per the author. Photos stay on the Mac; with a key, the search words and text descriptions of the first results go to TypeSafe. Accuracy figures are the author's own, in FINDINGS.md. Album changes are written to the Photos app only when you ask.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit f1f32f134b3d](https://github.com/mumit/photosearch/tree/f1f32f134b3d6f12480de81a2830dc6977e46665). Inspected the README, LICENSE, FINDINGS.md pointers, `src/photosearch/smartbox.py` and `src/photosearch/checks.py` at the pinned commit; PyPI package 0.3.0 confirmed. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
