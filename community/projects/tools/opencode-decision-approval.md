# OpenCode Decision Approval (OpenCode V2 plugin that lets Jev approve low-risk shell permission requests and defers the rest to you)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Server-side OpenCode V2 plugin that hooks permission evaluation and sends only eligible shell commands to Jev through OpenCode's experimental Decision API as a `risk` predicate. A command at or below the configured risk threshold, after local lexical rules, can be auto-allowed with an audit log; unknown, chained, redirected or secret-touching commands, errors and timeouts all fall back to normal human approval. It starts in `dryRun` mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jiz4oh/opencode-decision-approval) |
| Maintainer | [jiz4oh](https://github.com/jiz4oh). Independently curated. |
| Format | JavaScript OpenCode plugin with a JSON config |
| Requirements | OpenCode V2 2.2.0+ server exposing the experimental decision generation API and a configured Jev model (the example uses `opencode/jev-1.13`). |
| License | [MIT](https://github.com/jiz4oh/opencode-decision-approval/blob/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/runtime.js`](https://github.com/jiz4oh/opencode-decision-approval/blob/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6/src/runtime.js) at the pinned commit. |

## When to use

- Cut permission prompts for clearly read-only shell commands in T3 Code, OpenChamber or the OpenCode TUI while keeping a human for anything unclear.
- Mismatch: the lexical filter is a heuristic, not a shell parser, and the raw command goes to the model provider.

## How it works

`src/runtime.js` calls `ctx.experimental.generate.decisions` with the configured model, and `src/decision.js` and `src/policy.js` apply the eligible-prefix rules, the `riskThreshold` and the audit write before allowing. Integration evidence: [`src/runtime.js`](https://github.com/jiz4oh/opencode-decision-approval/blob/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6/src/runtime.js).

## Get started

From the upstream README (not run on the review host):

```sh
# add the absolute plugin path to the `plugins` array of opencode.json(c)
cp examples/decision-approval.json ~/.config/opencode/decision-approval.json
# keep dryRun true until the audit log looks right, then restart OpenCode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the decision flow and safety notes: [github.com/jiz4oh/opencode-decision-approval#readme](https://github.com/jiz4oh/opencode-decision-approval#readme)
- Example configuration: [github.com/jiz4oh/opencode-decision-approval/blob/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6/examples/decision-approval.json](https://github.com/jiz4oh/opencode-decision-approval/blob/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6/examples/decision-approval.json)

## Limits and data handling

Eligible command text (and any task context inside it) goes to the model provider your OpenCode server uses; the plugin has no key store of its own. It only evaluates existing `ask` requests and cannot override explicit denies. Listed beside similar approval plugins, not as a recommendation. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 65cb80065a8a](https://github.com/jiz4oh/opencode-decision-approval/tree/65cb80065a8ab3083d68f0f6a9481d94bb1ebaf6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
