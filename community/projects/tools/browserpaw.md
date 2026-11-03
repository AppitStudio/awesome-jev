# BrowserPaw (MCP tools that automate your own signed-in Chrome, with an optional bounded Jev micro-loop for fuzzy targets)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome extension plus a local native bridge that lets MCP clients inspect and act on pages in the Chrome profile you already use. Click, fill and named-target tools resolve deterministically first; for fuzzy matches an optional bounded semantic decision, and an optional micro-loop of up to 60 steps, can use Jev, with independent read-only verification before it reports completion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GoldenLoaf24h/browserpaw) |
| Maintainer | [GoldenLoaf24h](https://github.com/GoldenLoaf24h). Independently curated. |
| Format | Chrome MV3 extension, native-messaging bridge and MCP server (TypeScript, pnpm) |
| Requirements | Chrome with Developer mode, Node and pnpm; for the remote mode `TYPESAFE_API_KEY` or a key saved in the popup. |
| License | [AGPL-3.0](https://github.com/GoldenLoaf24h/browserpaw/blob/d8b48343d173031b0f2d92cb9993cd2457956062/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/native-server/src/jev/jev-client.ts`](https://github.com/GoldenLoaf24h/browserpaw/blob/d8b48343d173031b0f2d92cb9993cd2457956062/app/native-server/src/jev/jev-client.ts) at the pinned commit. |

## When to use

- Let an MCP agent work in your logged-in Chrome without a copied profile, with ownership of pages kept per task.
- Mismatch: Jev is optional (model modes are Off, Local and Remote), and AGPL-3.0 terms apply if you modify and host it.

## How it works

`app/native-server/src/jev/jev-client.ts` uses the TypeSafe SDK to ask for a bounded decision over candidate elements (resolving the answering release from the response rather than a pinned alias); temporary network or rate-limit failures pause inference for 30 seconds, and the micro-loop stops on uncertain delivery. Integration evidence: [`app/native-server/src/jev/jev-client.ts`](https://github.com/GoldenLoaf24h/browserpaw/blob/d8b48343d173031b0f2d92cb9993cd2457956062/app/native-server/src/jev/jev-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/GoldenLoaf24h/browserpaw.git
cd browserpaw
pnpm install
pnpm build
node app/native-server/dist/scripts/register-dev.js
# then load app/chrome-extension/.output/chrome-mv3 in chrome://extensions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the model modes and the bounded micro-loop: [github.com/GoldenLoaf24h/browserpaw#readme](https://github.com/GoldenLoaf24h/browserpaw#readme)
- Install guide with Jev configuration: [github.com/GoldenLoaf24h/browserpaw/blob/main/INSTALL.md](https://github.com/GoldenLoaf24h/browserpaw/blob/main/INSTALL.md)

## Limits and data handling

In remote mode, candidate descriptions and context go to TypeSafe on your key, so keep secrets out of locator descriptions; the extension acts in your real browser session. The repository's NOTICE credits mcp-chrome as third-party code. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit d8b48343d173](https://github.com/GoldenLoaf24h/browserpaw/tree/d8b48343d173031b0f2d92cb9993cd2457956062). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
