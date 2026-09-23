# Agent Seek

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Cheap web recall for agents: You.com discovers candidates; TypeSafe Jev cascade-ranks them into a small scored JSON list (HTTP API, MCP, and a simple search UI). Agent Seek does not write answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Gitmaxd/agent-seek) |
| Maintainer | [Gitmaxd](https://github.com/Gitmaxd). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python service (FastAPI) with REST + MCP + optional hosted demo at [agentseek.dev](https://agentseek.dev). |
| Requirements | Python **3.12+**. Self-host needs `YDC_API_KEY` and `TYPESAFE_API_KEY` (plus a local Bearer). Live demo burns operator quota / per-IP limits—do not treat demo keys as secrets. |
| License | [MIT](https://github.com/Gitmaxd/agent-seek/blob/e974d4c5108d1239c4a3b237a77762dac2cfe12b/LICENSE). You.com and TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`packages/core/rank/jev.py`). Local install and live ranking were **not** run on the review host. This page does **not** reproduce any live demo Bearer tokens from upstream README. |

## When to use

Use it when an agent needs **scored web candidates** (snip or deep mode) with prompt-injection signals before reading pages. Prefer [jegrep](jegrep.md) for local code/docs search, or [jevseek](jevseek.md) for token-level DeepSeek+Jev demos.

## How it works

[`packages/core/rank/jev.py`](https://github.com/Gitmaxd/agent-seek/blob/e974d4c5108d1239c4a3b237a77762dac2cfe12b/packages/core/rank/jev.py) posts Score/related questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) over answerability and injection risk; the cascade ranks You.com discover hits. Hard gates may relax with `gates_relaxed: true` when the scored list would otherwise empty.

## Get started

```sh
git clone https://github.com/Gitmaxd/agent-seek.git
cd agent-seek
git checkout e974d4c5108d1239c4a3b237a77762dac2cfe12b
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # set YDC_API_KEY, TYPESAFE_API_KEY, AGENT_SEEK_API_KEY
# follow upstream README to run the API/MCP on :8787
```

Hosted try path: [agentseek.dev](https://agentseek.dev) (operator quota; not verified end-to-end here).

## Examples and demos

- OpenAPI / health / sandbox inspect routes (no key for some inspect endpoints).
- Eval fixtures under `evals/` and `fixtures/jev_*.json`.

## Limits and data handling

Queries and candidate text leave the host for You.com and TypeSafe on live ranking. Max **100** discover candidates; deep fetch capped. Demo keys are public operator quotas, not TypeSafe/You.com secrets.

## Review and maintenance

Reviewed on **2026-09-23** at [commit e974d4c](https://github.com/Gitmaxd/agent-seek/tree/e974d4c5108d1239c4a3b237a77762dac2cfe12b) (MIT). AI-assisted review of README, LICENSE, `packages/core/rank/jev.py`. No live spend.

Related: [jegrep](jegrep.md), [blink](blink.md), [jevseek](jevseek.md).
