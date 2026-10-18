# memory-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code project memory that keeps only facts still true (SQLite, revalidated on use), plus an injected-context mod where Jev answers one yes/no per rule file to decide which long domain rules enter the prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jsilva74/memory-gate) |
| Maintainer | [jsilva74](https://github.com/jsilva74). Independently curated. |
| Format | Claude Code hooks + mods (shell/Python) |
| Requirements | Claude Code; TypeSafe key for the injected-context mod. |
| License | [MIT](https://github.com/jsilva74/memory-gate/blob/7b22062caeedc621d762e1b156d150bf13881b41/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mods/injected-context/hooks/jev.sh`](https://github.com/jsilva74/memory-gate/blob/7b22062caeedc621d762e1b156d150bf13881b41/mods/injected-context/hooks/jev.sh) at the pinned commit. |

## When to use

- Keep agent memory accurate across sessions.
- Load only the rule files that apply to a request.
- Mismatch: Claude Code only; the Jev mod adds a translation call for non-English prompts.

## How it works

`mods/injected-context/hooks/jev.sh` asks Jev whether the requested work falls under each rule file description; matching files are injected once per session. Integration evidence: [`mods/injected-context/hooks/jev.sh`](https://github.com/jsilva74/memory-gate/blob/7b22062caeedc621d762e1b156d150bf13881b41/mods/injected-context/hooks/jev.sh).

## Get started

From the upstream README: install the hooks into Claude Code, then enable the injected-context mod with your TypeSafe key.

```sh
git clone https://github.com/jsilva74/memory-gate
# see README to install hooks and mods
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- LinkedIn article linked in README

## Limits and data handling

Prompt text and rule descriptions go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7b22062caeed](https://github.com/jsilva74/memory-gate/tree/7b22062caeedc621d762e1b156d150bf13881b41). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
