# cmd-mod-jev-guard (Jev auto mode for Command Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command Code mod that risk-scores every tool call with Jev and answers deny, ask or allow, denies calls that follow instructions planted in content the agent read, scans tool results for prompt injection and sweeps instruction files.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/felinae98/cmd-mod-jev-guard) |
| Maintainer | [felinae98](https://github.com/felinae98). Independently curated. |
| Format | Command Code mod (TypeScript/JavaScript) |
| Requirements | Command Code (`cmd`); a TypeSafe key (`JEV_API_KEY`), an AI Gateway or OpenRouter key, or an existing `cmd login`. |
| License | [MIT](https://github.com/felinae98/cmd-mod-jev-guard/blob/4051a8b64c72678ff182318463f410a9dad9e0f9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/felinae98/cmd-mod-jev-guard/blob/4051a8b64c72678ff182318463f410a9dad9e0f9/src/jev.js) at the pinned commit. |

## When to use

- Auto-approve clearly safe tool calls in Command Code while risky ones wait for a real confirm dialog.
- Catch prompt injection in tool results and unexpected behavior in skills or `AGENTS.md` files.
- Mismatch: Command Code only; for other agents use the upstream jev-guard.

## How it works

The mod hooks `beforeToolCall`, `onPermissionRequest`, `transformInput` and `afterToolCall`; for each call it sends the session context and the call to a System One endpoint (TypeSafe at `https://api.typesafe.ai/v1/systemone` or another backend, see `src/jev.js`) and maps the scores to deny, ask or allow. Policy and questions are vendored from jev-guard (MIT). Integration evidence: [`src/jev.js`](https://github.com/felinae98/cmd-mod-jev-guard/blob/4051a8b64c72678ff182318463f410a9dad9e0f9/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/felinae98/cmd-mod-jev-guard.git && cd cmd-mod-jev-guard
cmd mods add -g ./
# restart cmd or /reload; /jev-guard doctor checks the setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hooks comparison table in the README: [github.com/felinae98/cmd-mod-jev-guard#readme](https://github.com/felinae98/cmd-mod-jev-guard#readme)
- Upstream policy: [github.com/leepokai/jev-guard](https://github.com/leepokai/jev-guard)

## Limits and data handling

Tool calls and session context are sent to the chosen backend for scoring. Do not run it together with jev-guard's native hooks. Community project, not affiliated with TypeSafe or Command Code.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 4051a8b64c72](https://github.com/felinae98/cmd-mod-jev-guard/tree/4051a8b64c72678ff182318463f410a9dad9e0f9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
