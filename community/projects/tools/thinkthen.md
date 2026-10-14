# ThinkThen

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and SDK for typed questions about text: `decide`, `choose` and `score` return values and exit codes a shell can branch on, with TypeSafe Jev as one backend.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/botassembly/thinkthen) |
| Maintainer | [botassembly](https://github.com/botassembly). Independently curated. |
| Format | CLI + language bindings (Rust core) |
| Requirements | TypeSafe key for the hosted backend (or Ollama/other servers). |
| License | [MIT](https://github.com/botassembly/thinkthen/blob/d057ff25c39974a5808135481f6ff5674c7126e0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/thinkthen/src/core/adapters/systemone.rs`](https://github.com/botassembly/thinkthen/blob/d057ff25c39974a5808135481f6ff5674c7126e0/crates/thinkthen/src/core/adapters/systemone.rs) at the pinned commit. |

## When to use

- Gate a shell script on a yes/no question about a message.
- Mismatch: 0.2 examples need development builds; public release is 0.1.2.

## How it works

Each command sends one typed question to a configured System One backend; exit code 0/1/3 maps to yes/no/not sure. Overhead measurements are documented upstream. Integration evidence: [`crates/thinkthen/src/core/adapters/systemone.rs`](https://github.com/botassembly/thinkthen/blob/d057ff25c39974a5808135481f6ff5674c7126e0/crates/thinkthen/src/core/adapters/systemone.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://thinkthen.dev/install.sh | sh
thinkthen decide 'Does the customer ask for money back?' < message.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How-to demos: `demos/`.
- Backends: [thinkthen.dev/install/backends/](https://thinkthen.dev/install/backends/)

## Limits and data handling

Text goes to the configured backend. Review the install script before piping to sh.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit d057ff25c399](https://github.com/botassembly/thinkthen/tree/d057ff25c39974a5808135481f6ff5674c7126e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
