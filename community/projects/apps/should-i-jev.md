# Should I Jev?

[All projects](../README.md) · [Web apps](README.md#web-apps)

Describe a feature and get a verdict on what should power it—plain code, TypeSafe Jev, an LLM, Jev+LLM, classical ML, or not enough to judge—via nineteen parallel Jev questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yakubmurcek/should-i-jev) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [shouldijev.vercel.app](https://shouldijev.vercel.app) |
| Pricing and access | Hosted demo and MIT source; TypeSafe key required for new verdicts (BYOK). Checked 2026-09-24. |
| Jev evidence | [README](https://github.com/yakubmurcek/should-i-jev/blob/d01fbb942b20afb00d610368f1365200fce072be/README.md) describes nineteen parallel typed questions and offline tests. |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Live hosted verdicts not measured on the review host. |
| Maintainer | [yakubmurcek](https://github.com/yakubmurcek). Independently curated. |
| Format | Application |
| Platform and availability | Next.js 15 web app; [Try app](https://shouldijev.vercel.app) or local `npm run dev`. |
| Jev's role | Jev answers nineteen typed questions; application code maps them to a mechanism verdict (never asks Jev which mechanism to pick). |
| Requirements | Node.js; `TYPESAFE_API_KEY` for new verdicts. |
| License | [MIT](https://github.com/yakubmurcek/should-i-jev/blob/d01fbb942b20afb00d610368f1365200fce072be/LICENSE). |

## When to use

Use when deciding **whether Jev fits** a feature versus code/LLM/ML. Prefer TypeSafe docs jaggedness list for prose-only guidance.

## How it works

One Jev request fans out nineteen questions; local logic weighs signals into a verdict that can say “just write code” (per README).

## Get started

```sh
git clone https://github.com/yakubmurcek/should-i-jev.git
cd should-i-jev
git checkout d01fbb942b20afb00d610368f1365200fce072be
npm install
cp .env.example .env.local   # TYPESAFE_API_KEY
npm run dev
```

## Examples and demos

- Hosted [shouldijev.vercel.app](https://shouldijev.vercel.app).
- README screenshots and offline test suite.

## Limits and data handling

Feature descriptions reach TypeSafe when producing new verdicts. Permalinks may use KV when configured.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit d01fbb9](https://github.com/yakubmurcek/should-i-jev/tree/d01fbb942b20afb00d610368f1365200fce072be). AI-assisted README inspection; live hosted path not measured.

Related: [Jev as LLM](jev-as-llm.md).
