# Jev Orchestration by gkrtjd99 (Claude Code and Codex hooks where Jev picks the model and effort for delegated subagent work)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Native hooks for Claude Code and Codex that run before the main agent delegates a task: Jev classifies the task and picks a model and effort profile from an explicit registry. It also has a hook-free planning aid that asks Jev once for advice before a plan is written, and a separate verifier. Docs are in Korean.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gkrtjd99/Jev_Orchestration) |
| Maintainer | [gkrtjd99](https://github.com/gkrtjd99). Independently curated. |
| Format | Node.js hooks and agent skill |
| Requirements | Node.js, Claude Code or Codex, and a TypeSafe API key; sending data to TypeSafe needs explicit consent in the installer. |
| License | [MIT](https://github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`orchestration/src/jev.mjs`](https://github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/orchestration/src/jev.mjs) at the pinned commit. |

## When to use

- Experiment with Jev routing delegated agent work to cheaper or stronger models.
- Mismatch: if you need measured savings; the author has not shown a quality or cost advantage.

## How it works

`orchestration/src/jev.mjs` calls `https://api.typesafe.ai/v1/systemone` in two stages; the default `shadow` mode only records Jev's choice, while `active` applies it. Sessions cache answers and use a circuit breaker. Integration evidence: [`orchestration/src/jev.mjs`](https://github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/orchestration/src/jev.mjs).

## Get started

Review the install plan, then install for one host.

```sh
git clone https://github.com/gkrtjd99/Jev_Orchestration
cd Jev_Orchestration
node orchestration/scripts/install.mjs --runtime claude   # shows the plan; confirm with --yes
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup (Korean): [github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/docs/SETUP.ko.md](https://github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/docs/SETUP.ko.md)
- Verification scope: [github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/docs/VERIFICATION.ko.md](https://github.com/gkrtjd99/Jev_Orchestration/blob/005d2529cf6357be51dd4ca20be7433bc6de94f8/docs/VERIFICATION.ko.md)

## Limits and data handling

The README states that quality and efficiency gains over plain Claude Code are not measured, that live `active` mode was not run, and that in a small pilot the controller mode failed grading. Installing writes to `~/.claude/settings.json` (or Codex hooks) and `~/.config/jev-hooks/`. Task summaries are sent to TypeSafe once you consent.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 005d2529cf63](https://github.com/gkrtjd99/Jev_Orchestration/tree/005d2529cf6357be51dd4ca20be7433bc6de94f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
