# buildornot (BUILD, MAYBE or DON'T BUILD verdicts on side-project ideas, judged by Jev)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Command-line tool that judges a side-project idea: it searches GitHub and Hacker News for prior art, has Jev rate pain, reach, feasibility and deal-breakers and how likely each match does the same job, and prints BUILD, MAYBE or DON'T BUILD with the reasons.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/blakestone-x/buildornot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/blakestone-x/buildornot#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free. Jev calls use your own TypeSafe key (the README says a run is well under a cent). Checked 2026-10-25. |
| Jev evidence | [`buildornot.py`](https://github.com/blakestone-x/buildornot/blob/c4024bd47a4583380c308f2c54d9062144f3a5fd/buildornot.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [blakestone-x](https://github.com/blakestone-x). Independently curated. |
| Format | Python CLI (standard library only) |
| Platform and availability | Any OS with Python 3.10+; install with uvx or pipx from GitHub. |
| Jev's role | Core: Jev answers every judgment (levels out of five, deal-breakers, prior-art matches) and code turns them into a score and verdict. |
| Requirements | Python 3.10+; a TypeSafe API key. |
| License | [MIT](https://github.com/blakestone-x/buildornot/blob/c4024bd47a4583380c308f2c54d9062144f3a5fd/LICENSE) |

## When to use

- Sanity-check a side-project idea against existing tools before spending evenings on it.
- Get JSON with every raw Jev answer for your own analysis.
- Mismatch: a one-line idea with no `--for` or `--builder` context gives a weak verdict.

## How it works

`buildornot.py` posts the idea, your context and the prior-art search results to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and scores the answers against BUILD and DON'T BUILD thresholds. Integration evidence: [`buildornot.py`](https://github.com/blakestone-x/buildornot/blob/c4024bd47a4583380c308f2c54d9062144f3a5fd/buildornot.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
uvx --from git+https://github.com/blakestone-x/buildornot buildornot "your idea" --for "who it's for"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with sample output: [github.com/blakestone-x/buildornot#readme](https://github.com/blakestone-x/buildornot#readme)

## Limits and data handling

The idea text goes to TypeSafe, and search terms go to GitHub and Hacker News. Each run is saved, including the idea text, under `~/.buildornot/runs/` unless you pass `--no-save`.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit c4024bd47a45](https://github.com/blakestone-x/buildornot/tree/c4024bd47a4583380c308f2c54d9062144f3a5fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
