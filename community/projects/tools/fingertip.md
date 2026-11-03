# fingertip (MCP server that lets an agent drive an iOS simulator or a macOS app through Accessibility, with Jev taking each step of a whole instruction)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and optional Mac app that lets an agent see and drive an iOS simulator or a macOS app: it reads the screen through Accessibility, then taps, types, scrolls and screenshots, with no XCTest runner. Its `run_instruction` tool hands a natural-language instruction to Jev, which chooses among the actionable elements the Swift code lists and judges whether the goal is met.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deadcode-labs/fingertip) |
| Maintainer | [deadcode-labs](https://github.com/deadcode-labs). Independently curated. |
| Format | MCP server and Mac app (Swift package) |
| Requirements | macOS 27 and Xcode 27 (Swift 6.2+) per the README; `sim-use` for simulators; Accessibility and Screen Recording permissions; `TYPESAFE_API_KEY` for `run_instruction`. |
| License | [MIT](https://github.com/deadcode-labs/fingertip/blob/b1fe854aca81c777eb9990f584e117c6009e00cb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Sources/FingertipCore/Jev.swift`](https://github.com/deadcode-labs/fingertip/blob/b1fe854aca81c777eb9990f584e117c6009e00cb/Sources/FingertipCore/Jev.swift) at the pinned commit. |

## When to use

- Have Claude Code walk a flow in your iOS or macOS app and check what is on screen.
- Mismatch: simulators and Mac apps on the same Mac only; the Jev-driven `run_instruction` tool is optional next to the direct tap and read tools.

## How it works

`Sources/FingertipCore/Jev.swift` posts to `/v1/systemone` with URLSession (no Swift SDK): the Swift code enumerates the candidate elements `e0…eN` and Jev only chooses among them and judges the goal, with a changed-screen check before each tap. Integration evidence: [`Sources/FingertipCore/Jev.swift`](https://github.com/deadcode-labs/fingertip/blob/b1fe854aca81c777eb9990f584e117c6009e00cb/Sources/FingertipCore/Jev.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/deadcode-labs/fingertip.git
cd fingertip
swift build -c release
claude mcp add --scope user fingertip -- "$PWD/.build/release/fingertip-mcp"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- How Jev decides each step: [github.com/deadcode-labs/fingertip/blob/main/docs/jev.md](https://github.com/deadcode-labs/fingertip/blob/main/docs/jev.md)
- Latest release with Fingertip.dmg: [github.com/deadcode-labs/fingertip/releases/latest](https://github.com/deadcode-labs/fingertip/releases/latest)

## Limits and data handling

Screen text the agent reads goes to the model; with `run_instruction`, element lists and the instruction go to TypeSafe on your key. By default the MCP refuses to drive terminals, editors with terminals, password managers and similar apps. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit b1fe854aca81](https://github.com/deadcode-labs/fingertip/tree/b1fe854aca81c777eb9990f584e117c6009e00cb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
