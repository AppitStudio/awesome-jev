# jev-decide (abdullahaamuda)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

System One decision layer for browser/desktop automation—page-state judgments via TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/abdullahaamuda-code/jev-decide) |
| Maintainer | [abdullahaamuda-code](https://github.com/abdullahaamuda-code). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent skill (`SKILL.md`) plus stdlib-only `scripts/jev_ask.py`. |
| Requirements | Python 3; `TYPESAFE_API_KEY` (or gitignored `api_key.txt`). |
| License | [MIT](https://github.com/abdullahaamuda-code/jev-decide/blob/ed682177752e39db860c40990ef95328f1f4929d/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when agents burn tokens re-reading huge a11y snapshots for one click/target judgment.

## How it works

Send trimmed page state plus typed questions; Jev returns calibrated answers; confidence gates act/disclose/ignore. Destructive actions never gated by Jev alone. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/abdullahaamuda-code/jev-decide.git
cd jev-decide
git checkout ed682177752e39db860c40990ef95328f1f4929d
export TYPESAFE_API_KEY=…
python scripts/jev_ask.py --state-file page.yml --questions '{…}'
```

Pin revision `ed682177752e39db860c40990ef95328f1f4929d` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Text-only (no screenshots). Live TypeSafe calls not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit ed68217](https://github.com/abdullahaamuda-code/jev-decide/tree/ed682177752e39db860c40990ef95328f1f4929d). AI-assisted README and LICENSE inspection; install/live paths not executed.
