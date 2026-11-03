# wlf-jev (agent skill that designs, wires in and calibrates Jev questions in your codebase)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill for Claude Code, Codex, Copilot CLI and any agent that reads skills: it turns "classify, check, score or route X" into Jev typed questions, writes the code from templates (classifier, guard check, batch run, an ask-Jev agent tool), and calibrates thresholds against a labelled set. Its rule: Jev makes judgments, code makes decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/theamazingwolf/skills) |
| Maintainer | [theamazingwolf](https://github.com/theamazingwolf). Independently curated. |
| Format | Agent skill pack (TypeScript templates + Node scripts) |
| Requirements | An agent that reads skills; Node 22+ and a TypeSafe API key for live calibration runs. |
| License | [MIT](https://github.com/theamazingwolf/skills/blob/b76ffa9285d09dd61f02ded9301a848eb10b8b23/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/wlf-skills/skills/wlf-jev/assets/templates/ask-jev-tool.ts`](https://github.com/theamazingwolf/skills/blob/b76ffa9285d09dd61f02ded9301a848eb10b8b23/plugins/wlf-skills/skills/wlf-jev/assets/templates/ask-jev-tool.ts) at the pinned commit. |

## When to use

- Add a calibrated Jev classifier or guard to a project with your coding agent's help.
- Mismatch: it helps you build Jev questions; it is not a ready-made app.

## How it works

Templates such as `ask-jev-tool.ts` use `TypeSafeClient` from `@typesafe-ai/sdk` 0.7.x, and `scripts/run-questions.mjs` runs a question spec over a labelled dataset live or in mock mode to measure accuracy before thresholds are set. Integration evidence: [`plugins/wlf-skills/skills/wlf-jev/assets/templates/ask-jev-tool.ts`](https://github.com/theamazingwolf/skills/blob/b76ffa9285d09dd61f02ded9301a848eb10b8b23/plugins/wlf-skills/skills/wlf-jev/assets/templates/ask-jev-tool.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add theamazingwolf/skills --skill wlf-jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skill folder: [github.com/theamazingwolf/skills/tree/main/plugins/wlf-skills/skills/wlf-jev](https://github.com/theamazingwolf/skills/tree/main/plugins/wlf-skills/skills/wlf-jev)

## Limits and data handling

Anything placed in a question's state is sent to TypeSafe on your key; templates screen secret-like text first. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit b76ffa9285d0](https://github.com/theamazingwolf/skills/tree/b76ffa9285d09dd61f02ded9301a848eb10b8b23). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
