# jev-browse (cooper667)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Claude Code plugin that runs a plain-English Playwright checklist: TypeSafe Jev on Cloudflare Workers AI (`typesafe/jev`) picks elements from the accessibility tree and judges each check. Distinct from other `jev-browse` / browser-skill listings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cooper667/jev-browse) |
| Maintainer | [cooper667](https://github.com/cooper667). Independently curated. |
| Format | Claude Code marketplace plugin + `skills/jev-browse` runner. |
| Requirements | Claude Code; Playwright in the target checkout; Cloudflare Workers AI account/token in `~/.config/jev/env`. |
| License | [MIT](https://github.com/cooper667/jev-browse/blob/7fb471c6f23c5062f5567e8841b12b8b6613ce77/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Cloudflare/Playwright runs not executed. Distinct from [Jev Browser Skill](jev-browser-skill.md) (zurfyx) and [jev-browser-skill (hqman)](hqman-jev-browser-skill.md). |

## When to use

Use it when Claude should **QA a flow it just built** from a short English checklist and get a single verdict line plus screenshots. Prefer indexed Playwright SDKs when you need locator assertions rather than Jev judgments.

## How it works

[`skills/jev-browse/runner/engine/jev.ts`](https://github.com/cooper667/jev-browse/blob/7fb471c6f23c5062f5567e8841b12b8b6613ce77/skills/jev-browse/runner/engine/jev.ts) calls Workers AI Jev over the accessibility tree for actions and checks. Code owns Playwright execution; layout/color checks are reported as not judged.

## Get started

```sh
# In Claude Code:
/plugin marketplace add cooper667/jev-browse
/plugin install jev-browse@jev-browse
# Configure ~/.config/jev/env with CLOUDFLARE_ACCOUNT_ID + CLOUDFLARE_API_TOKEN
# Ask Claude to "qa check" a flow, or invoke the jev-browse skill.
```

Pin review: [commit 7fb471c](https://github.com/cooper667/jev-browse/tree/7fb471c6f23c5062f5567e8841b12b8b6613ce77).

## Examples and demos

- README sample `[qa] verdict PASS` log lines.
- `skills/jev-browse/SKILL.md` step-writing guide.

## Limits and data handling

Accessibility-tree text goes to Cloudflare Workers AI. A pass is Jev's judgment, not a locator assertion. This listing did not run the plugin or spend Workers AI credits.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 7fb471c](https://github.com/cooper667/jev-browse/tree/7fb471c6f23c5062f5567e8841b12b8b6613ce77). AI-assisted README + skill/runner inspection. No live spend.

Related: [Jev Browser Skill](jev-browser-skill.md), [jev-browser-skill (hqman)](hqman-jev-browser-skill.md), [ajevt-browser](ajevt-browser.md).
