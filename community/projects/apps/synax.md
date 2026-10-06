# Synax

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Open-source local workspace for coding agents and codebase docs (agent chats, files, diffs, terminal) whose Electron app offers optional Jev-assisted Computer Use: with a TypeSafe key (or OpenRouter), Jev picks bounded semantic actions for the app-hosted Cua Driver instead of the default Direct Cua strategy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/coldmint9/Synax) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/coldmint9/Synax#readme); desktop builds on [GitHub Releases](https://github.com/coldmint9/Synax/releases/latest). |
| Pricing and access | Free Apache-2.0 app (macOS/Windows releases, v1.6.6 at review) and source build. Agents and Jev use your own provider keys (TypeSafe or OpenRouter for Jev); usage billed by them. Checked 2026-10-06. |
| Jev evidence | README *Computer Use* section and [`services/local-node/modules/computer-use/`](https://github.com/coldmint9/Synax/tree/bafa633b6b236b014f13f8a87b4c3b57683b3cda/services/local-node/modules/computer-use) (Jev credentials and controller) plus the 2026-09-28 optional-Jev design doc; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [coldmint9](https://github.com/coldmint9). Independently curated. |
| Format | Electron desktop app and local web mode |
| Platform and availability | macOS and Windows desktop releases; build from source on macOS, Windows or Linux (Node.js 22). |
| Jev's role | Optional Computer Use controller: Jev chooses among bounded semantic actions that the Cua Driver then performs; Auto/Direct Cua needs no Jev account or network request. |
| Requirements | Node.js 22, npm 10+, Git and native build tools for source builds; agent provider keys; `TYPESAFE_API_KEY` in the launching environment (or an OpenRouter provider) for Jev. |
| License | [Apache-2.0](https://github.com/coldmint9/Synax/blob/bafa633b6b236b014f13f8a87b4c3b57683b3cda/LICENSE). |

## When to use

- Work with coding agents, source, diffs and a terminal in one local app, and add desktop Computer Use when a task needs it.
- Try a Jev-driven action chooser for Computer Use while keeping a no-network default.
- Mismatch: Jev only applies to Computer Use in the Electron app; it does not power the coding agents.

## How it works

Desktop packaging bundles a pinned, SHA-256-verified Cua Driver 0.30.2. The default **Auto** strategy uses Direct Cua with no Jev call. When you set `TYPESAFE_API_KEY` for the app and enable Jev in the project's Computer Use settings — or select an OpenRouter provider for Jev — the controller asks Jev to choose from bounded semantic actions, which the driver executes.

## Get started

Install a release, or run from source, then enable Jev in the project's Computer Use settings (live calls per action):

```sh
git clone https://github.com/coldmint9/Synax.git
cd Synax
npm install
npm run dev        # see README for desktop (Electron) and production builds
# TYPESAFE_API_KEY=... in the environment that launches the desktop app
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Design and implementation plan docs for hosted Cua with optional Jev (`docs/superpowers/specs/2026-09-28-…`).
- README *Local Git merge requests* and terminal verification workflow.

## Limits and data handling

Computer Use controls your desktop; review permissions. Jev requests send the Computer Use observation and goal to TypeSafe or OpenRouter. Whether the latest release already includes the Jev option was not verified; build from source for the pinned commit. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit bafa633b6b23](https://github.com/coldmint9/Synax/tree/bafa633b6b236b014f13f8a87b4c3b57683b3cda). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
