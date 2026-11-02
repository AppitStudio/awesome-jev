# jev-prompt-grader (Claude Code plugin that grades every prompt with Jev through Composio and rewrites weak ones)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that sends each prompt to Jev through the Composio MCP server, grades it from Excellent to Horrible and, when it is not Excellent, rewrites it using the conversation as context. The same repo has a jev-grader skill for the Claude app.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rodrigofaerman/skills) |
| Maintainer | [rodrigofaerman](https://github.com/rodrigofaerman). Independently curated. |
| Format | Claude Code plugin + Claude skill |
| Requirements | Claude Code (hooks early access); an MCP server named `Composio` with the `jev` toolkit connected. |
| License | [MIT](https://github.com/rodrigofaerman/skills/blob/ce9d0d12014299b0440abd0286c1b85f6dbdfd1f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev-prompt-grader/hooks/register.tsx`](https://github.com/rodrigofaerman/skills/blob/ce9d0d12014299b0440abd0286c1b85f6dbdfd1f/plugins/jev-prompt-grader/hooks/register.tsx) at the pinned commit. |

## When to use

- Get a quick quality check and a better version of your prompts before Claude runs them.
- Mismatch: depends on Composio's Jev toolkit rather than a direct TypeSafe key.

## How it works

`plugins/jev-prompt-grader/hooks/register.tsx` calls Composio's `JEV_EVALUATE_STATE` tool (`jev-latest`) with two choice questions on each prompt, shows the grade in a band and pane, and triggers the rewrite when needed. Integration evidence: [`plugins/jev-prompt-grader/hooks/register.tsx`](https://github.com/rodrigofaerman/skills/blob/ce9d0d12014299b0440abd0286c1b85f6dbdfd1f/plugins/jev-prompt-grader/hooks/register.tsx).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin install jev-prompt-grader --marketplace rodrigofaerman/skills
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plugin README: [github.com/rodrigofaerman/skills/tree/main/plugins/jev-prompt-grader](https://github.com/rodrigofaerman/skills/tree/main/plugins/jev-prompt-grader)

## Limits and data handling

Each prompt (up to 8,000 characters) goes to Jev through Composio. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit ce9d0d120142](https://github.com/rodrigofaerman/skills/tree/ce9d0d12014299b0440abd0286c1b85f6dbdfd1f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
