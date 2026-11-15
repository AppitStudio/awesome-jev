# dsh-jev-planning (DeepSeek Harness plugin that runs staged planning through a Jev judge and holds writes until the exact plan file is approved)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for DeepSeek Harness, ported from the Jevstice extension for oh-my-pi. Three tools split the owner's request into checkable requirements, review a Markdown plan in outline, detail and final phases, and answer one-off typed decisions. Until a final plan is approved, a gate refuses writes, edits, mutating shell commands, delegation and plugin changes (reading stays allowed); the approval is bound to the plan's exact bytes and drops if the file changes. `/jev status` reports the stage without any judge call.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bondiano/dsh-jev-planning) |
| Maintainer | [bondiano](https://github.com/bondiano). Independently curated. |
| Format | DeepSeek Harness plugin (JavaScript) |
| Requirements | DeepSeek Harness, and a key for at least one Jev route: OpenCode, OpenRouter or TypeSafe. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.js`](https://github.com/bondiano/dsh-jev-planning/blob/310af7d3700e3d34080dcc73e6a7d399fdc2e44e/index.js) at the pinned commit. |

## When to use

- Force a coding agent to get a judged plan before it changes anything.
- Mismatch: quick one-line edits; the gate deliberately slows consequential work.

## How it works

`index.js` tries judges in order: OpenCode's System One endpoint (`jev-1.13-free`), OpenRouter's decisions API (`~typesafe/jev-latest`) and TypeSafe (`https://api.typesafe.ai/v1/systemone`, `jev-latest`); a provider without a key is skipped and, with none, the tools report unavailability instead of approving. Integration evidence: [`index.js`](https://github.com/bondiano/dsh-jev-planning/blob/310af7d3700e3d34080dcc73e6a7d399fdc2e44e/index.js).

## Get started

Add the plugin to your DeepSeek Harness loader configuration and provide one judge key.

```sh
git clone https://github.com/bondiano/dsh-jev-planning
export TYPESAFE_API_KEY=...    # or OPENROUTER_API_KEY / OPENCODE_API_KEY
# add '@local/dsh-jev-planning' (planDir: .dsh/jev) to the DSH plugin rows, as shown in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bondiano/dsh-jev-planning/blob/310af7d3700e3d34080dcc73e6a7d399fdc2e44e/README.md](https://github.com/bondiano/dsh-jev-planning/blob/310af7d3700e3d34080dcc73e6a7d399fdc2e44e/README.md)

## Limits and data handling

Requirements, plan sections and decision questions go to whichever judge provider has a key; keys are read from the environment or the DSH credential store and never stored by the plugin. Version 0.1.0, private package. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 310af7d3700e](https://github.com/bondiano/dsh-jev-planning/tree/310af7d3700e3d34080dcc73e6a7d399fdc2e44e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
