# pi-herdr-orchestrator (Pi subagents in herdr panes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding agent extension that runs each subagent as a real Pi session in a herdr terminal pane, returns results through written report files, and can add optional Jev gates that classify each handoff.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HaiYangMa13/pi-herdr-orchestrator) |
| Maintainer | [HaiYangMa13](https://github.com/HaiYangMa13). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 0.60+, herdr with its Pi integration; optional TypeSafe key (`jev.apiKey` in config or `TYPESAFE_API_KEY`) for the Jev gates. |
| License | [MIT](https://github.com/HaiYangMa13/pi-herdr-orchestrator/blob/f4bffe8c2db6a9ad69273cf8fe95a98920dd2c2b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/HaiYangMa13/pi-herdr-orchestrator/blob/f4bffe8c2db6a9ad69273cf8fe95a98920dd2c2b/src/jev.ts) at the pinned commit. |

## When to use

- Watch, attach to and scroll every subagent instead of waiting on an invisible in-process one.
- Add cheap Jev checks on handoffs and routing between subagents.
- Mismatch: Jev is optional; without herdr there is nothing to run.

## How it works

When configured, `src/jev.ts` posts narrow classification questions to `https://api.typesafe.ai/v1/systemone` on each handoff, and the agent descriptions are what the Jev router matches when no definition is given; results come back as `result.md` files that wake the parent. Integration evidence: [`src/jev.ts`](https://github.com/HaiYangMa13/pi-herdr-orchestrator/blob/f4bffe8c2db6a9ad69273cf8fe95a98920dd2c2b/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
herdr integration install pi
pi install npm:pi-herdr-orchestrator
# optional: set jev.apiKey in ~/.pi/agent/pi-herd/config.json or export TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes: [github.com/HaiYangMa13/pi-herdr-orchestrator/blob/main/DESIGN.md](https://github.com/HaiYangMa13/pi-herdr-orchestrator/blob/main/DESIGN.md)
- Jev gates section in the README: [github.com/HaiYangMa13/pi-herdr-orchestrator#readme](https://github.com/HaiYangMa13/pi-herdr-orchestrator#readme)

## Limits and data handling

With Jev gates on, handoff text is sent to TypeSafe. Community project, not affiliated with TypeSafe, Pi or herdr.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit f4bffe8c2db6](https://github.com/HaiYangMa13/pi-herdr-orchestrator/tree/f4bffe8c2db6a9ad69273cf8fe95a98920dd2c2b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
