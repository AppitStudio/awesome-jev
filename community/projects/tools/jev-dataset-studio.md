# Jev Dataset Studio by Unjuno (self-hosted no-code web app that labels text data with Jev and exports training datasets)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Import CSV or JSONL, configure in forms where to annotate, which features to add and how to lay out rows, and Jev adds classifications, multi-labels, condition checks and importance scores. Keeps source positions, the context used, the model and review history, and exports per-use-case layouts. A deterministic demo judge with fictional Japanese samples works without a key. Japanese UI and docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Unjuno/jev-dataset-studio) |
| Maintainer | [Unjuno](https://github.com/Unjuno). Independently curated. |
| Format | Self-hosted Python web app (Docker Compose with PostgreSQL, or Python 3.12 with SQLite) |
| Requirements | Docker Compose 2.24+ (or Python 3.12) and a TypeSafe API key for real Jev labels. |
| License | [MIT](https://github.com/Unjuno/jev-dataset-studio/blob/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`studio/providers.py`](https://github.com/Unjuno/jev-dataset-studio/blob/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0/studio/providers.py) at the pinned commit. |

## When to use

- Build labelled training data from existing text with Jev, keeping provenance and human review.
- Mismatch: non-Japanese teams who need an English UI (the docs are Japanese).

## How it works

`studio/providers.py` sends labelling questions to `https://api.typesafe.ai/v1/systemone`; the key stays server-side and is never written into exports. Every label starts as needs-review. Integration evidence: [`studio/providers.py`](https://github.com/Unjuno/jev-dataset-studio/blob/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0/studio/providers.py).

## Get started

Start with Docker Compose, try the demo judge, then add `TYPESAFE_API_KEY` to `.env`.

```sh
git clone https://github.com/Unjuno/jev-dataset-studio.git && cd jev-dataset-studio
docker compose up --build -d   # http://localhost:8000
cp .env.example .env   # set TYPESAFE_API_KEY, then docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/Unjuno/jev-dataset-studio/blob/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0/README.md](https://github.com/Unjuno/jev-dataset-studio/blob/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0/README.md)

## Limits and data handling

Imported text is sent to TypeSafe for each labelling run. `docker compose down -v` deletes the data volume.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit a0ae48368e88](https://github.com/Unjuno/jev-dataset-studio/tree/a0ae48368e88ef37f8f0afaef0e06c7e9cb2d2d0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
