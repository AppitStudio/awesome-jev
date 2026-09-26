# stingray

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code/Codex Stop hook: TypeSafe Jev catches half-done turns (no action, broken promise, empty watch, wrong language).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nanako0129/stingray) |
| Maintainer | [Nanako0129](https://github.com/Nanako0129). Independently curated. |
| Format | Shell Stop hook for Claude Code and Codex. |
| Requirements | bash; TypeSafe API key for Jev; Claude Code or Codex Stop hook wiring per upstream. |
| License | [MIT](https://github.com/Nanako0129/stingray/blob/473071aed66df074ee1e2b85832d4e1fa082f77b/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when agent turns often **announce work then exit** without tools. Prefer softer nudge hooks when you only want advisory continue prompts.

## How it works

On Stop, sends turn/context judgments to TypeSafe Jev and intercepts premature exits with a nudge; counts running background jobs locally.

## Get started

```sh
git clone https://github.com/Nanako0129/stingray.git
cd stingray
git checkout 473071aed66df074ee1e2b85832d4e1fa082f77b
# Install as Claude Code / Codex Stop hook per README; needs TypeSafe key
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 473071a](https://github.com/Nanako0129/stingray/tree/473071aed66df074ee1e2b85832d4e1fa082f77b). AI-assisted README and license inspection; install/live paths not executed.
