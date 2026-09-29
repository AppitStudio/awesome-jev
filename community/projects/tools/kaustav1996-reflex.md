# Reflex (kaustav1996)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi-based coding agent and personal assistant that uses TypeSafe Jev for tool-call gates, model-tier routing, skill/connector selection, completion checks, and result screening—code owns thresholds; Jev can add a question or block, never remove one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kaustav1996/reflex) |
| Tags | Open source · Free source build · BYOK |
| Maintainer | [kaustav1996](https://github.com/kaustav1996). Author submission via issue [#364](https://github.com/AppitStudio/awesome-jev/issues/364). Distinct from [Reflex-1](matu79go-reflex-1.md) (open decision model) and [jev-reflex (xnuonux)](jev-reflex-xnuonux.md). |
| Format | Node.js coding agent CLI (`reflex`) built on the Pi coding agent, with TypeSafe extension under `src/extensions/typesafe/`. Package name `reflex-agent` **0.1.0**. |
| Requirements | Node ≥ 22.19 on macOS or Linux; an LLM via OpenRouter or a direct provider; TypeSafe or OpenRouter key for Jev; optional voice provider and `ffmpeg`/`sox`. |
| License | [MIT](https://github.com/kaustav1996/reflex/blob/1e9416fb1de589d2901b5e70eeaeb72be1f04c6b/LICENSE). Provider usage may incur charges when live. |
| Disclosure | Author submission (issue #364). Catalog review is AI-assisted source inspection; no live TypeSafe or OpenRouter spend on the review host. Listing is not an endorsement. |

## When to use

Use when you want a full Pi-based coding agent where Jev judges every mutating tool call, routes model tier and skills per request, and screens outside results—while local policy still owns allow/ask/block. Prefer lighter Pi extensions such as [pi-jev](pi-jev.md) when you only need a gate/output judge without the full agent stack.

## How it works

The TypeSafe extension posts typed questions (Noul, Choice, Score) for action gating (`gate.ts` / `policy.ts`), request-level model-tier + skill/connector selection (`brief.ts`, `router.ts`, `selector.ts`), progress/completion monitors, voice intent, browser steps, and screening of long outside results (`screen.ts`). Deterministic code keeps protected-path asks and session allow-lists; Jev answers cannot remove a code-imposed question. Integration evidence: [`src/extensions/typesafe/`](https://github.com/kaustav1996/reflex/tree/1e9416fb1de589d2901b5e70eeaeb72be1f04c6b/src/extensions/typesafe) at the pinned commit.

## Get started

```sh
git clone https://github.com/kaustav1996/reflex.git
cd reflex
git checkout 1e9416fb1de589d2901b5e70eeaeb72be1f04c6b
npm install && npm run build
npm link   # installs the `reflex` command; first run starts onboarding
```

Onboarding configures an LLM, a Jev provider/model (TypeSafe direct or OpenRouter), risk appetite, and optional voice. Live Jev and LLM paths need keys and incur provider charges. This listing did not run install, onboarding, or live calls.

## Examples and demos

Upstream README documents measured allow/ask/block examples on `jev-1.13.0`, the pink `⚡ TYPESAFE` session line, and settings for provider/model. No separate hosted demo; the local CLI is the usage path. Offline `npm test` exists upstream; it was not executed on the review host.

## Limits and data handling

Tool arguments, session summaries, and screened outside text can reach TypeSafe or OpenRouter when a Jev key is configured; LLM traffic follows the chosen provider. Voice providers receive audio/transcripts when enabled. Browser cookies/sessions stay with Chrome under your accounts. Jev is text-only and adversarial content can sway it—hence code-owned floors. Not a measured accuracy or latency claim for this catalog review.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) against [commit 1e9416f](https://github.com/kaustav1996/reflex/tree/1e9416fb1de589d2901b5e70eeaeb72be1f04c6b) for issue [#364](https://github.com/AppitStudio/awesome-jev/issues/364): MIT LICENSE, package `reflex-agent` **0.1.0**, README and `src/extensions/typesafe/{gate,policy,brief,router,client,screen}.ts` inspected via GitHub API. No `npm install`, offline tests, or live TypeSafe/OpenRouter calls on the review host.

Related: [pi-jev](pi-jev.md), [pi-jev-permit](pi-jev-permit.md), [Ten Levels of Jev](ten-levels-of-jev.md).
