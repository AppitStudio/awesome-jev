# Open Intelligent UI (CopilotKit generative UI framework where TypeSafe Jev picks the renderer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CopilotKit's open-source generative UI app: before each user turn TypeSafe Jev chooses between A2UI tables and Open Generative UI charts/visuals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CopilotKit/OpenIntelligentUI) |
| Maintainer | [CopilotKit](https://github.com/CopilotKit). Independently curated. |
| Format | Python agent + React web app (MIT) |
| Requirements | Node, Python, an OpenAI key for the chat model and a TypeSafe API key for Jev routing. |
| License | [MIT](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/agent/src/visualization_router.py`](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/apps/agent/src/visualization_router.py) at the pinned commit. |

## When to use

- Let Jev decide how to present an answer (table vs chart).
- Study a production-style Jev router in a generative UI stack.
- Mismatch: needs both OpenAI and TypeSafe keys.

## How it works

`visualization_router.py` posts to `https://api.typesafe.ai/v1/systemone` (`JEV_MODEL=jev-latest`) to select the renderer and visualization; the chat itself runs on `chat-latest`. Integration evidence: [`apps/agent/src/visualization_router.py`](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/apps/agent/src/visualization_router.py).

## Get started

Run `make` setup per README, add `OPENAI_API_KEY` and `TYPESAFE_API_KEY` to `apps/agent/.env`, then start the dev servers.

```sh
git clone https://github.com/CopilotKit/OpenIntelligentUI.git && cd OpenIntelligentUI
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/README.md](https://github.com/CopilotKit/OpenIntelligentUI/blob/8391a94c1c3939c679e40ddd7bfc08a9ef690e70/README.md)

## Limits and data handling

Conversation context is sent to TypeSafe for routing and to OpenAI for chat.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 8391a94c1c39](https://github.com/CopilotKit/OpenIntelligentUI/tree/8391a94c1c3939c679e40ddd7bfc08a9ef690e70). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
