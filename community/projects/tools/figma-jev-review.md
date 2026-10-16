# Figma Jev Review

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Figma plugin that reviews selected interface copy against declared criteria and cites the exact weak TextNodes, so clicking a finding selects and zooms to the original layer; it never writes copy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/figma-jev-review) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Figma plugin (development import from `manifest.json`) |
| Requirements | Figma Desktop, Node.js for the build, a TypeSafe API key entered per session. |
| License | [MIT](https://github.com/gbesse/figma-jev-review/blob/8d6dd45a4346d7e4013007a38ed054a43757640a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.ts`](https://github.com/gbesse/figma-jev-review/blob/8d6dd45a4346d7e4013007a38ed054a43757640a/src/client.ts) at the pinned commit. |

## When to use

- Check checkout or general UI copy against a criteria pack and jump to the weakest text layers.
- Mismatch: a copy review aid, not accessibility, legal or design scoring; thresholds are not calibrated and it is not yet on Figma Community.

## How it works

Pass one scores visible criteria over the selected node IDs, names and text; only weak criteria trigger pass two, where Jev chooses among up to 255 selected TextNodes. Requests go to `https://api.typesafe.ai/v1/systemone` only after you click Review. Integration evidence: [`src/client.ts`](https://github.com/gbesse/figma-jev-review/blob/8d6dd45a4346d7e4013007a38ed054a43757640a/src/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gbesse/figma-jev-review.git && cd figma-jev-review
npm ci && npm run build
# Figma Desktop: Plugins > Development > Import plugin from manifest > manifest.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline citation demo: `npm run demo:citation`.
- Privacy notes: `docs/privacy.md`.

## Limits and data handling

Selected text goes to TypeSafe on your key; the key is not persisted.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 8d6dd45a4346](https://github.com/gbesse/figma-jev-review/tree/8d6dd45a4346d7e4013007a38ed054a43757640a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
