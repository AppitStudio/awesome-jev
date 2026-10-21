# jevfetch (verbatim web reading for agents)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Web-reading tool and agent skill that splits a page into blocks, asks Jev whether each block answers the question, and returns only matching passages verbatim with their heading paths, as a WebFetch alternative.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/a2sys-ai/jevfetch) |
| Maintainer | [a2sys-ai](https://github.com/a2sys-ai). Independently curated. |
| Format | Agent skill, CLI and Python library |
| Requirements | uv, Node.js (for `npx skills`), a TypeSafe API key. |
| License | [MIT](https://github.com/a2sys-ai/jevfetch/blob/3f095cf619329a818757c05083be1a380828d299/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevfetch/jev.py`](https://github.com/a2sys-ai/jevfetch/blob/3f095cf619329a818757c05083be1a380828d299/jevfetch/jev.py) at the pinned commit. |

## When to use

- Look up a specific fact on a long docs page and quote it exactly.
- Cut agent time and cost versus paraphrasing fetch tools.
- Mismatch: not for summaries or translations that need the whole page.

## How it works

`jevfetch/jev.py` sends page blocks to Jev as yes/no questions about the query; matching blocks come back unchanged with headings, and the skill tells the agent how to handle each status. Integration evidence: [`jevfetch/jev.py`](https://github.com/a2sys-ai/jevfetch/blob/3f095cf619329a818757c05083be1a380828d299/jevfetch/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
npx skills add a2sys-ai/jevfetch --skill jevfetch -a claude-code
export TYPESAFE_API_KEY=your-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark and limits: [github.com/a2sys-ai/jevfetch/blob/main/bench/RESULTS.md](https://github.com/a2sys-ai/jevfetch/blob/main/bench/RESULTS.md)
- Korean README: [github.com/a2sys-ai/jevfetch/blob/main/README.ko.md](https://github.com/a2sys-ai/jevfetch/blob/main/README.ko.md)

## Limits and data handling

Page text and your question are sent to TypeSafe. Benchmark figures are the author's (30 documentation questions vs WebFetch).

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 3f095cf61932](https://github.com/a2sys-ai/jevfetch/tree/3f095cf619329a818757c05083be1a380828d299). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
