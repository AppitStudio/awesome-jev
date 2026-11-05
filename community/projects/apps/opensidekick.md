# OpenSidekick (MIT Chrome side-panel browser agent with optional beta Jev smart checks as a second opinion on risky actions)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Open-source Chrome side-panel agent that reads the page and clicks, types, navigates and works across tabs with any model you choose (OpenRouter, OpenAI, Claude, Gemini, Groq, local). Optional beta Smart checks use TypeSafe's Jev for yes/no safety verdicts and are off until you switch them on; Jev is used for those checks only, not as the chat model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/esterhuizen/opensidekick) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/esterhuizen/opensidekick#readme) (source-built; no separate product site verified). |
| Pricing and access | Free per the README (MIT, no account or telemetry); provider keys and usage are your own cost. Checked 2026-11-05. |
| Jev evidence | [`src/background/decisions.js`](https://github.com/esterhuizen/opensidekick/blob/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8/src/background/decisions.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [esterhuizen](https://github.com/esterhuizen). Independently curated. |
| Format | Chrome MV3 extension |
| Platform and availability | Chrome side-panel extension (source build / unpacked) |
| Jev's role | Optional Smart checks: typed yes/no safety verdicts before or after agent actions. |
| Requirements | Chrome, a chat-model key of your choice; Smart checks need an OpenRouter or TypeSafe key. |
| License | [MIT](https://github.com/esterhuizen/opensidekick/blob/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8/LICENSE) |

## When to use

- Get an inexpensive second opinion before a browser agent submits or navigates.
- Run a browser agent with your own model and keys.
- Mismatch: Jev is an optional beta feature of a general browser agent.

## How it works

`src/background/decisions.js` sends typed yes/no questions to the TypeSafe `/v1/systemone` endpoint (or via OpenRouter) and shows the verdicts in the side panel. Integration evidence: [`src/background/decisions.js`](https://github.com/esterhuizen/opensidekick/blob/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8/src/background/decisions.js).

## Get started

From the upstream README (not run on the review host):

```sh
# build from source or load unpacked per the README; then Settings → Smart checks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with Smart checks setup: [github.com/esterhuizen/opensidekick/blob/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8/README.md](https://github.com/esterhuizen/opensidekick/blob/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8/README.md)

## Limits and data handling

Page excerpts for Smart checks go to TypeSafe or OpenRouter on your key; browser agents can act on logged-in sites, so review actions. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 15bd3d232e95](https://github.com/esterhuizen/opensidekick/tree/15bd3d232e959e3f64741cc10bc2dc62b41d4fe8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
