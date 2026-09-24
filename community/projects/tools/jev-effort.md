# jev-effort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial Claude Code helper: TypeSafe Jev (OpenRouter / TypeSafe / Vercel Gateway) picks per-step reasoning effort and lease without breaking the prompt cache.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ifoster01/jev-effort) |
| Maintainer | [ifoster01](https://github.com/ifoster01) / jev-effort contributors. Independently curated. |
| Format | Node.js setup + hook scripts (`src/jev.mjs`, `src/setup.mjs`). |
| Requirements | Claude Code; provider credentials for OpenRouter, TypeSafe, or Vercel AI Gateway per `ROUTES` in `jev.mjs`. |
| License | [MIT](https://github.com/ifoster01/jev-effort/blob/19944cad93883b5f2b8c9bd57b420a140d885125/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Upstream README cites cost-savings benchmarks—**not** re-measured here. Distinct from [jev-effort-router](jev-effort-router.md) (Hermes) and [pi-jev-effort](pi-jev-effort.md). |

## When to use

Use it to **vary Claude Code effort per generation** with a calibrated lease. Prefer Hermes/Pi-specific effort routers when that is your agent host.

## How it works

[`src/jev.mjs`](https://github.com/ifoster01/jev-effort/blob/19944cad93883b5f2b8c9bd57b420a140d885125/src/jev.mjs) builds Choice questions for effort (`low`…`max`) and lease length, posting to OpenRouter Decisions (`typesafe/jev-1.13`), TypeSafe `/v1/systemone` (`jev-latest`), or Vercel `evaluate`. Setup wires Claude Code hooks; code owns applying the chosen effort.

## Get started

```sh
git clone https://github.com/ifoster01/jev-effort.git
cd jev-effort
git checkout 19944cad93883b5f2b8c9bd57b420a140d885125
# follow README / docs/usage.md for setup.mjs and provider env
```

## Examples and demos

- `docs/how-it-works.md`, `docs/usage.md`.
- README benchmark tables (vendor-reported).

## Limits and data handling

Task/history snippets leave the host on live provider calls. Treat effort answers as advisory—verify Claude Code hook behavior on your build.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 19944ca](https://github.com/ifoster01/jev-effort/tree/19944cad93883b5f2b8c9bd57b420a140d885125). AI-assisted README/LICENSE/`src/jev.mjs` inspection. No live Claude Code or provider spend.

Related: [jev-effort-router](jev-effort-router.md), [pi-jev-effort](pi-jev-effort.md), [opencode-smart-reasoning](opencode-smart-reasoning.md).
