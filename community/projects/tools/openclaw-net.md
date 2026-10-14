# OpenClaw.NET

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted .NET AI agent runtime with desktop companion; includes opt-in TypeSafe Jev decision routing (shadow mode first, safety floors, fallback to the existing router).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/clawdotnet/openclaw.net) |
| Maintainer | [clawdotnet](https://github.com/clawdotnet). Independently curated. |
| Format | .NET agent runtime and gateway |
| Requirements | .NET; `TYPESAFE_API_KEY` in the gateway environment for Jev routing. |
| License | [MIT](https://github.com/clawdotnet/openclaw.net/blob/a9147c225ef003a2169f94587c33a21c0799706b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/OpenClaw.Core/Validation/JevRoutingConfiguration.cs`](https://github.com/clawdotnet/openclaw.net/blob/a9147c225ef003a2169f94587c33a21c0799706b/src/OpenClaw.Core/Validation/JevRoutingConfiguration.cs) at the pinned commit. |

## When to use

- Run a local or team agent gateway in .NET with tools and memory.
- Evaluate Jev turn routing in shadow mode before letting it act.
- Mismatch: Jev routing ships disabled; it is a pilot.

## How it works

When an operator enables `DynamicTurnRouting.Jev` (shadow or active), the gateway sends turn context to `api.typesafe.ai/v1/systemone` and compares or applies Jev's routing choice with safety floors and fallback. Integration evidence: [`src/OpenClaw.Core/Validation/JevRoutingConfiguration.cs`](https://github.com/clawdotnet/openclaw.net/blob/a9147c225ef003a2169f94587c33a21c0799706b/src/OpenClaw.Core/Validation/JevRoutingConfiguration.cs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/clawdotnet/openclaw.net
cd openclaw.net
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Routing guide: `docs/jev-routing.md`.

## Limits and data handling

With Jev routing enabled, turn context goes to TypeSafe and is billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit a9147c225ef0](https://github.com/clawdotnet/openclaw.net/tree/a9147c225ef003a2169f94587c33a21c0799706b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
