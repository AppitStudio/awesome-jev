# jev-browser by MaciejWiatr (Claude Code browser control in background Chrome tabs, with Jev Ultrafast runs)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Claude Code plugin that gives Claude the Claude in Chrome tool set over the Chrome DevTools Protocol in background tabs of your real, signed-in Chrome, with a separate agent cursor, a human-like mouse mode, per-task tab groups and remembered site actions, plus an optional `jev_run` tool that hands a narrow goal to the Jev Ultrafast agent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MaciejWiatr/jev-browser) |
| Maintainer | [MaciejWiatr](https://github.com/MaciejWiatr). Independently curated. |
| Format | Claude Code plugin (Node.js, with a Python agent) |
| Requirements | Chrome or another Chromium browser, Claude Code, uv and Node 18+; for `jev_run` only, a TypeSafe API key and an OpenRouter (or Ollama) text-model key. |
| License | [MIT](https://github.com/MaciejWiatr/jev-browser/blob/fcee5259f4eeaa958b380a5e0a1695605db25a1f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`install.sh`](https://github.com/MaciejWiatr/jev-browser/blob/fcee5259f4eeaa958b380a5e0a1695605db25a1f/install.sh) at the pinned commit. |

## When to use

- Let Claude Code use your logged-in Chrome without stealing focus or your mouse.
- Finish short, well-defined browser goals in a few seconds with `jev_run`.
- Mismatch: Jev is used only by the optional `jev_run` agent; the step-by-step tools do not need it. Distinct from the separately listed Jev Ultrafast.

## How it works

`install.sh` clones browser-use's Jev Ultrafast into `~/.jev/jev-ultrafast` and tells you to add `TYPESAFE_API_KEY` there; `jev_run` then lets that agent choose browser actions with Jev while a text model handles reading, and the plugin's own CDP tools do the rest. Integration evidence: [`install.sh`](https://github.com/MaciejWiatr/jev-browser/blob/fcee5259f4eeaa958b380a5e0a1695605db25a1f/install.sh).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/MaciejWiatr/jev-browser/main/install.sh | bash
# enable chrome://inspect/#remote-debugging, then (optional) add TYPESAFE_API_KEY and TEXT_MODEL_API_KEY to ~/.jev/jev-ultrafast/.env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and demo: [github.com/MaciejWiatr/jev-browser#readme](https://github.com/MaciejWiatr/jev-browser#readme)

## Limits and data handling

The plugin acts in your real Chrome profile and stops at login pages and CAPTCHAs. With `jev_run`, page state goes to TypeSafe and to your text-model provider. Speed figures are the author's.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit fcee5259f4ee](https://github.com/MaciejWiatr/jev-browser/tree/fcee5259f4eeaa958b380a5e0a1695605db25a1f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
