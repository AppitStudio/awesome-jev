# GTM Engineer Starter by Jordan Crawford (Claude Code and Codex skills for go-to-market research, with a Jev calibrated judge that scores prospect lists)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Free, open-source starter kit of six Claude Code / Codex skills for go-to-market engineering: build account dossiers, label Won / Lost / 10X customers, write your ideal-customer profile as rules, and score a prospect list. Its `calibrated-judge` skill asks Jev typed questions about each evidence packet and turns the probabilities into accept, reject, review or insufficient.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SantaJordan/gtm-engineer-starter) |
| Maintainer | [Jordan Crawford / Blueprint](https://github.com/SantaJordan). Independently curated. |
| Format | Agent skills and Python scripts |
| Requirements | Python 3 and Claude Code or Codex; a TypeSafe or OpenRouter key for live Jev scoring (the bundled example runs offline with no keys). |
| License | [MIT](https://github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/calibrated-judge/scripts/jev_client.py`](https://github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/skills/calibrated-judge/scripts/jev_client.py) at the pinned commit. |

## When to use

- Score a list of companies or people for ideal-customer or persona fit with evidence you can show.
- Decide which rows a human must review instead of trusting a prose opinion.
- Mismatch: if you want a hosted lead database; this kit works on your own CRM and research data.

## How it works

`skills/calibrated-judge/scripts/jev_client.py` is the only client for Jev: TypeSafe `POST https://api.typesafe.ai/v1/systemone` with `jev-1.13.0`, or OpenRouter's decisions API with `typesafe/jev-1.13`. The skill accepts a row above 0.90 on a support question, rejects above 0.90 on a named disqualifier, and sends the rest to a human review queue with a decision log. Integration evidence: [`skills/calibrated-judge/scripts/jev_client.py`](https://github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/skills/calibrated-judge/scripts/jev_client.py).

## Get started

Clone the kit and run the offline checks and worked example first; add a key only when you score real rows.

```sh
git clone https://github.com/SantaJordan/gtm-engineer-starter ~/gtm
cd ~/gtm
python3 -m pip install -r requirements.txt
make check   # offline: tests plus a replay of the method on a fictional company
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Start here: [github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/START-HERE.md](https://github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/START-HERE.md)
- Calibrated judge skill: [github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/skills/calibrated-judge/SKILL.md](https://github.com/SantaJordan/gtm-engineer-starter/blob/68f5444fa5b460924d1717378ed75411f81f0195/skills/calibrated-judge/SKILL.md)

## Limits and data handling

Evidence packets about companies and people are sent to TypeSafe or OpenRouter (a third-party host) when scoring live. The 0.90 threshold is a starting point the README tells you to check on your own rows. It is the free version of a method the author teaches commercially at Blueprint; this listing covers only the MIT repository.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 68f5444fa5b4](https://github.com/SantaJordan/gtm-engineer-starter/tree/68f5444fa5b460924d1717378ed75411f81f0195). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
