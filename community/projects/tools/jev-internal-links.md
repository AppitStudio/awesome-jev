# Jev Internal Links

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Claude Code skill that crawls a site's sitemap, shortlists related pages locally, asks TypeSafe Jev (via OpenRouter Decisions) which internal link each paragraph needs, applies your confidence/quota rules, and builds an approval report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NicoSKOOL/jev-internal-links) |
| Maintainer | [NicoSKOOL](https://github.com/NicoSKOOL). Independently curated. |
| Format | Claude Code skill + Python scripts. |
| Requirements | Claude Code; Python 3.10+; OpenRouter API key with Decisions/Jev access. |
| License | [MIT](https://github.com/NicoSKOOL/jev-internal-links/blob/5f76ff2c4e8d65df2a5176bac0924f27101f976e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live crawls not run. Upstream cost examples not re-measured. Related to [AnchorLint](anchorlint.md) but proposes new links rather than auditing existing ones. |

## When to use

Use to **propose** missing internal links with calibrated Jev choices. Prefer [AnchorLint](anchorlint.md) to audit already-built HTML links.

## How it works

Crawl → local shortlist → batched Jev Choice/Noul questions per paragraph → deterministic rule layer (`config.yaml`) → Claude picks verbatim anchor phrases → dashboard/CSV report.

## Get started

```sh
git clone https://github.com/NicoSKOOL/jev-internal-links.git ~/.claude/skills/jev-internal-links
cd ~/.claude/skills/jev-internal-links
git checkout 5f76ff2c4e8d65df2a5176bac0924f27101f976e
pip install -r requirements.txt
# configure OPENROUTER_API_KEY; run scripts/run.py https://example.com
```

## Examples and demos

- README cost walkthrough on a 164-page site (upstream).
- `docs/dashboard.jpg` report screenshot.

## Limits and data handling

Page text goes to OpenRouter/Jev and Claude for anchors. Re-runs without new Jev calls are local after caching per upstream design.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 5f76ff2](https://github.com/NicoSKOOL/jev-internal-links/tree/5f76ff2c4e8d65df2a5176bac0924f27101f976e). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [AnchorLint](anchorlint.md), [jev-seo](jev-seo.md).
