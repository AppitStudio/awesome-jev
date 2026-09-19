# pi-warden

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Pi coding-agent extension that combines local checks with Jev judgments to hold selected actions, flag project-rule violations and steer stalled work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DevMortimer/pi-warden) |
| Maintainer | [Ryan Gapac / DevMortimer](https://github.com/DevMortimer) |
| Format | TypeScript · Pi extension and reusable guard modules; version 0.29.1 |
| Jev's role | Judges action scope/irreversibility, rule violations, code/output concerns, completion claims and selected context-retention decisions. |
| Requirements | Node.js 22.19+, Pi 0.85.1+ below 1.0; `pi-typesafe` dependency. Provider credentials for model judgments; local checks can run without a key. |
| Access and costs | MIT source/npm package; live judgments incur provider usage and steering can add coding-agent turns. No app purchase requirement was found. |
| License | [MIT](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/LICENSE) |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use it to explore a supervisory layer for Pi: identify destructive command patterns,
feed rule violations back to a coding agent, flag repeated failures, and retain useful
parts of long tool output. It is an advisory and workflow-control integration, not a
sandbox or a guarantee that an action is safe, authorized or correctly reviewed.

## How it works

The [action guard](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/src/guard.ts)
first checks local patterns and configured policies. Recognized read-only operations can
skip model calls. Jev then answers narrow questions over redacted, bounded action and
conversation summaries. Code combines probabilities with configured thresholds and the
local verdict; model judgments normally cannot reduce the local pattern floor.

The default `steer` mode blocks a held action and sends feedback to the agent. `confirm`
asks through the UI; `advise` generally does not block. Explicit user command rules can
have their own dialog/deny semantics. Rule and quality findings generally let writes
proceed and send corrective feedback. At this commit off-task steering is trace-only,
a narrower behavior than some prose documentation suggests.

The [backend adapter](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/src/backend.ts)
uses `pi-typesafe` for TypeSafe by default, with optional OpenRouter routing. The catalog
review inspected this integration boundary, not the dependency's live wire behavior or
an exact resolved Jev model revision. Returned model identifiers are retained in verdicts.

## Get started

With a compatible Pi and Node installation:

```sh
pi install npm:pi-warden
```

Inside Pi, run `/warden enable` and review the data notice. Skip key entry for local-only
pattern and runaway checks. Model-backed rule judgments need a TypeSafe key, supplied
privately through the setup UI or `TYPESAFE_API_KEY`. The shared `pi-typesafe` keystore
stores a UI-entered key in owner-only user configuration.

Use `/warden status` to inspect active settings and `ctrl+shift+w` for traces. The upstream
`/warden test` command uses synthetic input, but with a live backend it can still incur a
provider request; synthetic input does not imply an offline transport.

For project-specific rules, create `pi-warden.md` with one rule per Markdown heading,
optionally scoped by a `paths:` line. Start with the
[configuration examples](https://github.com/DevMortimer/pi-warden/tree/c9921c3ebc48f62348199eb03119c645d98cdb8b/examples).
A model-backed write check sends sampled code and applicable rules to the provider.
Inspect the resulting trace and feedback before relying on the policy in routine work.

## Examples and demos

- [Session examples](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/docs/examples.md) describe upstream guard behavior and trace output.
- [Configuration guide](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/docs/configuration.md) documents user/project policies, exclusions, thresholds and backend selection.
- [Test suite](https://github.com/DevMortimer/pi-warden/tree/c9921c3ebc48f62348199eb03119c645d98cdb8b/tests) includes fake-judge guard cases, redaction, hold handling, rule loading, context retention and UI tests. The documented offline development command is `npm run check` after installing dependencies.

## Limits and data handling

By default, a provider failure keeps the local verdict and permits calls that the local
checks did not already hold, with an error reason (`action.failOpen: true`). Setting it
false raises the result to a hold. Request limits eventually leave only offline checks.
Thresholds, sampled excerpts and narrow pattern matching can miss meaningful problems;
quality notices and suspected security issues often steer rather than block.

A held retry may interpret a later user message as approval using Jev or an offline
text heuristic. This is part of the extension's implementation, not proof that its
interpretation of authorization is correct. Review policies for consequential actions.

The [data-handling guide](https://github.com/DevMortimer/pi-warden/blob/c9921c3ebc48f62348199eb03119c645d98cdb8b/docs/data-handling.md)
lists prompt/history excerpts, commands, paths, sampled source and tool output that may
reach TypeSafe or OpenRouter. Redaction is best-effort, not guaranteed removal of secrets.
Configured rule exclusions are useful when code must remain local.

Local state includes consent/settings, an owner-only key file, hold outcome logs and
full compressed-tool-output copies in temporary files. Those full copies can contain
secrets and persist until removed. Upstream benchmark and stability reports were not
reproduced; neither source inspection nor synthetic tests establish production protection.

## Review and maintenance

Reviewed **2026-09-19** at
[`c9921c3ebc48f62348199eb03119c645d98cdb8b`](https://github.com/DevMortimer/pi-warden/tree/c9921c3ebc48f62348199eb03119c645d98cdb8b).
Inspected README, MIT license, package/peer requirements, backend adapter, action guard,
configuration defaults, extension call sites, rule-check integration, data-handling docs,
examples and representative fake-judge tests. No package installation, test execution,
Pi session, live provider request or upstream benchmark was performed.
