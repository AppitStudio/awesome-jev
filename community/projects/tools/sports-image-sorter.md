# sports-image-sorter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI and review UI that sorts sports photos into per-sport folders with local vision engines and conservative fusion, with an optional Jev cloud engine for image Choice questions behind explicit off-device gates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nematatu/sports-image-sorter-local) |
| Maintainer | [nematatu](https://github.com/nematatu). Independently curated. |
| Format | Python CLI with SQLite state and a local review UI |
| Requirements | Python 3.10+ and Pillow; the `local` extra (PyTorch, Transformers) for neural engines; macOS for Apple Vision; for Jev, the cloud gates, `TYPESAFE_DANGER_ZONE_IMAGES=1` and a TypeSafe key. |
| License | [MIT](https://github.com/nematatu/sports-image-sorter-local/blob/e43ede4326a16d876cbfa35d1bf2d7c1471909eb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sports_sorter/engines/external.py`](https://github.com/nematatu/sports-image-sorter-local/blob/e43ede4326a16d876cbfa35d1bf2d7c1471909eb/sports_sorter/engines/external.py) at the pinned commit. |

## When to use

- Sort a personal sports photo library without uploading images by default.
- Compare a Jev image Choice engine with local CLIP, SigLIP 2 and Apple Vision engines on your own photos.
- Mismatch: the Jev engine is implemented but the README's run table lists it as not run by the author.

## How it works

`scan` hashes images read-only, each enabled engine classifies them, and weighted fusion sends ambiguous images to an unsorted folder rather than forcing a sport. The Jev engine in `sports_sorter/engines/external.py` sends a resized JPEG to `https://api.typesafe.ai/v1/systemone` with the sport options as a Choice question, only after the cloud gates are opened. Exports are copy-only and verified by SHA-256. Integration evidence: [`sports_sorter/engines/external.py`](https://github.com/nematatu/sports-image-sorter-local/blob/e43ede4326a16d876cbfa35d1bf2d7c1471909eb/sports_sorter/engines/external.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/nematatu/sports-image-sorter-local.git && cd sports-image-sorter-local
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[local,dev]"
sports-sorter engines   # shows availability and off-device warnings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/engines.md (engine list and cloud gates)
- README quick start (English and Japanese)

## Limits and data handling

With the Jev engine enabled, downscaled photos leave the machine for TypeSafe. Jev image input needs TypeSafe's image access flag.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit e43ede4326a1](https://github.com/nematatu/sports-image-sorter-local/tree/e43ede4326a16d876cbfa35d1bf2d7c1471909eb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
