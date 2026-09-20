# AnchorLint

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Evidence-first internal-link auditor for built HTML sites: deterministic destination/fragment/hygiene checks plus an optional TypeSafe Jev pass on whether an anchor's promise matches its destination and source context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/prantikmedhi/anchorlint) |
| Maintainer | [prantikmedhi](https://github.com/prantikmedhi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI (`anchorlint`); install from GitHub archive (not on PyPI at review time). |
| Requirements | Python 3.11+. Rules/heuristic audit needs no key. Semantic `--provider jev` needs `TYPESAFE_API_KEY` and incurs provider charges. |
| License | [MIT](https://github.com/prantikmedhi/anchorlint/blob/f753b683795fd43ff8166f0ed18d2b1c439d38e5/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest inspected. Live TypeSafe calls were not run. Distinct from [jev-seo](jev-seo.md) (SERP/GEO focus). |

## When to use

Use it after a static-site build when you care whether internal links still mean what their anchors say, with retained source/destination evidence for CI baselines. Prefer classical broken-link checkers for existence-only scans, or [jev-seo](jev-seo.md) for SERP/GEO workflows.

## How it works

Local code extracts anchors and destinations from built HTML or inventories. Optional semantic audit posts bounded context through [`src/anchorlint/jev.py`](https://github.com/prantikmedhi/anchorlint/blob/f753b683795fd43ff8166f0ed18d2b1c439d38e5/src/anchorlint/jev.py) to `https://api.typesafe.ai/v1/systemone`. AnchorLint combines probabilities in code and routes ambiguous cases to review; it does not rewrite pages or invent rankings.

## Get started

```sh
git clone https://github.com/prantikmedhi/anchorlint.git
cd anchorlint
git checkout f753b683795fd43ff8166f0ed18d2b1c439d38e5
python3 -m pip install -e .
python3 -m pytest -q
anchorlint audit examples/site --base-url https://example.com --format json --output audit.json
# Optional live semantic pass (charges TypeSafe):
# export TYPESAFE_API_KEY=… && anchorlint audit ./dist --base-url https://example.com --provider jev --max-links 25
```

## Examples and demos

- Bundled `examples/site` deliberately includes bad links (nonzero findings expected).
- Docs: installation, CLI, CI baselines, and [How Jev works](https://github.com/prantikmedhi/anchorlint/blob/f753b683795fd43ff8166f0ed18d2b1c439d38e5/docs/jev.md).

## Limits and data handling

Does not execute JavaScript, crawl the live web, or edit a CMS. Semantic mode sends link context and destination excerpts to TypeSafe. High Jev confidence is not proof of correctness. `--max-links` caps paid calls; read coverage/errors in every report.

## Review and maintenance

Reviewed on **2026-09-21** at [commit f753b68](https://github.com/prantikmedhi/anchorlint/tree/f753b683795fd43ff8166f0ed18d2b1c439d38e5): MIT. AI-assisted source review of `jev.py`, README, and LICENSE. **`pytest`**: **76 passed**, 6 skipped (440 subtests). No live TypeSafe calls.

Related: [jev-seo](jev-seo.md), [Sniff Test](snifftest.md).
