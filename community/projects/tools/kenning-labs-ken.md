# Ken by Kenning Labs (self-hosted MCP server that keeps one linked record of your tasks, people and projects, with Jev as an optional judge)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Self-hosted MCP server (Python, one SQLite file, alpha) that keeps the current state of your life as one linked record of tasks, people, projects, documents and preferences, shared by every MCP app you use (Claude, ChatGPT, Cursor). When an agent starts a task, Ken adds the linked people, projects and last report it needs. A judge checks every write for duplicates and contradictions and leaves the unsure ones to you. The judge and the Today ranking can run on a decisions model: OpenAI Decisions by default when the main model is OpenAI, or TypeSafe Jev with its own key. Jev is optional; the main model can be OpenAI, any OpenAI-compatible API, a local model or your Claude Code login.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kenning-labs/ken) |
| Maintainer | [kenning-labs](https://github.com/kenning-labs). Independently curated. |
| Format | MCP server and CLI (Python, `uv tool install`) |
| Requirements | Python 3.11+ and uv; a model for the checks (OpenAI key, OpenAI-compatible host, local model or Claude Code login); a `TYPESAFE_API_KEY` in `decisions:` only if you pick Jev. |
| License | [AGPL-3.0](https://github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/sashko_po/status/2122447254233428245)). |
| Jev evidence | [`engine/src/ken/decisions.py`](https://github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/engine/src/ken/decisions.py) at the pinned commit. |

## When to use

- Give every MCP app one shared, current record of your work and life, with each write checked.
- Mismatch: a hosted team knowledge base; it is a personal, alpha, single-file server (Ken Cloud is a separate early-access hosted option).

## How it works

`engine/src/ken/decisions.py` defines a `Jev` class behind Ken's `Decisions` interface that posts choice, noul (yes probability) and score questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; `engine/config.example.yaml` shows the `decisions: provider: jev` block that turns it on. Integration evidence: [`engine/src/ken/decisions.py`](https://github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/engine/src/ken/decisions.py).

## Get started

Install the engine with uv, run the setup, then set the Jev block in your config if you want Jev as the judge.

```sh
uv tool install 'ken-engine[mcp] @ git+https://github.com/kenning-labs/ken#subdirectory=engine'
ken init
# optional, in Ken's config.yaml:
# decisions:
#   provider: jev
#   api_key: "YOUR_TYPESAFE_API_KEY"
#   model: "jev-latest"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/README.md](https://github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/README.md)
- Architecture: [github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/ARCHITECTURE.md](https://github.com/kenning-labs/ken/blob/0531b288911f1ddddc16a24b176ae8f69b9fe30b/ARCHITECTURE.md)

## Limits and data handling

Records live in one local SQLite file; text you write is sent to the model you choose, and judge questions go to TypeSafe only when Jev is configured. Ken Cloud (early access, hosted in Frankfurt; price not stated in the README) is a separate service and was not reviewed. Alpha software.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 0531b288911f](https://github.com/kenning-labs/ken/tree/0531b288911f1ddddc16a24b176ae8f69b9fe30b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
