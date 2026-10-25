# Overseer and workflow gate (Claude Code plan runner and approval gate, with optional Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Two Claude Code plugins: Overseer runs a project's PLAN.md through the sessions you pick and judges finished work against the plan within a weekly budget, and the workflow gate blocks the Workflow tool until you approve the plan; with a TypeSafe key, Jev suggests intent, model and agent type, scores review findings and checks whether spend delivered.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VictorGjn/overseer) |
| Maintainer | [VictorGjn](https://github.com/VictorGjn). Independently curated. |
| Format | Claude Code plugins (Node.js hooks and browser editor) |
| Requirements | Claude Code and Node 20+; a TypeSafe API key only for the Jev features. |
| License | [MIT](https://github.com/VictorGjn/overseer/blob/2383d1fb3bcddd41072637614a4cd93f575ef901/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/workflow-gate/hooks/advise.mjs`](https://github.com/VictorGjn/overseer/blob/2383d1fb3bcddd41072637614a4cd93f575ef901/plugins/workflow-gate/hooks/advise.mjs) at the pinned commit. |

## When to use

- Approve agent workflow plans before they run, in the browser or terminal.
- Get a Jev suggestion of which agent type and model each step needs.
- Mismatch: every Jev feature is off without `TYPESAFE_API_KEY`.

## How it works

`plugins/workflow-gate/hooks/advise.mjs` posts agent missions and your agent-type descriptions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) from the local server, so the key never reaches the browser. Integration evidence: [`plugins/workflow-gate/hooks/advise.mjs`](https://github.com/VictorGjn/overseer/blob/2383d1fb3bcddd41072637614a4cd93f575ef901/plugins/workflow-gate/hooks/advise.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add VictorGjn/overseer
/plugin install overseer@overseer
/plugin install workflow-gate@overseer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Workflow gate README: [github.com/VictorGjn/overseer/blob/main/plugins/workflow-gate/README.md](https://github.com/VictorGjn/overseer/blob/main/plugins/workflow-gate/README.md)
- README: [github.com/VictorGjn/overseer#readme](https://github.com/VictorGjn/overseer#readme)

## Limits and data handling

With a key set, agent missions and agent-type descriptions go to TypeSafe; the editor header says so.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 2383d1fb3bcd](https://github.com/VictorGjn/overseer/tree/2383d1fb3bcddd41072637614a4cd93f575ef901). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
