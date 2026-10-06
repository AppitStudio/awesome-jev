# autoloop

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Config-driven GitHub issue → triage → implement → review → PR pipeline for coding agents, with an experimental, off-by-default Jev shadow mode (`typesafe/jev-1.13` via OpenRouter) that evaluates triage and auto-merge decision points alongside the pipeline and only logs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sanctum-Origo-Systems/autoloop) |
| Product homepage | [andywidjaja.com](https://andywidjaja.com/autoloop) |
| Maintainer | [Sanctum-Origo-Systems](https://github.com/Sanctum-Origo-Systems). Independently curated. |
| Format | CLI tool with `autoloop.toml` configuration |
| Requirements | Python with `uv`, GitHub access and your coding agent. Jev shadow mode needs an OpenRouter key with Decisions API access (`OPENROUTER_API_KEY` by default). |
| License | [Apache-2.0](https://github.com/Sanctum-Origo-Systems/autoloop/blob/0c6af4ca08afe7057a22b5c53ab97d64e099ae98/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure whether a calibrated decision model would agree with your pipeline's triage and auto-merge choices before trusting it with any gate.
- Collect a JSONL record of decision points for later review (`jev_report`).
- Mismatch: the `gate` mode is reserved and not implemented; today Jev never changes what autoloop does.

## How it works

With `[jev] mode = "shadow"`, [`src/autoloop/jev.py`](https://github.com/Sanctum-Origo-Systems/autoloop/blob/0c6af4ca08afe7057a22b5c53ab97d64e099ae98/src/autoloop/jev.py) asks Jev about every triage and auto-merge decision point; `jev_log` appends observations to `autoloop/jev_decisions.jsonl`, and probabilities inside the `gate_low`–`gate_high` band (0.15–0.85) are marked uncertain. A backfill script and report summarise agreement with the existing pipeline.

## Get started

Install a tagged release and add a `[jev]` block in shadow mode (live OpenRouter calls per decision point):

```sh
uv tool install git+https://github.com/Sanctum-Origo-Systems/autoloop@<tag>
autoloop version
# autoloop.toml
# [jev]
# mode = "shadow"
# model = "typesafe/jev-1.13"
# api_key_env = "OPENROUTER_API_KEY"
```

Shadow mode is billed by OpenRouter per decision point; the main pipeline's agent costs are separate.

## Examples and demos

- README section *Experimental: Decision Model (Jev)* with every config field.
- `docs/jev-response-sample.json` and `scripts/backfill_jev.py`.

## Limits and data handling

Experimental and off by default; shadow only. Issue/PR context is sent to OpenRouter and TypeSafe when enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 0c6af4ca08af](https://github.com/Sanctum-Origo-Systems/autoloop/tree/0c6af4ca08afe7057a22b5c53ab97d64e099ae98). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
