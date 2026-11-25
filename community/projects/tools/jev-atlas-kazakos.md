# Jev Atlas by Evangelos Kazakos (one-page guide to the papers, open models, leaderboards and code that followed Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Static research page, hosted on GitHub Pages, that collects the papers on Jev-style decision models with short evidence notes and section references, a taxonomy of model families, findings and criticism, a code audit, leaderboard snapshots (Jev Decision Index, JevBench and others), demos and resources. Updated 25 November 2026.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ekazakos/jev-atlas) |
| Maintainer | [Evangelos Kazakos](https://github.com/ekazakos). Independently curated. |
| Format | Static website (HTML, GitHub Pages) |
| Requirements | None; a web browser. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.html`](https://github.com/ekazakos/jev-atlas/blob/a377cafc414ba071cbcc357394fd7e4935703ba1/index.html) at the pinned commit. |

## When to use

- Get oriented in the research and open models around Jev with pointers to the primary sources.
- Mismatch: if you want a maintained database; this is one author's curated page.

## How it works

`index.html` is the whole site: each paper entry cites the arXiv version and section behind its summary, and `boards/` holds leaderboard screenshots. It describes Jev and open models; it does not call any API. Integration evidence: [`index.html`](https://github.com/ekazakos/jev-atlas/blob/a377cafc414ba071cbcc357394fd7e4935703ba1/index.html).

## Get started

Open the hosted page.

```sh
open https://ekazakos.github.io/jev-atlas/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted page: [ekazakos.github.io/jev-atlas/](https://ekazakos.github.io/jev-atlas/)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Summaries and selection are the author's; leaderboard images are snapshots. Not to be confused with the listed Jev Atlas by gorock007 (jev.gorock.sh), a different project.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit a377cafc414b](https://github.com/ekazakos/jev-atlas/tree/a377cafc414ba071cbcc357394fd7e4935703ba1). Inspected the page source at the pinned commit and checked that the hosted page loads. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
