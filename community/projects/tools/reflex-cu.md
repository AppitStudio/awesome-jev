# reflex-cu (computer use MCP server that reads the UI tree and asks Jev the small reflex questions)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server for Claude Code, Codex and other agents that operates a macOS or Windows desktop, or a remote Windows machine over SSH, by reading the accessibility tree instead of taking a screenshot every step. Its find, check and wait tools hand the quick decisions (which element, did that work, has it loaded) to Jev, optionally with the screenshot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/8itlab/reflex-computer-use) |
| Maintainer | [8itlab](https://github.com/8itlab). Independently curated. |
| Format | Python MCP server |
| Requirements | Python 3, macOS Accessibility and Screen Recording permissions or Windows; `TYPESAFE_API_KEY` (or an OpenRouter or other System One gateway) for the Jev tools. |
| License | [MIT](https://github.com/8itlab/reflex-computer-use/blob/3e1250c8e384df80c97aa1385f33a6f414a14e32/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`reflexcu/core.py`](https://github.com/8itlab/reflex-computer-use/blob/3e1250c8e384df80c97aa1385f33a6f414a14e32/reflexcu/core.py) at the pinned commit. |

## When to use

- Let a coding agent drive desktop apps with fewer screenshots and model round trips.
- Mismatch: tool descriptions and element labels are in Chinese; only find, check, wait and steps need Jev.

## How it works

`reflexcu/core.py` merges the UI-tree observation and sends it to Jev's `/v1/systemone` endpoint (`jev-latest` by default) as choice and yes/no questions; with `look: true` the screenshot goes along so Jev can find bare icons or objects in game scenes. Integration evidence: [`reflexcu/core.py`](https://github.com/8itlab/reflex-computer-use/blob/3e1250c8e384df80c97aa1385f33a6f414a14e32/reflexcu/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/8itlab/reflex-computer-use && cd reflex-cu
python3 -m venv ~/.reflexcu/venv
~/.reflexcu/venv/bin/pip install -r requirements-macos.txt
claude mcp add reflexcu -s user -- ~/.reflexcu/venv/bin/python "$PWD/reflexcu/server.py"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/8itlab/reflex-computer-use/blob/main/README.en.md](https://github.com/8itlab/reflex-computer-use/blob/main/README.en.md)

## Limits and data handling

UI element text and, with `look`, screenshots are sent to TypeSafe or the gateway you configure. The agent can click and type on your desktop; review its permissions. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 3e1250c8e384](https://github.com/8itlab/reflex-computer-use/tree/3e1250c8e384df80c97aa1385f33a6f414a14e32). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
