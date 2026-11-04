# Skill Studio (desktop and CLI eval studio for agent skills that grades outputs with code checks and Jev judge packs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Electron desktop app, local web server and CLI for writing agent skills, giving them cases, running headless Claude Code or Cursor agents on them and grading outputs with code checks plus TypeSafe Jev judge packs. Judge answers are stored so you can reweight without new calls, a blind review queue calibrates the judges against your own ratings, and labelled anchors gate whether a pack can be trusted. Without a key it runs code checks only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/milesroxas/skill-studio) |
| Maintainer | [milesroxas](https://github.com/milesroxas). Independently curated. |
| Format | TypeScript pnpm project (Electron app, `st` CLI and local server) |
| Requirements | Node 24 and pnpm; a TypeSafe API key for judged layers; the `claude` or `cursor-agent` CLI signed in to generate outputs. |
| License | [MIT](https://github.com/milesroxas/skill-studio/blob/907e013c5844678ee7c0f7b16d400bc3c16b5135/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judges/design/index.ts`](https://github.com/milesroxas/skill-studio/blob/907e013c5844678ee7c0f7b16d400bc3c16b5135/src/judges/design/index.ts) at the pinned commit. |

## When to use

- Measure whether a skill edit improved subjective outputs (writing, HTML, agent process) with stored Jev judgments and your own blind ratings.
- Mismatch: it needs your TypeSafe key and a signed-in coding-agent CLI, and judge answers are only trusted after anchors pass.

## How it works

`src/judges/design/index.ts` builds Jev judge packs with the TypeSafe SDK (`noul` and image questions) that `src/application/grade.ts` runs per case; without `TYPESAFE_API_KEY` grading leaves every judged layer null. Integration evidence: [`src/judges/design/index.ts`](https://github.com/milesroxas/skill-studio/blob/907e013c5844678ee7c0f7b16d400bc3c16b5135/src/judges/design/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
pnpm dev                                  # desktop app
pnpm st run <skill-dir> --engine claude --model sonnet --name "v0 first draft"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with setup, the eval loop and the CLI: [github.com/milesroxas/skill-studio#readme](https://github.com/milesroxas/skill-studio#readme)
- Guide: [github.com/milesroxas/skill-studio/blob/907e013c5844678ee7c0f7b16d400bc3c16b5135/docs/guide.md](https://github.com/milesroxas/skill-studio/blob/907e013c5844678ee7c0f7b16d400bc3c16b5135/docs/guide.md)

## Limits and data handling

Each judged case sends the agent's output (and images, for image-based packs) to TypeSafe on your key, billed there; agent runs use your coding-agent subscription. The server mode is meant for your own Tailscale login only. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 907e013c5844](https://github.com/milesroxas/skill-studio/tree/907e013c5844678ee7c0f7b16d400bc3c16b5135). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
