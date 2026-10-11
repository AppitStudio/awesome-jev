# opencode-jev-pre-llm

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 plugin that captures each user prompt, asks TypeSafe Jev whether it is deterministic, and if so injects a `[JEV PRE-ANALYSIS]` block with temperature 0 so the LLM answers directly; otherwise reasoning proceeds normally.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/murilogteixeira/opencode-jev-pre-llm) |
| Maintainer | [murilogteixeira](https://github.com/murilogteixeira). Independently curated. |
| Format | OpenCode V2 plugin |
| Requirements | Node.js 18+; OpenCode V2; TypeSafe API key. |
| License | [MIT](https://github.com/murilogteixeira/opencode-jev-pre-llm/blob/bbe16aef162eec2b5a37c94ef1924aa86b8fd1ff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Trim unnecessary reasoning on simple, deterministic coding-agent prompts.
- Mismatch: Young project; prompt text is sent to the hosted Jev API.

## How it works

A pre-LLM hook sends the prompt to the System One API (`jev-latest` by default); if Jev is unavailable the plugin fails open. (Summarized from the upstream [README](https://github.com/murilogteixeira/opencode-jev-pre-llm/blob/bbe16aef162eec2b5a37c94ef1924aa86b8fd1ff/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `opencode plugin add github:murilogteixeira/opencode-jev-pre-llm` and set `JEV_API_KEY`.

## Limits and data handling

Prompts are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit bbe16aef162e](https://github.com/murilogteixeira/opencode-jev-pre-llm/tree/bbe16aef162eec2b5a37c94ef1924aa86b8fd1ff). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
