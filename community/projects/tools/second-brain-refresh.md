# second-brain (knowledge refresh skill)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code agent skill that finds stale pages in a wiki, memory or rules folder, asks Jev whether each was superseded or duplicates another, moves outdated pages to `_archive/` and rebuilds the index Claude reads first.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/strickland-inc/second-brain) |
| Maintainer | [strickland-inc](https://github.com/strickland-inc). Independently curated. |
| Format | Claude Code skill (Python, standard library only) |
| Requirements | Python 3; Claude Code; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/strickland-inc/second-brain/blob/91544cb355a8e5261003d49788bf030d3c5ae60a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/kota_on_x/status/2112091631801229372)). |
| Jev evidence | [`scripts/refresh.py`](https://github.com/strickland-inc/second-brain/blob/91544cb355a8e5261003d49788bf030d3c5ae60a/scripts/refresh.py) at the pinned commit. |

## When to use

- Keep Claude Code memory and project wiki pages from contradicting newer decisions.
- Want a reviewable plan before anything is archived.
- Mismatch: Japanese-language README; tuned for Markdown knowledge folders.

## How it works

Each page gets a type, a date and a shelf life. `scripts/refresh.py` sends pages to `https://api.typesafe.ai/v1/systemone` to score whether newer pages replace them and whether similar pages overlap or conflict. Only changed pages are asked again. `plan` writes the proposed moves, and `apply --yes` applies them; nothing is deleted. Integration evidence: [`scripts/refresh.py`](https://github.com/strickland-inc/second-brain/blob/91544cb355a8e5261003d49788bf030d3c5ae60a/scripts/refresh.py).

## Get started

From the upstream README: clone into `.claude/skills/second-brain`, set `TYPESAFE_API_KEY`, then run the scan, judge, plan and apply steps from the vault root.

```sh
git clone https://github.com/strickland-inc/second-brain .claude/skills/second-brain
python3 .claude/skills/second-brain/scripts/refresh.py scan
python3 .claude/skills/second-brain/scripts/refresh.py judge
python3 .claude/skills/second-brain/scripts/refresh.py plan
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README trial: 22 Claude Code memories, 2 flagged as superseded

## Limits and data handling

Page text goes to TypeSafe during `judge`. Staleness calls are model judgments; review `.refresh/plan.md` before `apply --yes`.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 91544cb355a8](https://github.com/strickland-inc/second-brain/tree/91544cb355a8e5261003d49788bf030d3c5ae60a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
