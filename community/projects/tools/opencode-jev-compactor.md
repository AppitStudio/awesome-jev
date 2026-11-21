# OpenCode Jev Compaction by Christian Taillon (Jev decides which old tool calls OpenCode's compaction can shrink)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An OpenCode plugin that hooks the native compaction step: code first sorts every past tool call into pin, protect or drop-eligible, then Jev answers narrow yes/no questions about whether each eligible call and its full result are still needed, and the plugin appends compact keep/stale guidance for OpenCode's own summary. Jev never writes the summary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/christian-taillon/opencode-jev-compactor) |
| Maintainer | [christian-taillon](https://github.com/christian-taillon). Independently curated. |
| Format | TypeScript OpenCode plugin |
| Requirements | OpenCode with plugin support and a TypeSafe API key; Node/pnpm to build from source. |
| License | [MIT](https://github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/grok/status/2124176546638319627)). |
| Jev evidence | [`src/jev/client.ts`](https://github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/src/jev/client.ts) at the pinned commit. |

## When to use

- Make long OpenCode sessions compact more aggressively without losing edits, shell commands or failed results.
- Mismatch: other coding agents; it targets OpenCode's experimental compaction hook only.

## How it works

`src/jev/client.ts` posts one chronological state and batched Noul questions to the configured TypeSafe System One endpoint (validated base URL); a deterministic policy keeps anything above the `keepThreshold` (default 0.15), and calls are skipped entirely when the possible reduction is too small to matter. Integration evidence: [`src/jev/client.ts`](https://github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/src/jev/client.ts).

## Get started

Clone, build, and register the plugin in your OpenCode config (an example is in `example/opencode.jsonc`).

```sh
git clone https://github.com/christian-taillon/opencode-jev-compactor
cd opencode-jev-compactor
pnpm install && pnpm build
# then add the plugin to opencode.jsonc (see example/opencode.jsonc) and set TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/README.md](https://github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/README.md)
- Example config: [github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/example/opencode.jsonc](https://github.com/christian-taillon/opencode-jev-compactor/blob/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e/example/opencode.jsonc)
- Mentioned on X: [x.com/grok/status/2124176546638319627](https://x.com/grok/status/2124176546638319627)

## Limits and data handling

Session transcript excerpts (tool names, inputs and results that are eligible) are sent to TypeSafe. Depends on an experimental OpenCode hook that may change.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 2e1e7b2bb79f](https://github.com/christian-taillon/opencode-jev-compactor/tree/2e1e7b2bb79f9f507f69ac13243e4bac9e197f4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
