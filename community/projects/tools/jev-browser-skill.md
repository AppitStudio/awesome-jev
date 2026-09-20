# Jev Browser Skill

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Reference Claude Code / Codex skill: TypeSafe Jev chooses browser operations and targets from a code-built element table (no planner LLM). Pedagogical companion to fuller agents such as Jev Ultrafast.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zurfyx/jev-browser-skill) |
| Maintainer | [zurfyx](https://github.com/zurfyx). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill (`SKILL.md`) plus dependency-free `scripts/*.mjs` and an explainer site ([jev-browser.vercel.app](https://jev-browser.vercel.app)). |
| Requirements | Chromium/Chrome for CDP automation; `TYPESAFE_API_KEY` or equivalent for live Jev (`scripts/jev.mjs` posts to `https://api.typesafe.ai/v1/systemone`). |
| License | [MIT](https://github.com/zurfyx/jev-browser-skill/blob/7db9b4cf1cfca82f0742c75054e22cb8089ee908/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and skill scripts inspected. No automated unit suite; live browser/Jev runs were not executed on the review host. |

## When to use

Use it to learn or install a minimal Jev-driven browser loop inside Claude Code or Codex, or to walk the explainer site’s recorded Hacker News trace. Prefer [Jev Ultrafast](jev-ultrafast.md) or [Jev Browser (tontoko)](jev-browser-tontoko.md) for production-oriented Playwright agents with helpers, region narrowing, and richer guards. Cap of ~250 visible controls per page is intentional teaching surface.

## How it works

[`scripts/core.mjs`](https://github.com/zurfyx/jev-browser-skill/blob/7db9b4cf1cfca82f0742c75054e22cb8089ee908/scripts/core.mjs) observes a numbered control table, builds one multi-question System One request (operation + speculative targets), and [`readDecision`](https://github.com/zurfyx/jev-browser-skill/blob/7db9b4cf1cfca82f0742c75054e22cb8089ee908/scripts/core.mjs) accepts only offered indices. [`scripts/jev.mjs`](https://github.com/zurfyx/jev-browser-skill/blob/7db9b4cf1cfca82f0742c75054e22cb8089ee908/scripts/jev.mjs) calls `api.typesafe.ai/v1/systemone`. Browser code executes CDP input events; secrets typed into password fields never enter the Jev request. Jev never generates field text—values come from `--text` / `--secret` flags.

## Get started

```sh
git clone https://github.com/zurfyx/jev-browser-skill.git
cd jev-browser-skill
git checkout 7db9b4cf1cfca82f0742c75054e22cb8089ee908
# Install as a Claude Code / Codex skill per upstream SKILL.md, or run scripts with a key:
# TYPESAFE_API_KEY=… node scripts/…   # see README for goal CLI
```

Explainer without a key: open [jev-browser.vercel.app](https://jev-browser.vercel.app) (walks a committed trace).

## Examples and demos

- Upstream [`docs/demo.gif`](https://github.com/zurfyx/jev-browser-skill/blob/7db9b4cf1cfca82f0742c75054e22cb8089ee908/docs/demo.gif) / MP4 and Hacker News login→search trace.
- Site step-through of recorded decisions (no live Jev required for the walkthrough).
- No package-level automated test script in-repo at this revision.

## Limits and data handling

Page text and control labels leave the machine on each Jev step. At most ~255 options per question; large pages need region narrowing (Ultrafast). Probabilities are for debugging—not proof of task success. Upstream timing tables are author-measured, not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 7db9b4c](https://github.com/zurfyx/jev-browser-skill/tree/7db9b4cf1cfca82f0742c75054e22cb8089ee908): MIT. AI-assisted source review of `scripts/core.mjs`, `scripts/jev.mjs`, `SKILL.md`, README, and LICENSE. No `npm test` target; no live CDP or TypeSafe calls on the review host.

Related: [Jev Ultrafast](jev-ultrafast.md), [Jev Browser (tontoko)](jev-browser-tontoko.md), [pi-Jev-browser](pi-jev-browser.md), [JevOnly](jevonly.md).
