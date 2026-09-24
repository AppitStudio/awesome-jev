# plain-language-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill/CLI that runs AI-written text through six TypeSafe Jev plain-language checks (terminology, sentence ease, concreteness, one-pass comprehension, fluff, everyday wording) and returns pass / human-review / reject-with-rewrite instructions—the author model rewrites; Jev does not generate prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Wujiaowang/plain-language-gate) |
| Maintainer | [Wujiaowang](https://github.com/Wujiaowang). Independently curated. |
| Format | Python skill (`SKILL.md`, `gate.py`, `checks.py`); stdlib only. |
| Requirements | Python 3.8+; `TYPESAFE_API_KEY` (or OpenRouter / Vercel AI Gateway per README). |
| License | [MIT](https://github.com/Wujiaowang/plain-language-gate/blob/cb8d699d032b3df11396b9f298dcafefb24abc56/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Jev/gate loops not run. Docs primarily Chinese; checks work on languages Jev reads. |

## When to use

Use it as a **readability gate before delivery**. Prefer [Jev Score](jev-score.md) for multi-criteria document scoring UIs.

## How it works

One Jev call runs six parallel judgments; code maps to pass/review/rewrite with optional rewrite loops. See [`gate.py`](https://github.com/Wujiaowang/plain-language-gate/blob/cb8d699d032b3df11396b9f298dcafefb24abc56/gate.py) and [`checks.py`](https://github.com/Wujiaowang/plain-language-gate/blob/cb8d699d032b3df11396b9f298dcafefb24abc56/checks.py).

## Get started

```sh
git clone https://github.com/Wujiaowang/plain-language-gate.git
cd plain-language-gate
git checkout cb8d699d032b3df11396b9f298dcafefb24abc56
export TYPESAFE_API_KEY=…
# Copy into agent skills dir per README, or run gate.py as CLI
```

## Examples and demos

- README rewrite-loop table on a ~4700-character report.
- `SKILL.md` / `SKILL-MECHANICS.md`.

## Limits and data handling

Draft text is sent to TypeSafe/Gateway. Cost/latency figures in the README are upstream-reported, not re-measured. Universal terminology checks can stay hard on jargon-dense genres—as documented upstream.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit cb8d699](https://github.com/Wujiaowang/plain-language-gate/tree/cb8d699d032b3df11396b9f298dcafefb24abc56). AI-assisted README + gate/checks inspection.

Related: [Jev Score](jev-score.md), [clear-head](clear-head.md).
