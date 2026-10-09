# prose-check

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for Claude Code, Codex, and Muse Code that checks the agent's final reply each turn against the writing rules in `CLAUDE.md` or `AGENTS.md` using TypeSafe Jev, and asks the agent to rewrite once when a rule is broken.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vgeshel/prose-check) |
| Maintainer | [vgeshel](https://github.com/vgeshel). Independently curated. |
| Format | Agent plugin + marketplace for Claude Code, Codex, and Muse Code |
| Requirements | `TYPESAFE_API_KEY`; Claude Code with function hooks (tested 2.1.294) or Bun for Codex/Muse Code. |
| License | [MIT](https://github.com/vgeshel/prose-check/blob/46654c64679b331727fcda0c935dd6d3fe5f7ba7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Enforce project writing rules on agent replies automatically.
- Mismatch: one Jev request per checked reply; Claude Code function hooks are early access.

## How it works

Hooks read the loaded instruction file's writing rules and ask Jev whether the final reply breaks them; a failure triggers one rewrite. (Summarized from the upstream [README](https://github.com/vgeshel/prose-check/blob/46654c64679b331727fcda0c935dd6d3fe5f7ba7/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `claude plugin marketplace add vgeshel/prose-check` then `claude plugin install prose-check@prose-check`.

## Limits and data handling

Replies and rules are sent to TypeSafe; see the README's 'Data and cost' section. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 46654c64679b](https://github.com/vgeshel/prose-check/tree/46654c64679b331727fcda0c935dd6d3fe5f7ba7). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
