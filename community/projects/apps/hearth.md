# Hearth

[All projects](../README.md) · [Apps](README.md) · [Web apps](README.md#web-apps)

Local rental-search agent: drives Chrome across Craigslist, Facebook Marketplace, Redfin, and Zillow from one plain-language request, and returns a shortlist. TypeSafe Jev chooses browser actions; the app never messages sellers or starts transactions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [Project homepage](https://github.com/Nancy-Chauhan/hearth-jev-rental-search#readme) — source-run; no separate product website. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Needs a TypeSafe API key (`TYPESAFE_API_KEY`). Provider usage can incur charges. Live marketplace searches were not run on the review host. |
| Jev evidence | [`jev_ultrafast/model.py`](https://github.com/Nancy-Chauhan/hearth-jev-rental-search/blob/c9c2d5f4b28884aded9e61a054baad14748a2ad1/jev_ultrafast/model.py) posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest` via `TYPESAFE_MODEL`). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Package directory is named `jev_ultrafast` but this is **not** [browser-use/jev-ultrafast](../tools/jev-ultrafast.md)—it is a rental-search application built on a similar choose-not-generate loop. Offline `pytest`: **63 passed**. Live Chrome/marketplace runs not executed. |
| Maintainer | [Nancy-Chauhan](https://github.com/Nancy-Chauhan). Independently curated. |
| Format | Python app (`jev-ultrafast` 0.1.0 package name; console script `jev`) with local UI on port 8766. |
| Platform and availability | Local source-run with Google Chrome remote debugging. Experimental **0.1.0**. |
| Jev's role | Selects among code-built browser actions/targets for the rental search loop. Does not message sellers or complete transactions. |
| Requirements | Python ≥ 3.12, `uv`, Google Chrome with a dedicated profile on CDP port 9222, `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Nancy-Chauhan/hearth-jev-rental-search/blob/c9c2d5f4b28884aded9e61a054baad14748a2ad1/LICENSE). |

## When to use

Use it to watch a bounded multi-marketplace rental shortlist where Jev only chooses among observed page actions. Prefer [Jev Ultrafast](../tools/jev-ultrafast.md) for the general browser research loop, or [Jev Search](jev-search.md) for link ranking without CDP. Always confirm availability on the original listing pages.

## How it works

The local UI starts a search; the agent observes each marketplace tab and asks TypeSafe System One to pick the next action from a finite set. Results are labelled from listing text (tick vs unknown). Activity rail shows cost and duration. Stop is always available.

## Get started

```sh
git clone https://github.com/Nancy-Chauhan/hearth-jev-rental-search.git
cd hearth-jev-rental-search
git checkout c9c2d5f4b28884aded9e61a054baad14748a2ad1
uv sync
cp .env.example .env   # set TYPESAFE_API_KEY
# start Chrome with --remote-debugging-port=9222 and a temp profile, then:
# BU_CDP_URL=http://127.0.0.1:9222 uv run jev
# open http://127.0.0.1:8766
uv run pytest
```

## Examples and demos

- Upstream README includes a demo video attachment and setup for macOS/Linux Chrome profiles.
- This listing: `uv run pytest` → **63 passed**. No live CDP or TypeSafe search.

## Limits and data handling

Live searches send page/state context to TypeSafe and interact with third-party rental sites under their terms. The agent only reads and reports. Facebook/marketplace login or CAPTCHA friction may apply. Distinct from the separately listed browser-use **Jev Ultrafast** tool despite the shared package folder name.

## Review and maintenance

Reviewed on **2026-09-21** at [commit c9c2d5f](https://github.com/Nancy-Chauhan/hearth-jev-rental-search/tree/c9c2d5f4b28884aded9e61a054baad14748a2ad1): MIT; AI-assisted source review of README, LICENSE, `jev_ultrafast/model.py`, and offline tests. No live TypeSafe or Chrome run.

Related: [Jev Ultrafast](../tools/jev-ultrafast.md), [Jev Search](jev-search.md), [jevnav](../tools/jevnav.md).
