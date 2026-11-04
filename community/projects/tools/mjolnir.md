# Mjolnir (control plane for Claude Code, Codex and other coding agents that uses Jev as its default turn classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust control plane (`mj`) that runs Claude Code, Codex, Kimi Code, Grok Build, OpenCode and other agent sessions side by side, keeps them alive after the terminal closes and moves sessions between accounts or machines. By default it asks Jev to read whether a turn stopped for input, a quota limit or a transient failure, to decide on automatic continuation, and to power semantic help search. A single `[jev] enabled = false` setting turns every Jev request off.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BrokkAi/mjolnir) |
| Maintainer | [BrokkAi](https://github.com/BrokkAi). Independently curated. |
| Format | Rust workspace with CLI, TUI, desktop app and npm launcher (`@brokkai/mjolnir`) |
| Requirements | Install script or `npm install -g @brokkai/mjolnir`; your own agent harness subscriptions. Jev needs no key through the project's public proxy, or your TypeSafe key. |
| License | [GPL-3.0-only](https://github.com/BrokkAi/mjolnir/blob/146cf220b7a26b1097332c93361e3198f36e1fab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mj-controller/src/continuation.rs`](https://github.com/BrokkAi/mjolnir/blob/146cf220b7a26b1097332c93361e3198f36e1fab/mj-controller/src/continuation.rs) at the pinned commit. |

## When to use

- Supervise several long-running coding-agent sessions and let a typed classifier decide whether a stopped turn needs you, a retry or a continuation.
- Mismatch: Jev traffic is on by default and goes through a public proxy unless you add your own key or switch it off.

## How it works

`mj-controller/src/continuation.rs` posts the clipped turn state and typed questions to a Brokk-run Jev proxy (`/v2/continuation-verdict`) or directly to `https://api.typesafe.ai/v1/systemone` with your key; the worker maps the verdicts to turn states such as awaiting input, quota stop or retry. Integration evidence: [`mj-controller/src/continuation.rs`](https://github.com/BrokkAi/mjolnir/blob/146cf220b7a26b1097332c93361e3198f36e1fab/mj-controller/src/continuation.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/BrokkAi/mjolnir/master/install.sh | bash
# or: npm install -g @brokkai/mjolnir
# opt out of all Jev requests: set `enabled = false` under `[jev]` in config.toml
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the default-on Jev disclosure: [github.com/BrokkAi/mjolnir#readme](https://github.com/BrokkAi/mjolnir#readme)
- Security page listing what leaves the machine: [mjolnir.brokk.ai/security/](https://mjolnir.brokk.ai/security/)
- Documentation: [mjolnir.brokk.ai/](https://mjolnir.brokk.ai/)

## Limits and data handling

By default, up to 1 KiB of your latest prompt, 2 KiB of the latest reply, a transcript summary, tool titles and help-filter text go to TypeSafe's hosted Jev through a public proxy (or to api.typesafe.ai on your key); `[jev] enabled = false` stops it. GPL-3.0 terms apply. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 146cf220b7a2](https://github.com/BrokkAi/mjolnir/tree/146cf220b7a26b1097332c93361e3198f36e1fab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
