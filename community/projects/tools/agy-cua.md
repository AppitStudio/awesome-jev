# agy-cua (background computer use for Antigravity)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Unofficial MCP plugin that gives Google Antigravity (app and `agy` CLI) background computer use on macOS through the open-source Cua Driver, with an optional Jev lane that picks each guarded step in about 0.2 to 0.3 s and refuses secure fields and send or commit actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saariuslystoned/agy-cua) |
| Maintainer | [saariuslystoned](https://github.com/saariuslystoned). Independently curated. |
| Format | Antigravity plugin with stdio MCP servers and a bash CLI (macOS) |
| Requirements | macOS, Google Antigravity, the signed Cua Driver app with Accessibility and Screen Recording grants; a TypeSafe key in macOS Keychain for the Jev lane. |
| License | [MIT](https://github.com/saariuslystoned/agy-cua/blob/fc7fb3829c01c8cd0b772f983e19e0ff537d53a9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/smokyproductco/status/2111598635972800596)). |
| Jev evidence | [`bin/agy-cua-jev-mcp`](https://github.com/saariuslystoned/agy-cua/blob/fc7fb3829c01c8cd0b772f983e19e0ff537d53a9/bin/agy-cua-jev-mcp) at the pinned commit. |

## When to use

- Give an Antigravity agent click, type and read access to Mac apps without paying for a separate computer-use API or stealing your cursor.
- Use the Jev lane for fast step choices with explicit refusal codes.
- Mismatch: macOS only; v0.2.0 and unofficial, so Antigravity or Cua Driver updates may break it.

## How it works

The Gemini agent in Antigravity calls MCP tools; `agy-cua-jev-mcp` asks Jev (`jev-1.13.0`) to choose the next action among candidates from the current window snapshot, then Cua Driver performs it in the background and the result is verified. A safety policy blocks secure elements, mail send and commit actions. Integration evidence: [`bin/agy-cua-jev-mcp`](https://github.com/saariuslystoned/agy-cua/blob/fc7fb3829c01c8cd0b772f983e19e0ff537d53a9/bin/agy-cua-jev-mcp).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/saariuslystoned/agy-cua && cd agy-cua
bin/agy-cua jev-key     # stores the key in macOS Keychain
bin/agy-cua doctor
bin/agy-cua install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post: [x.com/smokyproductco/status/2111598635972800596](https://x.com/smokyproductco/status/2111598635972800596)
- Six-task head-to-head write-up: `docs/benchmark-2026-10-14.md`.

## Limits and data handling

Window contents and accessibility data go to TypeSafe for Jev steps (and to Google for the Antigravity model). Not affiliated with Google or Cua.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit fc7fb3829c01](https://github.com/saariuslystoned/agy-cua/tree/fc7fb3829c01c8cd0b772f983e19e0ff537d53a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
