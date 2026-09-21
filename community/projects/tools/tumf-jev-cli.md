# jev-cli (tumf)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial dependency-light Python CLI and stdio MCP server for TypeSafe Jev: ask `noul` / `choice` / `score` (and multi-question `run`) and get machine-readable answers—not chat prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tumf/jev-cli) |
| Maintainer | [tumf](https://github.com/tumf) / [tumf/jev-cli](https://github.com/tumf/jev-cli). Independently curated; this page is not an upstream submission or endorsement. Unofficial—not maintained by TypeSafe. |
| Format | PyPI package **jev-cli 0.6.2** (`uv tool install jev-cli`) exposing `jev` and `jev-mcp` entry points. |
| Requirements | Python ≥ 3.13 via [uv](https://docs.astral.sh/uv/). Live calls need `TYPESAFE_API_KEY` (or credential file via `jev auth`). |
| License | [MIT](https://github.com/tumf/jev-cli/blob/980cb98f5f529ba310ce4c7481a55e034b0a0829/LICENSE). TypeSafe inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest`: **53 passed** (7 MCP stdio subprocess tests failed on this host due to interpreter path isolation; core CLI tests passed). Live TypeSafe calls were not run. Distinct from [jev (okooo5km)](okooo5km-jev.md), [typesafe-cli](typesafe-cli.md), and [typesafeai-cli](typesafeai-cli.md). |

## When to use

Use it when a shell script or MCP host needs compact typed judgments with structured stderr/exit codes and a bundled `jev-mcp` server in the same install. Prefer [okooo5km/jev](okooo5km-jev.md) for a stdlib Agent Skill packaging path, [typesafe-cli](typesafe-cli.md) for a TypeScript/npm `jev` bin, or [typesafeai-cli](typesafeai-cli.md) for recipe-style ask/decide/screen/verify via the official Python SDK.

## How it works

The CLI posts typed questions to the official TypeSafe System One API by default (see upstream README). `jev-mcp` exposes the same primitives over stdio MCP. Auth prefers `TYPESAFE_API_KEY`, with `jev auth set` / `jev auth status` for a credential file. Multiple questions can be sent in one `run`.

## Get started

```sh
uv tool install jev-cli
jev --version   # expect: jev 0.6.2
export TYPESAFE_API_KEY=...   # do not paste secrets into chat
# jev noul "…" --state "…"
```

From source:

```sh
git clone https://github.com/tumf/jev-cli.git
cd jev-cli
git checkout 980cb98f5f529ba310ce4c7481a55e034b0a0829
uv sync
uv run pytest -q
```

## Examples and demos

- Upstream README includes terminal screenshots and a short demo video under `assets/`.
- This listing: `uv run pytest -q` → **53 passed**, 7 failed (MCP stdio subprocess spawning), 14 subtests passed. No live TypeSafe call.

## Limits and data handling

Live commands send state and questions to TypeSafe. Keys should stay in the environment or the auth file—not in chat. Unofficial community wrapper—not affiliated with TypeSafe. Confirm provider pricing separately.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 980cb98](https://github.com/tumf/jev-cli/tree/980cb98f5f529ba310ce4c7481a55e034b0a0829): **0.6.2**, MIT. AI-assisted source review of README, LICENSE, `pyproject.toml`, and offline pytest. No live provider call.

Related: [jev (okooo5km)](okooo5km-jev.md), [typesafe-cli](typesafe-cli.md), [typesafeai-cli](typesafeai-cli.md), [jev-mcp](jev-mcp.md).
