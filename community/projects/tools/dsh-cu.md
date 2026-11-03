# dsh-cu (Windows computer use CLI for agents, with Jev as one of the brains that pick the next action)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Dependency-free Node CLI that lets agents read the Windows screen (UI Automation and OCR), click, type and open apps through one JSON action protocol, across monitors and in a background mode that never steals focus. Its `run` command can be driven by TypeSafe Jev, an OpenAI-compatible model, your DSH session's model, or no model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vit-cerny/dsh-cu) |
| Maintainer | [vit-cerny](https://github.com/vit-cerny). Independently curated. |
| Format | Node.js CLI (Windows) |
| Requirements | Windows 10 or 11, Node.js 18+, PowerShell 5.1; `TYPESAFE_API_KEY` to use Jev as the brain. |
| License | [MIT](https://github.com/vit-cerny/dsh-cu/blob/1b9935cee3790e7569f699931d3e2bc1de251696/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/dsh-cu.mjs`](https://github.com/vit-cerny/dsh-cu/blob/1b9935cee3790e7569f699931d3e2bc1de251696/bin/dsh-cu.mjs) at the pinned commit. |

## When to use

- Give a coding agent simple, scriptable control of Windows apps.
- Mismatch: Windows only; Jev is one of several optional brains.

## How it works

`bin/dsh-cu.mjs` defines a `typesafe` brain that posts the screen description and goal to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) to choose the next action; the same action protocol works with the other brains. Integration evidence: [`bin/dsh-cu.mjs`](https://github.com/vit-cerny/dsh-cu/blob/1b9935cee3790e7569f699931d3e2bc1de251696/bin/dsh-cu.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g vit-cerny/dsh-cu
dsh-cu start "notepad"
dsh-cu run "open notepad and type hello world into it"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Brain configuration: [github.com/vit-cerny/dsh-cu#readme](https://github.com/vit-cerny/dsh-cu#readme)

## Limits and data handling

With the Jev brain, screen text and your goal are sent to TypeSafe. The tool clicks and types on your desktop; review what you let it run. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 1b9935cee379](https://github.com/vit-cerny/dsh-cu/tree/1b9935cee3790e7569f699931d3e2bc1de251696). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
