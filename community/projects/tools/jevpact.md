# Jevpact (Codex desktop plugin that compacts context at the right moment)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local plugin and service for the Codex desktop app on macOS that watches ongoing work, asks Jev whether the current step has a usable conclusion and whether the task is waiting on something, then pauses the agent, triggers Codex's native compaction and resumes only actionable work; a development preview.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/transcendr/jevpact) |
| Maintainer | [transcendr](https://github.com/transcendr). Independently curated. |
| Format | Codex plugin with local Node.js service |
| Requirements | macOS, Codex desktop app, Node.js 22.13+; a TypeSafe Jev API key. |
| License | [CC-BY-4.0](https://github.com/transcendr/jevpact/blob/f979e023b2950a915a1dccaf1c86af2a46081b52/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/aienginerd/status/2114683545142665456)). |
| Jev evidence | [`plugins/jevpact/src/jev.js`](https://github.com/transcendr/jevpact/blob/f979e023b2950a915a1dccaf1c86af2a46081b52/plugins/jevpact/src/jev.js) at the pinned commit. |

## When to use

- Choose compaction checkpoints in long Codex desktop sessions instead of a fixed token limit.
- Mismatch: macOS Codex desktop only; development preview that relies on a private desktop interface; no promise of fewer tokens.

## How it works

`plugins/jevpact/src/jev.js` posts a bounded view of recent work to `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`); Codex performs the compaction itself. Integration evidence: [`plugins/jevpact/src/jev.js`](https://github.com/transcendr/jevpact/blob/f979e023b2950a915a1dccaf1c86af2a46081b52/plugins/jevpact/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/transcendr/jevpact.git && cd jevpact
codex plugin marketplace add . && codex plugin add jevpact@jevpact
node plugins/jevpact/bin/jevpact.js service install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Package README: [github.com/transcendr/jevpact/blob/main/plugins/jevpact/README.md](https://github.com/transcendr/jevpact/blob/main/plugins/jevpact/README.md)

## Limits and data handling

Bounded excerpts of recent task activity go to TypeSafe; history stays local. Licensed CC BY 4.0 (attribution required). Discovered on X.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit f979e023b295](https://github.com/transcendr/jevpact/tree/f979e023b2950a915a1dccaf1c86af2a46081b52). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
