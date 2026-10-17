# paper-sift

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Claude Code plugin that builds a reading list for learning a research area: it collects up to 800 candidate papers from Semantic Scholar, screens every abstract with Jev against the survey's rules, reads the best open-access papers, and reports a ranked list.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucasddmc/paper-sift) |
| Maintainer | [lucasddmc](https://github.com/lucasddmc). Independently curated. |
| Format | Claude Code plugin (Python scripts) |
| Requirements | Claude Code, Python 3, a TypeSafe API key; a Semantic Scholar key is optional. |
| License | [MIT](https://github.com/lucasddmc/paper-sift/blob/b425a47c912f5c6777f80e508df8aec8174cf3da/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/paper_sift/jev.py`](https://github.com/lucasddmc/paper-sift/blob/b425a47c912f5c6777f80e508df8aec8174cf3da/scripts/paper_sift/jev.py) at the pinned commit. |

## When to use

- Get a sorted 'start here' reading list for a new research area in minutes.
- Reuse the deterministic collect, screen, read, report pipeline with Jev as the abstract filter.
- Mismatch: one recipe (learning an area) for now; only open-access full text is read.

## How it works

Claude drafts a search plan with you; then scripts gather candidates from the citation graph, recommendations and keyword search, and `jev.py` posts each abstract with yes/no and subtopic questions to `https://api.typesafe.ai/v1/systemone`, where a rule in the survey spec decides what passes. The README reports a 100-paper survey costing about US$0.02 in Jev calls. Integration evidence: [`scripts/paper_sift/jev.py`](https://github.com/lucasddmc/paper-sift/blob/b425a47c912f5c6777f80e508df8aec8174cf3da/scripts/paper_sift/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add lucasddmc/paper-sift
claude plugin install paper-sift@paper-sift
python3 ~/.claude/plugins/cache/.../scripts/setup_key.py typesafe
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- OpenCode port by a contributor: [github.com/vitornegromonte/socratica](https://github.com/vitornegromonte/socratica)

## Limits and data handling

The area description, titles, abstracts and open-access full text go to TypeSafe on your key; queries go to Semantic Scholar, OpenAlex and arXiv.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit b425a47c912f](https://github.com/lucasddmc/paper-sift/tree/b425a47c912f5c6777f80e508df8aec8174cf3da). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
