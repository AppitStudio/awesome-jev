# Tessera (single-owner desktop agent harness with memory, and optional Jev routing and risk checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python standard-library agent harness for one owner: captured turns and tool outcomes, AetherMind memory over MCP with a durable outbox, shell hooks that can block a tool call, optional swarm jobs and realtime voice. With Jev enabled it picks direct, tools or delegate routes, takes part in shell risk checks and memory recall, and logs each decision's probabilities and latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MaverickKB/Tessera-CT) |
| Maintainer | [MaverickKB](https://github.com/MaverickKB). Independently curated. |
| Format | Python 3.11+ CLI (standard library) |
| Requirements | Python 3.11+; your chosen model providers; a TypeSafe API key only if Jev is enabled. |
| License | [Apache-2.0](https://github.com/MaverickKB/Tessera-CT/blob/d2a3afef6519069e4ea8b296097759edf17afbad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tessera/cua_jev.py`](https://github.com/MaverickKB/Tessera-CT/blob/d2a3afef6519069e4ea8b296097759edf17afbad/tessera/cua_jev.py) at the pinned commit. |

## When to use

- Build a personal agent where routing and risk checks are logged decisions, not prompts.
- Mismatch: Jev is off by default; a starting point, not a finished product.

## How it works

`tessera/cua_jev.py` posts state and questions to a configured `/v1/systemone` endpoint (key via `TYPESAFE_API_KEY` credential reference); with Jev off, heuristics are used. Integration evidence: [`tessera/cua_jev.py`](https://github.com/MaverickKB/Tessera-CT/blob/d2a3afef6519069e4ea8b296097759edf17afbad/tessera/cua_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && .venv/bin/python -m pip install -e .
.venv/bin/python -m tessera init
.venv/bin/python -m tessera run "Explain the files in this directory"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide: [github.com/MaverickKB/Tessera-CT/blob/main/docs/SETUP.md](https://github.com/MaverickKB/Tessera-CT/blob/main/docs/SETUP.md)

## Limits and data handling

With Jev on, turn and tool context for each decision goes to the configured endpoint. Tests and the demo need no live providers.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit d2a3afef6519](https://github.com/MaverickKB/Tessera-CT/tree/d2a3afef6519069e4ea8b296097759edf17afbad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
