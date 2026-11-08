# TypeSafe SDK for Godot (GDScript addon for the TypeSafe Jev System One API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community Godot 4.7 addon that adds a `TypeSafeClient` node for the System One API, aiming at parity with the Python SDK and HTTP reference, with examples and parity tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/IAmNo1Special/typesafe-sdk-godot) |
| Maintainer | [IAmNo1Special](https://github.com/IAmNo1Special). Independently curated. |
| Format | Godot 4 addon (GDScript, MIT) |
| Requirements | Godot 4.7 and a TypeSafe API key. |
| License | [MIT](https://github.com/IAmNo1Special/typesafe-sdk-godot/blob/b2515056566b744127b0b55e3caa3e5b752525a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`addons/typesafe_sdk/core/constants.gd`](https://github.com/IAmNo1Special/typesafe-sdk-godot/blob/b2515056566b744127b0b55e3caa3e5b752525a1/addons/typesafe_sdk/core/constants.gd) at the pinned commit. |

## When to use

- Ask Jev typed questions from game logic in Godot.
- Drive NPC or game-state decisions without parsing LLM text.
- Mismatch: unofficial community SDK, not maintained by TypeSafe.

## How it works

`addons/typesafe_sdk/core/constants.gd` sets `https://api.typesafe.ai` and `jev-latest`; the addon posts to `/v1/systemone` and parses typed `system_one_response` answers. Integration evidence: [`addons/typesafe_sdk/core/constants.gd`](https://github.com/IAmNo1Special/typesafe-sdk-godot/blob/b2515056566b744127b0b55e3caa3e5b752525a1/addons/typesafe_sdk/core/constants.gd).

## Get started

Copy `addons/typesafe_sdk` into your Godot project, enable the plugin, and add a TypeSafeClient node.

```sh
git clone https://github.com/IAmNo1Special/typesafe-sdk-godot.git && cd typesafe-sdk-godot
export TYPESAFE_API_KEY=...
godot --headless --script tests/parity_check.gd
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/IAmNo1Special/typesafe-sdk-godot/blob/b2515056566b744127b0b55e3caa3e5b752525a1/README.md](https://github.com/IAmNo1Special/typesafe-sdk-godot/blob/b2515056566b744127b0b55e3caa3e5b752525a1/README.md)

## Limits and data handling

Game state you pass is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit b2515056566b](https://github.com/IAmNo1Special/typesafe-sdk-godot/tree/b2515056566b744127b0b55e3caa3e5b752525a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
