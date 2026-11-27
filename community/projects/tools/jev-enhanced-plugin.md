# jev-enhanced-plugin by Jason Hsieh (agent plugin for Codex, Claude Code and Oh My Pi that adds advisory Jev judgments to six existing skills)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent plugin with six existing skills (code review, code simplifier, grilling, humanizer in English and Traditional Chinese, and a reply checker), each with one addition: a pack of typed Jev questions at the steps where the skill relied on the agent's impression, such as whether quoted evidence supports a review finding. Jev's output is advisory and never approves a change or removes a finding. A seventh skill explains how to migrate further skills.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JiaWeiXie/decision-enhanced-plugin) |
| Maintainer | [Jason Hsieh](https://github.com/JiaWeiXie) (JiaWeiXie). Independently curated. |
| Format | Agent plugin (skills + Node.js CLI) |
| Requirements | Node.js 20+, OpenAI Codex, Claude Code or Oh My Pi, and a TypeSafe key. |
| License | [MIT](https://github.com/JiaWeiXie/decision-enhanced-plugin/blob/953dec550f739b75b80d5d4ff2cb236d23c9089f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/JiaWeiXie/decision-enhanced-plugin/blob/953dec550f739b75b80d5d4ff2cb236d23c9089f/src/jev.mjs) at the pinned commit. |

## When to use

- Coding-agent users who want calibrated second opinions inside review and rewriting skills they already use.
- Mismatch: an automatic gate; the plugin never blocks or approves anything by itself.

## How it works

`src/jev.mjs` builds each pack's state (reference material first, the text under judgment after) and sends all questions for a job in one request through the vendored TypeSafe JS SDK to `https://api.typesafe.ai`. Anything code can check exactly, such as diffs and dependency graphs, is computed locally and not sent. Integration evidence: [`src/jev.mjs`](https://github.com/JiaWeiXie/decision-enhanced-plugin/blob/953dec550f739b75b80d5d4ff2cb236d23c9089f/src/jev.mjs).

## Get started

Add the repository as a plugin marketplace in your agent host, then install the plugin.

```sh
claude plugin marketplace add JiaWeiXie/decision-enhanced-plugin
claude plugin install jev-enhanced-plugin@jev-enhanced-plugin
# Codex: codex plugin marketplace add JiaWeiXie/decision-enhanced-plugin
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Skills: [github.com/JiaWeiXie/decision-enhanced-plugin/tree/main/skills](https://github.com/JiaWeiXie/decision-enhanced-plugin/tree/main/skills)
- Evals: [github.com/JiaWeiXie/decision-enhanced-plugin/tree/main/evals](https://github.com/JiaWeiXie/decision-enhanced-plugin/tree/main/evals)

## Limits and data handling

Pack state (findings, quoted evidence, draft passages) is sent to TypeSafe; code-only fields stay local. The author's wording checks were small spot checks, not a benchmark. Bundled third-party skills keep their own licences (MIT, Apache-2.0, CC-BY-SA-4.0) as listed in `licenses/`. The README uses the name jev-enhanced-plugin; the repository is `decision-enhanced-plugin`.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 953dec550f73](https://github.com/JiaWeiXie/decision-enhanced-plugin/tree/953dec550f739b75b80d5d4ff2cb236d23c9089f). Inspected the README, LICENSE, `licenses/`, `NOTICE` and `src/jev.mjs` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
