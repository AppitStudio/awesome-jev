# optim-jev (token savings for Claude Code and Codex)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin with three Jev-powered optimizers for long agent sessions: a compacter that drops stale tool calls instead of summarizing the whole chat, a router that sends each file edit to the right model by project rules, and a skill filter that sends only relevant skills per prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Oqura-ai/optim-jev) |
| Maintainer | [Oqura-ai](https://github.com/Oqura-ai). Independently curated. |
| Format | Claude Code plugin and Codex plugin (TypeScript hooks, Python) |
| Requirements | Claude Code with plugin support (or Codex for the router), Python 3.10+, a TypeSafe API key. |
| License | [MIT](https://github.com/Oqura-ai/optim-jev/blob/d839fb3e3b3ffb1e72645d7225d19555e7ed276e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/optim-jev.ts`](https://github.com/Oqura-ai/optim-jev/blob/d839fb3e3b3ffb1e72645d7225d19555e7ed276e/hooks/optim-jev.ts) at the pinned commit. |

## When to use

- Keep long Claude Code sessions cheaper without changing how you work.
- Let a smaller model handle edits your project rules say it can, such as tests.
- Mismatch: measured cost reports are Claude-only; Codex gets the router and an off-by-default advisory skills mode.

## How it works

Hooks in `hooks/optim-jev.ts` read the key from the plugin setting or `TYPESAFE_API_KEY` and bridge to Python tools that ask Jev which tool outputs are stale, which model fits an edit and which skills matter; each tool fails open if Jev is unavailable. Integration evidence: [`hooks/optim-jev.ts`](https://github.com/Oqura-ai/optim-jev/blob/d839fb3e3b3ffb1e72645d7225d19555e7ed276e/hooks/optim-jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Oqura-ai/optim-jev.git
claude plugin marketplace add ./optim-jev
claude plugin install optim-jev@optim-jev
export TYPESAFE_API_KEY=your-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tool guides: [github.com/Oqura-ai/optim-jev/tree/main/docs](https://github.com/Oqura-ai/optim-jev/tree/main/docs)
- Codex support: [github.com/Oqura-ai/optim-jev/blob/main/docs/codex.md](https://github.com/Oqura-ai/optim-jev/blob/main/docs/codex.md)

## Limits and data handling

Session snippets, prompts and edit context are sent to TypeSafe. Router and skills are off by default in Claude Code. Community project, not affiliated with TypeSafe or Anthropic.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit d839fb3e3b3f](https://github.com/Oqura-ai/optim-jev/tree/d839fb3e3b3ffb1e72645d7225d19555e7ed276e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
