# Agent Stack by JavierBertolino (multi-agent delivery workflow for Codex, Claude Code, Cursor and OpenCode, with Jev-judged web and mobile QA)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable workflow that turns an issue into a governed path (resolver, designer, OpenSpec, developer, design QA, PR) and installs it into a project for Codex, Claude Code, Cursor or OpenCode with `astack init`. Its standalone `web-qa` (browser MCP) and `mobile-qa` (Maestro MCP) agents use Jev twice per checkpoint: to pick the next action from a closed candidate set the agent built from what it observed, and to return verdicts across functional, view and business-rule checks. Jev never drives the browser or device itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JavierBertolino/agent-stack) |
| Maintainer | [JavierBertolino](https://github.com/JavierBertolino). Independently curated. |
| Format | npm CLI and agent skills (`agent-stack`, MIT) |
| Requirements | Node.js 18+, a supported coding agent, and for Jev QA a TypeSafe key (or Vercel AI Gateway / custom gateway) set with `astack auth jev`. |
| License | [MIT](https://github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/jbetook/status/2122536345599930689)). |
| Jev evidence | [`.agent-stack/resources/web-qa/ask-jev.ts`](https://github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/.agent-stack/resources/web-qa/ask-jev.ts) at the pinned commit. |

## When to use

- Add browser and mobile QA agents whose next steps and verdicts come from typed Jev answers.
- Mismatch: a hosted QA service; it runs inside your coding agent.

## How it works

`.agent-stack/resources/web-qa/ask-jev.ts` sends the checkpoint state and `next_action` / verdict questions to Jev (`https://api.typesafe.ai/v1/systemone`, `jev-latest`, or a configured gateway); `docs/jev.md` documents the questions. Integration evidence: [`.agent-stack/resources/web-qa/ask-jev.ts`](https://github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/.agent-stack/resources/web-qa/ask-jev.ts).

## Get started

Initialise a project, then configure the Jev QA provider.

```sh
cd my-project
npx agent-stack init
astack auth jev --provider=typesafe   # stores the key at user level, never in the repo
astack doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev QA design: [github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/docs/jev.md](https://github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/docs/jev.md)
- README: [github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/README.md](https://github.com/JavierBertolino/agent-stack/blob/62d90f1404b2cb69ba8736aa44c90fddd740011f/README.md)

## Limits and data handling

Compressed checkpoint text goes to TypeSafe (or the chosen gateway) on your key; credentials stay at user level. Jev QA is off (`JEV_PROVIDER=none`) until configured.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 62d90f1404b2](https://github.com/JavierBertolino/agent-stack/tree/62d90f1404b2cb69ba8736aa44c90fddd740011f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
