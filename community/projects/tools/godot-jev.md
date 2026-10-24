# Godot Jev (Godot 4 addon wrapping the Jev System One API)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Godot 4.7+ addon that exposes Jev as an autoload: choice, score, noul and box questions about game state, batched in one request, with native Godot inputs such as Dictionary, Image and Texture2D.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlvianEka/godot-jev) |
| Maintainer | [AlvianEka](https://github.com/AlvianEka). Independently curated. |
| Format | Godot 4 addon (GDScript) |
| Requirements | Godot 4.7+; a TypeSafe API key. |
| License | [MIT](https://github.com/AlvianEka/godot-jev/blob/b82c6cbeebfef297de088a2b431fbc11e712f180/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`addons/godot_jev/jev_config.gd`](https://github.com/AlvianEka/godot-jev/blob/b82c6cbeebfef297de088a2b431fbc11e712f180/addons/godot_jev/jev_config.gd) at the pinned commit. |

## When to use

- Let NPCs or game systems judge state (danger, intent, mood) with probabilities.
- Ask several questions about one frame or state in a single request.
- Mismatch: shipped games should not embed your API key; use a proxy.

## How it works

`jev_config.gd` points the client at `https://api.typesafe.ai` with `jev-latest` (or pinned `jev-1.13.0`); `jev.gd` builds questions, retries 429/529 with backoff and cancels requests when a bound node leaves the scene tree. Integration evidence: [`addons/godot_jev/jev_config.gd`](https://github.com/AlvianEka/godot-jev/blob/b82c6cbeebfef297de088a2b431fbc11e712f180/addons/godot_jev/jev_config.gd).

## Get started

From the upstream README (not run on the review host): install from the Godot Asset Store or AssetLib, then:

```sh
# Project > Project Settings > Plugins: enable Godot Jev
export TYPESAFE_API_KEY=...   # or Jev.api_key / jev/config/api_key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Godot AssetLib: [godotengine.org/asset-library/asset/5531](https://godotengine.org/asset-library/asset/5531)
- README: [github.com/AlvianEka/godot-jev#readme](https://github.com/AlvianEka/godot-jev#readme)

## Limits and data handling

Game state and images you pass are sent to TypeSafe. Box questions need a preview model.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b82c6cbeebfe](https://github.com/AlvianEka/godot-jev/tree/b82c6cbeebfef297de088a2b431fbc11e712f180). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
