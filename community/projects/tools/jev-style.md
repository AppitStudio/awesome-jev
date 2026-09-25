# Jev-Style

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small calibrated decision models you run locally, with a systemone-compatible server, agent skills, Claude Code guard, and MCP tools—weights on Hugging Face; independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lawrence3699/jev-style) |
| Maintainer | [lawrence3699](https://github.com/lawrence3699). Independently curated. |
| Format | Python local server + agent skills / Claude Code guard / MCP; torch/MLX/GGUF weights. |
| Requirements | Python environment per upstream; local weights from Hugging Face; optional Claude Code for guard/skills. |
| License | [Apache-2.0](https://github.com/lawrence3699/jev-style/blob/2bb3151de3969083a1c32c4317dabe9b387a5a2b/LICENSE). |
| Disclosure | Independent open model tooling—not TypeSafe-hosted Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Demo/CI claims are upstream-reported; local serve not run on the review host. |

## When to use

Use for **on-machine System One–compatible decisions** plus agent wiring (skills/MCP/guard). Prefer hosted TypeSafe Jev when you need the official cloud model.

## How it works

Local checkpoints serve typed decisions over a systemone-compatible API; bundled skills and MCP tools call that server from agents; an optional Claude Code guard gates tool use.

## Get started

```sh
git clone https://github.com/lawrence3699/jev-style.git
cd jev-style
git checkout 2bb3151de3969083a1c32c4317dabe9b387a5a2b
# Demo: https://huggingface.co/spaces/chaoliangUNSW/jev-style-v3
# Follow upstream README for serve/skills/MCP
```

## Examples and demos

- HF Spaces playground; README demo GIF.
- Agent skills section and guard/MCP wiring in the repo.

## Limits and data handling

Local by default; HF downloads and Spaces traffic follow those hosts. Not official Jev. Quality depends on chosen weights and task.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 2bb3151de3969083a1c32c4317dabe9b387a5a2b](https://github.com/lawrence3699/jev-style/tree/2bb3151de3969083a1c32c4317dabe9b387a5a2b). AI-assisted README and LICENSE inspection; serve/skills not executed.
