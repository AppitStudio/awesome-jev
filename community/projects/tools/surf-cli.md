# Surf CLI

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome-control CLI for AI agents with opt-in `surf semantic.*` commands: TypeSafe Jev selects the next action from Surf's allowed menu and checks whether the goal was reached.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nicobailon/surf-cli) |
| Maintainer | [nicobailon](https://github.com/nicobailon). Independently curated. |
| Format | CLI (`npm install -g surf-cli`) with an unpacked Chrome extension and native messaging host; Jev semantic commands are optional |
| Requirements | Node.js and npm, Chrome (or a supported Chromium browser) with the extension loaded in developer mode. Semantic commands need a TypeSafe key via `TYPESAFE_API_KEY` or `surf semantic auth set`. |
| License | [MIT](https://github.com/nicobailon/surf-cli/blob/5fbdcabfd58e2a391777436baedcd64c862a94f0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let a coding agent operate a website whose structure it does not know yet, with Jev choosing among Surf's validated actions instead of generating selectors.
- Gate writes explicitly (`--allow-write`, confidence thresholds) while still using natural-language goals.
- Mismatch: if you already know the exact steps, plain Surf commands are cheaper and send nothing to TypeSafe.

## How it works

Only `surf semantic.*` crosses the remote-AI boundary. Surf observes the current page, builds an allowed action menu, and sends a bounded, value-free observation to TypeSafe; Jev selects the next action, Surf validates permissions and confidence thresholds and executes it, then Jev checks whether the goal holds. Local input values go only to the browser fill/compare step, not to TypeSafe ([README: Optional Jev semantic commands](https://github.com/nicobailon/surf-cli/blob/5fbdcabfd58e2a391777436baedcd64c862a94f0/README.md#optional-jev-semantic-commands)).

## Get started

Install the CLI and extension per the README, then store a key and run a semantic command (live Jev calls):

```sh
npm install -g surf-cli
# load the extension (surf extension-path) and install the native host per the README
printf '%s\n' "$TYPESAFE_KEY" | surf semantic auth set
surf semantic.find "the control for notification preferences"
surf semantic.act "Open notification settings" --max-steps 5
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README examples for `semantic.find`, `semantic.act` with `--input` values and `--allow-write`, and per-action thresholds (`--threshold write=0.85`).

## Limits and data handling

Semantic commands send a page observation (not your input values) to TypeSafe and incur usage charges. Writes require explicit authorization flags. Credentials are stored in a shared `typesafe/credentials.json` (mode 0600 on POSIX) unless `TYPESAFE_API_KEY` is set.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 5fbdcabfd58e](https://github.com/nicobailon/surf-cli/tree/5fbdcabfd58e2a391777436baedcd64c862a94f0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
