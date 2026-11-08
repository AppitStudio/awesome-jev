# AI Security Crew (MCP security review plus an asc-guard hook that asks TypeSafe Jev before agent tool calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Security tooling for AI coding agents: an MCP security reviewer and `asc-guard`, a Claude Code hook that asks Jev four narrow questions before each tool call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Srajangpt1/ai-security-crew) |
| Maintainer | [Srajangpt1](https://github.com/Srajangpt1). Independently curated. |
| Format | Python MCP server + Claude Code hooks (MIT) |
| Requirements | Python/uvx, Claude Code, and `TYPESAFE_API_KEY` for the guard. |
| License | [MIT](https://github.com/Srajangpt1/ai-security-crew/blob/0e1390b0b18b4b36e085fd5995fb255c5885d448/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/mcp_security_review/guard/jev.py`](https://github.com/Srajangpt1/ai-security-crew/blob/0e1390b0b18b4b36e085fd5995fb255c5885d448/src/mcp_security_review/guard/jev.py) at the pinned commit. |

## When to use

- Gate shell, network and MCP calls of coding agents.
- Benchmark the guard against agent-guard-bench cases.
- Mismatch: fail-open when Jev is unreachable.

## How it works

`guard/jev.py` sends the pending tool call to Jev; `guard/engine.py` turns answers into allow/ask. Without a key the hook exits immediately, and if Jev is unreachable it steps aside to normal permissions. Integration evidence: [`src/mcp_security_review/guard/jev.py`](https://github.com/Srajangpt1/ai-security-crew/blob/0e1390b0b18b4b36e085fd5995fb255c5885d448/src/mcp_security_review/guard/jev.py).

## Get started

Install per README and add `TYPESAFE_API_KEY`; the guard hooks register with Claude Code.

```sh
git clone https://github.com/Srajangpt1/ai-security-crew.git && cd ai-security-crew
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Srajangpt1/ai-security-crew/blob/0e1390b0b18b4b36e085fd5995fb255c5885d448/README.md](https://github.com/Srajangpt1/ai-security-crew/blob/0e1390b0b18b4b36e085fd5995fb255c5885d448/README.md)

## Limits and data handling

Tool-call details go to TypeSafe on every guarded call.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 0e1390b0b18b](https://github.com/Srajangpt1/ai-security-crew/tree/0e1390b0b18b4b36e085fd5995fb255c5885d448). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
