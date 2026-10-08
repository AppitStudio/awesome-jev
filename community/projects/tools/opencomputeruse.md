# OpenComputerUse

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Background computer use for agents as an MCP server: start a session with a desktop app, drive it by window coordinates or accessibility elements while your own pointer, focus and frontmost app stay put, and run `run_recipe` step lists where each step's interactive elements become one Jev `choice` question (or Cloudflare Clef-flash), acting only when the model is confident.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IAmJSD/OpenComputerUse) |
| Maintainer | [IAmJSD](https://github.com/IAmJSD). Independently curated. |
| Format | Desktop app + `opencomputeruse` MCP server binary (stdio or HTTP) |
| Requirements | Rust to build; macOS Accessibility/Screen Recording permissions (or Windows UIA / Linux Xvfb); `TYPESAFE_API_KEY` or the app setting for Jev recipes. |
| License | [MIT](https://github.com/IAmJSD/OpenComputerUse/blob/881037886bedc9d69065f4ba640e1ce70d6396ff/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Claude Code, Codex or OpenCode use a desktop app without taking over your screen.
- Run fixed UI chores (`click the address bar`, `press enter`) with a cheap decision model instead of the calling LLM.
- Mismatch: recipes have no branching; Linux lacks the accessibility tree, so recipes are unavailable there.

## How it works

[`src/recipe.rs`](https://github.com/IAmJSD/OpenComputerUse/blob/881037886bedc9d69065f4ba640e1ce70d6396ff/src/recipe.rs) sends each step and the window's elements to Jev (`jev-latest`) or Clef-flash as a single `choice` question and acts on the chosen element above a confidence threshold; an unplaceable step stops and returns a screenshot and tree. Platform backends live under `crates/`.

## Get started

Build, then register with your MCP client (README *Install into a client*):

```sh
git clone https://github.com/IAmJSD/OpenComputerUse.git && cd OpenComputerUse
cargo build --release
opencomputeruse install claude   # or claude-desktop / codex / opencode
```

Only `run_recipe` steps call Jev (billed to your key); other tools are local.

## Examples and demos

- README *Recipes* JSON example (address bar → example.com → More information link).

## Limits and data handling

Recipe steps send window element names to TypeSafe or Cloudflare. Grants desktop control to the connected agent. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 881037886bed](https://github.com/IAmJSD/OpenComputerUse/tree/881037886bedc9d69065f4ba640e1ce70d6396ff). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
