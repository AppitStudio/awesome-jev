# jevzf

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Meaning search for fzf: rank piped lines by TypeSafe Jev relevance (CLI filter or stock fzf Ctrl-R binding); unofficial.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zachlandes/jevzf) |
| Maintainer | [zachlandes](https://github.com/zachlandes). Independently curated. |
| Format | Node.js CLI filter and fzf key-binding helper. |
| Requirements | Node.js 20+; TypeSafe credentials for live meaning search; optional stock fzf 0.65+. |
| License | [Apache-2.0](https://github.com/zachlandes/jevzf/blob/0995cff6614098b083c79576d3c45d3dae123c86/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when **fzf/pipe candidates** should be ordered by intent, not substring match. Without a key it passes input through unchanged.

## How it works

Scores/filters lines with Jev against a meaning query; optional fzf binding reloads candidates via `jevzf -- {q}` without forking fzf.

## Get started

```sh
git clone https://github.com/zachlandes/jevzf.git
cd jevzf
git checkout 0995cff6614098b083c79576d3c45d3dae123c86
# npm pack && npm install -g ./jevzf-*.tgz (pre-npm-publish RC); needs TypeSafe key for live rank
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 0995cff](https://github.com/zachlandes/jevzf/tree/0995cff6614098b083c79576d3c45d3dae123c86). AI-assisted README and license inspection; install/live paths not executed.
