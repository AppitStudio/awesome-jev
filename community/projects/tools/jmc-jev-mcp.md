# jmc-jev-mcp

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server that judges JDK Flight Recorder recordings with TypeSafe Jev / Laya typed questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/thegreystone/jmc-jev-mcp) |
| Maintainer | [thegreystone](https://github.com/thegreystone). Independently curated. |
| Format | Java · MCP server for JFR (MIT) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`MIT`](https://github.com/thegreystone/jmc-jev-mcp/blob/4587fae6116723ab0e88997398268cdadef09f7a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

MCP server that judges JDK Flight Recorder recordings with TypeSafe Jev / Laya typed questions. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/thegreystone/jmc-jev-mcp.git
cd jmc-jev-mcp
git checkout 4587fae6116723ab0e88997398268cdadef09f7a
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: JevClient.java + JudgmentTools.java call TypeSafe Jev over JFR metrics. ([upstream evidence](https://github.com/thegreystone/jmc-jev-mcp/blob/4587fae6116723ab0e88997398268cdadef09f7a/src/main/java/se/hirt/jmc/jevmcp/JevClient.java)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 4587fae61167](https://github.com/thegreystone/jmc-jev-mcp/tree/4587fae6116723ab0e88997398268cdadef09f7a). AI-assisted README and license inspection; install/live paths not executed.
