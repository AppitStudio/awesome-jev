# Jev Bookmarks by kitepon (CLI that picks a starting page from your Chrome history, lets jev-ultrafast drive the browser and keeps only pages Jev judged useful)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Per-project address book for coding agents. Given a goal, it checks the project's saved bookmarks, then asks a Chrome extension for history matches; Jev picks a starting URL, jev-ultrafast operates a dedicated Chrome profile, and Jev judges whether the page reached was useful before saving it. Callable from Claude Code, Codex, Cursor and Grok Build through an installed skill. README in Japanese and English.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kitepon/jev-bookmarks) |
| Maintainer | [Quo / kitepon](https://github.com/kitepon). Independently curated. |
| Format | Python CLI + Chrome extension + agent skill |
| Requirements | Python 3.12, uv, Git, Google Chrome, a TypeSafe API key (or a `TYPESAFE_ANSWER_COMMAND` that holds it) and a working jev-ultrafast setup. |
| License | [MIT](https://github.com/kitepon/jev-bookmarks/blob/0f87410a8168254cb8a8208f16073fed91a7ffcd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_bookmarks/typesafe.py`](https://github.com/kitepon/jev-bookmarks/blob/0f87410a8168254cb8a8208f16073fed91a7ffcd/src/jev_bookmarks/typesafe.py) at the pinned commit. |

## When to use

- Agent users who keep sending the agent to the same sites and want it to remember which pages actually helped, per project.
- Mismatch: a general bookmark manager; it is built for agents and needs jev-ultrafast.

## How it works

`src/jev_bookmarks/typesafe.py` posts `choice` questions to `https://api.typesafe.ai/v1/systemone` (model `jev-latest`) to pick an entry URL from up to 80 history titles and to judge the observed page; it can instead pipe the request to a command so the key stays off the machine. Integration evidence: [`src/jev_bookmarks/typesafe.py`](https://github.com/kitepon/jev-bookmarks/blob/0f87410a8168254cb8a8208f16073fed91a7ffcd/src/jev_bookmarks/typesafe.py).

## Get started

Clone, install with uv, then install the browser profile and the agent skill.

```sh
git clone https://github.com/kitepon/jev-bookmarks.git && cd jev-bookmarks
uv sync --locked && uv tool install --editable .
jev-bookmarks install --typesafe-env /path/to/typesafe.env --browser-env /path/to/jev-ultrafast.env
jev-bookmarks harness install
jev-bookmarks run 'Show the Example Domain page'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design and acceptance criteria: [github.com/kitepon/jev-bookmarks/blob/main/docs/design.md](https://github.com/kitepon/jev-bookmarks/blob/main/docs/design.md)
- Upstream browser agent: [github.com/browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)

## Limits and data handling

Preview. History titles and host/path displays (up to 80) and part of the observed page text go to TypeSafe; the browser agent uses its own configured model. It runs a dedicated Chrome profile with no shared logins. Full runs are verified mainly on macOS per the README.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 0f87410a8168](https://github.com/kitepon/jev-bookmarks/tree/0f87410a8168254cb8a8208f16073fed91a7ffcd). Inspected README.en.md, LICENSE and `src/jev_bookmarks/typesafe.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
