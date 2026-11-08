# AgenticX (multi-agent platform whose group-chat router asks TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python SDK + CLI + desktop studio for multi-agent systems; an httpx TypeSafe client lets group chats route un-mentioned messages with Jev and show a visible decision card.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DemonDamon/AgenticX) |
| Maintainer | [DemonDamon](https://github.com/DemonDamon). Independently curated. |
| Format | Python SDK + CLI + desktop (Apache-2.0) |
| Requirements | Python, AgenticX install, and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/DemonDamon/AgenticX/blob/631b0047451c50ae19192b9f752eb1523e6150f6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agenticx/llms/typesafe_client.py`](https://github.com/DemonDamon/AgenticX/blob/631b0047451c50ae19192b9f752eb1523e6150f6/agenticx/llms/typesafe_client.py) at the pinned commit. |

## When to use

- Route group-chat turns between agents with Jev.
- Show the routing decision to users as a card.
- Mismatch: docs are largely Chinese.

## How it works

`typesafe_client.py` posts to `https://api.typesafe.ai/v1/systemone`; `agenticx/runtime/group_router.py` asks Jev who should answer when no agent is @-mentioned. Integration evidence: [`agenticx/llms/typesafe_client.py`](https://github.com/DemonDamon/AgenticX/blob/631b0047451c50ae19192b9f752eb1523e6150f6/agenticx/llms/typesafe_client.py).

## Get started

Install AgenticX per README and set the TypeSafe key in its config (`typesafe_config.py`).

```sh
git clone https://github.com/DemonDamon/AgenticX.git && cd AgenticX
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DemonDamon/AgenticX/blob/631b0047451c50ae19192b9f752eb1523e6150f6/README.md](https://github.com/DemonDamon/AgenticX/blob/631b0047451c50ae19192b9f752eb1523e6150f6/README.md)

## Limits and data handling

Messages and agent descriptions are sent to TypeSafe for routing.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 631b0047451c](https://github.com/DemonDamon/AgenticX/tree/631b0047451c50ae19192b9f752eb1523e6150f6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
