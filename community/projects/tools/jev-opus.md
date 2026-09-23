# jev-opus

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Opus 5.5 sessions where TypeSafe Jev re-picks reasoning effort every step via per-message effort statements so the Anthropic prompt cache can keep growing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WXK-AI/jev-opus) |
| Maintainer | [WXK-AI](https://github.com/WXK-AI). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node CLI + Claude Code plugin **jev-opus 0.3.0** (npm). |
| Requirements | Node **≥ 22.18**; Claude Code **2.1.280+** logged in; TypeSafe key (`apikey_…`) or OpenRouter key (`sk-or-…`) for Jev (local heuristics if missing). |
| License | [MIT](https://github.com/WXK-AI/jev-opus/blob/b525d4ccfb68a97e54b101c24e18c108d02b6dff/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, package, `src/jev/`, `src/router/`). Live Claude/Jev runs were **not** executed on the review host. |

## When to use

Use it when you want mid-prompt effort changes on Opus 5.5 without discarding the prompt cache. Prefer [jev-effort-router](jev-effort-router.md) for Hermes/Ollama:Cloud joint model+effort routing, or [Astra-Ares](astra-ares.md) for Codex Astra effort adaptation.

## How it works

Gateway mode (`jev-opus claude`) or driver mode (`jev-opus "task"`) asks Jev for effort, then inserts Anthropic **per-message** effort statements and keeps them in history ([`src/jev/client.ts`](https://github.com/WXK-AI/jev-opus/blob/b525d4ccfb68a97e54b101c24e18c108d02b6dff/src/jev/client.ts), [`src/router/router.ts`](https://github.com/WXK-AI/jev-opus/blob/b525d4ccfb68a97e54b101c24e18c108d02b6dff/src/router/router.ts)). Local heuristics apply when no Jev key is configured.

## Get started

```sh
npm install -g jev-opus
jev-opus init
jev-opus claude
```

Pin for review: [commit b525d4c](https://github.com/WXK-AI/jev-opus/tree/b525d4ccfb68a97e54b101c24e18c108d02b6dff). Live classification sends task/step context to TypeSafe or OpenRouter and may incur charges (plus Claude usage).

## Examples and demos

- README demo SVG showing mid-prompt effort path and cache growth (illustrative).
- Upstream CI workflow (not re-run on the review host).

## Limits and data handling

Requires a Claude Code version that supports per-message effort. Without a Jev key, heuristics still run. This listing did not measure cache hit rates or task success.

## Review and maintenance

Reviewed on **2026-09-23** at [commit b525d4c](https://github.com/WXK-AI/jev-opus/tree/b525d4ccfb68a97e54b101c24e18c108d02b6dff) (**0.3.0**, MIT). AI-assisted source review. No live Claude or TypeSafe spend.

Related: [jev-effort-router](jev-effort-router.md), [Astra-Ares](astra-ares.md), [pi-jev-effort](pi-jev-effort.md).
