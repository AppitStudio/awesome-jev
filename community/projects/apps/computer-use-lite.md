# Computer Use (lite) by ajokhai (Mac computer use for any AI, with an optional Jev mode)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Menu bar app and native MCP server that let an AI operate the whole Mac, not just a browser: Claude, ChatGPT, Gemini, OpenRouter or a local model plans the steps, and in its Jev modes TypeSafe Jev picks the next action and element from the app's accessibility tree.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ajokhai/computer-use-lite) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ajokhai/computer-use-lite#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download; public source with no license file (no open-source license granted). Provider calls use your own keys; through MCP the AI app you already use does the thinking. Checked 2026-10-25. |
| Jev evidence | [`cu/jev.py`](https://github.com/ajokhai/computer-use-lite/blob/bee723832f49063e32eb2a23a423c49c30db2b4d/cu/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ajokhai/status/2114000645309243593)). |
| Maintainer | [ajokhai](https://github.com/ajokhai). Independently curated. |
| Format | macOS menu bar app with Rust MCP server (Python, Rust, Swift) |
| Platform and availability | macOS; DMG on GitHub Releases (v0.1.15 at review), signed with a local certificate rather than a verified Developer ID. |
| Jev's role | Optional: in the Vision + Jev and Jev Only modes, Jev chooses the next action, the target element and the text to type from the accessibility tree; other modes do not use Jev. |
| Requirements | A Mac with Accessibility and Screen Recording permissions; a key for the chosen model provider (a TypeSafe key only for the Jev modes), or an MCP client such as Claude or Cursor with no key. |
| License | No LICENSE file on the reviewed commit on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Let an assistant you already use drive native Mac apps, not just a browser.
- Try a cheap text-only Jev mode for routine clicks and typing.
- Mismatch: no license file, so reuse terms are not granted; screenshots go to the vision provider you pick.

## How it works

`cu/jev.py` posts the task, the accessibility-tree elements and a list of operations to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and reads back the chosen action and element; a vision model takes over when Jev is unsure. Integration evidence: [`cu/jev.py`](https://github.com/ajokhai/computer-use-lite/blob/bee723832f49063e32eb2a23a423c49c30db2b4d/cu/jev.py).

## Get started

From the upstream README (not run on the review host): download `Computer Use <version>.dmg` from the latest release, drag it into Applications, grant Accessibility and Screen Recording, then add keys under Settings › API Keys or connect an AI app. To use the MCP server from any client:

```sh
{"command": "/Applications/Computer Use.app/Contents/Frameworks/cu-mcp", "args": []}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/ajokhai/computer-use-lite/releases/latest](https://github.com/ajokhai/computer-use-lite/releases/latest)
- Creator's X demo: [x.com/ajokhai/status/2114000645309243593](https://x.com/ajokhai/status/2114000645309243593)

## Limits and data handling

The app can click, type and open apps on your Mac; review what you ask it to do. Accessibility-tree text goes to TypeSafe in the Jev modes, and screenshots go to the vision provider you choose; a local model keeps everything on the Mac.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit bee723832f49](https://github.com/ajokhai/computer-use-lite/tree/bee723832f49063e32eb2a23a423c49c30db2b4d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
