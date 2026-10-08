# jev-max

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Jev browser agent aimed at pages ordinary Jev agents miss: a piercing snapshot walks open shadow roots and same-origin iframes into one indexed element table, a vision fallback handles canvas, clicks are occlusion-checked, one Jev request per cycle picks the operation and target (TypeSafe or OpenRouter), a small LLM writes text only for fill/select, and an independent Jev check verifies DONE; ships as a Python library, CLI and MCP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saloni-garg/jev-max) |
| Maintainer | [saloni-garg](https://github.com/saloni-garg). Independently curated. |
| Format | Python package from source (`jev-max` CLI, `jev_max.Agent`, `jev-max mcp`) |
| Requirements | Python 3.10+, Playwright Chromium; `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`, plus `TEXT_MODEL_API_KEY` for text fields. |
| License | [MIT](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Automate sites built with web components or embedded frames.
- Expose a Jev browser agent to any MCP host.
- Mismatch: cross-origin frames are only recorded as regions; canvas needs a vision model.

## How it works

[`jev_max/snapshot.js`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/jev_max/snapshot.js) builds the element table; [`jev_max/agent.py`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/jev_max/agent.py) and [`jev_max/model.py`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/jev_max/model.py) run the decide/act/verify loop; [`jev_max/mcp_server.py`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/jev_max/mcp_server.py) exposes it over MCP.

## Get started

Install from the repository (the README's `pip install jev-max` name was not on PyPI at review time):

```sh
pip install git+https://github.com/saloni-garg/jev-max.git
playwright install chromium
jev-max snapshot --url https://example.com   # no API key needed
```

Each cycle is one Jev request plus occasional text-model or vision calls on your keys.

## Examples and demos

- Benchmark tasks: [`jev_max/benchmark/tasks.yaml`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/jev_max/benchmark/tasks.yaml).
- Example: [`examples/run.py`](https://github.com/saloni-garg/jev-max/blob/1fea15516af1bca6cf60010a729241776496948a/examples/run.py).

## Limits and data handling

Page element text goes to TypeSafe or OpenRouter. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 1fea15516af1](https://github.com/saloni-garg/jev-max/tree/1fea15516af1bca6cf60010a729241776496948a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
