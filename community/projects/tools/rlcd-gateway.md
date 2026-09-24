# RLCD Gateway

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted Go gateway for LLMs and decision models: route Claude Code/Codex/OpenAI/Anthropic traffic with context pruning, plus Jev/open-rlcd System One audit and calibration on a live dashboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JimmyWesley/rlcd-gateway) |
| Maintainer | [JimmyWesley](https://github.com/JimmyWesley). Independently curated. |
| Format | Go binary via npm/PyPI/releases (`rlcd-gateway`). |
| Requirements | macOS/Linux/Windows binary; provider credentials as configured; optional Jev/open-rlcd backends. |
| License | [Apache-2.0](https://github.com/JimmyWesley/rlcd-gateway/blob/0541ab1887e36c8e3e8358567742a17f241bcb57/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live gateway not run. |

## When to use

Use for a **single local base URL** that prunes context and audits System One decisions. Prefer Jev Runway for Codex-only tool-output trimming.

## How it works

Clients point `ANTHROPIC_BASE_URL` / `OPENAI_BASE_URL` at the gateway; it proxies providers, prunes stale tool output, and offers a Jev-compatible `/v1/systemone` with logging/calibration (per README).

## Get started

```sh
npx rlcd-gateway
# ANTHROPIC_BASE_URL=http://127.0.0.1:4777 claude
```

Pin tip `0541ab1887e36c8e3e8358567742a17f241bcb57`.

## Examples and demos

- Dashboard at `http://127.0.0.1:4777/ui/` (when running).
- Release binaries for major platforms.

## Limits and data handling

Prompts and tool outputs pass through the gateway to configured providers. Decision audit logs stay local unless you export them.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 0541ab1](https://github.com/JimmyWesley/rlcd-gateway/tree/0541ab1887e36c8e3e8358567742a17f241bcb57). AI-assisted README inspection; live proxy not run.
