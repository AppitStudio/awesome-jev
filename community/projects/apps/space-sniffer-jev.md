# SpaceSniffer, Jev edition (3D disk-space map for Windows that asks Jev which folders are safe to clear)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows disk-space map that draws your drive as a 3D city: every folder is a district sized by the space it takes. As soon as a folder is scanned, Jev labels what kind of folder it is, whether it only holds regenerable data such as caches, temp files and old installers, and how confident it is; safe-looking folders get a neon outline and land in a Reclaimable list. Jev never deletes anything; you confirm every deletion. Not affiliated with the original SpaceSniffer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NoxLoveYa/space-sniffer) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/NoxLoveYa/space-sniffer#readme) (source-built; no separate product site verified). |
| Pricing and access | Free and open source; uses OpenCode's limited-time free Jev tier when available, otherwise your own OpenCode or TypeSafe key. Checked 2026-10-30. |
| Jev evidence | [`electron/jev.ts`](https://github.com/NoxLoveYa/space-sniffer/blob/4cf4541a2b14a388ecfa67a7e55e2dc154de3de1/electron/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [NoxLoveYa](https://github.com/NoxLoveYa). Independently curated. |
| Format | Electron + three.js desktop app |
| Platform and availability | Windows; portable exe on GitHub Releases (v0.1.1) or build from source. |
| Jev's role | Labels each scanned folder and scores whether it is safe to clear. |
| Requirements | Windows; an OpenCode key (free jev-1.13-free tried first while it lasts) or a TypeSafe key. |
| License | [GPL-3.0](https://github.com/NoxLoveYa/space-sniffer/blob/4cf4541a2b14a388ecfa67a7e55e2dc154de3de1/LICENSE) |

## When to use

- Find caches and leftovers eating your disk, with a second opinion before deleting.
- Mismatch: Windows only; treat the confirmation dialog, not Jev, as the real safety check.

## How it works

`electron/jev.ts` builds a provider chain (OpenCode's free `jev-1.13-free`, then paid OpenCode or `https://api.typesafe.ai/v1/systemone`) and sends each folder's summary with three questions. Integration evidence: [`electron/jev.ts`](https://github.com/NoxLoveYa/space-sniffer/blob/4cf4541a2b14a388ecfa67a7e55e2dc154de3de1/electron/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm start
npm run dist   # portable exe in release/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Release v0.1.1: [github.com/NoxLoveYa/space-sniffer/releases](https://github.com/NoxLoveYa/space-sniffer/releases)

## Limits and data handling

For each folder it sends the path (with your Windows username replaced by <user>), size and file-type summary to the configured provider.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 4cf4541a2b14](https://github.com/NoxLoveYa/space-sniffer/tree/4cf4541a2b14a388ecfa67a7e55e2dc154de3de1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
