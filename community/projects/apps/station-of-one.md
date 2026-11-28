# Station of One by Tarik Moody (hourly synthetic-voice newscast where Jev decides which stories air)

[All projects](../README.md) · [Web apps](README.md#web-apps)

ONE 1.0 FM, a fictional radio station with one listener, run by an agent on a Fly.io Sprite for Hacksgiving 2026. Every hour from 7 am to 7 pm Central it scrapes about 1,300 public posts from Hacker News, Reddit, RSS, Bluesky and Google News, merges duplicates, has Jev answer five typed questions per post (will it matter in a week? new or reaction? which part of the show? primary source? could it harm a private person?), and publishes a five-minute newscast with story pages, a control room showing every Jev decision, a daily debate show and music stations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tmoody1973/station-of-one) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://patient-mountain-3400.fly.storage.tigris.dev/index.html) |
| Pricing and access | Free to listen on the public site and podcast feed; self-hosting needs a Fly.io Sprite and paid connectors (Apify, TypeSafe, Pinecone, voices, Box). Checked 2026-11-28. |
| Jev evidence | [`station/steps/judge.py`](https://github.com/tmoody1973/station-of-one/blob/ece741d85e14f310bfa471a3cd6978b2ca0c0fbb/station/steps/judge.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Tarik Moody](https://github.com/tmoody1973). Independently curated. |
| Format | Python agent + static site |
| Platform and availability | Public website and podcast feed; the agent runs on a Fly.io Sprite (Python). |
| Jev's role | Jev answers five questions per post plus a "same story?" merge question; code reads only the probabilities to build the rundown, and every answer is logged and shown in the control room. |
| Requirements | To self-host: a Fly.io Sprite with the Apify, TypeSafe, Pinecone, voice and Box connectors. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- People curious how a decision model can act as a newsroom editor, with every call visible.
- Mismatch: a reliable news source; voices are synthetic and the show is machine-edited.

## How it works

`station/steps/judge.py` sends every post to Jev (`jev-latest`) with the per-post questions through the Sprites connector gateway and records each decision; later steps write scripts and audio from the posts Jev ranks highest. Integration evidence: [`station/steps/judge.py`](https://github.com/tmoody1973/station-of-one/blob/ece741d85e14f310bfa471a3cd6978b2ca0c0fbb/station/steps/judge.py).

## Get started

Listen on the public site, or run single steps by hand on a Sprite with the connectors attached.

```sh
git clone https://github.com/tmoody1973/station-of-one && cd station-of-one
uv sync && uv run pytest -q
uv run python -m station judge --run data/runs/2026-11-27T09
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Control room: [patient-mountain-3400.fly.storage.tigris.dev/control-room/index.html](https://patient-mountain-3400.fly.storage.tigris.dev/control-room/index.html)
- Podcast feed: [patient-mountain-3400.fly.storage.tigris.dev/feed.xml](https://patient-mountain-3400.fly.storage.tigris.dev/feed.xml)

## Limits and data handling

Public posts are scraped and sent to TypeSafe and other connectors. The station is fictional and machine-edited. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit ece741d85e14](https://github.com/tmoody1973/station-of-one/tree/ece741d85e14f310bfa471a3cd6978b2ca0c0fbb). Inspected the README and `station/steps/judge.py` at the pinned commit and confirmed the public front page loads (HTTP 200); no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
