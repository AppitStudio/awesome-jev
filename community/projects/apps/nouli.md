# Nouli (terminal app, CLI and Rust library that keeps connected decision histories, with Jev through its TypeSafe connection)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Terminal app, command-line tool and Rust library for decision histories: you add facts as context, ask a plain question, and earlier answers and files stay in a ledger-backed graph you can reference with `@`. It connects to any service that supports System One or OpenAI Decisions, and `nouli connect` has a TypeSafe recipe with `jev-latest` as the model; the project also publishes nine small task-specific models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nouli-ai/nouli) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://nouli.ai/) |
| Pricing and access | Free to install and run (MIT); remote inference through your own TypeSafe key is billed by TypeSafe. No paid Nouli plan was found. Checked 2026-11-04. |
| Jev evidence | [`nouli-cli/src/connect/recipes.rs`](https://github.com/nouli-ai/nouli/blob/41b1c70f3a4ff015b9c4c6e126163e65ec34af16/nouli-cli/src/connect/recipes.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [nouli-ai](https://github.com/nouli-ai). Independently curated. |
| Format | Rust CLI and TUI (Homebrew and install script for Apple silicon macOS and GNU/Linux) |
| Platform and availability | Terminal on Apple silicon macOS and ARM64/x86_64 GNU/Linux (Homebrew, install script or source). |
| Jev's role | One of the connectable decision services; answers typed questions about the facts in a session. |
| Requirements | macOS (Apple silicon) or GNU/Linux with glibc 2.38+; a service connection such as a TypeSafe key for remote inference. |
| License | [MIT](https://github.com/nouli-ai/nouli/blob/41b1c70f3a4ff015b9c4c6e126163e65ec34af16/LICENSE) |

## When to use

- Keep a reviewable history of typed decisions in the terminal and reuse earlier answers as new context.
- Mismatch: Jev is one of several supported services, and Nouli's own local models need their own runtimes.

## How it works

`nouli-cli/src/connect/recipes.rs` defines the TypeSafe connection (`https://api.typesafe.ai`, model `jev-latest`) and the core's System One transport posts typed questions to `/v1/systemone`. Integration evidence: [`nouli-cli/src/connect/recipes.rs`](https://github.com/nouli-ai/nouli/blob/41b1c70f3a4ff015b9c4c6e126163e65ec34af16/nouli-cli/src/connect/recipes.rs).

## Get started

From the upstream README (not run on the review host):

```sh
brew install nouli-ai/tap/nouli
nouli connect
nouli
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the quickstart and model list: [github.com/nouli-ai/nouli#readme](https://github.com/nouli-ai/nouli#readme)
- Website and guide: [nouli.ai/](https://nouli.ai/)

## Limits and data handling

With a TypeSafe connection, the context rows and question you send go to TypeSafe on your key and provider fees apply. Install and the TUI were not run on the review host. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 41b1c70f3a4f](https://github.com/nouli-ai/nouli/tree/41b1c70f3a4ff015b9c4c6e126163e65ec34af16). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
