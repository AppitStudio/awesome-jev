# nu_plugin_jev by David Cary (Nushell plugin that asks Jev typed questions from the pipeline)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Jev as Nushell commands: pipe in state and run `jev noul`, `jev choice`, `jev score` or `jev ask` to get a float, an answer record with confidence and probabilities, or the whole reply. It is deliberately narrow, so an agent's nu environment can ask for a judgment without being handed `http post`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/quietlight/nu_plugin_jev) |
| Maintainer | [quietlight](https://github.com/quietlight). Independently curated. |
| Format | Rust Nushell plugin |
| Requirements | Rust and Nushell 0.117.x (the plugin protocol is locked to nu's minor version); a TypeSafe API key. |
| License | [MIT](https://github.com/quietlight/nu_plugin_jev/blob/e84c16ec5101e7cf7ba380605093464806eafa0c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/api.rs`](https://github.com/quietlight/nu_plugin_jev/blob/e84c16ec5101e7cf7ba380605093464806eafa0c/src/api.rs) at the pinned commit. |

## When to use

- Give a shell or agent a typed Jev judgment step in Nushell scripts without general network access.
- Mismatch: image questions or other shells; text only, Nushell only.

## How it works

`src/api.rs` has the endpoint `https://api.typesafe.ai/v1/systemone` compiled in (no URL argument), sends text state only (Box is refused), caps requests at 256 KiB with a 60 s timeout, and reads the key from `~/.config/typesafe/api_key` before falling back to `$env.TYPESAFE_API_KEY`. `--model` picks the model (default `jev-latest`). Integration evidence: [`src/api.rs`](https://github.com/quietlight/nu_plugin_jev/blob/e84c16ec5101e7cf7ba380605093464806eafa0c/src/api.rs).

## Get started

Install with cargo, register the plugin, then pipe text into a question.

```sh
cargo install --git https://github.com/quietlight/nu_plugin_jev --locked
plugin add ~/.cargo/bin/nu_plugin_jev
plugin use jev
open ticket.md | jev noul 'Does the author ask for a refund?'
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with command examples: [github.com/quietlight/nu_plugin_jev/blob/e84c16ec5101e7cf7ba380605093464806eafa0c/README.md](https://github.com/quietlight/nu_plugin_jev/blob/e84c16ec5101e7cf7ba380605093464806eafa0c/README.md)

## Limits and data handling

Piped text leaves the machine to TypeSafe; the plugin narrows where data goes, not whether it goes. Version-locked to Nushell 0.117.x.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit e84c16ec5101](https://github.com/quietlight/nu_plugin_jev/tree/e84c16ec5101e7cf7ba380605093464806eafa0c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
