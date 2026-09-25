# jev-swap

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Scan TS/JS/Python codebases for LLM calls that are really decisions, generate TypeSafe Jev modules, and shadow-test savings on recorded or proxied traffic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0xjba/jev-swap) |
| Maintainer | [0xjba](https://github.com/0xjba). Independently curated. |
| Format | npm CLI (`jev-swap` / `npx jev-swap`); Node ≥ 22.12; optional Python 3.9+ for Python scanning. |
| Requirements | Node 22.12+; `TYPESAFE_API_KEY` for live shadow/proxy (or `--mock`). |
| License | [MIT](https://github.com/0xjba/jev-swap/blob/c6b82425c57a211b22e63e432e6b2959470b3c71/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **find migrate-able decision LLM calls** and prove Jev parity/savings before swapping production traffic.

## How it works

`scan` → `convert` → `shadow` (or `proxy`) pipeline targeting `@typesafe-ai/sdk` / `typesafe-sdk`. Explorer site lists open-source savings estimates (vendor/upstream claims).

## Get started

```sh
npx jev-swap scan ./your-app
npx jev-swap convert
npx jev-swap shadow samples.jsonl --mock
# reviewed tip: c6b82425c57a211b22e63e432e6b2959470b3c71
```

## Examples and demos

- Website [jev-swap.vercel.app](https://jev-swap.vercel.app) and Explorer.
- README OpenAI/Anthropic/AI SDK/LangChain coverage list.

## Limits and data handling

Source and recorded samples may leave the machine during live shadow. Explorer savings figures are upstream/site-reported, not catalog-verified.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit c6b8242](https://github.com/0xjba/jev-swap/tree/c6b82425c57a211b22e63e432e6b2959470b3c71). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [daf-jev](daf-jev.md).
