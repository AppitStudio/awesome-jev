# jev-healthcare-lab

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open experiment comparing TypeSafe Jev vs DeepSeek on 96 healthcare tasks across 12 scenarios (quality, latency, cost) with per-task data and prompts—honest about where Jev is weak.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JuneYaooo/jev-healthcare-lab) |
| Maintainer | [JuneYaooo](https://github.com/JuneYaooo). Independently curated. |
| Format | Python research lab + scenario READMEs (Chinese/English). |
| Requirements | Python toolchain per scenario; TypeSafe and DeepSeek API access to reproduce comparisons. |
| License | [MIT](https://github.com/JuneYaooo/jev-healthcare-lab/blob/8978023a011b94cf3df0d10bc3eb97dd6fafe9bb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement or clinical advice. Upstream accuracy/cost tables not re-measured. Live API reproduction not run. Not a patient-facing product. |

## When to use

Use to **inspect published healthcare decision-task comparisons** before adopting Jev for narrow clinical-text judgments. Prefer production clinical systems with human review; do not treat exam scores as diagnosis capability.

## How it works

Scenarios cover records, documentation, service routing, quality/hallucination checks, medication, trials matching, evidence/PICO, calculators, knowledge quizzes, multimodal ASR/OCR, acute diagnosis, and TCM—each with prompts, answers, and scoring notes (per README).

## Get started

```sh
git clone https://github.com/JuneYaooo/jev-healthcare-lab.git
cd jev-healthcare-lab
git checkout 8978023a011b94cf3df0d10bc3eb97dd6fafe9bb
# Open scenario READMEs under scenarios/; follow comparison details in comparisons/
```

## Examples and demos

- Summary tables in the root README (Jev vs DeepSeek win counts, latency, $/1k inputs—upstream-reported).
- Per-scenario folders with itemized tests.

## Limits and data handling

Offline public/synthetic materials; not proof of hospital time savings. Some tasks show low Jev accuracy (e.g. trial matching, clinical scores, complex extraction)—README flags these as unsuitable for unattended decisions.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 8978023](https://github.com/JuneYaooo/jev-healthcare-lab/tree/8978023a011b94cf3df0d10bc3eb97dd6fafe9bb). AI-assisted README and LICENSE inspection; scenario suites not re-run.
