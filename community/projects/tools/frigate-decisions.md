# Frigate Decisions (asks Frigate camera frames yes/no questions with Jev and turns the answers into Frigate alerts and detections)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Docker service that runs next to Frigate NVR: while a camera sees movement it asks Jev plain-language yes/no questions about the latest frame (for example "Is a dog lying on the sofa?"), and when an answer stays above a threshold for a set time it creates a Frigate event with its recording. It asks nothing when nothing moves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nat-e/frigate-decisions) |
| Maintainer | [nat-e](https://github.com/nat-e). Independently curated. |
| Format | Python service in a Docker image (MIT, uses the `typesafe-sdk` package) |
| Requirements | A running Frigate instance on the same Docker network (it uses Frigate's internal API on port 5000), a `TYPESAFE_API_KEY` and a `frigate-decisions.yml` rules file. |
| License | [MIT](https://github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/frigate_decisions/providers.py`](https://github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/src/frigate_decisions/providers.py) at the pinned commit. |

## When to use

- Detect things Frigate's fixed object list cannot, such as a dog on the sofa, an open garage door or a parcel on the doorstep.
- Keep costs low by asking only while a camera sees motion.
- Mismatch: image input is still experimental at TypeSafe, and the provider interface is Jev-only in this snapshot.

## How it works

`providers.py` wraps `typesafe_sdk.TypeSafeClient` and sends the downscaled camera frame (280 to 1568 px per side) with `Noul` questions and the experimental image header; the watcher checks motion locally, asks every few seconds while something moves and creates or ends Frigate events from `threshold`, `min_duration` and `end_after`. Integration evidence: [`src/frigate_decisions/providers.py`](https://github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/src/frigate_decisions/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
# docker-compose.yml, next to your frigate service
services:
  frigate-decisions:
    build: https://github.com/nat-e/frigate-decisions.git
    environment:
      TYPESAFE_API_KEY: ${TYPESAFE_API_KEY}
    volumes:
      - ./frigate-decisions.yml:/config/config.yml:ro
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (setup, configuration, writing good questions, limits): [github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/README.md](https://github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/README.md)
- Example config: [github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/examples/config.yml](https://github.com/nat-e/frigate-decisions/blob/3d6bfd008a7473cc2b9c8081a604d9fa412c4253/examples/config.yml)

## Limits and data handling

Camera frames from the cameras you configure are sent to TypeSafe on your key; the README estimates a couple of thousand input tokens per frame with a few questions. Frigate cannot create events in the past, events created through its API are not published on its MQTT topic, and probabilities can produce false events, so tune `threshold` and `min_duration`.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 3d6bfd008a74](https://github.com/nat-e/frigate-decisions/tree/3d6bfd008a7473cc2b9c8081a604d9fa412c4253). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
