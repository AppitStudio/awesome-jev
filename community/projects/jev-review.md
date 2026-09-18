# Jev Review

[All projects](../README.md) · [Developer tools](../README.md#developer-tools)

Give a coding agent structured, experimental feedback on separate software-quality dimensions while it works.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NiazMorshed2007/jev-review) |
| Maintainer | [NiazMorshed2007](https://github.com/NiazMorshed2007). Independent community project. |
| Format | Local MCP server for a compatible coding agent. |
| Requirements | Node.js 20+, an MCP-capable client, and a TypeSafe key configured as `JEV_API_KEY`. |
| License | [MIT](https://github.com/NiazMorshed2007/jev-review/blob/main/LICENSE). |

## When to use

- You want a coding agent to compare quality signals before and after a focused change.
- You want to inspect separate dimensions such as readability, modularity, and testing rather than one blended score.
- You are exploring how typed judgments can participate in an agent's review loop.

Treat the results as experimental signals. They do not replace tests, code review, or security analysis.

## How it works

The agent supplies a task, diff, or selected file content to `jev_review`. The server asks Jev for rubric judgments and returns structured metrics and optional comparisons. It does not automatically discover repository files. The agent must interpret the result and decide what to change; Jev does not generate a root-cause explanation. See the [evaluation code](https://github.com/NiazMorshed2007/jev-review/tree/57690af54ef7d862c2483342c1e61c14dffcf727/src/evaluation).

## Get started

Configure `JEV_API_KEY` through your client's private environment, then follow the upstream [client setup](https://github.com/NiazMorshed2007/jev-review#client-setup). Its portable installation command is:

```sh
npx plugins add NiazMorshed2007/jev-review
```

Choose the supported client, restart it, and verify the MCP connection using that client's instructions. Manual setup is also documented. This installs upstream code; actually invoking a review sends supplied context to TypeSafe and can incur charges.

An example first request after setup:

```text
Use jev-review on this focused diff. Explain which dimensions need attention,
inspect the code to understand why, and keep the test results alongside the scores.
```

## Examples and demos

- [Demo video](https://github.com/NiazMorshed2007/jev-review#demo).
- [Tool inputs and output](https://github.com/NiazMorshed2007/jev-review#mcp-tool).
- [Quality dimensions](https://github.com/NiazMorshed2007/jev-review#quality-dimensions).
- [Agent skill](https://github.com/NiazMorshed2007/jev-review/blob/main/skills/jev-review/SKILL.md) — the upstream review workflow.

## Limits and data handling

The server runs locally, but the task, diff, files, and context you supply leave the machine for TypeSafe. Keep secrets and unrelated content out of review input. A previous evaluation is compared locally. The [key loader](https://github.com/NiazMorshed2007/jev-review/blob/57690af54ef7d862c2483342c1e61c14dffcf727/src/config/environment.ts) expects `JEV_API_KEY`, which differs from the official SDK variable. See the [upstream privacy notes](https://github.com/NiazMorshed2007/jev-review#security-and-privacy).

## Review and maintenance

Documentation was rechecked on 2026-09-19 at [57690af](https://github.com/NiazMorshed2007/jev-review/tree/57690af54ef7d862c2483342c1e61c14dffcf727). The catalog's 2026-09-18 review passed 13 mocked tests, typecheck, and build on Node.js 22. Plugin installation and live inference were not tested; quality on real code was not evaluated. See [validation scope](../../docs/validation.md#community-project-checks).

Related: [quality-rubric example](../../examples/quality-rubric/README.md) for the simpler scoring pattern.
