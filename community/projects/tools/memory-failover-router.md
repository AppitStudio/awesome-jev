# Memory Failover Router (local agent-memory endpoint that fails over from Hindsight to a local store and ranks recall with Jev)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

One local endpoint for Claude Code, Hermes and scripts that fronts two memory stores, Hindsight as primary and Mnemosyne as a local fallback, switching automatically when the paid model API fails. Recalled memories are ranked by Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tauseefau/memory-failover-router) |
| Maintainer | [tauseefau](https://github.com/tauseefau). Independently curated. |
| Format | Python service + Docker Compose templates, MCP and HTTP |
| Requirements | Docker; Hindsight and Mnemosyne; a TypeSafe key for ranking. |
| License | [MIT](https://github.com/tauseefau/memory-failover-router/blob/beb6b9c409b351a3ecab6468b288970bffec85ed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/router/app.py`](https://github.com/tauseefau/memory-failover-router/blob/beb6b9c409b351a3ecab6468b288970bffec85ed/scripts/router/app.py) at the pinned commit. |

## When to use

- Keep agent memory working when the primary provider is down.
- Mismatch: an early personal setup.

## How it works

`scripts/router/app.py` serves port 8899, routes reads and writes to the healthy store, and sends recall candidates to `https://api.typesafe.ai/v1/systemone` to rank them. Integration evidence: [`scripts/router/app.py`](https://github.com/tauseefau/memory-failover-router/blob/beb6b9c409b351a3ecab6468b288970bffec85ed/scripts/router/app.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see README: start the Hindsight template, then run scripts/router/app.py on :8899
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/tauseefau/memory-failover-router#readme](https://github.com/tauseefau/memory-failover-router#readme)

## Limits and data handling

Recall candidates (memory text) are sent to TypeSafe for ranking. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit beb6b9c409b3](https://github.com/tauseefau/memory-failover-router/tree/beb6b9c409b351a3ecab6468b288970bffec85ed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
