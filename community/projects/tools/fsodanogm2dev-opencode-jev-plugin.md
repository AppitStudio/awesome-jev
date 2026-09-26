# opencode-jev-plugin (fsodanogm2dev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode / OhMyOpenCode plugin that routes agent infrastructure decisions through TypeSafe Jev (local Unix-socket broker with cache) for safety pre-checks, subagent routing, and prompt/token reductions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fsodanogm2dev/opencode-jev-plugin) |
| Maintainer | [fsodanogm2dev](https://github.com/fsodanogm2dev). Independently curated. |
| Format | JavaScript OpenCode plugin + broker.js sidecar. |
| Requirements | OpenCode (or OmO); Node.js; TYPESAFE_API_KEY or key in ~/.config/opencode/jev.json. |
| License | [MIT](https://github.com/fsodanogm2dev/opencode-jev-plugin/blob/3b7daad785027b42961e82042598315f1f08f31f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Distinct owner/repo from prior OpenCode Jev listings. |

## When to use

Use when you want **OpenCode hooks** backed by a cached local Jev broker. Compare with opencode-jev-router / opencode-jev-guard for overlapping scopes.

## How it works

[`src/plugin.js`](https://github.com/fsodanogm2dev/opencode-jev-plugin/blob/3b7daad785027b42961e82042598315f1f08f31f/src/plugin.js) registers lifecycle hooks; [`src/broker.js`](https://github.com/fsodanogm2dev/opencode-jev-plugin/blob/3b7daad785027b42961e82042598315f1f08f31f/src/broker.js) pools calls to api.typesafe.ai /v1/systemone. Safety fails closed; routing fails open per upstream.

## Get started

```sh
git clone https://github.com/fsodanogm2dev/opencode-jev-plugin.git
cd opencode-jev-plugin
git checkout 3b7daad785027b42961e82042598315f1f08f31f
# install into ~/.config/opencode/plugins/ per upstream README
```

## Examples and demos

- Upstream capability table (reasoning budget, log compression, skill pruning, GC, routing, command safety).
- jev.json.example configuration template.

## Limits and data handling

Prompts/tool args/logs sent through hooks go to TypeSafe when uncached. Token-savings numbers are author-estimated.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 3b7daad](https://github.com/fsodanogm2dev/opencode-jev-plugin/tree/3b7daad785027b42961e82042598315f1f08f31f). AI-assisted README and LICENSE inspection of plugin/broker; install/live paths not executed.
