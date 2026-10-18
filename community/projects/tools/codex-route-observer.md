# codex-route-observer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy that observes Codex/OpenAI-style coding-agent traffic and uses TypeSafe Jev to categorize current request usage for a dashboard of routes, models, and spend-ish signals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jeancsil/codex-route-observer) |
| Maintainer | [jeancsil](https://github.com/jeancsil). Independently curated. |
| Format | Python package with static dashboard assets |
| Requirements | Python; TYPESAFE_API_KEY; point Codex/OpenAI clients at the local proxy. |
| License | [Apache-2.0](https://github.com/jeancsil/codex-route-observer/blob/817ecd87479c80246a84b0ea69e5b0dbbcb5e1c6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/codex_route_observer/jev_usage.py`](https://github.com/jeancsil/codex-route-observer/blob/817ecd87479c80246a84b0ea69e5b0dbbcb5e1c6/src/codex_route_observer/jev_usage.py) at the pinned commit. |

## When to use

- Want Jev-labeled categories on live coding-agent request streams.
- Need a local observer dashboard without changing the agent itself.
- Mismatch: observer/proxy; not an official Codex product.

## How it works

`jev_usage.py` posts usage-categorization questions to `api.typesafe.ai` for models such as `jev-1.13.0` / `jev-1.14.0`. The proxy records route metadata and surfaces it in a small static UI. Integration evidence: [`src/codex_route_observer/jev_usage.py`](https://github.com/jeancsil/codex-route-observer/blob/817ecd87479c80246a84b0ea69e5b0dbbcb5e1c6/src/codex_route_observer/jev_usage.py).

## Get started

Clone, configure `.env` with TYPESAFE_API_KEY, run the observer, and point clients at it.

```sh
git clone https://github.com/jeancsil/codex-route-observer && cd codex-route-observer
cp .env.example .env  # set TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README architecture notes
- .env.example TypeSafe endpoint knobs

## Limits and data handling

Request payloads may be summarized or sampled for Jev. Not affiliated with OpenAI/Codex.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 817ecd87479c](https://github.com/jeancsil/codex-route-observer/tree/817ecd87479c80246a84b0ea69e5b0dbbcb5e1c6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
