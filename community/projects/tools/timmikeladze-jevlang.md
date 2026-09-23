# JevLang (TimMikeladze)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Policy engine for routes/gates/actions in TypeScript or Python: Jev answers only the questions the policy needs; signed journal for replay (distinct from sumanmichael/jevlang).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TimMikeladze/JevLang) |
| Maintainer | [TimMikeladze](https://github.com/TimMikeladze). Independently curated. Not an endorsement. |
| Format | TypeScript library (`jevlang` via bun) + Python bindings/docs. |
| Requirements | Node 22+ / Bun; optional `TYPESAFE_API_KEY` for live calls. Pure offline validation/replay without network. |
| License | [MIT](https://github.com/TimMikeladze/JevLang/blob/cbcadc115d1dc13de2a5e6f2a566486daffa2f58/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, `src/client.js`). Live Jev **not** run. Distinct from sumanmichael/jevlang. |

## When to use

Use it when routing/triage/tool gates should be declared once as policy with validated, journaled decisions. Prefer harness-specific routers when you only need model/effort selection.

## How it works

Policies declare questions; [`src/client.js`](https://github.com/TimMikeladze/JevLang/blob/cbcadc115d1dc13de2a5e6f2a566486daffa2f58/src/client.js) talks to TypeSafe System One with retries; code owns validation, decision, and signed journal replay.

## Get started

```sh
bun add jevlang
# or
git clone https://github.com/TimMikeladze/JevLang.git
cd JevLang
git checkout cbcadc115d1dc13de2a5e6f2a566486daffa2f58
# offline decision/validation paths need no key
```

## Examples and demos

- README “decide once, trust everywhere” overview.
- `examples/nextjs/` and docs under `docs/`.

## Limits and data handling

Policy state and question text go to TypeSafe when live. Offline paths do not call the network. Journal verification details are author-documented; not re-audited here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit cbcadc1](https://github.com/TimMikeladze/JevLang/tree/cbcadc115d1dc13de2a5e6f2a566486daffa2f58) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [DecideKit](decidekit.md), [daf-jev](daf-jev.md), [agent-chaperone](agent-chaperone.md).
