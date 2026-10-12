# jev-face (Imjungjuna)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A 3D face in the browser that reacts in real time to typed text: TypeSafe Jev judges recipient emotion and strength, driving ARKit blendshapes on a face mesh. Distinct from rbrisuda/jevface.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Imjungjuna/jev-face) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project README](https://github.com/Imjungjuna/jev-face#readme) |
| Pricing and access | Free MIT-licensed source. Requires your TypeSafe API key for live judgments (billed by TypeSafe). Checked 2026-10-12. |
| Jev evidence | [`src/emotions.js`](https://github.com/Imjungjuna/jev-face/blob/03a96c5d0a2ce3c56b3ef6b0a0ed5a556769db7d/src/emotions.js) and [`src/main.js`](https://github.com/Imjungjuna/jev-face/blob/03a96c5d0a2ce3c56b3ef6b0a0ed5a556769db7d/src/main.js) wire Jev judgments to blendshapes. LICENSE file is MIT. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. App not run on the review host. |
| Maintainer | [Imjungjuna](https://github.com/Imjungjuna). Independently curated. |
| Format | Browser WebGL app (Three.js) |
| Platform and availability | Modern desktop browsers. |
| Jev's role | Jev only judges emotion/intensity from text; rendering is local. |
| Requirements | TypeSafe API key in the UI/config per README. |
| License | [MIT](https://github.com/Imjungjuna/jev-face/blob/03a96c5d0a2ce3c56b3ef6b0a0ed5a556769db7d/LICENSE) |

## When to use

- Creative demo of System One affect judgments driving a face.
- Mismatch: Not a production avatar product; demo quality depends on mesh/assets.

## How it works

As you type, text is sent to Jev; answers update blendshape weights locally.

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Imjungjuna/jev-face.git
cd jev-face
# npm/pnpm install & dev per README
```

## Limits and data handling

Typed text goes to TypeSafe; billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 03a96c5d0a2c](https://github.com/Imjungjuna/jev-face/tree/03a96c5d0a2ce3c56b3ef6b0a0ed5a556769db7d). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
