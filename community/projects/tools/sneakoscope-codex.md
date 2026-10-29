# Sneakoscope Codex (macOS control center and bounded workflows for Codex, with optional Jev decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local tool for the Codex CLI and desktop app (`sks`): a macOS menu-bar control center for connections, subagent models, MCP servers, image generation and diagnostics, bounded agent workflows, a checkable repository index and evidence checks. Optional Jev decisions, with cloud consent, choose subagent models and can pick parallel work when a task has independent parts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mandarange/sneakoscope-codex) |
| Maintainer | [mandarange](https://github.com/mandarange). Independently curated. |
| Format | npm CLI (`sneakoscope`) and native macOS menu-bar app |
| Requirements | Node.js, Codex, macOS for the control center, and an OpenRouter key for Jev decisions. |
| License | [MIT](https://github.com/mandarange/sneakoscope-codex/blob/7f5b2193b3211b9e2ba05e141f0cd4ecbc9931c9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/daniel164293555/status/2115610776547516807)). |
| Jev evidence | [`native/sks-menubar/Sources/LocalDecisionModels.swift`](https://github.com/mandarange/sneakoscope-codex/blob/7f5b2193b3211b9e2ba05e141f0cd4ecbc9931c9/native/sks-menubar/Sources/LocalDecisionModels.swift) at the pinned commit. |

## When to use

- Make Codex runs bounded and explainable, with a GUI for settings.
- Mismatch: Jev is optional; large and fast-moving project.

## How it works

`native/sks-menubar/Sources/LocalDecisionModels.swift` pins `typesafe/jev-1.13` through OpenRouter and manages the decision mode and consent. Integration evidence: [`native/sks-menubar/Sources/LocalDecisionModels.swift`](https://github.com/mandarange/sneakoscope-codex/blob/7f5b2193b3211b9e2ba05e141f0cd4ecbc9931c9/native/sks-menubar/Sources/LocalDecisionModels.swift).

## Get started

From the upstream README (not run on the review host):

```sh
npm install --global sneakoscope@latest
sks doctor --fix --global-only --yes
sks menubar install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm: [www.npmjs.com/package/sneakoscope](https://www.npmjs.com/package/sneakoscope)
- README: [github.com/mandarange/sneakoscope-codex#readme](https://github.com/mandarange/sneakoscope-codex#readme)

## Limits and data handling

With Jev decisions on, task descriptions go to OpenRouter; indexing and safety checks run locally.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 7f5b2193b321](https://github.com/mandarange/sneakoscope-codex/tree/7f5b2193b3211b9e2ba05e141f0cd4ecbc9931c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
