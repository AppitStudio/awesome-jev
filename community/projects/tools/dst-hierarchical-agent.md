# DST Hierarchical Agent (Don't Starve Together player and companion mods driven by TypeSafe Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Two Don't Starve Together mods with a shared Python controller: a Jev-driven agent that controls your character and Jev AI companions you can summon.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wjc1207/DST-Hierarchical-Agent) |
| Maintainer | [wjc1207](https://github.com/wjc1207). Independently curated. |
| Format | Game mods + Python MCP controller (no SPDX license file on the reviewed commit) |
| Requirements | Don't Starve Together, Python 3, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mcp_agent/jev_client.py`](https://github.com/wjc1207/DST-Hierarchical-Agent/blob/bd4afc20c77bfd2dd9867e068f7c61a4738233f5/mcp_agent/jev_client.py) at the pinned commit. |

## When to use

- Let Jev play or accompany you in Don't Starve Together.
- Study hierarchical control with a fast decision layer.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`mcp_agent/jev_client.py` calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` for low-level action choices under a hierarchical controller. Integration evidence: [`mcp_agent/jev_client.py`](https://github.com/wjc1207/DST-Hierarchical-Agent/blob/bd4afc20c77bfd2dd9867e068f7c61a4738233f5/mcp_agent/jev_client.py).

## Get started

Install the mods, set JEV_API_KEY/TYPESAFE_API_KEY, and start the controller per README.

```sh
git clone https://github.com/wjc1207/DST-Hierarchical-Agent.git && cd DST-Hierarchical-Agent
export TYPESAFE_API_KEY=...
pip install -r requirements.txt && python mcp_agent/mcp_agent.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/wjc1207/DST-Hierarchical-Agent/blob/bd4afc20c77bfd2dd9867e068f7c61a4738233f5/README.md](https://github.com/wjc1207/DST-Hierarchical-Agent/blob/bd4afc20c77bfd2dd9867e068f7c61a4738233f5/README.md)

## Limits and data handling

Game state is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit bd4afc20c77b](https://github.com/wjc1207/DST-Hierarchical-Agent/tree/bd4afc20c77bfd2dd9867e068f7c61a4738233f5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
