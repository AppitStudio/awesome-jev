# call-pele-answer (agent skill turning answers into interactive pages with Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source agent skill for Claude Code, Codex CLI, Cursor and OpenCode that turns a long AI answer into a single offline interactive HTML page, splitting it into blocks and choosing a diagram, table or text form for each; Jev routes block forms in about 200 ms.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dotpopo/call-pele-answer) |
| Maintainer | [dotpopo](https://github.com/dotpopo). Independently curated. |
| Format | Agent skill and Node.js CLI |
| Requirements | Node.js 18+ (no npm install); an agent such as Claude Code; optional TypeSafe API key (a free endpoint or local rules also work). |
| License | [MIT](https://github.com/dotpopo/call-pele-answer/blob/20b819d4985328ffae735c1bc0d2380921213d80/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/ytiomin/status/2113572737264525485)). |
| Jev evidence | [`skills/call-pele-answer/scripts/routers/systemone.mjs`](https://github.com/dotpopo/call-pele-answer/blob/20b819d4985328ffae735c1bc0d2380921213d80/skills/call-pele-answer/scripts/routers/systemone.mjs) at the pinned commit. |

## When to use

- Make long agent answers readable as diagrams, tables and switchable views.
- Recolor and annotate blocks, then hand notes back to your agent.
- Mismatch: output is a static HTML page, not a hosted app.

## How it works

`skills/call-pele-answer/scripts/routers/systemone.mjs` is the System One adapter: it scores candidate forms per block with `jev-latest` against TypeSafe directly or another `/v1/systemone` endpoint, with keys read from the environment and never written into pages. Integration evidence: [`skills/call-pele-answer/scripts/routers/systemone.mjs`](https://github.com/dotpopo/call-pele-answer/blob/20b819d4985328ffae735c1bc0d2380921213d80/skills/call-pele-answer/scripts/routers/systemone.mjs).

## Get started

In Claude Code (not run on the review host):

```sh
/plugin marketplace add dotpopo/call-pele-answer
/plugin install call-pele-answer@call-pele-answer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/dotpopo/call-pele-answer/blob/main/README.en.md](https://github.com/dotpopo/call-pele-answer/blob/main/README.en.md)
- Promo video: [github.com/dotpopo/call-pele-answer/blob/main/docs/promo.mp4](https://github.com/dotpopo/call-pele-answer/blob/main/docs/promo.mp4)

## Limits and data handling

Answer blocks are sent to the configured routing endpoint when Jev routing is on.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 20b819d49853](https://github.com/dotpopo/call-pele-answer/tree/20b819d4985328ffae735c1bc0d2380921213d80). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
