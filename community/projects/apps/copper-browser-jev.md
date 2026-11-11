# Copper (small WebKit browser for macOS with a Jev-first agent command)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Small, quiet WebKit browser for the Mac built on Search by Office Commun; its `copper` CLI and `/jev <goal>` command let Jev pick each action from a numbered list of what is on the page in the signed-in browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/copper-browser/Copper) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://copper-browser.github.io/Copper/) |
| Pricing and access | Free download (MIT); Jev runs use your own TypeSafe key. Checked 2026-11-11. |
| Jev evidence | [`Sources/Search/Fork/Intelligence.swift`](https://github.com/copper-browser/Copper/blob/c468ab48c1d9cbc621f8a876b092b391125fe93e/Sources/Search/Fork/Intelligence.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/CollinRijock/status/2120261269412581601)). |
| Maintainer | [copper-browser](https://github.com/copper-browser). Independently curated. |
| Format | macOS app and CLI (Swift, MIT) |
| Platform and availability | macOS 14 or later (Apple Silicon or Intel) |
| Jev's role | Jev picks each browser action from a numbered list of page controls for `copper run` and `/jev` goals. |
| Requirements | macOS 14+, a TypeSafe key configured for Copper's Jev lane (see `docs/intelligence.md`), and the agent toggle **Let agents drive this window**. |
| License | [MIT](https://github.com/copper-browser/Copper/blob/c468ab48c1d9cbc621f8a876b092b391125fe93e/LICENSE) |

## When to use

- Drive your own signed-in browser from a terminal agent with typed action picks.
- Use a light WebKit browser with built-in ad blocking and reading mode.
- Mismatch: GitHub fork of Search by Office Commun; macOS only; agent control is off until you enable it.

## How it works

`Sources/Search/Fork/Intelligence.swift` posts to `https://api.typesafe.ai/v1/systemone`; `Sources/Search/Fork/MCP/Ultrafast.swift` runs the Jev fast path behind `copper run` and `/jev`, and the README warns that Jev's DONE is a claim to verify with `copper observe`. Integration evidence: [`Sources/Search/Fork/Intelligence.swift`](https://github.com/copper-browser/Copper/blob/c468ab48c1d9cbc621f8a876b092b391125fe93e/Sources/Search/Fork/Intelligence.swift).

## Get started

Install with Homebrew, enable agent control in settings, then run a goal from the CLI.

```sh
brew install --cask copper-browser/copper/copper
copper run "find the Acme invoice for March 2026 and stop when it is visible"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/copper-browser/Copper/blob/c468ab48c1d9cbc621f8a876b092b391125fe93e/README.md](https://github.com/copper-browser/Copper/blob/c468ab48c1d9cbc621f8a876b092b391125fe93e/README.md)

## Limits and data handling

Page descriptions (and screenshots in vision modes) go to TypeSafe when a Jev run is active; saved card and custom-field values are not returned in MCP, CLI output or Jev traces per the bundled skill.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit c468ab48c1d9](https://github.com/copper-browser/Copper/tree/c468ab48c1d9cbc621f8a876b092b391125fe93e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
