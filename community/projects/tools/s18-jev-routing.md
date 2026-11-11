# S18Share (agent runtime with Jev fast decision routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source agent runtime and orchestration API with MCP tools, memory and RAG, whose query routing, skill matching and planner fast-paths can use Jev, falling back to built-in regex guards when Jev is unkeyed, unreachable or low-confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/riteshverma/s18) |
| Maintainer | [riteshverma](https://github.com/riteshverma). Independently curated. |
| Format | Agent runtime and API (Python, Apache-2.0) |
| Requirements | Python with `uv`, a `GEMINI_API_KEY` for the agents, and `JEV_API_KEY` (or `TYPESAFE_API_KEY`) to turn on Jev routing. |
| License | [Apache-2.0](https://github.com/riteshverma/s18/blob/139495d15f237dc819265cac913c12ff5cdbeab7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/decisions/jev_client.py`](https://github.com/riteshverma/s18/blob/139495d15f237dc819265cac913c12ff5cdbeab7/core/decisions/jev_client.py) at the pinned commit. |

## When to use

- Route agent queries and skills with typed decisions before the planner runs.
- Mismatch: small project; Jev is optional with regex fallback.

## How it works

`core/decisions/jev_client.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; `core/decisions/router.py` uses the answers, `S18_DECISIONS_ENABLED=0` turns it off, and `scripts/jev_probe.py` checks your key. Integration evidence: [`core/decisions/jev_client.py`](https://github.com/riteshverma/s18/blob/139495d15f237dc819265cac913c12ff5cdbeab7/core/decisions/jev_client.py).

## Get started

Sync dependencies, set your keys, then start the API.

```sh
git clone https://github.com/riteshverma/s18.git && cd s18
uv sync && uv run python api.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/riteshverma/s18/blob/139495d15f237dc819265cac913c12ff5cdbeab7/README.md](https://github.com/riteshverma/s18/blob/139495d15f237dc819265cac913c12ff5cdbeab7/README.md)

## Limits and data handling

Query text for routing goes to TypeSafe on your key when enabled.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 139495d15f23](https://github.com/riteshverma/s18/tree/139495d15f237dc819265cac913c12ff5cdbeab7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
