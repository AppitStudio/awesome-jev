# Decision Model Arena

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Side-by-side games and questions for four decision models—OpenAI Decisions API, Microsoft Decision-1, TypeSafe Jev and local Laya—with code owning every rule and number.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dante01yoon/decision-model-arena) |
| Maintainer | [dante01yoon](https://github.com/dante01yoon). Independently curated. |
| Format | Local web arena (Python server + JS games) |
| Requirements | Python; keys for the hosted models you compare; Apple Silicon for local Laya. |
| License | [MIT](https://github.com/dante01yoon/decision-model-arena/blob/285c8036e1e40696fd3be7ceadc141e0635a80d6/LICENSE) |
| Jev evidence | [`arena/server.py`](https://github.com/dante01yoon/decision-model-arena/blob/285c8036e1e40696fd3be7ceadc141e0635a80d6/arena/server.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Show how different decision models answer identical typed questions in games and image checks.
- Mismatch: demo comparisons, not a benchmark; UI labels are Korean.

## How it works

Each side receives the same state and named choice/noul/score questions; the server adapts requests per provider and the games apply the answers. (Summarized from the upstream [README](https://github.com/dante01yoon/decision-model-arena/blob/285c8036e1e40696fd3be7ceadc141e0635a80d6/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): set the provider keys and run the arena server per the README.

## Limits and data handling

Game states and images go to each hosted provider you enable. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 285c8036e1e4](https://github.com/dante01yoon/decision-model-arena/tree/285c8036e1e40696fd3be7ceadc141e0635a80d6). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
