# NewJev (browser and Windows desktop agent where Jev picks each action from the page or UI tree)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

A computer-use agent that reads the browser DOM or the Windows UI Automation tree instead of screenshots; a planner LLM splits the goal, Jev picks the operation and target with probabilities, a text LLM only fills values, and risky clicks, logins and CAPTCHAs are handed back to you. Completion is checked by a final Jev yes/no.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Royarind/NewJev) |
| Maintainer | [Royarind](https://github.com/Royarind). Independently curated. |
| Format | Python app (Playwright + Windows UIA) |
| Requirements | Python, Playwright Chromium; Windows for desktop control. An OpenRouter key (used for Jev and the LLMs) or a native TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/jev/client.py`](https://github.com/Royarind/NewJev/blob/d4474c68b8e14db45f6d4e249a24a656d3d3cdad/app/jev/client.py) at the pinned commit. |

## When to use

- Try a DOM/UI-tree computer-use agent that uses Jev for action choice instead of a vision model.
- Mismatch: unattended automation of sensitive accounts; it drives real mouse and keyboard input.

## How it works

`app/jev/client.py` posts to `https://api.typesafe.ai/v1/systemone` (or the OpenRouter route) with the page snapshot as state and the candidate operations as a choice; below the confidence threshold the agent re-observes, then asks you. Integration evidence: [`app/jev/client.py`](https://github.com/Royarind/NewJev/blob/d4474c68b8e14db45f6d4e249a24a656d3d3cdad/app/jev/client.py).

## Get started

Create a virtual environment, install, add your keys to `.env`, and run (see the README).

```sh
git clone https://github.com/Royarind/NewJev && cd NewJev
python -m venv .venv && .venv\Scripts\activate
pip install -e .
playwright install chromium
copy .env.example .env   # add OPENROUTER_API_KEY or TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Royarind/NewJev/blob/d4474c68b8e14db45f6d4e249a24a656d3d3cdad/README.md](https://github.com/Royarind/NewJev/blob/d4474c68b8e14db45f6d4e249a24a656d3d3cdad/README.md)

## Limits and data handling

Page and UI-tree text and your goal are sent to the configured providers. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit d4474c68b8e1](https://github.com/Royarind/NewJev/tree/d4474c68b8e14db45f6d4e249a24a656d3d3cdad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
