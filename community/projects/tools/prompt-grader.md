# prompt-grader by David Hutcheson (Claude Code plugin where Jev grades how each session's first prompt opened)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Claude Code plugin that waits until Claude's first file edit (or the end of the first turn), then sends one request to Jev on OpenRouter that answers a fixed set of yes/no checks taken from Anthropic's prompting guides plus an overall grade. A side panel shows the grade, up to three gaps, and your prompt rewritten with a bracketed question for each gap. No Claude tokens are spent on grading.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/starskythehutch/prompt-grader) |
| Maintainer | [starskythehutch](https://github.com/starskythehutch). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | The latest Claude Code and an OpenRouter API key with a little credit. |
| License | [MIT](https://github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/jev.ts`](https://github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/hooks/jev.ts) at the pinned commit. |

## When to use

- Get quick feedback on whether your opening prompt told Claude enough, while you can still restart the session.
- Mismatch: grading later prompts or resumed sessions; only the first prompt of a new session is graded.

## How it works

`hooks/jev.ts` builds one request to OpenRouter's decisions endpoint (`https://openrouter.ai/api/alpha/decisions`, model `~typesafe/jev-latest`) from the first prompt, the model and effort, the skills and tools used and Claude's plan, and turns the answers into a grade; the checks and their sources are in `hooks/rubric-checks.ts`. Integration evidence: [`hooks/jev.ts`](https://github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/hooks/jev.ts).

## Get started

Install from the plugin's marketplace, then give it your OpenRouter key with `/plugin configure prompt-grader@prompt-grader` and restart Claude Code.

```sh
claude plugin install prompt-grader --marketplace starskythehutch/prompt-grader
# in a session: /plugin configure prompt-grader@prompt-grader  (paste OPENROUTER_API_KEY)
# reopen the panel any time: /prompt-grader
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: [github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/docs/mod-design.md](https://github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/docs/mod-design.md)
- Rubric checks with their sources: [github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/hooks/rubric-checks.ts](https://github.com/starskythehutch/prompt-grader/blob/c149eb0260e6a74230c207e4bc3309c29f044b5e/hooks/rubric-checks.ts)

## Limits and data handling

For each graded session OpenRouter and TypeSafe receive your first prompt, the model and effort, the names and descriptions of skills, connectors and memory files used, and Claude's plan text; tool arguments, results and file contents are not sent. The author's cost and latency figures were measured on 2026-11-22 against `jev-1.14-20261014`. End a prompt with `//raw` or set Mode to `off` to skip grading.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit c149eb0260e6](https://github.com/starskythehutch/prompt-grader/tree/c149eb0260e6a74230c207e4bc3309c29f044b5e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
