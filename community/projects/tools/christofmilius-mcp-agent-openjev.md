# mcp-agent-openjev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local OpenJev Choice/Noul/Score decision service for agents via MCP + CLI (LM Studio logprobs; not TypeSafe-hosted).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChristofMilius/mcp-agent-openjev) |
| Maintainer | [ChristofMilius](https://github.com/ChristofMilius). Independently curated. |
| Format | Python · MCP/CLI OpenJev service (MIT) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`MIT`](https://github.com/ChristofMilius/mcp-agent-openjev/blob/162bd0efdb34709b5ebd4b08ed566c25373a603b/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Local OpenJev Choice/Noul/Score decision service for agents via MCP + CLI (LM Studio logprobs; not TypeSafe-hosted). Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/ChristofMilius/mcp-agent-openjev.git
cd mcp-agent-openjev
git checkout 162bd0efdb34709b5ebd4b08ed566c25373a603b
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: src/mcp_agent_openjev/openjev.py + mcp_server.py implement local typed decisions. ([upstream evidence](https://github.com/ChristofMilius/mcp-agent-openjev/blob/162bd0efdb34709b5ebd4b08ed566c25373a603b/src/mcp_agent_openjev/openjev.py)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 162bd0efdb34](https://github.com/ChristofMilius/mcp-agent-openjev/tree/162bd0efdb34709b5ebd4b08ed566c25373a603b). AI-assisted README and license inspection; install/live paths not executed.
