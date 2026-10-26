# JEVision (flowchart UI tests for any Mac app, with Jev checking screens and finding elements)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS app for visual UI testing of any Mac app, including ones you cannot instrument: a test is a JSON flowchart walked block by block with the real mouse and keyboard, and Jev can check what a screenshot shows with a confidence threshold and find elements described in words such as "the blue Save button".

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dev-pikapik/JEVision) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/dev-pikapik/JEVision#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls are billed to your TypeSafe account or Cloudflare AI Gateway credits. Checked 2026-10-26. |
| Jev evidence | [`crates/jevision-vision/src/lib.rs`](https://github.com/dev-pikapik/JEVision/blob/f4a59e2e8c9eb1bf68b65ca61569dd8910f56a07/crates/jevision-vision/src/lib.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [dev-pikapik](https://github.com/dev-pikapik). Independently curated. |
| Format | macOS app (Swift with Rust crates) |
| Platform and availability | macOS 26+ source build; the README describes signed DMG and Homebrew installs, but no GitHub release was published at review time. |
| Jev's role | Optional vision provider: Jev answers how sure it is that a screen matches an expectation and locates elements by description; Anthropic, OpenAI, Gemini, Ollama and LM Studio are alternatives. |
| Requirements | macOS 26+ on Apple silicon or Intel; Xcode 26 and Rust 1.91 to build; a TypeSafe key or Cloudflare account for Jev, or another vision provider. |
| License | [MIT](https://github.com/dev-pikapik/JEVision/blob/f4a59e2e8c9eb1bf68b65ca61569dd8910f56a07/LICENSE) |

## When to use

- Test flows in Mac apps you do not own, without accessibility hooks or code changes.
- Gate checks on a confidence threshold instead of a plain yes or no.
- Mismatch: macOS only; other providers answer yes or no without a confidence.

## How it works

`crates/jevision-vision/src/lib.rs` defines the Jev provider with default address `https://api.typesafe.ai` and posts screenshot questions to `/v1/systemone`; a Cloudflare route to Jev is also supported. Integration evidence: [`crates/jevision-vision/src/lib.rs`](https://github.com/dev-pikapik/JEVision/blob/f4a59e2e8c9eb1bf68b65ca61569dd8910f56a07/crates/jevision-vision/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/dev-pikapik/JEVision.git && cd JEVision
apps/macos/scripts/build.sh
open apps/macos/build/JEVision.app   # choose JEV in Settings and add TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dev-pikapik/JEVision#readme](https://github.com/dev-pikapik/JEVision#readme)

## Limits and data handling

Screenshots and check questions go to the vision provider you choose. Tests drive the real mouse and keyboard on your Mac.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit f4a59e2e8c9e](https://github.com/dev-pikapik/JEVision/tree/f4a59e2e8c9eb1bf68b65ca61569dd8910f56a07). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
