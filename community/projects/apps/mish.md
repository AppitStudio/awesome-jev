# Mish

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local-first AI design workspace: write a brief and a local agent CLI builds the design; in the agency fast lane, TypeSafe Jev routes the brief to a site family and verifies facts before publishing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZeroSum-Solutions/mish) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/ZeroSum-Solutions/mish/releases/latest](https://github.com/ZeroSum-Solutions/mish/releases/latest) |
| Pricing and access | Free Apache-2.0 app; uses your agent CLI subscription (Claude Code/Codex) and your own TypeSafe key for routing/verification. |
| Jev evidence | [`packages/agency-fast-lane/src/route.ts`](https://github.com/ZeroSum-Solutions/mish/blob/0d6c0b6e5df6abc98afd8881eb287686a4260476/packages/agency-fast-lane/src/route.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [ZeroSum-Solutions](https://github.com/ZeroSum-Solutions). Independently curated. |
| Format | Desktop app (TypeScript/Electron-style monorepo) |
| Platform and availability | macOS (Apple Silicon DMG, not notarized) or build from source |
| Jev's role | One Jev request places the brief on the Website Shape Atlas and picks a family package; Jev then checks each fact against the brief and strict mode blocks publishing on invented or missing facts. |
| Requirements | macOS arm64; `claude` or `codex` CLI on PATH; TypeSafe key for the fast lane. |
| License | [Apache-2.0](https://github.com/ZeroSum-Solutions/mish/blob/0d6c0b6e5df6abc98afd8881eb287686a4260476/LICENSE) |

## When to use

- Produce client website designs from a brief with a typed route and a fact check before publishing.
- Mismatch: Jev covers routing/verification only; builds are done by your agent CLI.

## How it works

The brief is routed by Jev, the agent builds the design, and a Jev pass verifies facts against the brief in strict mode. (Summarized from the upstream [README](https://github.com/ZeroSum-Solutions/mish/blob/0d6c0b6e5df6abc98afd8881eb287686a4260476/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): download the DMG from Releases, open past Gatekeeper, and set the key with `od agency config set --key-stdin`.

## Limits and data handling

Brief and generated facts go to TypeSafe; design builds use your agent provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 0d6c0b6e5df6](https://github.com/ZeroSum-Solutions/mish/tree/0d6c0b6e5df6abc98afd8881eb287686a4260476). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
