# jev-browser-skill (hqman)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Standalone Playwright Chromium skill/`jb` CLI: Jev chooses in-page actions for a scoped browser goal. Default provider is Vercel AI Gateway; optional TypeSafe System One. Distinct from [zurfyx/jev-browser-skill](jev-browser-skill.md) (CDP teaching skill).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hqman/jev-browser-skill) |
| Maintainer | [hqman](https://github.com/hqman). Independently curated; this entry is not an upstream submission or endorsement. Not affiliated with Cline. |
| Format | Agent skill **`jb-browser`** + CLI **`jb`** (`jev-browser-skill` 0.1.0 private; not an npm publish). Derived from cline/plugins `jev-browser` (see NOTICE/CHANGES). |
| Requirements | Node.js **≥ 22.18** (type stripping); Playwright Chromium; Gateway or TypeSafe API key in `~/.jb/config.json` or env. |
| License | [Apache-2.0](https://github.com/hqman/jev-browser-skill/blob/37b30fec7c50a646493f11a64edef8b01c6cdb59/LICENSE) (see [NOTICE](https://github.com/hqman/jev-browser-skill/blob/37b30fec7c50a646493f11a64edef8b01c6cdb59/NOTICE)). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, NOTICE, package). Live browser/Gateway/TypeSafe runs were **not** executed on the review host. |

## When to use

Use it when a coding agent should run a bounded Playwright goal with Jev picking clicks/types via a local daemon. Prefer [Jev Browser Skill](jev-browser-skill.md) (zurfyx) for the minimal CDP teaching loop; prefer [openqa Jev Browser](openqa-jev-browser.md) for indexed CodexQA replay/generate.

## How it works

`jb run` starts a daemon session, observes the page, asks Jev for the next action, and executes via Playwright. `allowedOrigins` constrains navigations; password/file/hidden inputs are omitted from model observations. Artifacts under `~/.jb/data`. Skill lives at `skills/jev-browser/SKILL.md` (symlink into agent skill dirs; do not copy away from the clone).

## Get started

```sh
git clone https://github.com/hqman/jev-browser-skill.git
cd jev-browser-skill
git checkout 37b30fec7c50a646493f11a64edef8b01c6cdb59
npm install && npx playwright install chromium
# Configure ~/.jb/config.json from config.example.json (Gateway or TypeSafe key)
./bin/jb run --url https://example.com --goal "Open More information. Stop when visible." --max-steps 10
```

## Examples and demos

- README security boundary list; `CHANGES.md` vs upstream Cline plugin.
- `config.example.json`; skill markdown under `skills/jev-browser/`.

## Limits and data handling

Page text and action history go to the chosen provider. `needs_review` depends on the model selecting `REVIEW`—not a hard security gate. Video recording defaults on. This listing did not start the daemon or call providers.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 37b30fe](https://github.com/hqman/jev-browser-skill/tree/37b30fec7c50a646493f11a64edef8b01c6cdb59) (**0.1.0**, Apache-2.0). AI-assisted source review of README, LICENSE, NOTICE, package. No live provider spend.

Related: [Jev Browser Skill](jev-browser-skill.md), [Jev Browser (openqa-cn)](openqa-jev-browser.md), [pi-Jev-browser](pi-jev-browser.md).
