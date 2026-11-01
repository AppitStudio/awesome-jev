# Elefante (desktop multi-agent workspace with an API hub and browser harness, where Jev can route channel messages)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Electron workspace (bilingual English/Portuguese README) for running many AI agents on any engine, from OpenRouter, DeepSeek, Ollama, Groq, OpenAI and Anthropic to CLI harnesses such as Claude Code and Codex, with a native API hub and browser harness. Jev is an optional router that decides which agent takes a message.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vncsrmro/elefante) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/vncsrmro/elefante#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); you supply your own model and TypeSafe keys. Checked 2026-11-02. |
| Jev evidence | [`src/core/jev.ts`](https://github.com/vncsrmro/elefante/blob/fdffff7013e263489595829ac5c4a3036d2d751c/src/core/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [vncsrmro](https://github.com/vncsrmro). Independently curated. |
| Format | Electron desktop app (TypeScript/React) |
| Platform and availability | Windows, macOS and Linux (built from source). |
| Jev's role | Optional router that picks which agent takes a message. |
| Requirements | Windows, macOS or Linux; Node.js to build; your own provider keys and an optional TypeSafe key. |
| License | [Apache-2.0](https://github.com/vncsrmro/elefante/blob/fdffff7013e263489595829ac5c4a3036d2d751c/LICENSE) |

## When to use

- Run several agents side by side and let Jev pick who answers.
- Mismatch: Jev is optional and off unless chosen.

## How it works

`src/core/jev.ts` calls TypeSafe `/v1/systemone` as an optional router (`routerModel = 'jev'`) that answers which agent or agents should take a channel message, using the user's own key stored as `typesafe:key`. Integration evidence: [`src/core/jev.ts`](https://github.com/vncsrmro/elefante/blob/fdffff7013e263489595829ac5c4a3036d2d751c/src/core/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/vncsrmro/elefante.git && cd elefante
npm install
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/vncsrmro/elefante#readme](https://github.com/vncsrmro/elefante#readme)

## Limits and data handling

When Jev routing is on, each decision sends the channel's recent messages to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit fdffff7013e2](https://github.com/vncsrmro/elefante/tree/fdffff7013e263489595829ac5c4a3036d2d751c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
