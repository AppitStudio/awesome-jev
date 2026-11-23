# opencode-ensemble-jev by allcupsnotinprivate (OpenCode plugin where Jev assesses each Ensemble teammate's task to pick its coding model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

When OpenCode Ensemble spawns a teammate, Jev answers typed questions about the task (capability tier, complexity, planning, parallel work, isolation, review) and the plugin maps the tier to an explicitly allowed `provider/model`, enforces local constraints and records the decision.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/allcupsnotinprivate/opencode-ensemble-jev) |
| Maintainer | [allcupsnotinprivate](https://github.com/allcupsnotinprivate). Independently curated. |
| Format | OpenCode V2 server plugin (TypeScript, Bun) |
| Requirements | OpenCode 2.3.2 and Ensemble 0.21.5 (tested), Git and Bun; an OpenRouter API key. |
| License | [MIT](https://github.com/allcupsnotinprivate/opencode-ensemble-jev/blob/0a69498d5b6c0c77a9bf24045de59e3ced1f0754/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/allcupsnotinprivate/opencode-ensemble-jev/blob/0a69498d5b6c0c77a9bf24045de59e3ced1f0754/src/jev/client.ts) at the pinned commit. |

## When to use

- Spend strong models only on Ensemble tasks that need them.
- Mismatch: plain OpenCode without Ensemble.

## How it works

`src/jev/client.ts` calls Jev through the OpenRouter Decisions API (default model `typesafe/jev-1.13`, configured in `src/config.ts`). Integration evidence: [`src/jev/client.ts`](https://github.com/allcupsnotinprivate/opencode-ensemble-jev/blob/0a69498d5b6c0c77a9bf24045de59e3ced1f0754/src/jev/client.ts).

## Get started

Install Ensemble, install this plugin's dependencies, and add its absolute path to the project's `opencode.json`.

```sh
opencode plugin add @hueyexe/opencode-ensemble@0.21.5
git clone https://github.com/allcupsnotinprivate/opencode-ensemble-jev.git && cd opencode-ensemble-jev
bun install --frozen-lockfile   # then add this path to opencode.json plugins
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example config: [github.com/allcupsnotinprivate/opencode-ensemble-jev/blob/0a69498d5b6c0c77a9bf24045de59e3ced1f0754/examples/ensemble-jev.json](https://github.com/allcupsnotinprivate/opencode-ensemble-jev/blob/0a69498d5b6c0c77a9bf24045de59e3ced1f0754/examples/ensemble-jev.json)

## Limits and data handling

Task descriptions are sent to OpenRouter and TypeSafe. Reaches Jev through OpenRouter, not TypeSafe directly.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 0a69498d5b6c](https://github.com/allcupsnotinprivate/opencode-ensemble-jev/tree/0a69498d5b6c0c77a9bf24045de59e3ced1f0754). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
