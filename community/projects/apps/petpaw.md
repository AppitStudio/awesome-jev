# PetPaw

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Desktop pet companion for Apple Silicon Macs (SwiftUI, SceneKit, AVAudioEngine) with imported characters, voice and lip-sync: interaction reactions and poses are chosen by Cloud JEV (`typesafe-ai/jev`) or a Local Open-Jev mode that runs a 2B Open-Jev checkpoint ported to Swift/MLX on device, while Apple Foundation Models write moods and speech bubbles.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sirily11/pet-companion) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [pet-companion-kappa.vercel.app](https://pet-companion-kappa.vercel.app) · [download DMG](https://github.com/sirily11/pet-companion/releases/latest/download/PetCompanion.dmg) (v1.1.0) |
| Pricing and access | Free DMG on GitHub Releases. Cloud JEV needs your own key (stored in Keychain, billed by the provider); Local Open-Jev is a free ~4.6 GB download. Checked 2026-10-08. |
| Jev evidence | [`CatCompanion/Conversation/JevClient.swift`](https://github.com/sirily11/pet-companion/blob/2676201b6f4ce3d55f6f5768d99674dc3ac0918f/CatCompanion/Conversation/JevClient.swift) (cloud) and [`OpenJevRuntime.swift`](https://github.com/sirily11/pet-companion/blob/2676201b6f4ce3d55f6f5768d99674dc3ac0918f/CatCompanion/Conversation/OpenJevRuntime.swift) (local) score typed reaction choices. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [sirily11](https://github.com/sirily11). Independently curated. |
| Format | macOS app (DMG; build with Xcode + XcodeGen) |
| Platform and availability | Apple Silicon Mac; README targets macOS 27 (site mentions macOS 26+ for moods). |
| Jev's role | Chooses reactions and poses over declared typed choices. |
| Requirements | Apple Silicon Mac; Cloud JEV key or 16 GB RAM recommended for Local Open-Jev. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |

## When to use

- Want a desktop pet whose reactions are typed decisions, cloud or fully local.
- Example of running an Open-Jev checkpoint on device with MLX.
- Mismatch: macOS/Apple Silicon only.

## How it works

Reactions call Jev's evaluate API with typed choices (cloud) or the local Qwen-backbone Open-Jev runtime; speech and moods use Apple Foundation Models.

## Get started

Download the DMG, or build from source (README *Run*):

```sh
git clone https://github.com/sirily11/pet-companion.git && cd pet-companion
xcodegen generate
open CatCompanion.xcodeproj
```

Cloud JEV calls billed to your key; local mode is free.

## Examples and demos

- Settings → **Local Open-Jev** → *Manage local model…*.

## Limits and data handling

Cloud mode sends interaction context to the provider. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 2676201b6f4c](https://github.com/sirily11/pet-companion/tree/2676201b6f4ce3d55f6f5768d99674dc3ac0918f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
