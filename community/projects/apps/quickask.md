# QuickAsk (macOS menu bar assistant for Codex and Claude, with Jev routing and follow-up checks)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS menu bar assistant: press Option–Space, ask a question and send it to Codex or Claude using your existing CLI logins; Jev (or optionally OpenAI Decisions) routes which context to attach and checks whether an answer needs a follow-up.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cxrobx/quickask) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/cxrobx/quickask#readme) (source-built; no separate product site verified). |
| Pricing and access | Source available under BSL 1.1: free for personal use and internal use by your organisation; selling it needs a commercial licence from CX Ventures LLC. Converts to Apache-2.0 on 2030-09-30. Jev calls billed to your TypeSafe key. Checked 2026-10-26. |
| Jev evidence | [`Sources/QuickAsk/FollowUpCheck.swift`](https://github.com/cxrobx/quickask/blob/87193bd98f69d9d5fa37c8c516218826f0b64562/Sources/QuickAsk/FollowUpCheck.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [cxrobx](https://github.com/cxrobx). Independently curated. |
| Format | macOS menu bar app (Swift) |
| Platform and availability | macOS 14+; build from source or use the `dist/QuickAsk.app` in the repository (no GitHub release at review time). |
| Jev's role | Context router and follow-up checker: Jev answers typed questions about which context to include and whether a reply needs a follow-up. |
| Requirements | macOS 14+ (supplied binary for Apple silicon); Codex or Claude CLI logged in; a TypeSafe API key for Jev routing. |
| License | [Business Source License 1.1 (source available; converts to Apache-2.0 on 2030-09-30)](https://github.com/cxrobx/quickask/blob/87193bd98f69d9d5fa37c8c516218826f0b64562/LICENSE) |

## When to use

- Ask Codex or Claude a quick question from anywhere on your Mac.
- Attach only the context that helps.
- Mismatch: not open source until the change date; Codex or Claude usage counts against your own plans.

## How it works

`Sources/QuickAsk/FollowUpCheck.swift` and `ContextRouting.swift` post typed questions to `https://api.typesafe.ai/v1/systemone` pinned to `jev-1.13.0`; OpenAI's Decisions API is an alternative engine. Integration evidence: [`Sources/QuickAsk/FollowUpCheck.swift`](https://github.com/cxrobx/quickask/blob/87193bd98f69d9d5fa37c8c516218826f0b64562/Sources/QuickAsk/FollowUpCheck.swift).

## Get started

From the upstream README (not run on the review host):

```sh
open dist/QuickAsk.app   # or build from source as the README describes
# add TYPESAFE_API_KEY in settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cxrobx/quickask#readme](https://github.com/cxrobx/quickask#readme)

## Limits and data handling

Your question and context summaries go to TypeSafe for routing; the question goes to Codex or Claude through your CLI login.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 87193bd98f69](https://github.com/cxrobx/quickask/tree/87193bd98f69d9d5fa37c8c516218826f0b64562). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
