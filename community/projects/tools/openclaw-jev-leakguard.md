# openclaw-jev-leakguard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw outgoing-message guard: TypeSafe Jev (or local Kev) judges content × destination so client names, credentials, and internal details are blocked from the wrong channel.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yousan/openclaw-jev-leakguard) |
| Maintainer | [yousan](https://github.com/yousan). Independently curated. |
| Format | OpenClaw plugin with destination tiers + term lists; hooks outgoing posts. |
| Requirements | OpenClaw ≥ 2026.9.6; `@openclaw/typesafe` + TypeSafe key, or local Kev/`decisionModel`. |
| License | [MIT](https://github.com/yousan/openclaw-jev-leakguard/blob/a6117abd00e6be50449b0ba033bdcfa32d80e3b2/LICENSE). Hosted Jev sends message text to TypeSafe. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from [openclaw-jev-trigger](openclaw-jev-trigger.md) and [openclaw-typesafe-ai](openclaw-typesafe-ai.md). Live OpenClaw/TypeSafe paths not run on the review host. |

## When to use

Use when agents post across private/shared/public channels and you need meaning-aware leak checks beyond secret scanners. Prefer local Kev when message text must not leave the machine.

## How it works

Configures destination tiers and local term lists; each outbound message is judged for client/credential/internal leakage relative to the destination. Term lists stay local for hosted Jev; text goes to TypeSafe when using hosted judge.

## Get started

```sh
git clone https://github.com/yousan/openclaw-jev-leakguard.git
cd openclaw-jev-leakguard
git checkout a6117abd00e6be50449b0ba033bdcfa32d80e3b2
# follow upstream install + config examples
```

## Examples and demos

- Upstream demo GIF and `leakguard.check` gateway call examples.
- Local Kev and ONNX experimental notes in README.

## Limits and data handling

With hosted Jev, outgoing message text is sent to TypeSafe. Catalog checks did not install OpenClaw or run live guards.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit a6117ab](https://github.com/yousan/openclaw-jev-leakguard/tree/a6117abd00e6be50449b0ba033bdcfa32d80e3b2). AI-assisted README and license inspection; install/live paths not executed.
