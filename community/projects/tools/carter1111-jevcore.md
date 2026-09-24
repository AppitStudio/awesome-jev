# JevCore Agent

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Developer coding harness (`jevcoreagent` on npm) that turns a software request into TypeSafe Jev judgments—task classification, risk, execution mode, security review—then applies deterministic hard-policy overrides with MCP and CLI entrypoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/carter1111/jevcore) |
| Maintainer | [carter1111](https://github.com/carter1111). Independently curated. |
| Format | JavaScript/TypeScript npm package (`jevcoreagent`) with adapters and docs. |
| Requirements | Node.js; TypeSafe API key; host coding agent integration per SETUP.md. |
| License | [Apache-2.0](https://github.com/carter1111/jevcore/blob/5047ecb95b38129844c2aa3891e1dc61e435c10c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live harness sessions not run. Site jevcore.io not fully audited. |

## When to use

Use when you want a **reusable Jev decision layer** in front of coding agents with hard policy. Prefer [BoundedCode](boundedcode.md) / [agent-chaperone](agent-chaperone.md) for alternate supervisor/firewall shapes.

## How it works

CLI/MCP calls build typed Jev questions for classification and risk; Guard enforces deterministic denies; confidence-aware fallback documented upstream. Aliases include `jev-guard` pointing at the same CLI.

## Get started

```sh
npx jevcoreagent init
# or
git clone https://github.com/carter1111/jevcore.git
cd jevcore
git checkout 5047ecb95b38129844c2aa3891e1dc61e435c10c
# follow SETUP.md
```

## Examples and demos

- `Docs/` product and naming notes.
- `adapters/` integration surfaces.

## Limits and data handling

Prompts and diffs may reach TypeSafe. Trademark/NOTICE constraints apply—read upstream TRADEMARKS.md.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 5047ecb](https://github.com/carter1111/jevcore/tree/5047ecb95b38129844c2aa3891e1dc61e435c10c). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [BoundedCode](boundedcode.md), [agent-chaperone](agent-chaperone.md), [muratcakmak-jev-guard](muratcakmak-jev-guard.md).
