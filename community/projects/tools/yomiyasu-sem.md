# yomiyasu-sem by Komugi (Claude Code Stop hook where Jev catches meaning changes in edited Japanese specs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Add-on for the yomiyasu Japanese editing skill. When Claude rewrites a formal spec, it reads yomiyasu's check records, pairs changed sentences, checks lost obligation markers with rules and asks Jev whether an actor was added, a number now applies to something else or a modifier moved. Violations send the draft back through a Claude Code Stop hook (twice at most); unclear cases go to a person. Japanese README.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Komugi-powerplatform/yomiyasu-sem) |
| Maintainer | [Komugi-powerplatform](https://github.com/Komugi-powerplatform). Independently curated. |
| Format | Python hook (standard library only) |
| Requirements | Python 3.9+, Claude Code and yomiyasu v2.1.0+; a TypeSafe key, an OpenCode Zen key, or the time-limited free `jev-1.13-free` model on OpenCode Zen. Without any of them only the rule checks run. |
| License | [MIT](https://github.com/Komugi-powerplatform/yomiyasu-sem/blob/9b70d62e436e4c77048363a83e4bf82878a9d170/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`sem/jev.py`](https://github.com/Komugi-powerplatform/yomiyasu-sem/blob/9b70d62e436e4c77048363a83e4bf82878a9d170/sem/jev.py) at the pinned commit. |

## When to use

- Teams who use yomiyasu and Claude Code to polish Japanese specifications and need edits that keep the meaning.
- Mismatch: non-Japanese text or documents other than formal specs (`--doc-type formal`).

## How it works

`sem/jev.py` posts `noul` questions to TypeSafe's `https://api.typesafe.ai/v1/systemone` (`jev-latest`) when `TYPESAFE_API_KEY` is set, otherwise to OpenCode Zen's System One endpoint (`jev-1.13`). Thresholds are fixed from the bundled evaluation set, and answers near the line are re-asked up to two more times (median). Integration evidence: [`sem/jev.py`](https://github.com/Komugi-powerplatform/yomiyasu-sem/blob/9b70d62e436e4c77048363a83e4bf82878a9d170/sem/jev.py).

## Get started

Print the hook config and add it to `.claude/settings.json` next to yomiyasu's hook.

```sh
git clone https://github.com/Komugi-powerplatform/yomiyasu-sem && cd yomiyasu-sem
python3 sem/hook.py --print-config claude-code
export TYPESAFE_API_KEY=...   # or OPENCODE_API_KEY, or YOMIYASU_SEM_MODEL=jev-1.13-free
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Design notes and evaluation: [github.com/Komugi-powerplatform/yomiyasu-sem/blob/main/docs/design.md](https://github.com/Komugi-powerplatform/yomiyasu-sem/blob/main/docs/design.md)
- Field test material: [github.com/Komugi-powerplatform/yomiyasu-sem/tree/main/demo](https://github.com/Komugi-powerplatform/yomiyasu-sem/tree/main/demo)

## Limits and data handling

Only the changed sentence pair and one preceding original sentence are sent to Jev, not the full document. Decision records stay in `.yomiyasu-sem/`. yomiyasu itself is not bundled.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 9b70d62e436e](https://github.com/Komugi-powerplatform/yomiyasu-sem/tree/9b70d62e436e4c77048363a83e4bf82878a9d170). Inspected the README, LICENSE, `sem/jev.py` and `sem/hook.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
