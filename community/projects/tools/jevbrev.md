# jevbrev by Parker Brown (short .brev API definitions turned into Jev questions, answer readers and HTTP calls)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

A Rust CLI and library (also on npm as WebAssembly) that condenses an OpenAPI definition into a short `.brev` file, one plain-language line per action and input, then generates from it the two Jev request bodies that pick an action and fill its inputs, a reader for Jev's answers, the HTTP call to make or the question to ask when something is missing, plus compact tool definitions for LLMs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/parker-brown-family/jevbrev) |
| Maintainer | [parker-brown-family](https://github.com/parker-brown-family). Independently curated. |
| Format | Rust CLI/library + npm (WASM) package |
| Requirements | Rust (`cargo install jevbrev`) or Node (`npm install @parker-brown-family/jevbrev`); an API definition (OpenAPI) to condense. jevbrev never calls Jev or holds a key: your own code sends the generated request bodies with your TypeSafe key. |
| License | [MIT OR Apache-2.0](https://github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/parkerbrowndev/status/2123884501701165056)). |
| Jev evidence | [`src/frames.rs`](https://github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/src/frames.rs) at the pinned commit. |

## When to use

- Route typed natural-language requests to the right HTTP API action with Jev, without hand-writing question frames for every endpoint.
- Mismatch: you want a hosted agent or something that calls the API for you; jevbrev only generates request bodies and readers.

## How it works

`src/frames.rs` builds two complete `/v1/systemone` request bodies from a `.brev` file: call 1 asks which action a person's request wants, call 2 asks what the request says for each of that action's inputs. `src/read.rs` accepts the whole response (or just its `answers` map) and returns each input's value or marks it missing, so the app can make the HTTP call or ask the person a follow-up. Integration evidence: [`src/frames.rs`](https://github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/src/frames.rs).

## Get started

Install the CLI, draft a `.brev` file from an OpenAPI definition, then generate the Jev requests (see the upstream README for the exact subcommands).

```sh
cargo install jevbrev
# or: npm install @parker-brown-family/jevbrev
# see examples/shop.brev and the README for the draft/generate commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example .brev file: [github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/examples/shop.brev](https://github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/examples/shop.brev)
- README: [github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/README.md](https://github.com/parker-brown-family/jevbrev/blob/d6503914b6fbeb21c90d217e6b866cacc9dd71a5/README.md)
- Launch post on X: [x.com/parkerbrowndev/status/2123884501701165056](https://x.com/parkerbrowndev/status/2123884501701165056)

## Limits and data handling

jevbrev itself sends nothing; whatever your code passes to Jev (the user's request text and the action/input descriptions) goes to TypeSafe when you send it. Early release; output formats may change.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit d6503914b6fb](https://github.com/parker-brown-family/jevbrev/tree/d6503914b6fbeb21c90d217e6b866cacc9dd71a5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
