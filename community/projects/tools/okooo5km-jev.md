# jev (okooo5km)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial stdlib-only Python CLI and Agent Skill for TypeSafe Jev: `yes` / `pick` / `score` (and batch `run`) with calibrated probabilities via the TypeSafe API (default) or OpenRouter—not chat prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/okooo5km/jev) |
| Maintainer | [okooo5km](https://github.com/okooo5km). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Single-file CLI **0.3.2** under `jev/scripts/jev` plus Agent Skill packaging; install script / releases; `npx skills add okooo5km/jev`. |
| Requirements | Python ≥ 3.9 (stdlib only for the CLI). Live calls need `TYPESAFE_API_KEY` and/or `OPENROUTER_API_KEY` (`jev auth set`). |
| License | [Apache-2.0](https://github.com/okooo5km/jev/blob/2d4c4a0b6b481b2cbb744d269be5d9a987344b74/LICENSE). Provider inference billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest`: **196 passed**. Live auth/decision calls not run. Distinct from [typesafe-cli](typesafe-cli.md) (TypeScript `jev` bin) and [typesafeai-cli](typesafeai-cli.md) (Python SDK `typesafe` CLI). |

## When to use

Use it when a human or coding agent needs fast typed judgments from the shell or an Agent Skill without pulling an HTTP SDK. Prefer [typesafeai-cli](typesafeai-cli.md) for recipe-style ask/decide/screen/verify via the official SDK, or [typesafe-cli](typesafe-cli.md) / [jevkit](jevkit.md) for Node/Rust shells. Not for prose generation or judgments that must include explanations.

## How it works

The CLI posts noul/choice/score-shaped requests to `https://api.typesafe.ai/v1/systemone` or OpenRouter `https://openrouter.ai/api/alpha/decisions` (see [`jev/references/cli.md`](https://github.com/okooo5km/jev/blob/2d4c4a0b6b481b2cbb744d269be5d9a987344b74/jev/references/cli.md)). Provider selection: `--provider` → `JEV_PROVIDER` → config → key auto-detect. Skills install documents agent-friendly usage; `jev auth` manages keys without printing them.

## Get started

```sh
git clone https://github.com/okooo5km/jev.git
cd jev
git checkout 2d4c4a0b6b481b2cbb744d269be5d9a987344b74
python3 -m pytest tests/ -q
# install (review install.sh first) or: npx skills add okooo5km/jev -g
# jev auth set   # then: jev yes "…" -s "…"
```

## Examples and demos

- Upstream README.en.md shows `yes` / `pick` / `score` / `run mail` examples.
- This listing: `python3 -m pytest tests/` → **196 passed** (~69s) with local mock server. No live TypeSafe/OpenRouter call.

## Limits and data handling

Live commands send state/questions to TypeSafe or OpenRouter. Keys live under the XDG config dir (`.env` mode 600). Windows is untested upstream (WSL suggested). Unofficial community wrapper—not affiliated with TypeSafe or OpenRouter.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2d4c4a0](https://github.com/okooo5km/jev/tree/2d4c4a0b6b481b2cbb744d269be5d9a987344b74): **0.3.2**, Apache-2.0. AI-assisted source review of README.en.md, LICENSE, `jev/scripts/jev`, skill metadata, and offline tests. No live provider call.

Related: [typesafe-cli](typesafe-cli.md), [typesafeai-cli](typesafeai-cli.md), [jevkit](jevkit.md), [SemDecide](semdecide.md).
