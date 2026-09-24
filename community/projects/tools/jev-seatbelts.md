# jev-seatbelts

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Seven Claude Code hooks that catch common expensive agent mistakes (bad plans, fake packages, risky shells, secret commits, stuck debugging, …) with TypeSafe Jev on the judgment tiers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LocoLoboZ/jev-seatbelts) |
| Maintainer | [LocoLoboZ](https://github.com/LocoLoboZ). Independently curated. |
| Format | Python gates + Claude Code hooks (`install.py`, `hooks/hooks.json`). |
| Requirements | Claude Code; Python; `TYPESAFE_API_KEY` for live Jev-judged tiers; network for registry lookups where used. |
| License | [MIT](https://github.com/LocoLoboZ/jev-seatbelts/blob/77d3e159e512da3cc06a76993a5d7c314ded7501/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live hook/Jev paths not exercised on the review host. |

## When to use

Use when Claude Code should get **pre-tool seatbelts** before destructive or expensive mistakes. Prefer narrower single-purpose guards when you only need one check (e.g. package typosquat only).

## How it works

Gates attach as `PreToolUse` / related hooks; shared `lib/jevgate.py` handles key lookup, thresholds, retries, budgets, and logging. Some tiers are deterministic (registry existence); Jev judges resemblance and other semantic cases (per README).

## Get started

```sh
git clone https://github.com/LocoLoboZ/jev-seatbelts.git
cd jev-seatbelts
git checkout 77d3e159e512da3cc06a76993a5d7c314ded7501
export TYPESAFE_API_KEY=ts_...
python install.py
```

## Examples and demos

- README intro video thumbnail and gate list.
- Offline/fixture tests vs `judged` live cases documented upstream.

## Limits and data handling

Command/plan text may reach TypeSafe on judged tiers. Gates are individually toggleable via `GATEn_ENABLED`. Session call budgets apply.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 77d3e15](https://github.com/LocoLoboZ/jev-seatbelts/tree/77d3e159e512da3cc06a76993a5d7c314ded7501). AI-assisted README and LICENSE inspection; install/hooks not run live.

Related: [claude-code-jev](claude-code-jev.md), [agent-chaperone](agent-chaperone.md).
