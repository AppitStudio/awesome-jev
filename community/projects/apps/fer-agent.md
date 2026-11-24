# Fer Agent by Fernando Villar Peláez (open-source agent company in your browser where a built-in JEV agent decides whether each costly step is worth it)

[All projects](../README.md) · [Web apps](README.md#web-apps)

An English/Spanish web and desktop app where your AI agents live in a building: floors are teams, a boss shares out the work, and agents have their own model, heartbeat and spending caps. A built-in JEV agent checks costly steps (a web search, a retry, a new agent) and decides go ahead, reuse, stop or ask the boss.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ferjovipe/fer-agent) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://feragent.netlify.app) |
| Pricing and access | Free MIT app (browser, Mac and Windows builds). Agents run on your own OpenRouter key or provider subscription; JEV calls go through OpenRouter's decisions API and are billed to that key. Checked 2026-11-24. |
| Jev evidence | [`engine.js`](https://github.com/Ferjovipe/fer-agent/blob/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b/engine.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ai_thehive/status/2125016351576322493)). |
| Maintainer | [Ferjovipe](https://github.com/Ferjovipe). Independently curated. |
| Format | JavaScript web app with Electron desktop builds |
| Platform and availability | Browser (hosted site or local), plus Mac and Windows desktop builds from GitHub Releases. |
| Jev's role | The JEV agent uses `~typesafe/jev-latest` through OpenRouter's decisions API to answer a Choice before spending steps and to pick the best of several answers; other agents use whatever text models you choose. |
| Requirements | An OpenRouter key with credit (or another provider key); JEV needs OpenRouter. |
| License | [MIT](https://github.com/Ferjovipe/fer-agent/blob/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b/LICENSE) |

## When to use

- Run a small team of agents with spending caps and a cheap JEV gate before expensive steps.
- Mismatch: if you need a tested Jev integration; the Spanish notes say the version 6 JEV decisions API had not yet been tried with a real key.

## How it works

`engine.js` defines `JEV_MODEL = "~typesafe/jev-latest"` and the built-in JEV agent, and sends state plus a go-ahead/reuse/stop/ask Choice to OpenRouter's decisions API before costly agent actions. Integration evidence: [`engine.js`](https://github.com/Ferjovipe/fer-agent/blob/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b/engine.js).

## Get started

Open the hosted site and paste your OpenRouter key in Settings, or download a desktop build from Releases.

```sh
git clone https://github.com/Ferjovipe/fer-agent.git && cd fer-agent
npm install
# or open https://feragent.netlify.app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted app: [feragent.netlify.app](https://feragent.netlify.app)
- Brand site: [aithehive.com](https://aithehive.com)
- Spanish notes: [github.com/Ferjovipe/fer-agent/blob/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b/LEEME.txt](https://github.com/Ferjovipe/fer-agent/blob/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b/LEEME.txt)

## Limits and data handling

Prompts and agent context go to OpenRouter and the model providers you pick. The "internet as you" desktop feature uses browser sessions you are signed into, so agents can act in those accounts. The maintainer's notes (LEEME.txt) say JEV's decisions API in version 6 was still untested with a real key.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 57e5c30d5510](https://github.com/Ferjovipe/fer-agent/tree/57e5c30d5510cfff5020dd1c283f8d02b5f6dc6b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
