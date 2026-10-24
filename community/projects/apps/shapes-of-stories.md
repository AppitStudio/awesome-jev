# Shapes of Stories (story arcs of books and scripts scored with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Charts the shape of a novel, screenplay or transcript: Jev scores every passage of about 800 words on ten qualities such as fortune and tension plus events, and the fortune curve is matched to named arcs like Rags to Riches or Man in a Hole.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ferrum-Citadel/shapes-of-stories) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/Ferrum-Citadel/shapes-of-stories#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. The bundled gallery of fifty public-domain works needs no key; your own texts use your TypeSafe key. Checked 2026-10-24. |
| Jev evidence | [`backend/app/core/jev/client.py`](https://github.com/Ferrum-Citadel/shapes-of-stories/blob/fd0d3573a5524f63232a04bbe27b63f54412b5d5/backend/app/core/jev/client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Ferrum-Citadel](https://github.com/Ferrum-Citadel). Independently curated. |
| Format | Self-hosted web app (FastAPI and frontend, Docker) |
| Platform and availability | Self-hosted via Docker Compose. |
| Jev's role | Core: twenty typed questions per passage (ten 0-4 scales, nine yes/no events, one choice) produce the curves. |
| Requirements | Docker; your own TypeSafe API key for new texts. |
| License | [MIT](https://github.com/Ferrum-Citadel/shapes-of-stories/blob/fd0d3573a5524f63232a04bbe27b63f54412b5d5/LICENSE) |

## When to use

- See the emotional arc of a book or screenplay and click into any passage.
- Compare two works side by side.
- Mismatch: scores are calibrated against model labels, not human readers.

## How it works

`backend/app/core/jev/client.py` calls `https://api.typesafe.ai` for each passage; scores are smoothed on a 100-point timeline and matched against six arc templates. Integration evidence: [`backend/app/core/jev/client.py`](https://github.com/Ferrum-Citadel/shapes-of-stories/blob/fd0d3573a5524f63232a04bbe27b63f54412b5d5/backend/app/core/jev/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # SERVER_SECRET, JEV_MODE=live
docker compose up
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with method and calibration notes: [github.com/Ferrum-Citadel/shapes-of-stories#readme](https://github.com/Ferrum-Citadel/shapes-of-stories#readme)

## Limits and data handling

Uploaded text is sent to TypeSafe passage by passage. The author documents calibration limits in the README.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit fd0d3573a552](https://github.com/Ferrum-Citadel/shapes-of-stories/tree/fd0d3573a5524f63232a04bbe27b63f54412b5d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
