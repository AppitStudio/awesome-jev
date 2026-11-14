# StreetWalker (street survey that labels every building in three Philadelphia areas with Jev, escalating only low-confidence cases)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Deterministic survey of three Philadelphia areas: each building is classified (residential, commercial, restaurant, cafe and so on) with Jev decisions over OpenStreetMap tags and geometry, a confidence gate picks which to escalate to street imagery and a local vision model, and a human queue takes the rest. The author reports Tier 0 (Jev plus a calibrated stacker) labels 88% of buildings correctly and that the imagery and local-LLM tiers did not help. Includes a map replay viewer and decision records.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pranavrd/resto-jev) |
| Maintainer | [pranavrd](https://github.com/pranavrd). Independently curated. |
| Format | Python package with Postgres/PostGIS, a web replay viewer and decision records (no license file) |
| Requirements | Python, Docker for Postgres + PostGIS + pgvector, a Mapillary token for imagery, and a TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/streetwalker/jev_client.py`](https://github.com/pranavrd/resto-jev/blob/ca43cf44571fb61d7512a5d00c4b537f3edee6e5/src/streetwalker/jev_client.py) at the pinned commit. |

## When to use

- Label many map features cheaply while sending only uncertain cases to costlier tiers or people.
- Mismatch: the Yelp ranking half, which the author keeps private pending a data-license question.

## How it works

`src/streetwalker/jev_client.py` uses the TypeSafe SDK (`TypeSafeClient`) with `MODEL_VERSION = "jev-1.13.0"` from `jev_questions.py` (pinned, never `jev-latest` in pipelines) and records input/output tokens, latency and the returned model id per decision. Integration evidence: [`src/streetwalker/jev_client.py`](https://github.com/pranavrd/resto-jev/blob/ca43cf44571fb61d7512a5d00c4b537f3edee6e5/src/streetwalker/jev_client.py).

## Get started

Start the database, install the package and ingest the public data.

```sh
git clone https://github.com/pranavrd/resto-jev && cd resto-jev
cp .env.example .env && docker compose up -d db
python3 -m venv .venv && .venv/bin/pip install -e .
.venv/bin/python -m streetwalker.ingest all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/pranavrd/resto-jev/blob/ca43cf44571fb61d7512a5d00c4b537f3edee6e5/README.md](https://github.com/pranavrd/resto-jev/blob/ca43cf44571fb61d7512a5d00c4b537f3edee6e5/README.md)

## Limits and data handling

OSM tags and geometry go to TypeSafe on your key; raw data stays in `data/` and is never committed. Yelp-derived work is private and not part of the public repo.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit ca43cf44571f](https://github.com/pranavrd/resto-jev/tree/ca43cf44571fb61d7512a5d00c4b537f3edee6e5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
