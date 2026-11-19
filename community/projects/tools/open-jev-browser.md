# open-jev-browser by Kekeu-u (local panel and Chrome extension that runs Portuguese-language browser tasks with Jev choosing each click)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser automation driven by plain commands in Portuguese, with Jev (direct or via OpenRouter) choosing each click. Two separate modes: a local web panel that runs tasks in an isolated Chromium without your logins, streaming each step and a live screenshot, and a Chrome extension for tasks in your real, signed-in browser. Built on a patched fork of jkudish's jev-browser CLI (MIT), with pacing presets, a private-network block and a run history. Interface and docs are in Brazilian Portuguese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kekeu-u/open-jev-browser) |
| Maintainer | [Kekeu-u](https://github.com/Kekeu-u). Independently curated. |
| Format | Node.js CLI, local web panel and Chrome extension |
| Requirements | Node.js 22+ on Windows, macOS or Linux, Chrome or Chromium, and an OpenRouter key or `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Kekeu-u/open-jev-browser/blob/39fc8b26927159689472434e40fb376aeae81560/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-browser/src/questions.ts`](https://github.com/Kekeu-u/open-jev-browser/blob/39fc8b26927159689472434e40fb376aeae81560/jev-browser/src/questions.ts) at the pinned commit. |

## When to use

- Give Portuguese-language browser tasks to Jev from a local panel, or in your own Chrome session.
- Mismatch: an English-first or production automation tool; the author calls it a learning project, not a product.

## How it works

The bundled `jev-browser` fork asks Jev typed `choice` and `noul` questions built in `jev-browser/src/questions.ts` with `@typesafe-ai/sdk`; `front/server.js` picks TypeSafe or OpenRouter from the key you saved and runs the CLI with step events. Integration evidence: [`jev-browser/src/questions.ts`](https://github.com/Kekeu-u/open-jev-browser/blob/39fc8b26927159689472434e40fb376aeae81560/jev-browser/src/questions.ts).

## Get started

Run the installer script, add your key, and start the panel from the desktop icon or the CLI.

```sh
git clone https://github.com/Kekeu-u/open-jev-browser && cd open-jev-browser
node jev.mjs tudo    # install everything
node jev.mjs start   # start the service and open the panel
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Kekeu-u/open-jev-browser/blob/39fc8b26927159689472434e40fb376aeae81560/README.md](https://github.com/Kekeu-u/open-jev-browser/blob/39fc8b26927159689472434e40fb376aeae81560/README.md)
- Upstream CLI listing: [jevlist.ai/projects/jkudish-jev-agent-tools](https://jevlist.ai/projects/jkudish-jev-agent-tools)

## Limits and data handling

Page content and your task text go to OpenRouter or TypeSafe on your key. The extension mode acts inside your real logged-in Chrome, so use it only on sites and accounts you control. The author notes it is a personal test project, used at your own risk.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 39fc8b269271](https://github.com/Kekeu-u/open-jev-browser/tree/39fc8b26927159689472434e40fb376aeae81560). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
