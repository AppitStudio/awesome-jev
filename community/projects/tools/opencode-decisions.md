# opencode-decisions by atvari-eu (OpenCode plugin that wires System One decisions, Jev by default, into screening, approvals, model routing and done-checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode 2 plugin that adds decision-model judgments to the agent with no companion skill. It screens tool results for junk and prompt injection (failing closed), scrubs known secret formats with plain regex, gives the agent `jev_decide`, `jev_judge_many` and `jev_screen` tools, and can pick the model and effort per turn, vet permission requests, check whether the agent stopped early, and decide which tool calls to keep when compacting. Several features are off by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atvari-eu/opencode-decisions) |
| Maintainer | [atvari-eu](https://github.com/atvari-eu). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode 2 and access to a System One deployment: `TYPESAFE_API_KEY`, `OPENCODE_API_KEY` or an `opencode auth login` session. |
| License | [MIT](https://github.com/atvari-eu/opencode-decisions/blob/3cfec664ff44c625f3f825796fca11b5584966d7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/logic.ts`](https://github.com/atvari-eu/opencode-decisions/blob/3cfec664ff44c625f3f825796fca11b5584966d7/src/logic.ts) at the pinned commit. |

## When to use

- Add screening, approvals and routing driven by a cheap typed decision model inside OpenCode.
- Mismatch: the package is at version 0.1.0 and the more invasive features (approvals, done-check, compaction) are off until you turn them on.

## How it works

`src/logic.ts` resolves a System One deployment (the default is OpenCode's Console System One route; `TYPESAFE_API_KEY` is accepted) and ping-checks it at start; judged features fail closed on errors, and clean verdicts write nothing to the transcript. Integration evidence: [`src/logic.ts`](https://github.com/atvari-eu/opencode-decisions/blob/3cfec664ff44c625f3f825796fca11b5584966d7/src/logic.ts).

## Get started

From the upstream README (not run on the review host):

```sh
opencode plugin add github:atvari-eu/opencode-decisions
# restart OpenCode, then see the README's provider and credentials section
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the feature table and install options: [github.com/atvari-eu/opencode-decisions#readme](https://github.com/atvari-eu/opencode-decisions#readme)

## Limits and data handling

Tool results and prompts that are screened or judged go to the configured System One deployment on your credentials. The plugin is v0.1.0 and its judged features fail closed on errors, which can withhold content. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 3cfec664ff44](https://github.com/atvari-eu/opencode-decisions/tree/3cfec664ff44c625f3f825796fca11b5584966d7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
