# open-computer-use by MAX LIN (background computer use for Mac apps via the accessibility tree, with Jev as an optional decision backend)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Lets agents use your Mac's apps in the background while you keep using yours: no screenshots, no pointer, no app brought to the front. A Swift bridge reads the macOS accessibility tree into a numbered table of controls and acts on one of them through `AXPress`, `AXValue` and keys sent to the app's process, re-checking the UI before every input and executing each decision at most once. A coding agent (Claude Code, Codex) can drive it through the CLI with no model backend, or the built-in agent can take a goal and ask a decision backend one request per step. With Jev as that backend, the operation, its target and a risk rating are asked as typed choice and score questions instead of JSON.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/max1874/open-computer-use) |
| Maintainer | [max1874](https://github.com/max1874). Independently curated. |
| Format | Python CLI and agent with a Swift bridge, macOS only (MIT) |
| Requirements | macOS, Python 3.11+, uv, Xcode Command Line Tools and Accessibility permission; `JEV_API_KEY` only if you pick Jev for the built-in agent (a text model is still needed to write field values). |
| License | [MIT](https://github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`open_computer_use/model.py`](https://github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/open_computer_use/model.py) at the pinned commit. |

## When to use

- Let an agent operate a Mac app without taking over your screen, with Jev choosing the operation and target.
- Mismatch: canvas apps without accessibility controls, or Windows and Linux.

## How it works

`open_computer_use/model.py` (`ask_jev`) posts the observed state and named choice/score questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (overridable with `JEV_BASE_URL` and `JEV_MODEL`); other backends use an OpenAI-compatible chat API. Integration evidence: [`open_computer_use/model.py`](https://github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/open_computer_use/model.py).

## Get started

Install the CLI, grant Accessibility permission, then drive it from a coding agent or give the built-in agent a goal with Jev configured in `.env`.

```sh
curl -fsSL https://raw.githubusercontent.com/max1874/open-computer-use/main/install.sh | sh
open-computer-use status
# built-in agent with Jev: set JEV_API_KEY (and TEXT_MODEL_* for text) in .env, then
uv sync --extra agent && uv run --extra agent --env-file .env python examples/run.py --app TextEdit --goal '...'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/README.md](https://github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/README.md)
- Design notes: [github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/DESIGN.md](https://github.com/max1874/open-computer-use/blob/eee7dc2c64c0dfb48f032b564bc45a20e12281a1/DESIGN.md)

## Limits and data handling

The accessibility contents of the target app's window are sent to the chosen decision backend. Secure fields are classified first and their values omitted. Jev is optional; the coding-agent path uses no API key at all. Portions are derived from Browser Use's jev-ultrafast (credited in the license).

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit eee7dc2c64c0](https://github.com/max1874/open-computer-use/tree/eee7dc2c64c0dfb48f032b564bc45a20e12281a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
