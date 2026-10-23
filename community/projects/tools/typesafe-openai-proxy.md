# Typesafe routing proxy (decision fast path for Home Assistant voice)

[All projects](../README.md) · [Home automation](README.md#home-automation)

OpenAI-compatible proxy that sits behind the hass_local_openai_llm Home Assistant integration: one System One decision per request turns clear commands and state questions into Home Assistant tool calls, asks before risky actions, and forwards everything else unchanged to your LLM server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ksmarty/typesafe-openai-proxy) |
| Maintainer | [ksmarty](https://github.com/ksmarty). Independently curated. |
| Format | TypeScript server (Docker image or Node.js) |
| Requirements | Home Assistant with hass_local_openai_llm; an OpenAI-compatible LLM server; a System One endpoint (Jev via Ollama or a hosted API) or the offline heuristic backend. |
| License | [MIT](https://github.com/ksmarty/typesafe-openai-proxy/blob/290d50855a83e4800402eaf81a18c3cb261a5b49/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone.ts`](https://github.com/ksmarty/typesafe-openai-proxy/blob/290d50855a83e4800402eaf81a18c3cb261a5b49/src/systemone.ts) at the pinned commit. |

## When to use

- Make simple voice commands fast without replacing your Home Assistant conversation agent.
- Confirm before unlock, open or disarm actions.
- Mismatch: needs a decision backend configured; none is set out of the box.

## How it works

`src/systemone.ts` posts `{model, state, questions}` to `{baseUrl}/v1/systemone`; default thresholds are ported from the typesafe-conversation-agent reference and fitted to `jev-1.13.0`, and uncertain requests fall through verbatim. Integration evidence: [`src/systemone.ts`](https://github.com/ksmarty/typesafe-openai-proxy/blob/290d50855a83e4800402eaf81a18c3cb261a5b49/src/systemone.ts).

## Get started

From the upstream README after cloning the repository (not run on the review host):

```sh
docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Reference project it adapts: [github.com/the-sof/home-assistant-typesafe-conversation-agent](https://github.com/the-sof/home-assistant-typesafe-conversation-agent)

## Limits and data handling

Spoken requests and device context go to the configured decision server.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 290d50855a83](https://github.com/ksmarty/typesafe-openai-proxy/tree/290d50855a83e4800402eaf81a18c3cb261a5b49). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
