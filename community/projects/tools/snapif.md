# Snapif

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust crate and CLI that scores one agent tool call against a shipped policy and returns Auto, Review or Escalate, using TypeSafe Jev (`SNAPIF_BACKEND=typesafe`) or any compatible endpoint, with a shadow mode before enforcement.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snapif/snapif) |
| Maintainer | [snapif](https://github.com/snapif). Independently curated. |
| Format | Rust library + CLI (`cargo install snapif --features cli`, 0.2.0 at review) |
| Requirements | Rust toolchain; `SNAPIF_BACKEND=typesafe` with a TypeSafe key, or `compatible` with your endpoint; `fake` for offline scripts. |
| License | [MIT](https://github.com/snapif/snapif/blob/fb38f0b7f477e2000fc93e66a377fa5d4c579e71/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add a tool-call gate to an agent harness and run it in `--shadow` first to see verdicts without blocking.
- Embed `Policy::shipped("tool-gate")` scoring in a Rust host.
- Mismatch: `review` and `screen` policy packs are ask-only and never return Auto.

## How it works

The call JSON (tool name, args, trusted user request, untrusted content) is scored by a shipped policy ([`policies/tool-gate.toml`](https://github.com/snapif/snapif/blob/fb38f0b7f477e2000fc93e66a377fa5d4c579e71/policies/tool-gate.toml)) whose questions go to the configured backend; [`src/gate.rs`](https://github.com/snapif/snapif/blob/fb38f0b7f477e2000fc93e66a377fa5d4c579e71/src/gate.rs) maps the answers to Auto/Review/Escalate. Unset backend is an error and missing scores fail closed; `--shadow` still allows and prints the verdict.

## Get started

Install the CLI and try the offline fake backend in shadow mode:

```sh
cargo install snapif --features cli
printf '%s\n' '{"tool_name":"bash","tool_input":{"command":"ls"}}' | SNAPIF_BACKEND=fake snapif hook --shadow
# live: SNAPIF_BACKEND=typesafe (model defaults to jev-latest)
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Same call, three scores* scenarios.
- Hook JSON for Claude Code `PreToolUse`.

## Limits and data handling

`Auto` only means the policy has no objection; the host still decides. Tool arguments are sent to the backend when live. Not run live on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit fb38f0b7f477](https://github.com/snapif/snapif/tree/fb38f0b7f477e2000fc93e66a377fa5d4c579e71). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
