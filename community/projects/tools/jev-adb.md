# jev-adb

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server that controls an Android phone over ADB (USB or wireless) using TypeSafe Jev for typed UI understanding, with explicit user consent and safety gates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/srsergi0/jev-adb) |
| Maintainer | [srsergi0](https://github.com/srsergi0). Independently curated. |
| Format | MCP server (Node.js) |
| Requirements | Node.js; Android device with ADB debugging; TypeSafe key. |
| License | [MIT](https://github.com/srsergi0/jev-adb/blob/a95daa9d6678be61045d0d0bc9b4b8036ce92b88/LICENSE) |
| Jev evidence | [`src/jev.ts`](https://github.com/srsergi0/jev-adb/blob/a95daa9d6678be61045d0d0bc9b4b8036ce92b88/src/jev.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let an MCP client drive a real Android phone with fast typed decisions about the screen.
- Mismatch: needs ADB access to your device; review the safety gates before use.

## How it works

Reads the UI hierarchy over ADB, asks Jev typed questions about elements and next actions, and executes ADB actions after consent checks. (Summarized from the upstream [README](https://github.com/srsergi0/jev-adb/blob/a95daa9d6678be61045d0d0bc9b4b8036ce92b88/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README and register the `jev-adb` MCP server in your client.

## Limits and data handling

UI text from your phone goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit a95daa9d6678](https://github.com/srsergi0/jev-adb/tree/a95daa9d6678be61045d0d0bc9b4b8036ce92b88). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
