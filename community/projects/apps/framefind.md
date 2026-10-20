# FrameFind

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local Python web app that samples frames from an uploaded clip or public video URL, asks Jev image questions to find moments matching a plain-language description, and lets you play or export the matching snippets as MP4.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lyadalachanchu/framefind) |
| Tags | `Open source` · `Free` |
| Product homepage | [Repository README](https://github.com/Lyadalachanchu/framefind#readme) (source-built; no separate product site verified). |
| Pricing and access | Free MIT source; you pay TypeSafe per image call, with a local spending guard (`JEV_BUDGET_USD`, default $15). Checked 2026-10-21. |
| Jev evidence | [`app/jev.py`](https://github.com/Lyadalachanchu/framefind/blob/9458ac342e6b254ffc4df3d9b1a15623c9f545d0/app/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Lyadalachanchu](https://github.com/Lyadalachanchu). Independently curated. |
| Format | Local web app (Python, FFmpeg) |
| Platform and availability | Runs locally on macOS or Linux at `http://127.0.0.1:8765`; Windows through WSL2 only. |
| Jev's role | Core: Jev judges sampled video frames against your description and the matches become playable snippets. |
| Requirements | Python 3.11+, FFmpeg/ffprobe, a TypeSafe API key; Node.js 22+ recommended for YouTube imports. macOS or Linux (Windows via WSL2). |
| License | [MIT](https://github.com/Lyadalachanchu/framefind/blob/9458ac342e6b254ffc4df3d9b1a15623c9f545d0/LICENSE) |

## When to use

- Find a scene in a long video by describing it instead of scrubbing.
- Cut and export a short clip around a moment.
- Mismatch: frames go to TypeSafe for analysis; files up to 2 GB and 60 minutes.

## How it works

FFmpeg samples frames from the video; `app/jev.py` sends them with your description to `https://api.typesafe.ai/v1/systemone`, and frames above the confidence cutoff are grouped into snippets you can play, loop or export. Matches are cached per model. Integration evidence: [`app/jev.py`](https://github.com/Lyadalachanchu/framefind/blob/9458ac342e6b254ffc4df3d9b1a15623c9f545d0/app/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Lyadalachanchu/framefind.git && cd framefind
python3 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt
python start.py   # enter your key, open http://127.0.0.1:8765
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo GIF and MP4 in the README: [github.com/Lyadalachanchu/framefind#readme](https://github.com/Lyadalachanchu/framefind#readme)
- Architecture notes: [github.com/Lyadalachanchu/framefind/blob/main/docs/architecture.md](https://github.com/Lyadalachanchu/framefind/blob/main/docs/architecture.md)

## Limits and data handling

Video frames are sent to TypeSafe for image analysis. The key is entered at a hidden prompt and is not saved to disk, per the README.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 9458ac342e6b](https://github.com/Lyadalachanchu/framefind/tree/9458ac342e6b254ffc4df3d9b1a15623c9f545d0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
