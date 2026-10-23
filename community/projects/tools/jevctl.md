# jevctl (Jev judgments for agents from a CLI or MCP tool)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Rust CLI and single generic MCP tool that give coding agents fast semantic judgments: shared JSON context plus batched boolean, select and scale questions, answered by Jev with TypeSafe models and API details kept internal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iyazerski/jevctl) |
| Maintainer | [iyazerski](https://github.com/iyazerski). Independently curated. |
| Format | Rust CLI and MCP server |
| Requirements | macOS or Linux (x86_64 or ARM64); `TYPESAFE_API_KEY` in the process environment. |
| License | [MIT](https://github.com/iyazerski/jevctl/blob/25099f1601574fb9b713e32285fceeeda01c8d22/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.rs`](https://github.com/iyazerski/jevctl/blob/25099f1601574fb9b713e32285fceeeda01c8d22/src/client.rs) at the pinned commit. |

## When to use

- Let an agent ask yes/no, pick-one or scale questions during planning.
- Batch several judgments over one context in a single call.
- Mismatch: agent tooling; no UI.

## How it works

`src/client.rs` posts the translated questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; `jevctl doctor` checks readiness without making a request. Integration evidence: [`src/client.rs`](https://github.com/iyazerski/jevctl/blob/25099f1601574fb9b713e32285fceeeda01c8d22/src/client.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/iyazerski/jevctl/main/install.sh | sh
jevctl doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Request format and MCP setup in the README: [github.com/iyazerski/jevctl#readme](https://github.com/iyazerski/jevctl#readme)

## Limits and data handling

The context you pass is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 25099f160157](https://github.com/iyazerski/jevctl/tree/25099f1601574fb9b713e32285fceeeda01c8d22). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
