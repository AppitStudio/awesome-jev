# Command Space (macOS Spotlight replacement with an agent, local decisions and optional Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Launcher that replaces ⌘Space: apps, documents, paths, math and settings, plus an AI agent for questions and tasks and push-to-talk voice. Quick typed decisions run on a local model by default, with TypeSafe's Jev as an optional hosted backend.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/otron-io/command-space) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/otron-io/command-space#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download and source (GPL-3.0); the Jev backend uses your own key. Checked 2026-11-01. |
| Jev evidence | [`Sources/CommandSpace/Agent/DecisionEngine.swift`](https://github.com/otron-io/command-space/blob/204783fe379dd1e76a8155036aa1eb01c95f7751/Sources/CommandSpace/Agent/DecisionEngine.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [otron-io](https://github.com/otron-io). Independently curated. |
| Format | Native macOS app (Swift), DMG from GitHub Releases, Sparkle updates |
| Platform and availability | macOS. |
| Jev's role | Optional backend for fast typed decisions in the launcher and agent. |
| Requirements | macOS; optional TypeSafe key for the Jev backend. |
| License | [GPL-3.0](https://github.com/otron-io/command-space/blob/204783fe379dd1e76a8155036aa1eb01c95f7751/LICENSE) |

## When to use

- Launch apps and run quick commands from one bar, with fast typed decisions.
- Mismatch: Jev is optional; the default decision backend is a local model.

## How it works

`Sources/CommandSpace/Agent/DecisionEngine.swift` routes quick decisions (instant actions, nudges, suggestions, done checks) to `https://api.typesafe.ai/v1/systemone` when Jev is selected, or to a local grammar-constrained model otherwise. Integration evidence: [`Sources/CommandSpace/Agent/DecisionEngine.swift`](https://github.com/otron-io/command-space/blob/204783fe379dd1e76a8155036aa1eb01c95f7751/Sources/CommandSpace/Agent/DecisionEngine.swift).

## Get started

From the upstream README (not run on the review host):

```sh
# download Command-Space.dmg from GitHub Releases and drag it to Applications
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/otron-io/command-space/releases](https://github.com/otron-io/command-space/releases)

## Limits and data handling

Per the README, Jev sees requests and coarse context, never selected text, file contents or file names. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 204783fe379d](https://github.com/otron-io/command-space/tree/204783fe379dd1e76a8155036aa1eb01c95f7751). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
