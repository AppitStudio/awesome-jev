# TypeSafe AI for Agent Zero

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community Agent Zero plugin that asks TypeSafe Jev Choice / Noul / Score questions from chat via a `typesafe_query` tool and renders probability cards—bundling the official TypeSafe agent skill unchanged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/3clyp50/a0-typesafe-ai) |
| Maintainer | [3clyp50](https://github.com/3clyp50). Independently curated; not an official TypeSafe or Agent Zero product. |
| Format | Agent Zero plugin **typesafe_ai 1.0.0** (tool, WebUI cards, hooks, bundled `typesafe-ai` skill). |
| Requirements | A working Agent Zero install; TypeSafe API key in plugin settings or `TYPESAFE_API_KEY` via Agent Zero secrets/env. |
| License | [MIT](https://github.com/3clyp50/a0-typesafe-ai/blob/ab928cf321fc431d768d677963d25a5bf610cc9e/LICENSE) (bundled skill retains its own MIT copyright). |

## When to use

Use it when Agent Zero should batch typed judgments over shared evidence and inspect distributions in the UI. Prefer [Hermes Jev Skills](hermes-jev-skills.md) or [Advocaat](advocaat.md) for Hermes/Claude/Codex or TypeScript batching outside Agent Zero. Do not treat card probabilities as permission grants—Agent Zero still owns tool execution policy.

## How it works

[`tools/typesafe_query.py`](https://github.com/3clyp50/a0-typesafe-ai/blob/ab928cf321fc431d768d677963d25a5bf610cc9e/tools/typesafe_query.py) builds an `AsyncTypeSafeClient` against `https://api.typesafe.ai` and calls [`helpers/jev.py`](https://github.com/3clyp50/a0-typesafe-ai/blob/ab928cf321fc431d768d677963d25a5bf610cc9e/helpers/jev.py) `query()` → `client.system_one(...)`. Only explicit `state` and `questions` are sent; model/timeout live in plugin settings. Incomplete answer sets raise rather than silently acting.

## Get started

```sh
git clone https://github.com/3clyp50/a0-typesafe-ai.git
cd a0-typesafe-ai
git checkout ab928cf321fc431d768d677963d25a5bf610cc9e
# Install as an Agent Zero community plugin per upstream README / plugin.yaml
# Then: Plugins → TypeSafe AI → Settings → API key (or set TYPESAFE_API_KEY)
```

Live `typesafe_query` calls are billable and send the supplied state to TypeSafe. This listing did not install Agent Zero or call the API.

## Examples and demos

- README example combining department Choice, refund Noul, and urgency Score in one call.
- `tests/check_jev.py` and WebUI result cards under `webui/`.
- Bundled official skill under `resources/typesafe-ai/`.

## Limits and data handling

Plugin-stored keys sit in Agent Zero local plugin configuration—do not share `config.json` backups. Provider errors are returned without exposing raw response bodies. Upstream screenshots are illustrative; judgment quality was not measured here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ab928cf3](https://github.com/3clyp50/a0-typesafe-ai/tree/ab928cf321fc431d768d677963d25a5bf610cc9e): **1.0.0**, MIT. AI-assisted source review of README, `tools/typesafe_query.py`, `helpers/jev.py`, `plugin.yaml`, and license. Agent Zero install and live TypeSafe calls were not run on the review host.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [Advocaat](advocaat.md), [jev-mcp](jev-mcp.md).
