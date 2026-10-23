# godot-jev-actions (Jev action nodes for Godot 4)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Godot 4 addon with designer-facing Jev nodes: an ActionCatalog allowlist, an ActionPicker that turns a sentence or game state into one allowed action with arguments, and a FreeTextChoice that maps typed text to an authored choice. Nothing is generated.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/godot-jev-actions) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | Godot 4 addon (GDScript) |
| Requirements | Godot 4; a TypeSafe API key (or a proxy for shipped games). |
| License | [MIT](https://github.com/saembit/godot-jev-actions/blob/27651d7e78dd3b32b38b2bfd3136b7cad19f99d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`addons/jev_actions/jev_client.gd`](https://github.com/saembit/godot-jev-actions/blob/27651d7e78dd3b32b38b2bfd3136b7cad19f99d2/addons/jev_actions/jev_client.gd) at the pinned commit. |

## When to use

- Let players type commands or dialogue that map to actions you authored.
- Have NPCs pick from a fixed action list based on game state.
- Mismatch: shipped games should not carry the key; the README says to use a proxy.

## How it works

`jev_client.gd` posts typed questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`), retries 429/529/5xx, and has a fake callable for offline tests. ActionPicker asks one choice over actions, then one choice per argument. Integration evidence: [`addons/jev_actions/jev_client.gd`](https://github.com/saembit/godot-jev-actions/blob/27651d7e78dd3b32b38b2bfd3136b7cad19f99d2/addons/jev_actions/jev_client.gd).

## Get started

From the upstream README (not run on the review host):

```sh
# copy addons/jev_actions into your project
# Project > Project Settings > Plugins: enable Jev Actions
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Node reference and catalog format in the README: [github.com/saembit/godot-jev-actions#readme](https://github.com/saembit/godot-jev-actions#readme)

## Limits and data handling

Player input and game state you pass in are sent to TypeSafe. Not affiliated with TypeSafe or Godot.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 27651d7e78dd](https://github.com/saembit/godot-jev-actions/tree/27651d7e78dd3b32b38b2bfd3136b7cad19f99d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
