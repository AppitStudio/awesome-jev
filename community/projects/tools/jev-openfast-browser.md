# JEV OpenFast Browser

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Local chat-driven browser agent built on Jev Ultrafast: Jev (via OpenRouter) picks each operation and target from a numbered element table in a real Chrome tab, checks results before reporting success, and hands over for logins or CAPTCHAs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samuelyossef/jev-openfast) |
| Maintainer | [samuelyossef](https://github.com/samuelyossef). Independently curated. |
| Format | Python app (`uv`) with local chat UI (beta) |
| Requirements | Python 3.12+, `uv`, Chrome with remote debugging; OpenRouter key (paid) with a spending limit. |
| License | [MIT](https://github.com/samuelyossef/jev-openfast/blob/dd6c9954ec0ed582ee8ce614d840de03d9e6bf0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_ultrafast/model.py`](https://github.com/samuelyossef/jev-openfast/blob/dd6c9954ec0ed582ee8ce614d840de03d9e6bf0f/jev_ultrafast/model.py) at the pinned commit. |

## When to use

- Ask for a browsing task in chat and watch Jev drive a real tab step by step.
- Study verification and human handoff added on top of the Ultrafast decision loop.
- Mismatch: builds on the already-listed browser-use/jev-ultrafast; Windows is the primary tested platform.

## How it works

Each page becomes a numbered element table; Jev returns an operation (`CLICK`, `TYPE_TEXT`, `SCROLL_DOWN`, `DONE`, `BLOCKED` ...) and a target from that table, code executes it through Browser Harness, and a small text model writes words only for `TYPE_TEXT`. Integration evidence: [`jev_ultrafast/model.py`](https://github.com/samuelyossef/jev-openfast/blob/dd6c9954ec0ed582ee8ce614d840de03d9e6bf0f/jev_ultrafast/model.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/samuelyossef/jev-openfast.git && cd jev-openfast
uv sync
uv run --env-file .env jev   # open http://127.0.0.1:8766
uv run jev --doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Library use and limits sections in the README.

## Limits and data handling

Page element tables and your task go to OpenRouter (Jev and the text model) on your key; it drives your real browser, so supervise it.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit dd6c9954ec0e](https://github.com/samuelyossef/jev-openfast/tree/dd6c9954ec0ed582ee8ce614d840de03d9e6bf0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
