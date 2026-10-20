# ClauJev (Jev checks for Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that asks Jev short typed questions on six hooks to triage each request, pick the reasoning effort, guard destructive or credential-touching commands, review edits against plain-language rules and block an unfinished "done".

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Civalski/claujev) |
| Maintainer | [Civalski](https://github.com/Civalski). Independently curated. |
| Format | Claude Code plugin (Node.js hooks) |
| Requirements | Claude Code; a TypeSafe API key (asked for at install). |
| License | [MIT](https://github.com/Civalski/claujev/blob/cf25934c3579b0e8c0f654c04fbe9856061b7ffa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/claujev/hooks/claujev.mjs`](https://github.com/Civalski/claujev/blob/cf25934c3579b0e8c0f654c04fbe9856061b7ffa/plugins/claujev/hooks/claujev.mjs) at the pinned commit. |

## When to use

- Add a cheap second opinion to Claude Code sessions: command confirmation, rule checks and a final completeness check.
- Let a decision model set the effort level per request instead of a fixed setting.
- Mismatch: Claude Code only; checks add about 400 ms each, per the README.

## How it works

ClauJev listens to six Claude Code hooks. For each one it builds a small state (the request, the command or the diff), asks Jev typed questions and returns an action to Claude, or nothing. Integration evidence: [`plugins/claujev/hooks/claujev.mjs`](https://github.com/Civalski/claujev/blob/cf25934c3579b0e8c0f654c04fbe9856061b7ffa/plugins/claujev/hooks/claujev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin install claujev --marketplace Civalski/claujev
# enter your TypeSafe key, restart Claude Code, then /claujev:configure
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands table and how-it-works section in the README: [github.com/Civalski/claujev#readme](https://github.com/Civalski/claujev#readme)

## Limits and data handling

Requests, commands and diffs are sent to TypeSafe for each check. Community project, not affiliated with TypeSafe AI or Anthropic. The author's cost figure (US$0.07 for six days) is self-reported.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit cf25934c3579](https://github.com/Civalski/claujev/tree/cf25934c3579b0e8c0f654c04fbe9856061b7ffa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
