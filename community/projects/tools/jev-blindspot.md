# jev-blindspot

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code / Codex CLI side panel: TypeSafe Jev gates whether a prompt is worth a second look, then optional headless analysis lists blind spots without editing the session.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jsk4581/jev-blindspot) |
| Maintainer | [jsk4581](https://github.com/jsk4581). Community submission via Awesome Jev issue #400; independently curated. Listing is not an endorsement. |
| Format | npm CLI/plugin **jev-blindspot**; Claude Code / Codex hooks + browser panel. |
| Requirements | Node 20+; Linux or macOS; `TYPESAFE_API_KEY`; Claude Code 2.1.278+ or Codex CLI 0.144+ logged in. |
| License | [MIT](https://github.com/jsk4581/jev-blindspot/blob/e46f60ba44ecb321ce196a6dcf32f5bbdfeb9a14/LICENSE). TypeSafe and optional Anthropic/OpenAI usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, gate questions). Live Claude Code/Codex/Jev were **not** run on the review host. |

## When to use

Use it when you want prompt blind-spot cards beside Claude Code or Codex without intercepting or rewriting prompts. Prefer [claude-code-jev](claude-code-jev.md) / [hookgate](hookgate.md) when you need allow/block gates on tools instead of advisory prompt review.

## How it works

Each prompt hits a TypeSafe Jev gate (`worth_checking`, risk score, gap flags) in [`src/gate/questions.ts`](https://github.com/jsk4581/jev-blindspot/blob/e46f60ba44ecb321ce196a6dcf32f5bbdfeb9a14/src/gate/questions.ts). Only when the gate passes does a headless Claude/Codex read-only pass return up to five pasteable items in a browser panel. Quiet prompts show a grey line; failures surface on the card without blocking the agent.

## Get started

```sh
npm install -g jev-blindspot
mkdir -p ~/.config/jev-blindspot
echo 'TYPESAFE_API_KEY=your-key' > ~/.config/jev-blindspot/env && chmod 600 ~/.config/jev-blindspot/env
jev-blindspot install-hook
# Codex once: jev-blindspot install-hook codex --trust
# Then /blindspot (Claude Code) or /prompts:blindspot (Codex)
```

Pin for review: [commit e46f60b](https://github.com/jsk4581/jev-blindspot/tree/e46f60ba44ecb321ce196a6dcf32f5bbdfeb9a14).

## Examples and demos

- Upstream panel screenshot and README walkthrough.
- `jev-blindspot fixtures` compares expected vs actual gate decisions (not re-run here).

## Limits and data handling

Thresholds were author-tuned. Prompt text, recent exchanges, and directory/branch names go to TypeSafe; when the gate passes, Anthropic or OpenAI may see project files under your login. Gate failures fail open (no analysis). No live TypeSafe spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit e46f60b](https://github.com/jsk4581/jev-blindspot/tree/e46f60ba44ecb321ce196a6dcf32f5bbdfeb9a14) (MIT). AI-assisted source review. Closes community issue #400. No live TypeSafe spend.

Related: [hookgate](hookgate.md), [claude-code-jev](claude-code-jev.md), [clear-head](clear-head.md).
