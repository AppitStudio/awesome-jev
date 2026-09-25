# Flick (flick-computer-use)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Local stdio MCP computer-use server: agents hand Flick a goal, exact inputs, and completion conditions; TypeSafe Jev runs the observe→decide→act loop in Playwright (browser) or Swift Accessibility (macOS).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bgivenb/flick-computer-use) |
| Maintainer | [bgivenb](https://github.com/bgivenb). Independently curated. |
| Format | TypeScript MCP server (`computer_*` tools) + optional native macOS driver. |
| Requirements | Node.js 22+; `TYPESAFE_API_KEY`; Chromium via setup; Accessibility/Screen Recording for native macOS. |
| License | [MIT](https://github.com/bgivenb/flick-computer-use/blob/0ca67c380ca97106cc84de1925bb301277888e0a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use when an MCP coding agent should **delegate whole browser/macOS goals** with explicit until-conditions instead of driving every click itself.

## How it works

Host opens a session (`computer_open`), runs a goal (`computer_run` / `computer_execute`), polls status, and continues when Flick needs missing info. Jev chooses actions; screenshots can be interpreted by the host agent.

## Get started

```sh
git clone https://github.com/bgivenb/flick-computer-use.git
cd flick-computer-use
git checkout 0ca67c380ca97106cc84de1925bb301277888e0a
node scripts/setup-agent.mjs
# Set TYPESAFE_API_KEY in .env.local
npm run --silent mcp:config
npm run doctor
```

## Examples and demos

- INSTALL.md agent install prompt.
- `npm run test:live` smoke (live Jev; disposable local form).

## Limits and data handling

Goals, page text, and screenshots may leave the machine toward TypeSafe and any host vision model. Star-request text in the agent prompt is optional user-submitted wording, not an installer side effect.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 0ca67c3](https://github.com/bgivenb/flick-computer-use/tree/0ca67c380ca97106cc84de1925bb301277888e0a). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [macos-computer-use-kit](macos-computer-use-kit.md), [jev-browser-mcp (bothuany)](bothuany-jev-browser-mcp.md).
