# decision-playwright by Cheolmin Ki (Playwright skill for Copilot CLI and Claude Code where a decision model clicks and the host agent types)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Agent Skill that drives a real browser with Playwright. A decision model (TypeSafe Jev by default, or Microsoft-Decision-1.1 on Azure) chooses clicks, scrolling, dropdown options and navigation; when text is needed it stops with `NEEDS_TYPING` and the host agent's LLM types before handing control back.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cheolmin/decision-playwright) |
| Maintainer | [cheolmin](https://github.com/cheolmin). Independently curated. |
| Format | Agent Skill (Node.js scripts, Playwright) |
| Requirements | Node.js 18+, Chrome or Chromium, GitHub Copilot CLI or Claude Code, and a TypeSafe key (or an Azure AI Foundry deployment of Microsoft-Decision-1.1). |
| License | [MIT](https://github.com/cheolmin/decision-playwright/blob/e4ae4d6242925be81d7f8d3880e4975bf11ab416/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/decision-playwright/scripts/provider.mjs`](https://github.com/cheolmin/decision-playwright/blob/e4ae4d6242925be81d7f8d3880e4975bf11ab416/skills/decision-playwright/scripts/provider.mjs) at the pinned commit. |

## When to use

- Let a cheap decision model handle routine browser clicks while your coding agent only steps in for typing and checks.
- Mismatch: unattended browsing on sensitive accounts; the loop acts in a real browser.

## How it works

`skills/decision-playwright/scripts/provider.mjs` defaults to `DECISION_PROVIDER=typesafe`, posting page snapshots and action choices to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; a Foundry branch calls the Microsoft deployment instead. Integration evidence: [`skills/decision-playwright/scripts/provider.mjs`](https://github.com/cheolmin/decision-playwright/blob/e4ae4d6242925be81d7f8d3880e4975bf11ab416/skills/decision-playwright/scripts/provider.mjs).

## Get started

Copy the skill into your Claude Code or Copilot skills folder, install its dependencies and a browser, then run `dpw run "goal"`.

```sh
git clone https://github.com/cheolmin/decision-playwright.git
cp -r decision-playwright/skills/decision-playwright ~/.claude/skills/
cd ~/.claude/skills/decision-playwright && npm install
npx playwright-core install chromium
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the control loop: [github.com/cheolmin/decision-playwright/blob/e4ae4d6242925be81d7f8d3880e4975bf11ab416/README.md](https://github.com/cheolmin/decision-playwright/blob/e4ae4d6242925be81d7f8d3880e4975bf11ab416/README.md)

## Limits and data handling

Page snapshots and goals go to TypeSafe (or Azure) and are billed to your key. The skill controls a real browser, so review what it may click; the README suggests allow-listing the command, which removes approval prompts.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit e4ae4d624292](https://github.com/cheolmin/decision-playwright/tree/e4ae4d6242925be81d7f8d3880e4975bf11ab416). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
