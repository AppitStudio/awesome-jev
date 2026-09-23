# OpenCode Security Guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linux OpenCode shell permission guard: local command check plus TypeSafe Jev read-only score ≥ 0.90 for auto-allow (ask otherwise; deny stays final).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/koppert/opencode-security-guard) |
| Maintainer | [koppert](https://github.com/koppert). Independently curated. Not an endorsement. |
| Format | TypeScript OpenCode plugin (`opencode-security-guard`). |
| Requirements | OpenCode on Linux; OpenRouter credential via OpenCode connection or env; Node/npm for install. |
| License | [MIT](https://github.com/koppert/opencode-security-guard/blob/ee9df2f2169c2f930dabcb28ca2cda7d2ec8faa7/LICENSE). OpenRouter/TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, `jev.ts`, tests). Live OpenCode/Jev **not** run. Distinct from [opencode-jev-guard](opencode-jev-guard.md). |

## When to use

Use it when OpenCode shell allows should require both a local read-only check and a high Jev Noul score. Prefer broader tool-risk guards when you need PreToolUse across many tool kinds.

## How it works

[`jev.ts`](https://github.com/koppert/opencode-security-guard/blob/ee9df2f2169c2f930dabcb28ca2cda7d2ec8faa7/jev.ts) POSTs OpenRouter alpha Decisions (`typesafe/jev-1.13`) with a `strictly_read_only` Noul. Auto-allow only if local checks pass and score ≥ 0.90. Optional `/tmp` write exceptions skip Jev.

## Get started

```sh
# OpenCode config snippet (see upstream README)
git clone https://github.com/koppert/opencode-security-guard.git
cd opencode-security-guard
git checkout ee9df2f2169c2f930dabcb28ca2cda7d2ec8faa7
npm test   # offline unit tests when available
```

## Examples and demos

- README `allowTmpWrites` behaviour and deny-final rule.
- `tests/guard.test.ts`.

## Limits and data handling

Shell command strings go to OpenRouter/TypeSafe when classified. Linux-only. Fail-closed to `ask` on uncertainty/errors as documented.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit ee9df2f](https://github.com/koppert/opencode-security-guard/tree/ee9df2f2169c2f930dabcb28ca2cda7d2ec8faa7) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [opencode-jev-guard](opencode-jev-guard.md), [jev-guard](jev-guard.md), [grok-jev-guard](grok-jev-guard.md).
