# Jev Assistant by jbellsolutions (Mac voice assistant that works in Chrome, on your Mac and in cloud browsers)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Voice assistant preview for Apple Silicon Macs: LiveKit with GPT-Live 1 handles conversation, GPT-6 Luna does reasoning and task execution, and Jev makes the fast judgments (routing, next actions and checks) for tasks in your Chrome, on your Mac, in a Browser Use cloud browser or on an optional Orgo computer, with approvals before sends and changes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jbellsolutions/jev-assistant) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://github.com/jbellsolutions/jev-assistant/releases/tag/v1.0.0-preview.1) |
| Pricing and access | Open source (MIT); the preview installer is a free download. OpenAI, LiveKit, TypeSafe, Browser Use and optional Orgo/Composio usage is billed by those providers. Checked 2026-10-27. |
| Jev evidence | [`server/assistant/router.ts`](https://github.com/jbellsolutions/jev-assistant/blob/6752634bd4935a6d9bd95f9ba3377dac661992e8/server/assistant/router.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jbellsolutions](https://github.com/jbellsolutions). Independently curated. |
| Format | macOS app (.pkg installer) with Chrome extension |
| Platform and availability | macOS 15+ on Apple Silicon; unsigned preview installer. |
| Jev's role | Fast judge: routes requests and makes yes/no and choice checks during tasks, alongside the reasoning model. |
| Requirements | Apple Silicon Mac on macOS 15+; your own OpenAI, LiveKit, TypeSafe and Browser Use connections; Orgo and Composio optional. |
| License | [MIT](https://github.com/jbellsolutions/jev-assistant/blob/6752634bd4935a6d9bd95f9ba3377dac661992e8/LICENSE) |

## When to use

- Hand multi-step browser and Mac tasks to a voice assistant with saved progress and approvals.
- Mismatch: Phase 1 unsigned preview; several paid provider accounts are required.

## How it works

`server/assistant/router.ts` uses `@typesafe-ai/sdk` Choice questions to route each request; `core/decide.ts` and `core/verify.ts` ask Noul and Choice questions to pick and check actions. Integration evidence: [`server/assistant/router.ts`](https://github.com/jbellsolutions/jev-assistant/blob/6752634bd4935a6d9bd95f9ba3377dac661992e8/server/assistant/router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# download the .pkg from the v1.0.0-preview.1 release and follow docs/start-here.md
# developers: npm ci && npx playwright install chromium
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Start here: [github.com/jbellsolutions/jev-assistant/blob/main/docs/start-here.md](https://github.com/jbellsolutions/jev-assistant/blob/main/docs/start-here.md)
- README: [github.com/jbellsolutions/jev-assistant#readme](https://github.com/jbellsolutions/jev-assistant#readme)

## Limits and data handling

Task context, page state and voice transcripts go to the configured providers, including TypeSafe for judgments. The assistant can act in your signed-in Chrome; the installer is unsigned.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 6752634bd493](https://github.com/jbellsolutions/jev-assistant/tree/6752634bd4935a6d9bd95f9ba3377dac661992e8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
