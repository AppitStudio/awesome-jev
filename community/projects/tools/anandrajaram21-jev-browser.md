# jev-browser by anandrajaram21 (fast bug-reproduction browser agent where agent-browser acts, Jev makes every decision and small models write the rest)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Hand a bug report (for example `gh issue view 123`) to `jev-browser` and it drives Vercel's agent-browser through the app until it reports REPRODUCED, not reproduced or unclear, with the cost of the run. TypeSafe Jev makes every navigation and verdict decision, including from screenshots; small Groq-hosted models via OpenRouter write the little text that must be typed and the report. Ships as a standalone binary with an agent skill for Claude Code, Codex and Cursor. The maker's benchmark shows five reports reproduced 2.2× faster than a coding agent driving agent-browser itself, at about $0.0005–0.0008 each.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anandrajaram21/jev-browser) |
| Maintainer | [anandrajaram21](https://github.com/anandrajaram21). Independently curated. |
| Format | Standalone CLI binary (Bun/TypeScript) and agent skill; npm and Homebrew |
| Requirements | agent-browser 0.41+ with Chrome, a TypeSafe API key and an OpenRouter key; macOS, Linux or Windows. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/agent.ts`](https://github.com/anandrajaram21/jev-browser/blob/ea8ee30bf8cbec2137e09a88c14219d09c7b0a3d/src/agent.ts) at the pinned commit. |

## When to use

- Let a coding agent offload bug reproduction to a cheaper, faster browser loop.
- Mismatch: long scripted end-to-end suites; it is built for short repro goals.

## How it works

`src/agent.ts` uses `TypeSafeClient` from `@typesafe-ai/sdk` with `choice`, `noul` and image inputs for each step; `src/setup.ts` runs a live connectivity check with `jev-latest`. Integration evidence: [`src/agent.ts`](https://github.com/anandrajaram21/jev-browser/blob/ea8ee30bf8cbec2137e09a88c14219d09c7b0a3d/src/agent.ts).

## Get started

Install agent-browser and jev-browser, save both keys, install the skill and run the doctor.

```sh
npm i -g agent-browser && agent-browser install
npm i -g @anandrajaram21/jev-browser    # or the install.sh / Homebrew options in the README
jev-browser setup && jev-browser install-skill && jev-browser doctor
gh issue view 123 | jev-browser --session repro --report -
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/anandrajaram21/jev-browser/blob/ea8ee30bf8cbec2137e09a88c14219d09c7b0a3d/README.md](https://github.com/anandrajaram21/jev-browser/blob/ea8ee30bf8cbec2137e09a88c14219d09c7b0a3d/README.md)
- Releases: [github.com/anandrajaram21/jev-browser/releases](https://github.com/anandrajaram21/jev-browser/releases)

## Limits and data handling

Page text and screenshots go to TypeSafe and planner/text prompts to OpenRouter, on your keys saved in a local config file (mode 600). Benchmark figures are the maker's own, on five reports. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit ea8ee30bf8cb](https://github.com/anandrajaram21/jev-browser/tree/ea8ee30bf8cbec2137e09a88c14219d09c7b0a3d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
