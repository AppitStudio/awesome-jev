# jev-effort-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that asks TypeSafe Jev, each user turn, which Ollama:Cloud model **and** reasoning effort to use, then rewrites the outgoing `llm_request`—distinct from model-only routers and from manual effort controls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlphaPerseii3000/jev-effort-router) |
| Maintainer | [AlphaPerseii3000](https://github.com/AlphaPerseii3000). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python Hermes plugin **`hermes-plugin-jev-effort-router` 0.2.1** (`plugin.yaml` + `llm_request` middleware). |
| Requirements | Python **3.11+**; Hermes Agent on **`provider: ollama-cloud`** with `llm_request` middleware (Hermes **0.21.4+**). `OPENROUTER_API_KEY` for Decisions. Community install is blocked by Hermes plugin scan by default—review findings and use `--force` if you accept them. |
| License | [MIT](https://github.com/AlphaPerseii3000/jev-effort-router/blob/e16f2162c7a9947e9606888a0f507eb856f4e62e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `client.py`, `router.py`, `plugin.yaml`). Offline pytest and live Hermes/Jev were **not** run on the review host. |

## When to use

Use it when Hermes runs on Ollama:Cloud and you want **per-turn** joint routing of model + reasoning effort from Jev. Prefer [pi-jev-effort](pi-jev-effort.md) for Pi thinking-level scoring, or [Agent Router](agent-router.md) / Hermes Jev Skills for other routing surfaces. Other providers pass through untouched.

## How it works

On each user turn, middleware calls Jev with Choice questions for model route and reasoning effort ([`client.py`](https://github.com/AlphaPerseii3000/jev-effort-router/blob/e16f2162c7a9947e9606888a0f507eb856f4e62e/client.py), [`state.py`](https://github.com/AlphaPerseii3000/jev-effort-router/blob/e16f2162c7a9947e9606888a0f507eb856f4e62e/state.py)). Confidence guards and failure modes return `None` so the request stays byte-identical to an unrouted turn. On success, the provider request is rewritten with the selected model and effort; the main model still generates all tokens. Audit/memo/grid helpers and `/jev-effort-router` commands are documented upstream.

## Get started

```sh
hermes plugins install AlphaPerseii3000/jev-effort-router --force   # after reviewing scan findings
hermes plugins enable jev-effort-router
# set OPENROUTER_API_KEY in Hermes .env; restart session
hermes jev-effort-router status
```

Pin for review: [commit e16f216](https://github.com/AlphaPerseii3000/jev-effort-router/tree/e16f2162c7a9947e9606888a0f507eb856f4e62e). Live routing sends a bounded slice of conversation context to OpenRouter Decisions and can incur charges.

## Examples and demos

- CLI: `hermes jev-effort-router route "…"`, `grid`, `tail`, `reset`.
- Upstream tests under `tests/` (not executed on the review host).

## Limits and data handling

Ollama:Cloud-only routing grid. Hermes community install scanner flags expected network/exfil and doc `pip install` matches—review before `--force`. Failures leave requests unrouted. No live Jev spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit e16f216](https://github.com/AlphaPerseii3000/jev-effort-router/tree/e16f2162c7a9947e9606888a0f507eb856f4e62e) (**0.2.1**, MIT). AI-assisted source review of README, LICENSE, client/router. No Hermes install or live TypeSafe/OpenRouter calls.

Related: [pi-jev-effort](pi-jev-effort.md), [Hermes Jev Skills](hermes-jev-skills.md), [Agent Router](agent-router.md).
