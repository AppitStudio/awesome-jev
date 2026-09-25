# JevPaper

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome extension for arXiv: TypeSafe Jev marks abstract claims, body sentences that deliver them, and caveats—highlighting authors' own sentences rather than generating summaries (GPL-3.0, BYOK).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SRjoeee/jev-paper) |
| Maintainer | [SRjoeee](https://github.com/SRjoeee). Independently curated. |
| Format | Chrome Manifest V3 extension. |
| Requirements | Chrome 128+; bring-your-own TypeSafe/OpenRouter key per README. |
| License | [GPL-3.0](https://github.com/SRjoeee/jev-paper/blob/bdf46b7f29dd7a21430deb14da81d4852e4699c3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live arXiv/Jev marking not run on the review host. Upstream quality figures are author-reported. |

## When to use

Use when reading arXiv HTML to **jump from abstract claims to delivering sentences and caveats** without an LLM paraphrase.

## How it works

Code extracts candidate sentences; Jev answers typed ranking/classification questions (which sentence delivers this claim? is this a limitation?). Highlights stay on author text.

## Get started

```sh
git clone https://github.com/SRjoeee/jev-paper.git
cd jev-paper
git checkout bdf46b7f29dd7a21430deb14da81d4852e4699c3
# Load unpacked per README / Releases
```

## Examples and demos

- README demo GIF on *Attention Is All You Need*.
- Releases page for packaged builds.

## Limits and data handling

Paper text sent to the configured Jev endpoint when marking runs. GPL-3.0 applies to the extension source.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit bdf46b7](https://github.com/SRjoeee/jev-paper/tree/bdf46b7f29dd7a21430deb14da81d4852e4699c3). AI-assisted README and LICENSE inspection; Chrome install not run.
