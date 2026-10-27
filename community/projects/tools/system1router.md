# System1Router (automatic reasoning effort for Claude Code and OpenCode, with an optional Jev classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Sets the reasoning effort of every prompt you send to Claude Code or OpenCode, from low to max, by reading the prompt with recent context; the default classifier is a small local Ettin model (no key, nothing sent), and Jev can be selected as a hosted classifier or second opinion. It keeps your model and prompt cache and fails open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Valkea/System1Router) |
| Maintainer | [Valkea](https://github.com/Valkea). Independently curated. |
| Format | Rust binary with Claude Code and OpenCode integrations |
| Requirements | Linux or macOS (Apple Silicon); Claude Code or OpenCode; a TypeSafe API key only for the Jev provider. |
| License | [MIT](https://github.com/Valkea/System1Router/blob/f6ead259263c770c24e6f1031d96be4bcbd2fecd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classification.rs`](https://github.com/Valkea/System1Router/blob/f6ead259263c770c24e6f1031d96be4bcbd2fecd/src/classification.rs) at the pinned commit. |

## When to use

- Stop paying for high effort on routine turns without losing depth on hard ones.
- Compare a local effort classifier with Jev on your own prompts.
- Mismatch: the local model is the default; the README reports Jev at 54% exact-level accuracy versus 60% for the local model.

## How it works

`src/classification.rs` builds the request for the selected provider; with `system1router provider jev` it posts to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) and maps Jev's class to an effort level. Integration evidence: [`src/classification.rs`](https://github.com/Valkea/System1Router/blob/f6ead259263c770c24e6f1031d96be4bcbd2fecd/src/classification.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/Valkea/System1Router/main/install.sh | sh
system1router provider jev   # optional: use Jev instead of the local model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Valkea/System1Router#readme](https://github.com/Valkea/System1Router#readme)

## Limits and data handling

With the local provider nothing leaves the machine. With Jev selected, the prompt and bounded recent context go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit f6ead259263c](https://github.com/Valkea/System1Router/tree/f6ead259263c770c24e6f1031d96be4bcbd2fecd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
