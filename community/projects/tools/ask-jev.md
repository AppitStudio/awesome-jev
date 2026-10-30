# ask-jev (agent skill and zero-dependency runner for typed Jev decisions in Claude Code, Codex and other agents)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that tells a coding agent when and how to ask Jev for typed selections, labels, yes/no checks and scores instead of prompting and parsing text, with a Node.js runner that has no package dependencies. It can rank files and check claims, and works with TypeSafe, Jev on Cloudflare Workers AI or the Vercel AI Gateway. Includes a trigger-evaluation harness with saved results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justinramos101/ask-jev) |
| Maintainer | [justinramos101](https://github.com/justinramos101). Independently curated. |
| Format | Agent skill + Node.js runner |
| Requirements | Node.js 18+ and one of: a TypeSafe key, Cloudflare Workers AI credentials, or a Vercel AI Gateway key. |
| License | [MIT](https://github.com/justinramos101/ask-jev/blob/13eb58ba090e5df390533760c08a39c9af1fee45/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/ask-jev/scripts/ask-jev.mjs`](https://github.com/justinramos101/ask-jev/blob/13eb58ba090e5df390533760c08a39c9af1fee45/skills/ask-jev/scripts/ask-jev.mjs) at the pinned commit. |

## When to use

- Give a coding agent a cheap, typed way to make routing, classification and file-ranking calls.
- Mismatch: Jev does not read your workspace; the agent must assemble the state it sends.

## How it works

The skill workflow frames questions; `ask-jev.mjs` sends the request to the first configured provider and returns the typed answers and probabilities to the agent. Integration evidence: [`skills/ask-jev/scripts/ask-jev.mjs`](https://github.com/justinramos101/ask-jev/blob/13eb58ba090e5df390533760c08a39c9af1fee45/skills/ask-jev/scripts/ask-jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add justinramos101/ask-jev --skill ask-jev
export TYPESAFE_API_KEY=<your-key>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- CLI reference: [github.com/justinramos101/ask-jev/blob/13eb58ba090e5df390533760c08a39c9af1fee45/skills/ask-jev/references/cli.md](https://github.com/justinramos101/ask-jev/blob/13eb58ba090e5df390533760c08a39c9af1fee45/skills/ask-jev/references/cli.md)

## Limits and data handling

Text and file contents the agent puts in a request are sent to the chosen provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 13eb58ba090e](https://github.com/justinramos101/ask-jev/tree/13eb58ba090e5df390533760c08a39c9af1fee45). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
