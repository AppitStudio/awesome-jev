# Clay JEV People Ranker

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Agent Skill plus Python workflow that pulls Clay people-search results via the official Clay CLI, then uses TypeSafe Jev Choice + Noul to qualify semantic role fit (bundled example: current operating founders) before enrichment.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/promptgtm-shared/clay-jev-people-ranker) |
| Maintainer | [promptgtm-shared](https://github.com/promptgtm-shared) / PromptGTM. Independently curated; this page is not an upstream submission or endorsement. |
| Format | Agent Skill (`SKILL.md`) + `scripts/rank_clay_people.py` (httpx/pydantic). |
| Requirements | Python 3 with `httpx` and `pydantic`; official Clay CLI; `TYPESAFE_API_KEY`; Clay account/access per upstream Clay docs. |
| License | [MIT](https://github.com/promptgtm-shared/clay-jev-people-ranker/blob/2494b65218d4e4e940911db7c485710a3cff7050/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source/syntax review only—no Clay CLI or live TypeSafe run in this pass. Upstream README may report measured founder-ranking experiments; those figures were not reproduced here. |

## When to use

Use it for GTM/RevOps flows where Clay’s hard filters still leave ambiguous titles (founding investor vs operating founder, and similar). Prefer pure Clay filters when titles are unambiguous. Requires Clay + TypeSafe accounts for live ranking.

## How it works

[`scripts/rank_clay_people.py`](https://github.com/promptgtm-shared/clay-jev-people-ranker/blob/2494b65218d4e4e940911db7c485710a3cff7050/scripts/rank_clay_people.py) fetches candidates through the Clay CLI, builds a compact person state, and POSTs Choice/Noul questions to `https://api.typesafe.ai/v1/systemone`. Python applies probability thresholds and writes JSON/CSV. Candidate profile fields leave the host on live Jev calls.

## Get started

```sh
git clone https://github.com/promptgtm-shared/clay-jev-people-ranker.git
cd clay-jev-people-ranker
git checkout 2494b65218d4e4e940911db7c485710a3cff7050
python3 -m pip install -r scripts/requirements.txt
cp env.example .env   # set TYPESAFE_API_KEY; configure Clay per upstream
python3 scripts/rank_clay_people.py --help
```

Install the skill with `python install_skill.py --agent …` as documented in `SKILL.md` / `references/platform-installation.md`. Live Clay + TypeSafe usage is billed by those providers.

## Examples and demos

- Upstream README founder-ranking narrative and CLI flags (`--query`, thresholds, `--workers`).
- This listing: `py_compile` on `rank_clay_people.py` OK; `--help` OK. No Clay or TypeSafe network calls.

## Limits and data handling

People records and derived state reach TypeSafe when ranking. Thresholds and any published precision/recall figures are upstream-reported, not reproduced here. Clay CLI behavior depends on your Clay plan and auth.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2494b65](https://github.com/promptgtm-shared/clay-jev-people-ranker/tree/2494b65218d4e4e940911db7c485710a3cff7050): MIT; AI-assisted source review of README, LICENSE, `SKILL.md`, and `scripts/rank_clay_people.py`. No live TypeSafe or Clay call.

Related: [Testimonial miner](testimonial-miner.md), [jev-seo](jev-seo.md), [decision-first](decision-first.md).
