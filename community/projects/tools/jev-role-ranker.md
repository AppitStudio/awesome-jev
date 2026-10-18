# jev-role-ranker

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ranks job postings against a profile with TypeSafe Jev (fit, seniority, remote, sponsorship flags). Scores only sort; sponsorship refusals are flagged for a human and postings are never auto-rejected.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CapCurious/jev-role-ranker) |
| Maintainer | [CapCurious](https://github.com/CapCurious). Independently curated. |
| Format | Python CLI with recorded demos and a browser threshold explainer |
| Requirements | Python 3.10+; JEV_API_KEY or TYPESAFE_API_KEY for live ranking. |
| License | [MIT](https://github.com/CapCurious/jev-role-ranker/blob/aa4bec86a291a502aea176aa901851a09db8b301/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/CapCurious/jev-role-ranker/blob/aa4bec86a291a502aea176aa901851a09db8b301/jev_client.py) at the pinned commit. |

## When to use

- Screen many postings with typed Jev scores instead of free-form LLM prose.
- Want sponsorship refusals flagged without silent auto-reject.
- Mismatch: personal ranking tool; weights and thresholds are local parameters.

## How it works

`jev_client.py` calls `https://api.typesafe.ai/v1/systemone`. `jev_role_ranker.py` asks Jev several scored questions per posting, blends weights in code, and flags sponsorship issues without dropping rows. Integration evidence: [`jev_client.py`](https://github.com/CapCurious/jev-role-ranker/blob/aa4bec86a291a502aea176aa901851a09db8b301/jev_client.py).

## Get started

Clone, set a TypeSafe key (or use --demo), and rank example postings.

```sh
git clone https://github.com/CapCurious/jev-role-ranker && cd jev-role-ranker
python3 jev_role_ranker.py --demo rank examples/postings --limit 5 --sort fit
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [capcurious.github.io/jev-role-ranker/](https://capcurious.github.io/jev-role-ranker/)
- README demo ranking table

## Limits and data handling

Posting text is sent to TypeSafe when not in demo mode. Not a job board or placement service.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit aa4bec86a291](https://github.com/CapCurious/jev-role-ranker/tree/aa4bec86a291a502aea176aa901851a09db8b301). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
