# dsh-jev-context-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin: configurable rules that read event content, ask a decision model (TypeSafe Jev when the model id is `jev-*`) Choice questions, and execute the selected option's action—including Skill-catalog trimming and evidence-aware review gates. Distinct from [dsh-jev](dsh-jev.md) / [dsh-jev-decide](dsh-jev-decide.md) / other dsh-jev* plugins.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vb2250158/dsh-jev-context-gate) |
| Maintainer | [vb2250158](https://github.com/vb2250158). Independently curated. |
| Format | JavaScript DeepSeek Harness plugin (`package.json` workspace). |
| Requirements | DeepSeek Harness; decision-model provider access for Jev-native or JSON-probability modes. |
| License | [MIT](https://github.com/vb2250158/dsh-jev-context-gate/blob/a4dc35a4fdd72eaee0f663a776cb6554498d665a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live DSH sessions not run. README bilingual (ZH primary). |

## When to use

Use it to **gate or trim DSH context/Skills** with typed decisions before the main model sees them. Prefer simpler `jev_ask` plugins when you only need ad-hoc judgments without rule UI.

## How it works

Rules bind events (user message, Skill catalog/body inject, tool results) to questions and option actions. Jev-native models use structured calls when the provider supports them; otherwise JSON probability estimates (uncalibrated—as documented upstream).

## Get started

```sh
git clone https://github.com/vb2250158/dsh-jev-context-gate.git
cd dsh-jev-context-gate
git checkout a4dc35a4fdd72eaee0f663a776cb6554498d665a
npm run check   # offline; not re-run here
# Install into DeepSeek Harness per upstream packaging notes
```

## Examples and demos

- README rule semantics table; Skill-trim / custom-candidate filters.
- `README_en.md`; `DESIGN.md`.

## Limits and data handling

Event text and Skill blurbs go to the configured decision model. Script-generated questions run with local Node permissions—only load trusted scripts. Failures skip actions rather than crashing the host (per README).

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit a4dc35a](https://github.com/vb2250158/dsh-jev-context-gate/tree/a4dc35a4fdd72eaee0f663a776cb6554498d665a). AI-assisted README inspection.

Related: [dsh-jev](dsh-jev.md), [dsh-jev-interceptor](dsh-jev-interceptor.md), [dsh-jev-kit](dsh-jev-kit.md).
